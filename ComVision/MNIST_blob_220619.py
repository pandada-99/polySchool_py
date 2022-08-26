import cv2
from keras.models import load_model
import numpy as np

# 모델 input -> (0, 28, 28, 0), 배경 검정색, 숫자 흰색, 정규화(나누기 255)하기
if __name__ == "__main__":
    filename = "C:/Users/AI-00/PycharmProjects/ComVision/mnist_model.h5"
    model = load_model(filename)
    # model.summary()

    ###################################################################################################################
    src = cv2.imread("number.png")
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    test_img = cv2.erode(gray, None, iterations=2)
    _, test_img = cv2.threshold(test_img, 0, 255, cv2.THRESH_OTSU)
    # cv2.imshow("view_threshold", test_img)
    # key = cv2.waitKey(0)
    # if key == 27:  # esc
    #     cv2.destroyAllWindows()
    test_img = 255-test_img

    # 블롭 구하기
    n_blob, label_img, stats, centroids = cv2.connectedComponentsWithStats(test_img)
    print(n_blob) # 총 blob 갯수
    blob = []
    for i in range(1, n_blob):
        if (stats[i][3]) > 50:
            blob.append(stats[i][:4])

    # crop = test_img[blob[1][1]:(blob[1][1] + blob[1][3]), blob[1][0]:(blob[1][0] + blob[1][2])]
    # cv2.imshow("crop_img", crop)
    for i in range(len(blob)):
        crop = test_img[blob[i][1]:(blob[i][1]+blob[i][3]), blob[i][0]:(blob[i][0]+blob[i][2])]

        # 1 처럼 (28, 28)로 만들때 찌그러지는 애들은 border 주기
        if ((blob[i][1] + blob[i][3]) - blob[i][1]) > 4 * ((blob[i][0] + blob[i][2]) - blob[i][0]):
            crop = test_img[blob[i][1]:(blob[i][1]+blob[i][3]), blob[i][0]-50:(blob[i][0]+blob[i][2])+50]
            # cv2.imshow("crop_img", crop)
            # cv2.waitKey(0)

        view = crop.copy()
        view = 255-view
        view = cv2.cvtColor(view, cv2.COLOR_GRAY2BGR)
        # cv2.imshow("crop_img", crop)
        # key = cv2.waitKey(0)
        # if key == 27:  # esc
        #     cv2.destroyAllWindows()

        # crop = 255-crop
        crop = cv2.resize(crop, (28, 28))
        crop = crop / 255
        cv2.imshow("resize_img", crop)
        crop = np.expand_dims(crop, axis=0)
        crop = np.expand_dims(crop, axis=-1)

        prediction = model.predict(crop)
        index = prediction[0].argmax()
        cv2.putText(view, f"{index}", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, color=[0, 0, 255], thickness=3)

        cv2.imshow("view_img", view)
        key = cv2.waitKey(0)
        if key == 27:  # esc
            cv2.destroyAllWindows()

    # 블롭을 화면에 show
    # n_blob : 0 은 배경이므로 뺀다.
    show_img = src.copy()
    for i in range(1, n_blob):
        x, y, w, h, area = stats[i]
        # 너무 작은 블롭은 제외한다.
        if area > 50:
            cv2.rectangle(show_img, (x, y, w, h), (255, 0, 255), thickness=2)

    cv2.imshow("blob_img", show_img)
    key = cv2.waitKey(0)

    if key == 27:  # esc
        cv2.destroyAllWindows()
        exit(0)