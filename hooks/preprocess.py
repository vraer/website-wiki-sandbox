import re
import glob

def preprocess_markdown(file_path):
    with open(file_path, 'r') as f:
        content = f.readlines()

    modified_content = []
    for line in content:
        # Add 'markdown' and custom class to <details> tags
        if '<details>' in line:
            line = line.replace('<details>', '<details markdown>')
        
        # Update nested lists from 2 spaces to 4 spaces
        if re.match(r' {2}- ', line):
            line = re.sub(r' {2}- ', '    - ', line)

        modified_content.append(line)

    # Write back to the file
    with open(file_path, 'w') as f:
        f.writelines(modified_content)

# Search for all Markdown files in the 'docs/' directory
for file_path in glob.glob("docs/*.md", recursive=True):
    preprocess_markdown(file_path)
