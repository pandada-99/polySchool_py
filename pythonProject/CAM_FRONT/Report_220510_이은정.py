import json

def filter_def(list):
    for i in list:
        if not (list["class"] == "Dontcare" or list["level"] > 0):
            return i


if __name__=='__main__':
    for i in range(10):
        f = open("00000"+str(i)+".json")
        json_data = json.load(f)
        filename = "00000"+str(i)

        new_list = filter(filter_def, json_data["Object"])
        # print(list(new_list))
        json_data["Object"] = list(new_list)

        for i in json_data["Object"]:
            if i["class"] == 'Truck' or i["class"] == 'Car':
                i["class"] = 'Vehicle'

        f.close()

        f = open("modified_" + filename + ".json", "w")
        json.dump(json_data, f, indent="\t")
        f.close()