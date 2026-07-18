import os


SEARCH_DIRECTORIES = [
    os.environ.get("PROGRAMFILES"),
    os.environ.get("PROGRAMFILES(X86)"),
    os.path.join(os.environ.get("LOCALAPPDATA", "")),
]


def find_executable(app_name: str):

    app_name = app_name.lower()

    for directory in SEARCH_DIRECTORIES:

        if not directory or not os.path.exists(directory):
            continue

        for root, dirs, files in os.walk(directory):

            for file in files:

                if file.lower() == f"{app_name}.exe":
                    return os.path.join(root, file)

    return None