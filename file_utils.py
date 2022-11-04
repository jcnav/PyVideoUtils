import os
from os import path as osPath


def new_name_exist_file_split(path_file, local_name_file):
    if osPath.exists(osPath.join(path_file, local_name_file)):
        numb = 1
        while True:
            new_name = "{0}_{2}{1}".format(*osPath.splitext(local_name_file) + (numb,))

            if osPath.exists(osPath.join(path_file, new_name)):
                numb += 1
            else:
                return new_name
    return local_name_file


def new_name_exist_file(full_name_file):
    """
    If the file name exists, should generate the name with subindex. Cannot be repeated in the file system
    :param full_name_file:
    :return: full_name_file if the fine name doesn't exist or file_1.ext or file_2.ext depending on the existence
    in the file system
    """
    if osPath.exists(full_name_file):
        path_file, local_name_file = split_path_and_name_file(full_name_file)
        numb = 1
        while True:
            new_name = "{0}_{2}{1}".format(*osPath.splitext(local_name_file) + (numb,))

            if osPath.exists(osPath.join(path_file, new_name)):
                numb += 1
            else:
                return os.path.join(path_file, new_name)
    return full_name_file


def split_path_and_name_file(full_name_file):
    """
    split absolute path in relative path and file name
    :param full_name_file:
    :return: path_file and name_file
    """
    head_tail = os.path.split(full_name_file)
    return head_tail[0], head_tail[1]


def build_output_name_file(org_name_file, suffix):
    head_tail = os.path.splitext(org_name_file)
    return head_tail[0]+"_"+suffix+head_tail[1]
