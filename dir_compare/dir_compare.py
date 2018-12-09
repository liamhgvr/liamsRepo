# dir_compare
import hashlib
import os
import shutil
import errno
import sys
from stat import *

COMPARE_2_DIRS = 3
COMPARE_1_DIRS = 2

DEST_PATH = "/Users/liam/test_env/diff_server/c"
SOURCE_PATH = "/Users/liam/test_env/diff_server/b"
FULL_NAME = 'full_name'
SHORT_NAME = 'short_name'
PERM = 'permissions'
OWNER = 'owner'
GROUP = 'group'
ISFILE = 'is_file'

files_2_ignore = [".ipynb_checkpoints", "Untitled.ipynb"]


def is_file(path):
    # return boolean
    is_file_b = os.path.isfile(path)
    return is_file_b


def get_perm(item):
    # return int
    perm = oct(os.stat(item)[ST_MODE])[-3:]
    return perm


def get_owner(item):
    # return int
    owner = oct(os.stat(item)[ST_UID])[-3:]
    return owner


def get_group(item):
    # return int
    group = oct(os.stat(item)[ST_GID])[-3:]
    return group


def get_name_from_path(path):
    # return str
    name = path.split('/')[-1]
    return name


# def set_permissions(src_file):
#     dest_file = DEST_PATH + src_file.replace(SOURCE_PATH, '')
#     perm = get_perm(src_file)
#     print type(perm), perm
#
#     try:
#         print "setting permission: %s for %s" % (perm, dest_file)
#         os.chmod(dest_file, perm)
#     except Exception as e:
#         raise e


# def set_owner_group(src_file):
#     dest_file = DEST_PATH + src_file.replace(SOURCE_PATH, '')
#     owner = get_owner(src_file)
#     group = get_group(src_file)
#
#     try:
#         print "setting owner: %s and group: %s for %s" % (owner, group, dest_file)
#         os.chown(dest_file, owner, group)
#     except Exception as e:
#         raise e


def get_file_md5(fname):
    # return string
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def show_bad_files(file_list):
    # displays the diff files
    for key, value in file_list.iteritems():
        print "==> %s: %s" % (key, value)
        # cmd = "sudo ls -l " + key
        # os.system(cmd)

# def copy_missing_file(src_file):
#     # will create dir path if needed
#     dest_file = DEST_PATH + src_file.replace(SOURCE_PATH, '')
#
#     try:
#         shutil.copy2(src_file, dest_file)
#     except IOError as e:
#         # ENOENT(2): file does not exist, raised also on missing dest parent dir
#         if e.errno != errno.ENOENT:
#             raise
#         # try creating parent directories
#         os.makedirs(os.path.dirname(dest_file))
#         shutil.copy2(src_file, dest_file)


def get_dir_tree(path):
    # return dict of dict
    dir_tree = {}
    for root, directories, filenames in os.walk(path):

        for filename in filenames:
            if filename not in files_2_ignore:
                full_name = os.path.join(root, filename)
                short_name = full_name.replace(path, '').replace('/', '')

                # Get file attributes
                curr_item = {
                    SHORT_NAME: short_name,
                    PERM: get_perm(full_name),
                    OWNER: get_owner(full_name),
                    GROUP: get_group(full_name),
                    ISFILE: is_file(full_name)
                }

                dir_tree[full_name] = curr_item

    return dir_tree


def compare_1_dir(target_path):
    # return dict of dict
    duplicate_files = {}
    target_dir_tree = get_dir_tree(target_path)

    print "Scanning %s..." % target_path
    for file_key, file_values in target_dir_tree.iteritems():
        if file_values[ISFILE]:
            curr_md5 = get_file_md5(file_key)
            # Check for duplicates
            if curr_md5 in duplicate_files.keys():
                duplicate_files[curr_md5].append(file_key)
            else:
                duplicate_files[curr_md5] = [file_key]
        else:
            print "%s is a directory" % file_key

    return duplicate_files


def compare_2_dirs(target_path, source_path):
    # return dict of dict
    # checks if files are missing from target

    target_dir_tree = get_dir_tree(target_path)
    source_dir_tree = get_dir_tree(source_path)
    missing_files = {}
    different_files = {}

    print "============= Comparing Two Directories ================"
    if len(source_dir_tree.keys()) != len(target_dir_tree.keys()):
        print "Size don't match!"

    for file_key in source_dir_tree:

        # check for missing files
        if file_key not in target_dir_tree.keys():
            print "moving %s to missing files dict" % file_key
            missing_files[file_key] = source_dir_tree[file_key]

        # check for different in files
        elif source_dir_tree[file_key][PERM] != target_dir_tree[file_key][PERM] or \
                source_dir_tree[file_key][OWNER] != target_dir_tree[file_key][OWNER] or \
                source_dir_tree[file_key][GROUP] != target_dir_tree[file_key][GROUP]:
            print "moving %s to different files dict - permissions" % file_key
            different_files[file_key] = source_dir_tree[file_key]

    return missing_files, different_files


if __name__ == '__main__':

    # Set test defaults
    my_target = DEST_PATH
    my_source = SOURCE_PATH

    # Compering 2 directories
    if len(sys.argv) == COMPARE_2_DIRS:
        # Getting directories paths
        my_target = sys.argv[1]
        my_source = sys.argv[2]
        print "TARGET: %s SOURCE: %s " % (my_target, my_source)
        my_missing_files, my_different_files = compare_2_dirs(my_target, my_source)
        # Printing results
        print "================ Results ================"
        print "Missing files from origin: %s" % len(my_missing_files)
        show_bad_files(my_missing_files)
        print "Different files in source: %s" % len(my_different_files)
        show_bad_files(my_different_files)
    # Compering a single directory
    elif len(sys.argv) == COMPARE_1_DIRS:
        # Getting directory path
        my_target = sys.argv[1]
        print "TARGET: %s" % my_target
        my_duplicate_files = compare_1_dir(my_target)
        # Printing results
        print "================ Results ================"
        print "Duplicate files in target: %s" % len(my_duplicate_files)
        show_bad_files(my_duplicate_files)
    else:
        print "Missing target path!"
        exit(1)
