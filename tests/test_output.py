import pytest
from unittest.mock import patch
from app.io.output import print_to_console, write_to_file_builtin


@patch('builtins.print', return_value='Hello')
def test_print_to_console(mock_print):
    test_text = 'Hello'
    print_to_console(test_text)
    mock_print.assert_called_once_with(test_text)


def test_write_to_file_builtin_valid_text():
    write_to_file_builtin('data/output.txt', "Hello, World!")

    with open('data/output.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    assert content.strip() == "Hello, World!"


def test_write_to_file_builtin_none_input():
    with pytest.raises(ValueError):
        write_to_file_builtin('data/output.txt', None)
