def input_from_console():
    """
    Function to input text from the console.

    Returns:
    str. The text entered by the user from the console.
    """
    return input("Enter some text: ")

def read_from_file(file_path):
    """
    Function to read text from a file using built-in Python capabilities.

    Args:
        file_path (str): The path to the file.

    Returns:
        str. The content of the file as a string.

    Raises:
        FileNotFoundError: If the specified file is not found.
        IOError: If there is an error reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"Error reading file: {str(e)}"

def read_from_file_with_pandas(file_path):
    """
    Function to read text from a file using pandas.

    Args:
        file_path (str): The path to the file.

    Returns:
        str. The content of the file as a string.

    Raises:
        ImportError: If the pandas library is not installed.
        Exception: If there is an error reading the file with pandas.
    """
    try:
        import pandas as pd
        return pd.read_csv(file_path, delimiter=',').to_string(index=False)
    except ImportError:
        return "Pandas library is not installed. Install it using `pip install pandas`."
    except Exception as e:
        return f"Error reading file with pandas: {str(e)}"