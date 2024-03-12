from user_input import input_from_console, read_from_file, read_from_file_with_pandas
from output import output_to_console, write_to_file
def main():
    console_input = input_from_console()
    output_to_console(f"Text from console: {console_input}")

    file_path_builtin = "data/builtin_file.txt"
    file_content_builtin = read_from_file(file_path_builtin)
    output_to_console(f"Text from file (builtin): {file_content_builtin}")

    file_path_pandas = "data/pandas_file.csv"
    file_content_pandas = read_from_file_with_pandas(file_path_pandas)
    output_to_console(f"Text from file (pandas):\n{file_content_pandas}")

    output_text = "This is an output text."
    output_to_console(output_text)

    file_path_output = "data/output_file.txt"
    result_output = write_to_file(file_path_output, output_text)
    output_to_console(result_output)

if __name__ == "__main__":
    main()