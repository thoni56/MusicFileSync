#! /bin/python
from syncer import sync
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--from', type=str, required=True, help='source directory', dest="source_directory")  
    parser.add_argument('--to', type=str, required=True, help='destination directory', dest="destination_directory")
    parser.add_argument('--genres', type=str, help='comma-separated list of genres to match ("--genres rock,country")', dest="genres")

    args = parser.parse_args()
    source_dir = args.source_directory
    dest_dir = args.destination_directory

    if args.genres:
        genres = {"genre": args.genres.split(",")}
    else:
        genres = None

    sync(source_dir, dest_dir, metadata_filters=genres)

if __name__ == "__main__":
    main()