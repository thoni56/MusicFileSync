import glob
import os

from metadata_filterer import metadata_filter
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
    source_files = glob.glob(os.path.join(source, "**", "*"), recursive=True)
    filtered_files = metadata_filter(source_files, file_filters)
    updated_files = update_files(destination, filtered_files)
    deleted_files = delete_nonexisting_files(destination, source_files)
    return (updated_files, deleted_files)
