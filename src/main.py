from util.util import copy_dir, write_file
from page import generate_pages_recursive
import os, sys

dir_path_static = "./static"
markdown_path = "./content"
template_path = "./template.html"
dir_path_public = "./docs"

def main():
    
    basepath = sys.argv[0] if 0 < len(sys.argv) else "/"

    copy_dir(dir_path_static, dir_path_public)
    if not os.path.exists(markdown_path):
        raise Exception(f"missing index.md in path {markdown_path}")
    
    if not os.path.exists(template_path):
        raise Exception(f"missing template.html in path {template_path}")

    generate_pages_recursive(markdown_path,template_path, dir_path_public, basepath)


if __name__ == "__main__":
    main()