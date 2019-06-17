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
GAP = "==========================================================\n"
SCAN_TYPE = {'full': 2, 'md5': 1, 'name': 0}  # TODO: add scan type
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

files_2_ignore = [".ipynb_checkpoints", "Untitled.ipynb", ".DS_Store"]


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

def execute_cmd(fullname):
    # Executes the CMD command
    cmd = "ls -l '{}'".format(fullname)
    status, output = commands.getstatusoutput(cmd)
    print "- Execute CMD :", cmd

    if status is not 1:
        # print "- output:", output
        res = output.split(' ')
        return res
    else:
        return False


def get_file_md5(fname):
    # return string
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def print_duplicates(file_dict):
    # displays the dup files
    print "================ Printing Duplicates ================"
    print GAP

    for key, values in file_dict.iteritems():
        print "==> %s: %s" % (key, values)


def get_dir_tree(path):
    # returns dict of dicts
    dir_tree = {}
    print "============= Getting Dir Tree ================"
    print GAP

    # Prepare dict of items with: 'full_name' and 'short_name'
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            if filename not in files_2_ignore:  # NOT WORKING
                full_name = root + "/" + filename
                short_name = full_name.replace(path, '')

                # Get list of file attributes
                res = execute_cmd(full_name)

                dir_tree[short_name] = {
                    # KEY: short_name,
                    ISFILE: is_file(full_name),
                    FULL_NAME: full_name,
                    MD5: get_file_md5(full_name),
                    # PERM: res[0],
                    # OWNER: res[2],
                    # GROUP: res[4],
                    # SIZE: res[6],
                    # DATE: res[8:11],
                }

                # print "- Attributes  :", dir_tree[short_name][OWNER],
                # dir_tree[short_name][PERM],dir_tree[short_name][MD5]

    print "- Dir tree len:", len(dir_tree)
    return dir_tree


def compare_1_dir(target_path):
    # returns dict of dicts
    c = 0
    duplicate_files = {}
    target_dir_tree = get_dir_tree(target_path)
    print "=============  Comparing One Directory ================"
    print GAP

    # Create md5 map of files
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

    # Print Duplicates
    for key_md5, v in duplicate_files.iteritems():
        if len(duplicate_files[key_md5]) > 1:
            print "===> dup file {}: {}".format(key_md5, v)
            c += 1

    print "- Total Duplicates:", c
    return duplicate_files


def compare_2_dirs(target_path, source_path):
    # return dict of dict
    # checks if files are missing from target
    target_dir_tree = get_dir_tree(target_path)
    source_dir_tree = get_dir_tree(source_path)
    missing_files = {}
    different_files = {}
    print "============= Comparing Two Directories ================"
    print GAP

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

    # Defaults
    DEST_PATH = "/Users/liam/test_env/diff_server/c"
    SOURCE_PATH = "/Users/liam/test_env/diff_server/b"

    my_target = DEST_PATH
    my_source = SOURCE_PATH
    scan_type = 1

    if len(sys.argv) == COMPARE_2_DIRS:
        my_target = sys.argv[1], my_source = sys.argv[2]
        print GAP, "- Checking for duplicates between TARGET: %s SOURCE: %s " % (my_target, my_source)
        print GAP
        my_missing_files, my_different_files = compare_2_dirs(my_target, my_source)
        # print "================ Results ================"
        # print "Missing files from origin: %s" % len(my_missing_files)
        # show_bad_files(my_missing_files)
        # print "Different files in source: %s" % len(my_different_files)
        # show_bad_files(my_different_files)
    elif len(sys.argv) == COMPARE_1_DIRS:  # Checking for duplicates in a single directory
        my_target = sys.argv[1]
        print GAP, "- Checking for duplicates in target path: %s" % my_target
        print GAP
        my_duplicate_files = compare_1_dir(my_target)  # scan_type)
        # print_duplicates(my_duplicate_files)
    else:
        print "Missing target path!"
        exit(1)
