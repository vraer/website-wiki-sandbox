import re
import glob

def preprocess_markdown(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Flags to check if the file needs updating
    needs_update = False

    # Check and replace all variations of <details> with <details markdown>
    new_content, details_count = re.subn(r'<details[^>]*>', '<details markdown>', content)
    if details_count > 0:
        needs_update = True

    # Check and remove all <br> tags
    new_content, br_count = re.subn('<br>', '', new_content)
    if br_count > 0:
        needs_update = True

    # Only write back if changes were made
    if needs_update:
        with open(file_path, 'w') as f:
            f.write(new_content)

if __name__ == '__main__':
    # Locate all Markdown files in current directory and its subfolders
    for markdown_file in glob.glob('**/*.md', recursive=True):
        preprocess_markdown(markdown_file)
