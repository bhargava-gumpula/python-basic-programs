file_path = 'path_to_file.txt'  # Replace with the actual file path

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()

    # Split the contents into words
    words = file_contents.split()

    # Count the number of words
    word_count = len(words)

# Print the word count
print("The file contains", word_count, "words.")
