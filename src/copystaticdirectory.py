import os
import shutil


static_directory_path = "../static"
public_directory_path = "../public"


def copy_static_directory():
    __verify_static_content_directory__()
    __prepare_public_content_directory__()
    __copy_directory_files__(static_directory_path, public_directory_path)


def __verify_static_content_directory__():
    static_directory_exists = os.path.exists(static_directory_path)
    print(f"Static directory exists: {static_directory_exists}")
    if not static_directory_exists:
        raise Exception("Static directory does not exist")


def __prepare_public_content_directory__():
    public_directory_exists = os.path.exists(public_directory_path)
    print(f"Public directory exists: {public_directory_exists}")
    if public_directory_exists:
        print(f"Deleting existing public directory: {public_directory_path}")
        shutil.rmtree(public_directory_path)
    print(f"Creating new public directory: {public_directory_path}")
    os.mkdir(public_directory_path)


def __copy_directory_files__(source_directory_path, target_directory_path):
    is_source_directory_path = os.path.isdir(source_directory_path)
    print(f"Is source directory path '{source_directory_path}' a directory: {is_source_directory_path}")
    is_target_directory_path = os.path.isdir(target_directory_path)
    print(f"Is target directory path '{target_directory_path}' a directory: {is_target_directory_path}")

    if not is_source_directory_path:
        raise Exception(f"Invalid source directory path: {source_directory_path}. Source directory path must be an existing directory.")
    if not is_target_directory_path:
        raise Exception(f"Invalid target directory path: {target_directory_path}. Target directory path must be an existing directory.")

    source_directory_contents = os.listdir(source_directory_path)
    print(f"Source directory contents: {source_directory_contents}")

    for source_directory_content in source_directory_contents:
        print(f"Source directory content: {source_directory_content}")
        is_file = os.path.isfile(os.path.join(source_directory_path, source_directory_content))
        is_dir = os.path.isdir(os.path.join(source_directory_path, source_directory_content))
        if is_file:
            source_file_path = os.path.join(source_directory_path, source_directory_content)
            target_file_path = os.path.join(target_directory_path, source_directory_content)
            print(f"Copying file: {source_directory_content} from {source_file_path} to {target_file_path}")
            shutil.copyfile(source_file_path, target_file_path)
        if is_dir:
            new_source_directory_path = os.path.join(source_directory_path, source_directory_content)
            new_target_directory_path = os.path.join(target_directory_path, source_directory_content)
            print(f"Making new directory: {new_target_directory_path}")
            os.mkdir(new_target_directory_path)
            print(f"Copying directory: {source_directory_content} from {new_source_directory_path} to {new_target_directory_path}")
            __copy_directory_files__(new_source_directory_path, new_target_directory_path)