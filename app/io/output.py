def output_to_console(text):
    """
    Function to output text to the console.

    Args:
        text (str): The text to be displayed.

    Returns:
        None
    """
    print(text)

def write_to_file(file_path, text):
    """
    Function to write text to a file using built-in Python capabilities.

    Args:
        file_path (str): The path to the file.
        text (str): The text to be written to the file.

    Returns:
        str. A message indicating the success or failure of the operation.

    Raises:
        Exception: If there is an error writing to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        return f"Text successfully written to file: {file_path}"
    except Exception as e:
        return f"Error writing to file: {str(e)}"