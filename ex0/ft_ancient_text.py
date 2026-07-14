import sys

from typing import IO


"""Module that implements some simple file handling
tasks"""


def main(file_stream: IO[str]) -> None:
    """Main logic handling"""

    print("=== Cyber Archives Recovery ===")
    print("Accessing file", file_stream.name)
    print("---\n")

    fragment_num = 1
    content = file_stream.read().split("\n")

    for line in content:
        print(line)
        fragment_num += 1
    print("\n---")


if __name__ == "__main__":
    arguments_num = len(sys.argv)

    if arguments_num != 2:
        if len(sys.argv) < 2:
            print(
                "Error: no file was passed.",
                "Usage:",
                "ft_ancient_text.py <file>"
            )
        if len(sys.argv) > 2:
            print(
                "Error: more than one file was passed.",
                "Usage:",
                "ft_ancient_text.py <file>"
            )
        raise SystemExit

    file_stream = None
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
        main(file_stream)
    finally:
        if file_stream:
            file_stream.close()
            if file_stream.closed:
                print(
                    f"File '{file_stream.name}' closed."
                )
