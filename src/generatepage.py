import os

from src.block import markdown_to_html_node


title_placeholder = "{{ Title }}"
content_placeholder = "{{ Content }}"


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = __read_file_content__(from_path)
    template = __read_file_content__(template_path)

    page_title = __extract_title__(markdown)
    template = template.replace(title_placeholder, page_title)

    html_content = markdown_to_html_node(markdown).to_html()
    template = template.replace(content_placeholder, html_content)

    __create_page_file__(template, dest_path)


def __read_file_content__(file_path):
    print(f"Reading file {file_path}")
    with open(file_path, 'r') as f:
        return f.read()


def __extract_title__(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.strip().startswith('# '):
            # Grab the header text
            return line.strip()[2:]
    raise Exception('Could not find title in markdown')


def __create_page_file__(content, dest_path):
    dest_dir_name = os.path.dirname(dest_path)
    print(f"Generated page directory name: {dest_dir_name}")
    dest_dir_exists = os.path.exists(dest_dir_name)
    print(f"Generated page directory exists: {dest_dir_exists}")
    if not dest_dir_exists:
        print(f"Creating directory {dest_dir_name}")
        os.makedirs(dest_dir_name)
    print(f"Creating file {dest_path} in {dest_path}")
    with open(dest_path, 'w') as f:
        f.write(content)
