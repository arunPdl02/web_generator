from util.util import copy_static_to_public, write_file
from page import generate_page
import os

markdown_path = "./content/index.md"
template_path = "./template.html"
public_path = "./public"

def main():
    copy_static_to_public()
    if not os.path.exists(markdown_path):
        raise Exception(f"missing index.md in path {markdown_path}")
    
    if not os.path.exists(template_path):
        raise Exception(f"missing template.html in path {template_path}")
    html_page = generate_page(markdown_path, template_path, public_path )

    write_file(public_path, html_page, "index.html")


if __name__ == "__main__":
    main()