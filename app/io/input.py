import pandas as pd

def read_from_console() -> str:
    """
    Reads text input from the console.

    Returns:
        str: The user input as a string.
    """
    return input("Enter some text: ")


def read_from_file_builtin(filepath: str) -> str:
    """
    Reads text from a file using Python's built-in functionality.

    Args:
        filepath (str): Path to the input file.

    Returns:
        str: Contents of the file, or None if file is not found.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        raise


def read_from_file_pandas(filepath: str) -> str:
    """
    Reads data from a file using the pandas library.

    Args:
        filepath (str): Path to the input CSV file.

    Returns:
        str: String representation of the data.

    Raises:
        Exception: If an error occurs during reading.
    """
    try:
        df = pd.read_csv(filepath)
        return df.to_string(index=False)
    except Exception as e:
        print(f"Error reading with pandas: {e}")
        raise
