import re
import glob

def preprocess_markdown(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Replace all variations of <details> with <details markdown>
    content = re.sub(r'<details[^>]*>', '<details markdown>', content)
    
    # Remove <br> tags inside <details> sections
    inside_details = False
    lines = content.split('\n')
    modified_lines = []
    
    for line in lines:
        if '<details' in line:
            inside_details = True
        elif '</details>' in line:
            inside_details = False
        
        if inside_details:
            line = line.replace('<br>', '')
        
        modified_lines.append(line)
    
    modified_content = '\n'.join(modified_lines)

    with open(file_path, 'w') as f:
        f.write(modified_content)

if __name__ == '__main__':
    # Locate all Markdown files in current directory and its subfolders
    for markdown_file in glob.glob('**/*.md', recursive=True):
        preprocess_markdown(markdown_file)
