import json


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


im = Image.open('C:/Users/AI-00/PycharmProjects/startUpProject/json/8.json')
w = int(im.size[0])
h = int(im.size[1])

with open("labelme.json", "r") as json_file:
    json_data = json.load(json_file)

xmin, ymin = json_data['shapes'][0]['points'][0]
xmax, ymax = json_data['shapes'][0]['points'][1]

print(xmin, xmax, ymin, ymax)  # define your x,y coordinates (Labelme)

b = (xmin, xmax, ymin, ymax)

yolo = convert((w, h), b)