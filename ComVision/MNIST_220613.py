import cv2
from keras.models import load_model
import numpy as np

if __name__ == "__main__":
#
    filename = "C:/Users/AI-00/PycharmProjects/Tensorflow-gpu-2.6/mnist_data/my_MNIST_CNN.h5"
    model = load_model(filename)
    # model.summary()

    ###################################################################################################################
    src = cv2.imread("number.png")
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    print(src.shape)

    w_width = 150
    w_height = 150

    for y in range(40, gray.shape[0], 170):
        for x in range(0, gray.shape[1], 5):
            crop = gray[y:y + w_width, x:x + w_width]
            view = crop.copy()
            view = cv2.cvtColor(view, cv2.COLOR_GRAY2BGR)
            test_img = cv2.erode(crop, None, iterations=2)
            _, test_img = cv2.threshold(test_img, 0, 255, cv2.THRESH_OTSU)
            test_img = 255-test_img
            test_img = cv2.resize(test_img, (28, 28))
            cv2.imshow("resize", test_img)
            test_img = np.expand_dims(test_img, axis=0)
            test_img = np.expand_dims(test_img, axis=-1)
            # print(resizeImg.shape)

            prediction = model.predict(test_img)
            # print(prediction[0])
            # print(max(prediction[0]))
            index = prediction[0].argmax()
            if prediction[0][index] > 0.9:
                cv2.putText(view, f"{index}", (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, color=[0, 0, 255], thickness=1)

            cv2.imshow("crop_img", view)
            key = cv2.waitKey(1)

            if key == 27:  # esc
                cv2.destroyAllWindows()
                exit(0)