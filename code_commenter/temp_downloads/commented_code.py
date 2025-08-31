# This program first prints a greeting and then generates a right-angled triangle pattern using asterisks.

# Print a simple greeting message to the console.
print('hello world')


# Outer loop iterates 10 times, controlling the number of rows in the triangle.
for i in range(10):
    # Inner loop iterates from 0 up to the current value of i, printing asterisks for each iteration.
    # This creates the increasing number of asterisks in each row.
    for j in range(i):
        # Print an asterisk without a newline character, keeping the asterisks on the same line.
        print("*",end='')
    # After the inner loop completes, print a newline character to move to the next row.
    print('')