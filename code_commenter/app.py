# app.py
import os
import re
import json
import google.generativeai as genai
from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory
from dotenv import load_dotenv

# --- Initialization ---
load_dotenv()
app = Flask(__name__)
app.secret_key = os.urandom(24) # Needed for session management

# --- AI Configuration ---
try:
    API_KEY = os.getenv("GEMINI_API_KEY")
    if not API_KEY:
        raise ValueError("GEMINI_API_KEY not found in .env file")
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"Error initializing GenerativeAI: {e}")
    model = None

# --- Helper Functions from Notebook ---
def clean_code_json(response_text: str) -> dict:
    """
    Cleans a JSON-like response that may include markdown code fences.
    Returns a valid Python dictionary.
    """
    match = re.search(r"\{.*\}", response_text, re.DOTALL)
    if not match:
        raise ValueError("No valid JSON object found in the AI response.")
    
    json_str = match.group(0)
    data = json.loads(json_str)
    
    code = data.get("code_with_comments", "")
    code = re.sub(r"^```[a-zA-Z]*\n?", "", code, flags=re.MULTILINE)
    code = re.sub(r"\n?```$", "", code, flags=re.MULTILINE)
    data["code_with_comments"] = code.strip()
    
    return data

def get_commented_code(user_code: str) -> dict:
    """
    Sends the user's code to the AI model and returns the commented version.
    """
    if not model:
        raise ConnectionError("AI Model is not initialized. Check API key and configuration.")

    final_prompt = f"""
    You are a professional code reviewer and documentation expert.
    Your task is to take the provided code and add clear, concise, and professional comments
    that explain the logic, purpose, and functionality of the code.

    Requirements:
    1. Return the original code exactly as given, but with added comments in the appropriate places.
    2. Do not modify variable names, function names, or the structure of the code.
    3. Make comments helpful for a reader who is learning or maintaining the code.
    4. Return the result strictly as a JSON object with the following format:

    {{
      "code_with_comments": "...",   # The full code with comments included
      "extension": "..."             # The file extension of the code (e.g., .py for Python, .js for JavaScript, .cpp for C++)
    }}

    Here is the code you must work on:
    ```
    {user_code}
    ```
    """
    response = model.generate_content(final_prompt)
    return clean_code_json(response.text)


# --- Flask Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_code = request.form.get('code_input', '')
        code_file = request.files.get('code_file')

        if code_file and code_file.filename != '':
            try:
                # Read file content and decode it
                user_code = code_file.read().decode('utf-8')
            except UnicodeDecodeError:
                return render_template('index.html', error="Could not read the uploaded file. Please ensure it's a valid text file (e.g., UTF-8).")
        
        if not user_code.strip():
            return render_template('index.html', error="Please paste your code or upload a file.")

        try:
            result = get_commented_code(user_code)
            
            # Store results in session to handle download
            session['commented_code'] = result['code_with_comments']
            session['extension'] = result['extension'].strip('. ')
            
            return render_template(
                'index.html',
                commented_code=result['code_with_comments'],
                original_code=user_code,
                extension=session['extension']
            )
        except Exception as e:
            # Catch potential errors from the API or JSON parsing
            return render_template('index.html', error=f"An error occurred: {e}", original_code=user_code)

    return render_template('index.html')


@app.route('/download')
def download_file():
    """
    Handles the download of the commented code file.
    """
    commented_code = session.get('commented_code')
    extension = session.get('extension')

    if not commented_code or not extension:
        return redirect(url_for('index'))

    # Define a temporary directory for downloads
    download_dir = os.path.join(app.root_path, 'temp_downloads')
    os.makedirs(download_dir, exist_ok=True)
    
    filename = f"commented_code.{extension}"
    filepath = os.path.join(download_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(commented_code)

    return send_from_directory(directory=download_dir, path=filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)