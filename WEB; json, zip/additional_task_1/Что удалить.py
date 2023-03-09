import os
from collections.abc import Iterable


def human_read_format(size):
    list_word = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    index = 0
    while size >= 1024:
        size /= 1024
        index += 1
    return str(round(size)) + list_word[index]


def flatten(a):
    for el in a:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


def file_sizes(path):
    global number_slash, l
    list_size_files = []
    list_name_files = []
    list_catalog = []
    for i_elem in os.listdir(path):
        if os.path.isfile(os.path.abspath(os.path.join(path, i_elem))):
            file_path = os.path.abspath(os.path.join(path, i_elem))
            file_size = os.path.getsize(file_path)
            list_size_files.append(file_size)
            if len(file_path.split("\\")) > number_slash:
                if file_path.split("\\")[number_slash - 1] not in list_catalog:
                    list_catalog.append(file_path.split("\\")[number_slash - 1])
                    l = list_catalog
            else:
                list_name_files.append(file_path.split("\\")[number_slash - 1])
        else:
            result = file_sizes(os.path.abspath(os.path.join(path, i_elem)))
            list_size_files.append(result[0])
            list_name_files.append(*l)
    return list_size_files, list_name_files

l = ""
path = os.path.abspath(os.path.join(input()))
number_slash = len(path.split("\\")) + 1
result = file_sizes(path)
res = []
for i in range(len(result[1])):
    if type(result[0][i]) == list and type(result[0][i]) != int:
        result[0][i] = list(flatten(result[0][i]))
        res.append([result[1][i], sum(result[0][i])])
    else:
        result_sum = human_read_format(result[0][i])
        res.append([result[1][i], result[0][i]])
res = sorted(res, key=lambda x: x[1], reverse=True)
for n, i in enumerate(res):
    if n <= 9:
        print(i[0], "\t", "\t", "-----", human_read_format(i[1]))