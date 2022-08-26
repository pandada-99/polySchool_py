# 220510 AI기초프로그래밍(신교수님)
import glob
import json
import os

# f = open("./CAM_FRONT/000000.json")
# json_data = json.load(f)
#
# # for i in json_data["Object"]:
# #     print(i)
# # print()
#
# # print(json_data["Object"][0]["level"])
# # print(json_data["Object"][0]["class"])
#
# # for i in json_data["Object"]:
# #     if json_data["Object"][i]["level"] > 0 or json_data["Object"][i]["class"] == "Dontcare":
# #         print(json_data["Object"][i])
#
# # for i in json_data["Object"]:
# #    if i["class"] == "Dontcare" or i["level"] > 0:
# #        json_data["Object"].remove(i)
#
# def filter_def(list):
#     for i in list:
#         if not(list["class"] == "Dontcare" or list["level"] > 0):
#             return i
#
# new_list = filter(filter_def, json_data["Object"])
# # print(list(new_list))
# json_data["Object"] = list(new_list)
#
# for i in json_data["Object"]:
#     if i["class"] == 'Truck' or i["class"] == 'Car':
#         i["class"] = 'Vehicle'
#
# for i in json_data["Object"]:
#     print(i)
#
# # a = [1, 2, 3, 4, 5, 6]
# # a_new = filter(lambda i: i > 3, a)
# # a_new = list(a_new)
# # print(a_new)
#
#
# ################################### 수정 파일 저장하기 ####################################################################
# f.close()
#
# f = open("./CAM_FRONT/modified_000000.json", "w")
# json.dump(json_data, f, indent="\t")
# f.close()


for i in range(10):
    f = open("./CAM_FRONT/00000"+str(i)+".json")
    json_data = json.load(f)
    filename = "00000"+str(i)


    def filter_def(list):
        for i in list:
            if not (list["class"] == "Dontcare" or list["level"] > 0):
                return i


    new_list = filter(filter_def, json_data["Object"])
    # print(list(new_list))
    json_data["Object"] = list(new_list)

    for i in json_data["Object"]:
        if i["class"] == 'Truck' or i["class"] == 'Car':
            i["class"] = 'Vehicle'

    f.close()

    f = open("./CAM_FRONT/modified_" + filename + ".json", "w")
    json.dump(json_data, f, indent="\t")
    f.close()