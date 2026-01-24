import os
import shutil

def copy_files_recursive(src_directory, target_directory):
    if not os.path.exists(src_directory):
        raise Exception("Src directory is not valid")

    if os.path.exists(target_directory):
      shutil.rmtree(target_directory)
    os.mkdir(target_directory)

    items_in_src = os.listdir(src_directory)
    for item in items_in_src:
        item_path_in_src = os.path.join(src_directory, item)
        if os.path.isfile(item_path_in_src):
            shutil.copy(item_path_in_src, target_directory)
            continue
        item_path_in_target = os.path.join(target_directory, item)
        os.mkdir(item_path_in_target)
        copy_files_recursive(item_path_in_src, item_path_in_target)