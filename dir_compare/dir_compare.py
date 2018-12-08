# dir_compare
import hashlib
import os
import shutil
import errno
import sys
from stat import *

DEST_PATH = "/Users/liam/test_env/diff_server/c"
SOURCE_PATH = "/Users/liam/test_env/diff_server/b"
FULL_NAME = 'full_name'
PERM = 'permissions'
OWNER = 'owner'
GROUP = 'group'
ISFILE = 'is_file'

files_2_ignore = [".ipynb_checkpoints", "Untitled.ipynb"]


def get_perm(item):
    # return int
    perm = oct(os.stat(item)[ST_MODE])[-3:]
    return perm


def get_owner(item):
    # return int
    owner = oct(os.stat(item)[ST_UID])[-3:]
    return owner


def is_file(path):
    # return boolean
    is_file_b = os.path.isfile(path)
    return is_file_b


def get_group(item):
    # return int
    group = oct(os.stat(item)[ST_GID])[-3:]
    return group


def show_bad_files(file_list):
    # displays the diff files
    for item in file_list:
        cmd = "ls -l " + item[FULL_NAME]
        os.system(cmd)


def get_name_from_path(path):
    # return str
    name = path.split('/')[-1]
    return name


def set_permissions(src_file):
    dest_file = DEST_PATH + src_file.replace(SOURCE_PATH, '')
    perm = get_perm(src_file)
    print type(perm), perm

    try:
        print "setting permission: %s for %s" % (perm, dest_file)
        os.chmod(dest_file, perm)
    except Exception as e:
        raise e


def set_owner_group(src_file):
    dest_file = DEST_PATH + src_file.replace(SOURCE_PATH, '')
    owner = get_owner(src_file)
    group = get_group(src_file)

    try:
        print "setting owner: %s and group: %s for %s" % (owner, group, dest_file)
        os.chown(dest_file, owner, group)
    except Exception as e:
        raise e


def get_md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def copy_missing_file(src_file):
    # will create dir path if needed
    dest_file = DEST_PATH + src_file.replace(SOURCE_PATH, '')

    try:
        shutil.copy2(src_file, dest_file)
    except IOError as e:
        # ENOENT(2): file does not exist, raised also on missing dest parent dir
        if e.errno != errno.ENOENT:
            raise
        # try creating parent directories
        os.makedirs(os.path.dirname(dest_file))
        shutil.copy2(src_file, dest_file)


def get_dir_tree(path):
    # return dict of dict
    dir_tree = {}
    for root, directories, filenames in os.walk(path):

        for filename in filenames:
            if filename not in files_2_ignore:
                full_name = os.path.join(root, filename)

                curr_item = {
                    FULL_NAME: full_name,
                    PERM: get_perm(full_name),
                    OWNER: get_owner(full_name),
                    GROUP: get_group(full_name),
                    ISFILE: is_file(full_name)
                }

                short_name = full_name.replace(path, '')
                dir_tree[short_name] = curr_item

    return dir_tree


def compare_1_dir(target_path):

    duplicate_files = {
        'filename'
    }

    to_check = get_dir_tree(target_path)

    for file_key, file_value in to_check.iteritems():
        print file_key, to_check[file_key][ISFILE]
        print(get_md5(to_check[file_key][FULL_NAME]))

    diffs = {
        'duplicate': duplicate_files,
    }

    return diffs


def compare_2_dirs(target_path, source_path):
    # return list of dict
    # checks if files are missing from A

    missing_files = []
    different_files = []

    to_check = get_dir_tree(target_path)
    compare_with = get_dir_tree(source_path)

    print "============= Comparing Two Directories ================"
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
        'different': different_files,
    }

    return diffs


if __name__ == '__main__':

    my_target = DEST_PATH
    my_source = SOURCE_PATH

    if len(sys.argv) == 2:
        print "TARGET: %s" % my_target
        my_diffs = compare_1_dir(my_target)
        print "Duplicate files in target:", len(my_diffs['duplicate'])
        #show_bad_files(my_diffs['duplicate'])
        print "================ Results ================"
    elif len(sys.argv) == 3:
        my_target = sys.argv[1]
        my_source = sys.argv[2]
        print "TARGET: %s SOURCE: %s " % (my_target, my_source)
        my_diffs = compare_2_dirs(my_target, my_source)
        print "================ Results ================"
        print "Missing files from origin:", len(my_diffs['missing'])
        show_bad_files(my_diffs['missing'])
        print "Different files in source:", len(my_diffs['different'])
        show_bad_files(my_diffs['different'])
    else:
        print "Missing source path!"
        exit(1)


    #
    # for i in my_diffs['missing']:
    #     copy_missing_file(i[FULL_NAME])
    #
    # for i in my_diffs['different']:
    #     set_permissions(i[FULL_NAME])
    #     set_owner_group(i[FULL_NAME])
