import numpy as np
import cv2


def write(txt):
    mp = max(list(map(lambda x: len(x), txt)))

    scaley = 68
    h = 100 + len(txt) * scaley
    w = mp * 45

    img = np.zeros((h, w, 3), np.uint8)

    font = cv2.FONT_HERSHEY_SIMPLEX

    fontScale = 2
    lineType = 2

    for sidx in range(len(txt)):
        st = txt[sidx]
        off = sidx * scaley
        cv2.putText(img, st,
                    (60, off + 100),
                    font,
                    fontScale,
                    (255, 255, 255),
                    lineType)

    cv2.imwrite("out.jpg", img)


if __name__ == "__main__":
    write(['turn', 'on the computer', 'and toaster'])
