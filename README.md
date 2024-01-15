# Music File Sync

This is a program that will sync one source directory tree with a
destination and find all music files that match some criteria in the
source tree, "Genre" will be the first criteria implemented.

It then updates the source tree with any changed files from the source
and will delete files from the destination that are no longer
available in the source.

## Example Use

Assume you have a complete media library and you want to extract only
music files which has "Genre" equal to "Rock" or "Blues".

	musicfilesync --from source --to destination --genres=rock,blues


