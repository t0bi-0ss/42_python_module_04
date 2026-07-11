import sys

from typing import IO


"""Module that implements some simple file handling
tasks"""


def main(file_stream: IO[str]) -> None:
    """Main logic handling"""

    print("---\n")

    fragment_num = 1

    for line in file_stream:
        trailing_zeros = 3 - len(str(fragment_num))
        fragment_label = (
            f"[FRAGMENT {'0' * trailing_zeros}{fragment_num}]"
        )
        print(
            fragment_label, line, end=""
        )
        fragment_num += 1
    print("\n\n---")


if __name__ == "__main__":
    arguments_num = len(sys.argv)

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

    try:
        file_stream = open(sys.argv[1])
    except FileNotFoundError as msg:
        print(f"Error opening file '{sys.argv[1]}': ", end="")
        if not sys.argv[1]:
            print("file path provided was completely empty", msg)
        else:
            print(msg)
    except PermissionError as msg:
        print(
            f"Error opening file '{sys.argv[1]}':", msg
        )
    except IsADirectoryError as msg:
        print(
            f"Error opening file '{sys.argv[1]}':", msg
        )
    except OSError as msg:
        print(
            f"Error opening file '{sys.argv[1]}':",
            " An unexpected system error occured:",
            msg
        )
    else:
        print("=== Cyber Archives Recovery ===")
        print("Accessing file", file_stream.name)
        main(file_stream)
        file_stream.close()
        if file_stream.closed:
            print(
                f"File '{sys.argv[1]}' closed."
            )
