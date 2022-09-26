import cv2


def yolo2bbox(x, y, w, h, img_w, img_h):
    x = x * img_w
    y = y * img_h
    w = w * img_w
    h = h * img_h
    x1, y1 = x - w / 2, y - h / 2
    x2, y2 = x + w / 2, y + h / 2
    return [x1, y1, x2, y2]



if __name__ == '__main__':

    for i in range(1, 91):
        img = cv2.imread('data/HTP_house/HTP_house_' + str(i) + '.png')
        img_w = img.shape[1]
        img_h = img.shape[0]


        with open("data/HTP_house/HTP_house_" + str(i) + ".txt", "r") as f:
            text = f.read().split()
        for i in range(len(text)):
            text[i] = float(text[i])

        text = yolo2bbox(text[1], text[2], text[3], text[4], img_w, img_h)
        print(text)

        img = cv2.rectangle(img, (int(text[0]), int(text[1])), (int(text[2]), int(text[3])), (255, 0, 0), 1)

        cv2.imshow('rectangle', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()