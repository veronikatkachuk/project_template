def print_to_console(text: str) -> None:
    """
    Prints the given text to the console.

    Args:
        text (str): Text to be printed.
    """
    print(text)


def write_to_file_builtin(filepath: str, text: str) -> None:
    """
    Writes text to a file using Python's built-in functionality.

    Args:
        filepath (str): Path to the output file.
        text (str): Text to be written to the file.

    Raises:
        ValueError: If text is None.
    """
    if text is None:
        print(f"Error: Cannot write None to file: {filepath}")
        raise ValueError("Cannot write None to file")
    with open(filepath, 'w') as f:
        f.write(text)
