import glob
import os

def get_source_file_list(directory,
                         extensions = ['.mp3', '.aac', '.m4a', '.mp4', '.flac', '.wav', '.aiff', '.aif', '.wma', '.ogg', '.opus'],
                         music_filters=None):
    files = []
    for extension in extensions:
        files.extend(glob.glob(os.path.join(directory, '**'+extension), recursive=True))
    return files