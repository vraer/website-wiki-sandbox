import os
import yaml
import glob
import re

# Go through each markdown file
for filepath in glob.glob("docs/**/*.md", recursive=True):
    with open(filepath, "r", encoding="utf-8") as file:
        # Read the content of the markdown file
        content = file.read()

        # Keep track of the last position processed
        last_position = 0
        new_content = ""

        # Look for placeholder comments with specific format
        for match in re.finditer(r"<!-- TAGS=((?:'[^']*'(?:, )?)*) BEGIN -->", content):
            # Extract the tag names from the placeholder comment
            required_tags = set(match.group(1).split(", "))
            required_tags = {tag.strip().strip("'") for tag in required_tags}

            # Generate the heading with details and summary tags
            tag_names_with_links = " ".join(
                [f'<a href="../../tags/#{tag.replace(": ", "-").replace(" ", "-")}" class="md-tag">{tag}</a>' for tag in required_tags]  
                )
            heading = f'<!-- TAGS={match.group(1)} BEGIN -->\n<details class="md-tag-details"><summary class="md-tag-summary">Tags</summary>\n<p>{tag_names_with_links}</p></details>\n\n'  


            # List to store pages that meet the criteria
            matching_pages = []

            # Go through each markdown file to find matching tags
            for other_filepath in glob.glob("docs/**/*.md", recursive=True):
                with open(other_filepath, "r", encoding="utf-8") as other_file:
                    # Parse the front matter
                    lines = other_file.readlines()
                    if lines and lines[0].strip() == "---":
                        try:
                            end = lines[1:].index("---\n") + 1
                            front_matter = yaml.safe_load("".join(lines[1:end]))
                        except ValueError:
                            front_matter = {}
                        # Check if the tags meet the criteria
                        tags = set(front_matter.get("tags", []))
                        if required_tags.issubset(tags):
                            matching_pages.append((other_filepath, front_matter.get("title")))

            # Generate the markdown content with the links
            generated_content = ""
            for page, metadata_title in matching_pages:
                with open(page, "r", encoding="utf-8") as page_file:
                    # Read the content of the page
                    page_content = page_file.read()
                    # Use title from metadata if it exists
                    if metadata_title:
                        title = metadata_title
                    else:
                        # Search for the H1 title
                        h1_title_match = re.search(
                            r"^#\s+(.*)$", page_content, re.MULTILINE
                        )
                        if h1_title_match:
                            # Use the H1 title if it exists
                            title = h1_title_match.group(1)
                        else:
                            # Fall back to the filename in sentence case
                            title = (
                                os.path.splitext(os.path.basename(page))[0]
                                .replace("-", " ")
                                .capitalize()
                            )

                relative_path = os.path.relpath(page, os.path.dirname(filepath))
                generated_content += f"- [{title}]({relative_path})\n"

            # Find the index of the end comment
            end_comment_index = content.find("<!-- TAGS END -->", match.end())
            if end_comment_index ==-1:
                end_comment_index = len(content)

            # Append the content before the placeholder, the heading, and the generated content
            new_content += content[last_position:match.start()] + heading + generated_content
            last_position = end_comment_index

        # Append the rest of the content
        new_content += content[last_position:]

    # Write the modified content back to the markdown file
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(new_content)
