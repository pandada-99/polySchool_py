import cv2


if __name__ == '__main__':
    cascade_filename = "data/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_filename)

    src = cv2.imread("image/wonwoo2.jpg")
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Gray", gray)

    result = cascade.detectMultiScale(gray,
                                      scaleFactor=1.2,
                                      minNeighbors=1,
                                      minSize=(25, 25))
    print(result)

    for box in result:
        x, y, w, h = box
        cv2.rectangle(src, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
    cv2.imshow("img", src)

    cv2.waitKey(0)
    cv2.destroyAllWindows()