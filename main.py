import pandas as pd

from app.io.input import read_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import print_to_console, write_to_file_builtin

def generate_sample_csv():
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    df.to_csv('data/input.csv', index=False)


def main() -> None:
    # Read from console
    console_text = read_from_console()
    print_to_console('Console Input:')
    print_to_console(console_text)
    write_to_file_builtin('data/output_console.txt', console_text)
    print_to_console('Writing to file complete. Content:')
    print_to_console(read_from_file_builtin('data/output_console.txt'))

    # Read from file using built-in Python
    try:
        # Content in data/input.txt: HelloWorld
        file_text_builtin = read_from_file_builtin('data/input.txt')
        print_to_console('File Read (builtin):')
        print_to_console(file_text_builtin)
        write_to_file_builtin('data/output_builtin.txt', file_text_builtin)
        print_to_console('Writing to file complete. Content:')
        print_to_console(read_from_file_builtin('data/output_builtin.txt'))
    except FileNotFoundError:
        print_to_console('Skipping built-in file read due to missing file.')

    # Read from file using pandas
    generate_sample_csv()
    try:
        file_text_pandas = read_from_file_pandas('data/input.csv')
        print_to_console('File Read (pandas):')
        print_to_console(file_text_pandas)
        write_to_file_builtin('data/output_pandas.txt', file_text_pandas)
        print_to_console('Writing to file complete. Content:')
        print_to_console(read_from_file_builtin('data/output_pandas.txt'))
    except Exception:
        print_to_console('Skipping pandas file read due to an error.')

if __name__ == '__main__':
    main()