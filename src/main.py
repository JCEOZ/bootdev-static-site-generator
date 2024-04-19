import os
import shutil

static_directory_path = "../static"
public_directory_path = "../public"

def main():
    verify_static_content_directory()
    prepare_public_content_directory()



def verify_static_content_directory():
    static_directory_exists = os.path.exists(static_directory_path)
    print(f"Static directory exists: {static_directory_exists}")
    if not static_directory_exists:
        raise Exception("Static directory does not exist")


def prepare_public_content_directory():
    public_directory_exists = os.path.exists(public_directory_path)
    print(f"Public directory exists: {public_directory_exists}")
    if public_directory_exists:
        print(f"Deleting existing public directory: {public_directory_path}")
        shutil.rmtree(public_directory_path)
    print(f"Creating new public directory: {public_directory_path}")
    os.mkdir(public_directory_path)


main()
