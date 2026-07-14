"""Module that demonstrates different cases when using secure_archive()"""


def secure_archive(
        file_name: str, action: str, content_to_write: str = ""
        ) -> tuple[bool, str]:
    """Provides safe access to any file either for reading or writing"""

    possible_actions: dict[str, str] = {"read": "r", "write": "w"}

    # Action not recognized
    if action not in possible_actions.keys():
        print(
            f"Error: action '{action}' is not valid.",
            "Allowed actions: 'read' or 'write'"
            )
        return tuple()
    
    # Try to handle file
    try:
        with open(file_name, possible_actions[action]) as file_stream:
        if action == "read":
            content = file_stream.read()
        else:
            file_stream.write(content_to_write)
        
