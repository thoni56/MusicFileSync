import audio_metadata

def metadata_filter(files, metadata_filter):
    if (metadata_filter != {} and files != []):
        filtered_files = []
        for file in files:
            metadata = audio_metadata.load(file)
            for tagname, expected_value in metadata_filter.items():
                actual_value = getattr(metadata.tag, tagname, [])
                if (actual_value[0] == expected_value):
                    filtered_files.append(file)
        return filtered_files
    else:
        return files