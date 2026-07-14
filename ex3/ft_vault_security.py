"""Module that demonstrates different cases when using secure_archive()"""


def secure_archive(
        file_name: str,
        action: str,
        content_to_write: str = "") -> tuple[bool, str]:
    """Provides safe access to any file either for reading or writing"""

    possible_actions: dict[str, str] = {"read": "r", "write": "w"}

    # Action not recognized
    if action not in possible_actions.keys():
        message = "Error: action '{action}' is not valid. " \
            "Allowed actions: 'read' or 'write'"
        return (False, message)

    # Try to handle file
    try:
        with open(file_name, possible_actions[action]) as file_stream:
            if action == "read":
                content = file_stream.read()
            else:
                file_stream.write(content_to_write)
    except (
        UnicodeDecodeError,
        ValueError,
        OSError,
        PermissionError,
        IsADirectoryError,
        FileNotFoundError
    ) as msg:
        return (False, str(msg))
    else:
        if action == "read":
            return (True, content)
        else:
            return (True, "Content succesfully written to file")


def main() -> None:
    """Handles main logic"""

    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from nonexistent file:")
    print(secure_archive("nonexistentfile", "read"))

    print("\nUsing 'secure_archive' to read from an inaccesible file:")
    print(secure_archive("file.txt", "read"))

    print("\nUsing 'secure_archive' to read from regular file:")
    print(secure_archive("hola.txt", "read"))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(
        secure_archive(
            "new_file.txt", "write", secure_archive("hola.txt", "read")[1]
        )
    )


if __name__ == "__main__":
    main()
