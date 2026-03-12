import os
from md_to_html import markdown_to_html_node
from blocknode import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_content = get_file_content(from_path)
    template_content = get_file_content(template_path)
    html_node = markdown_to_html_node(md_content)
    html_string = html_node.to_html()
    title = extract_title(md_content)

    return template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_string)


def get_file_content(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f'Error: The file {from_path} was not found.')
    except Exception as e:
        print(f"An error occured: {e}")
