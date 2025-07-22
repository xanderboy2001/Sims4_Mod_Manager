import os

def print_directory_tree(start_path: str, prefix: str = ""):
    """Print the entire directory tree starting at path."""
    try:
        entries = sorted(os.listdir(start_path))
    except PermissionError:
        print(f"{prefix} [Permission Denied]")
        return
    except FileNotFoundError:
        print(f"{prefix} [Path Not Found]")
        return
    
    for i, entry in enumerate(entries):
        path = os.path.join(start_path, entry)
        connector = "├── " if i < len(entries) - 1 else "└── "
        print(f"{prefix}{connector}{entry}")
        if os.path.isdir(path):
            extension = "│   " if i < len(entries) - 1 else "    "
            print_directory_tree(path, prefix + extension)