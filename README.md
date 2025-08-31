```markdown
# AI Code Commenter - azario0

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)]()
[![Flask](https://img.shields.io/badge/Flask-2.x-blue.svg)]()

## Overview

AI Code Commenter is a web application built with Flask and powered by Google's Gemini AI. This application allows users to upload or paste their code, which is then automatically analyzed and commented by the AI, providing explanations of the logic, purpose, and functionality of the code. The commented code can then be viewed directly in the browser and downloaded.

## Features

*   **Code Input:**  Allows users to either paste code directly into a text area or upload a code file.
*   **AI-Powered Commenting:** Utilizes Google Gemini AI to automatically add professional comments to the code.
*   **Syntax Highlighting:** Provides code syntax highlighting for better readability in the browser.
*   **Side-by-Side Comparison:**  Displays the original and commented code for easy comparison.
*   **Download Functionality:** Allows users to download the commented code as a file.
*   **Clean and Responsive UI:** Uses a modern, clean design for an intuitive user experience.

## Technologies Used

*   **Python:**  The primary programming language.
*   **Flask:** A micro web framework for building the application.
*   **Google Generative AI (Gemini):**  The AI model used for commenting the code.
*   **HTML/CSS:** For the user interface.
*   **Prism.js:**  For syntax highlighting of the code.
*   **dotenv:** For managing the API key securely.

## Getting Started

### Prerequisites

*   Python 3.x
*   A Google Cloud account and an active Gemini API key.
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/azario0/code_commenter.git 
    cd code_commenter
    ```

2.  **Create a virtual environment** (recommended):

    ```bash
    python -m venv venv
    # Or, if you have virtualenv installed:
    # virtualenv venv
    ```

3.  **Activate the virtual environment:**

    *   On Linux/macOS: `source venv/bin/activate`
    *   On Windows: `venv\Scripts\activate`

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up your API key:**

    *   Create a `.env` file in the project root.
    *   Add your Gemini API key to the `.env` file:  `GEMINI_API_KEY="YOUR_API_KEY"` (Replace `YOUR_API_KEY` with your actual key).   
    
    ### Running the Application

1.  **Ensure your virtual environment is activated.**
2.  **Run the Flask app:**

    ```bash
    flask run
    ```

    This will start the development server.
3.  **Open your web browser** and go to `http://127.0.0.1:5000`.

## Usage

1.  **Paste your code** into the text area or **upload a code file**.
2.  Click the "Add Comments" button.
3.  The original and commented code will be displayed.
4.  Click the "Download" button to save the commented code as a file.

## File Structure

```
code_commenter/
├── app.py            # Main Flask application logic
├── requirements.txt   # Python dependencies
├── .env               # API keys (keep this private!)
├── LICENSE            # (If you choose to include one)
├── README.md          # This file
├── templates/
│   └── index.html     # The main HTML template
└── static/
    └── css/
        └── style.css  # Custom CSS for styling
```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 

## Contact

*   Your GitHub username:  [azario0](https://github.com/azario0)  (Replace with your actual GitHub profile link)
