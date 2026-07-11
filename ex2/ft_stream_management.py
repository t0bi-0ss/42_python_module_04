import sys

from typing import IO


"""Module that implements some simple file handling
tasks"""


def print_content(content: list[str]) -> None:
    """Prints file content with specific format"""

    print("---\n")
    fragment_num = 1
    for line in content:
        trailing_zeros = 3 - len(str(fragment_num))
        fragment_label = (
            f"[FRAGMENT {'0' * trailing_zeros}{fragment_num}]"
        )
        print(
            fragment_label, line
        )
        fragment_num += 1
    print("\n---")


def main(file_stream: IO[str]) -> None:
    """Main logic handling"""

    print("=== Cyber Archives Recovery ===")
    print("Accessing file", file_stream.name)

    # Store file's content
    content = file_stream.read().split("\n")

    # Print file's content
    print_content(content)

    # Close file
    file_stream.close()
    if file_stream.closed:
        print(
            f"File '{file_stream.name}' closed."
        )

    # Transform data
    print("Transform data:")
    transformed_content = [line + '#' for line in content]

    # Print transformed data
    print_content(transformed_content)

    # Rename sys.stdin
    io = sys.stdin

    # Ask for new file name
    print("Enter new file name (or empty): ", end="", flush=True)
    new_file_name = io.readline().strip("\n")

    # Write to new file or not
    if new_file_name:
        try:
            new_file_stream = open(new_file_name, mode="w")
        except PermissionError as msg:
            print(
                "[STDERR]",
                f"Error opening file '{new_file_name}':",
                msg,
                file=sys.stderr
            )
        except IsADirectoryError as msg:
            print(
                "[STDERR]",
                f"Error opening file '{new_file_name}':",
                msg,
                file=sys.stderr
            )
        except OSError as msg:
            print(
                "[STDERR]",
                f"Error opening file '{new_file_name}':",
                " An unexpected system error occured:",
                msg,
                file=sys.stderr
            )
        else:
            new_file_stream.write("\n".join(transformed_content))
            print(f"Saving data to '{new_file_name}'")
        finally:
            if new_file_name:
                new_file_stream.close()
                if new_file_stream.closed:
                    print(f"Data saved in file '{new_file_name}'")

    else:
        print("Not saving data")


if __name__ == "__main__":
    arguments_num = len(sys.argv)

    # Check for valid number of arguments
    if arguments_num != 2:
        if len(sys.argv) < 2:
            print(
                "Error: no file was passed.",
                " ft_ancient_text.py usage: ",
                "python3 ft_ancient_text.py {{file_name}}"
            )
        if len(sys.argv) > 2:
            print(
                "Error: more than one file was passed.",
                " ft_ancient_text.py usage: ",
                "python3 ft_ancient_text.py {{file_name}}"
            )
        raise SystemExit

    # Try to open file
    try:
        file_stream = open(sys.argv[1])
    except FileNotFoundError as msg:
        print(
            "[STDERR]",
            f"Error opening file '{sys.argv[1]}': ",
            end="",
            file=sys.stderr
        )
        if not sys.argv[1]:
            print("file path provided was completely empty",
                  msg,
                  file=sys.stderr
            )
        else:
            print(
                msg,
                file=sys.stderr
            )
    except PermissionError as msg:
        print(
            "[STDERR]",
            f"Error opening file '{sys.argv[1]}':",
            msg,
            file=sys.stderr
        )
    except IsADirectoryError as msg:
        print(
            "[STDERR]",
            f"Error opening file '{sys.argv[1]}':",
            msg,
            file=sys.stderr
        )
    except OSError as msg:
        print(
            "[STDERR]",
            f"Error opening file '{sys.argv[1]}':",
            " An unexpected system error occured:",
            msg
        )
    else:
        main(file_stream)
