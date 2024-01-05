from source_file_lister import get_source_file_list
from updater import update_files
from cleaner import delete_nonexisting_files

def sync(source, destination, file_filters=None):
    """
    Syncs the source directory with the destination directory.

    Arguments:
        source (str): The source directory.
        destination (str): The destination directory.

    Returns:
        (list, list): A tuple of lists. The first list contains the
        files that has been added to the destination directory, and
        the second list contains the files that has been removed from
        the destination directory.
    """
    source_files = get_source_file_list(source, file_filters)
    updated_files = update_files(destination, source_files)
    deleted_files = delete_nonexisting_files(destination, source_files)
    return (updated_files, deleted_files)
