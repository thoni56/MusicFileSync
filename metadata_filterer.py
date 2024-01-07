from tinytag import TinyTag as tinytag

def filter_on_metadata(files, metadata_filter):
    if (metadata_filter != {} and files != []):
        filtered_files = []
        for file in files:
            try:
                metadata = tinytag.get(file)
            except:
                print("METADATA: Could not read metadata for file: " + file)
            else:
                for tagname, expected_value in metadata_filter.items():
                    try:
                        actual_value = getattr(metadata, tagname, [])
                    except AttributeError:
                        continue
                    else:
                        if (actual_value == expected_value):
                            filtered_files.append(file)
        return filtered_files
    else:
        return files