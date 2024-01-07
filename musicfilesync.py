import glob
import os

from metadata_filterer import filter_on_metadata
from updater import update_files
from cleaner import delete_nonexisting_files

def sync(source, destination, metadata_filters=None):
    """
    Syncs the source directory with the destination directory.

    Arguments:
        source (str): The source directory.
        destination (str): The destination directory.
        metadata_filters (dict): A dictionary of metadata filters.

    Returns:
        (list, list): A tuple of lists. The first list contains the
        files that has been added to the destination directory, and
        the second list contains the files that has been removed from
        the destination directory because they did not exist in the source.
    """
    source_files = get_all_source_files(source)
    source_files = remove_non_audio_files(source_files)
    source_files = filter_on_metadata(source_files, metadata_filters)

    source_files = make_relative(source_files, source)

    updated_files = update_files(source, source_files, destination)
    deleted_files = delete_nonexisting_files(destination, source_files)

    return (updated_files, deleted_files)


def get_all_source_files(path):
    return [f for f in glob.glob(os.path.join(path, "**", "*"), recursive=True) if os.path.isfile(f)]


def make_relative(files, path):
    return [f.replace(path + '/', '') for f in files]


def remove_non_audio_files(files):
    audio_extensions = [".mp3", ".wav", ".flac", ".ogg", ".m4a", ".aac"]
    return [f for f in files if os.path.splitext(f)[1] in audio_extensions]


if __name__ == "__main__":
    (updated, deleted) = sync("/home/thoni/Music", "/tmp/bugg", {"genre": ["bugg", "lindy"]})
    print("Updated files:")
    print(updated)
    print("Deleted files:")
    print(deleted)