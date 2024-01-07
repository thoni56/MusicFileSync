import pathlib

def delete_nonexisting_files(destination, source_files):
    # Convert the file_list to a set for faster lookup
    source_files = set(source_files)

    deleted_files = []

    # Iterate through files in the destination directory
    for file in pathlib.Path(destination).glob('*'):
        if file.is_file():
            relative_file = file.relative_to(destination)
            if not file_in_source(relative_file, source_files):
                file.unlink()
                deleted_files.append(file.name)
    
    remove_empty_directories(destination)

    return deleted_files

def remove_empty_directories(destination):
    for dir in pathlib.Path(destination).glob('*'):
        if dir.is_dir():
            if not any(dir.iterdir()):
                # Directory is empty, delete it
                dir.rmdir()

def file_in_source(relative_path, source_files):
    return str(relative_path) in source_files
            