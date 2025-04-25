
# Project Template

## Description
This project is a Python-based text processing application that provides functionality for:
- Reading input from the console.
- Reading input from files using Python's built-in functionality and the `pandas` library.
- Writing output to the console and files.

## Requirements
You can install the required dependencies using `pipenv`:
```bash
pipenv install
```

The `requirements.txt` contains output of `pip freeze > requirements.txt`.

## Running the Application

To run the application, simply execute the `main.py` file:

```bash
python main.py
```

This will:
1. Prompt you to enter some text into the console.
2. Attempt to read text from a file (`data/input.txt`).
3. Attempt to read CSV data from `data/sample.csv` using `pandas`.
4. Print the results to the console and save them to `data/output.txt`.

## Running Tests

Run the following command:

```bash
pytest tests
```

## Example Output

When you run the application, you should see something like:

```
Enter some text: example input
Console Input:
example input
Writing to file complete. Content:
example input
File Read (builtin):
Sample text from file.
Writing to file complete. Content:
Sample text from file.
File Read (pandas):
 col1  col2
    1     4
    2     5
    3     6
Writing to file complete. Content:
 col1  col2
    1     4
    2     5
    3     6
```