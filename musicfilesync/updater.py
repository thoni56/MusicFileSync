import os
import pathlib
import shutil

def update_files(source, files, destination, verbose=False):
    updated_files = []

    for relative_path in files:
        source_file = pathlib.Path(source) / relative_path
        destination_file = pathlib.Path(destination) / relative_path

        # Create intermediate directories if they don't exist
        os.makedirs(destination_file.parent, exist_ok=True)

        if destination_file.exists():
            if mtime_for(source_file) > mtime_for(destination_file):
                if verbose:
                    clear_line()
                    print(f"Updating {relative_path}\r")
                shutil.copy2(source_file, destination_file)
                updated_files.append(relative_path)
            elif mtime_for(source_file) < mtime_for(destination_file):
                if verbose:
                    print(f"Warning: Destination file {destination_file} is newer than source file {source_file}.")
        else:
            if verbose:
                clear_line()
                print(f"Updating {relative_path}\r")
            shutil.copy2(source_file, destination_file)
            updated_files.append(relative_path)
    
    return updated_files


def mtime_for(file):
    return os.stat(file).st_mtime


def clear_line():
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    print(' ' * terminal_width, end='\r')