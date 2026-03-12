import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"
logger = []

def copy_static_to_public():
    global logger
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
        logger.append("removing public directory")
    os.mkdir(dir_path_public)
    copy_dir_r(dir_path_static, dir_path_public)

    # print(logger)


def copy_dir_r(src, dest):
    global logger
    logger.append(f"inside {src} dir")
    content = os.listdir(src)
    for file in content:
        src_file_path = os.path.join(src, file)
        dest_file_path = os.path.join(dest, file)
        if os.path.isfile(src_file_path):
            shutil.copy(src_file_path, dest_file_path)
            logger.append(f"copying file {file} from {src} to {dest}")
        
        if os.path.isdir(src_file_path):
            os.mkdir(dest_file_path)
            logger.append(f"making {dest_file_path} directory")
            copy_dir_r(src_file_path, dest_file_path)


def write_file(dest_path, file_content, file_name):
    output_path = os.path.join(dest_path, file_name)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    
    with open(output_path, 'w') as f:
        f.write(file_content)