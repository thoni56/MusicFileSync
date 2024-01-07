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
                if any(matching(getattr(metadata, tagname, None), expected_value) 
                        for tagname, expected_value in metadata_filter.items()):
                    filtered_files.append(file)
        return filtered_files
    else:
        return files
    
def matching(actual_value, expected_value):
    # Convert actual_value to lowercase if it's a string
    if isinstance(actual_value, str):
        actual_value = actual_value.lower()

    # If expected_value is a list, compare actual_value with each item in the list
    if isinstance(expected_value, list):
        # Convert each item in expected_value to lowercase
        expected_value = [item.lower() for item in expected_value]
        return actual_value in expected_value

    # If expected_value is a string, convert it to lowercase and compare
    elif isinstance(expected_value, str):
        expected_value = expected_value.lower()
        return actual_value == expected_value

    # Return False by default if none of the above conditions are met
    return False

