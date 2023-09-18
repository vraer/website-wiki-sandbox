import os
import re
import yaml
import glob

# List to store page information
page_info = []

# Loop through all markdown files
for filepath in glob.glob("docs/**/*.md", recursive=True):
    with open(filepath, "r", encoding="utf-8") as file:
        # Read the content of the file
        content = file.read()

        # Parse the front matter for tags and title
        lines = content.splitlines()
        front_matter = {}
        if lines and lines[0] == "---":
            try:
                end = lines[1:].index("---") + 1
                front_matter = yaml.safe_load("\n".join(lines[1:end]))
            except ValueError:
                front_matter = {}
            tags = front_matter.get("tags", [])
        else:
            tags = []

        # Search for the H1 title
        h1_title_match = re.search(r"^#\s+(.*)$", content, re.MULTILINE)
        if h1_title_match:
            # Use the H1 title if it exists
            title = h1_title_match.group(1)
        else:
            # Use the title from the front matter if it exists
            title = front_matter.get("title", '<span style="color:red">NONE</span>')

        # Store the information
        relative_path = os.path.relpath(filepath, "docs")
        filename = os.path.basename(filepath)
        location = os.path.dirname(relative_path)
        if location == '.':
            location = 'docs/'
        page_info.append((filename, location, title, tags))

# Sort the pages alphabetically by title
page_info.sort()

# Generate the markdown content with a single table
table = "| Index | File Name | Location | H1 Title | Tags |\n| --- | --- | --- | --- | --- |\n"
for index, (filename, location, title, tags) in enumerate(page_info, start=1):
    tags_str = " ".join(
        [f'<a href="../../tags/#{tag.replace(": ", "-").replace(" ", "-")}" class="md-tag" markdown="1">{tag}</a><br>' for tag in tags]
    )
    table += f"| {index} | [{filename}](./{location}/{filename}) | {location} | {title} | {tags_str} |\n"

# Insert the markdown content into a designated page
designated_page = "docs/all-pages.md"
with open(designated_page, "r", encoding="utf-8") as file:
    content = file.read()

# Look for placeholder comments
placeholder_start = "<!-- TABLE_START -->"
placeholder_end = "<!-- TABLE_END -->"
start_index = content.find(placeholder_start)
end_index = content.find(placeholder_end)

# Insert the content between the placeholders
if start_index != -1 and end_index != -1:
    new_content = content[:start_index + len(placeholder_start)] + "\n" + table + "\n" + content[end_index:]
    with open(designated_page, "w", encoding="utf-8") as file:
        file.write(new_content)
