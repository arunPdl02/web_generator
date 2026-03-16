import os
from md_to_html import markdown_to_html_node
from blocknode import extract_title
from util.util import write_file

def generate_page(from_path, template_path, dest_path, basepath):
    # print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    template_content = get_file_content(template_path)

    md_content = get_file_content(from_path)
    html_node = markdown_to_html_node(md_content)
    html_string = html_node.to_html()
    title = extract_title(md_content)

    page_html = (
        template_content
        .replace("{{ Title }}", title)
        .replace("{{ Content }}", html_string)
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )
    
    write_file(dest_path, page_html, "index.html")



def get_file_content(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f'Error: The file {from_path} was not found.')
    except Exception as e:
        print(f"An error occured: {e}")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dir_path_content):
        raise Exception(f"the source path {dir_path_content} doesn't exist")
    files = os.listdir(dir_path_content)
    for file in files:
        src_file_path = os.path.join(dir_path_content, file)
        dest_file_path = os.path.join(dest_dir_path, file)
        if os.path.isdir(src_file_path):
            os.mkdir(dest_file_path)
            generate_pages_recursive(src_file_path, template_path, dest_file_path, basepath)
        if os.path.isfile(src_file_path) and src_file_path[-3:] == ".md":
            generate_page(src_file_path, template_path, dest_dir_path, basepath)

