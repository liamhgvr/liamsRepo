# dir_compare
import hashlib
import os
import shutil
import errno
import subprocess
import sys
import commands
from stat import *

COMPARE_2_DIRS = 3
COMPARE_1_DIRS = 2

DEST_PATH = "/Users/liam/test_env/diff_server/c"
SOURCE_PATH = "/Users/liam/test_env/diff_server/b"
FULL_NAME = 'full_name'
SHORT_NAME = 'short_name'
KEY = 'key'
PERM = 'permissions'
OWNER = 'owner'
GROUP = 'group'
SIZE = 'size'
DATE = 'date'
MD5 = 'md5'
ISFILE = 'is_file'

files_2_ignore = [".ipynb_checkpoints", "Untitled.ipynb"]


def is_file(path):
    # return boolean
    is_file_b = os.path.isfile(path)
    return is_file_b


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


def print_duplicates(file_dict):
    # displays the dup files
    print "================ Results ================"
    for key, values in file_dict.iteritems():
        print "==> %s: %s" % (key, values)


def get_dir_tree(path):
    # returns dict of dicts
    dir_tree = {}

    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            if filename not in files_2_ignore:
                full_name = os.path.join(root, filename)
                short_name = full_name.replace(path, '')

                cmd = "ls -l " + full_name
                status, output = commands.getstatusoutput(cmd)
                res = output.split(' ')
                res = filter(None, res)

                curr_item = {
                    KEY: short_name,
                    FULL_NAME: full_name,
                    PERM: res[0],
                    OWNER: res[2],
                    GROUP: res[3],
                    SIZE: res[4],
                    MD5: get_file_md5(full_name),
                    # DATE: res[8:11],
                    ISFILE: is_file(full_name),
                }
                
                print "- %s ==> %s" % (short_name, curr_item)
                dir_tree[short_name] = curr_item

    return dir_tree


def compare_1_dir(target_path):
    # returns dict of dicts
    duplicate_files = {}
    target_dir_tree = get_dir_tree(target_path)

    # Create md5 map of files
    print "Scanning %s..." % target_path
    for file_key, file_values in target_dir_tree.iteritems():
        if file_values[ISFILE]:
            curr_md5 = file_values[MD5]
            # Check for duplicates
            if curr_md5 in duplicate_files.keys():
                duplicate_files[curr_md5].append(file_key)
            else:
                duplicate_files[curr_md5] = [file_key]
        else:
            print "%s is a directory" % file_key

    # Clean non dups
    for key_md5 in duplicate_files.iterkeys():
        if len(duplicate_files[key_md5]) == 1:
            duplicate_files.Remove(key_md5)

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
        my_target = sys.argv[1], my_source = sys.argv[2]
        print "TARGET: %s SOURCE: %s " % (my_target, my_source)
        my_missing_files, my_different_files = compare_2_dirs(my_target, my_source)
        # Printing results
        # print "================ Results ================"
        # print "Missing files from origin: %s" % len(my_missing_files)
        # show_bad_files(my_missing_files)
        # print "Different files in source: %s" % len(my_different_files)
        # show_bad_files(my_different_files)
    # Compering a single directory
    elif len(sys.argv) == COMPARE_1_DIRS:
        # Getting directory path
        my_target = sys.argv[1]
        print "TARGET: %s" % my_target
        my_duplicate_files = compare_1_dir(my_target)
        print_duplicates(my_duplicate_files)
    else:
        print "Missing target path!"
        exit(1)
