import os
import shutil

static_folder_path = "../static"
public_folder_path = "../public"

def main():
    static_folder_exists = os.path.exists(static_folder_path)
    print(f"Static folder exists: {static_folder_exists}")

    if not static_folder_exists:
        raise Exception("Static folder does not exist")

    public_folder_exists = os.path.exists(public_folder_path)
    print(f"Public folder exists: {public_folder_exists}")

    if public_folder_exists:
        print(f"Deleting existing public folder: {public_folder_path}")
        shutil.rmtree(public_folder_path)

    print(f"Creating new public folder: {public_folder_path}")
    os.mkdir(public_folder_path)


main()
