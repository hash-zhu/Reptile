# https://gitee.com/ityunjie/teaskill/blob/gh-photo/01.jpg
# D:\Git-Space\teaskill
import os
import csv


#
# git_url = "https://gitee.com/ityunjie/teaskill/raw/gh-photo/"
# list_dir = os.listdir ("D:/Git-Space/teaskill/")
# print (list_dir)
# # list_dir = [name.endswith("jpg" or "png") for name in list_dir]
# list_name = []
# for name in list_dir:
#     if name.endswith ("jpg"):
#         list_name.append (name)
#     if name.endswith ("png"):
#         list_name.append (name)
#
# print (list_name)
# with open ("path_url.txt", mode="w", newline='\n') as f:
#     csvWriter = csv.writer (f)
#     for name in list_name:
#         line = git_url + name + "\n"
#         f.write (str (line))
# print ("OVER!")


# def dome(filename: list, new_path: str) -> str:
def dome(path: str, savePathName: str, url: str) -> str:
    path_name = os.listdir(path)
    list_url = []
    # print(path_name)
    with open(savePathName, mode="w", newline="\n") as f:
        for name in path_name:
            f.write(url + name + "\n")
        return 'over'


if __name__ == '__main__':
    tea_skill_savePathName = "tea_skill_url.txt"
    tea_skill_file_savePathName = "tea_skill_file_url.txt"

    bc_savePathName = "bc_url.txt"
    bc_file_savePathName = "bc_file_url.txt"

    xy_savePathName = "xy_url.txt"
    xy_file_savePathName = "xy_file_url.txt"

    xy_path = "F:/----------------------------------------------------/听说/"
    bc_path = "F:/----------------------------------------------------/Baicang/"
    tea_skill_path = "F:/----------------------------------------------------/茶守艺上传图/茶守艺上传图/"

    xy_url = "https://xiya-1306375610.cos.ap-beijing.myqcloud.com/images/"
    xy_file_url = "https://xiya-1306375610.file.myqcloud.com/images/"

    bc_url = "https://baicang-1306375610.cos.ap-chengdu.myqcloud.com/images/"
    bc_file_url = "https://baicang-1306375610.file.myqcloud.com/images/"

    tea_skill_url = "https://teaskill-data-1306375610.cos.ap-nanjing.myqcloud.com/images/"
    tea_skill_file_url = "https://teaskill-data-1306375610.file.myqcloud.com/images/"

    print(dome(xy_path, xy_savePathName, xy_url))
