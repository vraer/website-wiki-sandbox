import re
import glob
import hashlib

hashes = {}

def file_hash(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def preprocess_markdown(file_path):
    current_hash = file_hash(file_path)
    if hashes.get(file_path) == current_hash:
        return  # Skip unchanged files

    with open(file_path, 'r') as f:
        content = f.read()

    content = re.sub(r'<details[^>]*>', '<details markdown>', content)

    inside_details = False
    lines = content.split('\\n')
    modified_lines = []

    for line in lines:
        if '<details' in line:
            inside_details = True
        elif '</details>' in line:
            inside_details = False

        if inside_details:
            line = line.replace('<br>', '')

        modified_lines.append(line)

    modified_content = '\\n'.join(modified_lines)

    with open(file_path, 'w') as f:
        f.write(modified_content)

    hashes[file_path] = current_hash  # Update the hash

if __name__ == '__main__':
    for markdown_file in glob.glob('**/*.md', recursive=True):
        preprocess_markdown(markdown_file)
