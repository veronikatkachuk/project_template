import pytest
from unittest.mock import patch
from app.io.input import read_from_console, read_from_file_builtin, read_from_file_pandas


@patch('builtins.input', return_value='Hello')
def test_read_from_console(mock_input):
    result = read_from_console()
    assert result == 'Hello'
    mock_input.assert_called_once_with('Enter some text: ')


def test_read_from_file_builtin_existing_file():
    with open('/tmp/input.txt', 'w', encoding='utf-8') as f:
        f.write('Sample text from file.')

    result = read_from_file_builtin('/tmp/input.txt')
    assert result == 'Sample text from file.'


def test_read_from_file_builtin_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_from_file_builtin('non_existing_file.txt')


def test_read_from_file_pandas_existing_file():
    with open('/tmp/sample.csv', 'w', encoding='utf-8') as f:
        f.write('Name,Age,City\nAlice,30,New York\nBob,25,Los Angeles')

    result = read_from_file_pandas('/tmp/sample.csv')
    assert 'Alice' in result


def test_read_from_file_pandas_error():
    with pytest.raises(Exception):
        read_from_file_pandas('non_existing__csv_file.csv')
