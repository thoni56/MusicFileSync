from source_file_lister import get_source_file_list
from updater import update

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
    updated_files = update(source_files, destination)
    return (updated_files, [])