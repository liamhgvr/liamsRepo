# dir_compare

import os
from stat import *


PATH_A = "/Users/liam/test_env/a"
PATH_B = "/Users/liam/test_env/diff_server/b"
FULL_NAME = 'full_name'
PERM = 'permissions'
OWNER = 'owner'
GROUP = 'group'

files_2_ignore = [".ipynb_checkpoints", "Untitled.ipynb"]


def get_perm(item):
    # return str
    perm = oct(os.stat(item)[ST_MODE])[-3:]
    return perm


def get_owner(item):
    # return str
    owner = oct(os.stat(item)[ST_UID])[-3:]
    return owner


def get_group(item):
    # return str
    group = oct(os.stat(item)[ST_GID])[-3:]
    return group


def show_bad_files(file_list):
    # displays the diff files
    for i in file_list:
        cmd = "ls -l " + i[FULL_NAME]
        os.system(cmd)


def get_name_from_path(path):
    # return str
    name = path.split('/')[-1]
    return name


def get_dir_tree(path):
    # return dict of dict
    dir_tree = {}
    for root, directories, filenames in os.walk(path):

        for filename in filenames:
            if filename not in files_2_ignore:
                full_name = os.path.join(root, filename)

                curr_item = {
                    'full_name': full_name,
                    PERM: get_perm(full_name),
                    'owner': get_owner(full_name),
                    'group': get_group(full_name)
                }

                short_name = full_name.replace(path, '')
                dir_tree[short_name] = curr_item

    return dir_tree


def main(path_a, path_b):
    # return list of dict
    # checks if files are missing from A

    missing_files = []
    different_files = []

    to_check = get_dir_tree(path_a)
    compare_with = get_dir_tree(path_b)

    print "============= Starting Compare ================"
    if len(compare_with.keys()) != len(to_check.keys()):
        print "Size don't match!"

    for file_key in compare_with:
        # check if file is missing
        if file_key not in to_check.keys():
            print "moving %s to missing files" % file_key
            missing_files.append(compare_with[file_key])
        # check if file is different
        elif compare_with[file_key][PERM] != to_check[file_key][PERM]:
            print "moving %s to different files - permissions" % file_key
            different_files.append(compare_with[file_key])
        elif compare_with[file_key][OWNER] != to_check[file_key][OWNER]:
            print "moving %s to different files - owner" % file_key
            different_files.append(compare_with[file_key])
        elif compare_with[file_key][GROUP] != to_check[file_key][GROUP]:
            print "moving %s to different files - group" % file_key
            different_files.append(compare_with[file_key])

    diffs = {
        'missing': missing_files,
        'different': different_files
    }

    return diffs


if __name__ == '__main__':

    my_diffs = main(PATH_A, PATH_B)

    print "================ Results ================"
    print "Missing files:", len(my_diffs['missing'])
    show_bad_files(my_diffs['missing'])
    print "Different files:", len(my_diffs['different'])
    show_bad_files(my_diffs['different'])
