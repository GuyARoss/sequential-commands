import numpy as np
import cv2

# @@ des wrong
YELLOW = (255, 215, 51)
RED = (255, 51, 51)
ORANGE = (255, 87, 51)
GREEN = (51, 255, 97)


def get_color_mapping(color_str):
    return {
        'yellow': YELLOW,
        'red': RED,
        'orange': ORANGE,
        'green': GREEN,
    }[color_str]


def write(txt):
    mp = map(lambda x: x[0], txt)
    w = " ".join(mp)

    img = np.zeros((300, len(w * 30), 3), np.uint8)

    font = cv2.FONT_HERSHEY_SIMPLEX

    fontScale = 2
    lineType = 2

    offset = 60
    for idx in range(len(txt)):
        i = txt[idx]
        color = get_color_mapping(i[1])
        f = len(i[0]) * 30

        cv2.putText(img, i[0],
                    (len(i[0]) + 20 + offset + (idx * 15), 150),
                    font,
                    fontScale,
                    color,
                    lineType)

        offset += f

    cv2.imshow("img", img)
    cv2.imwrite("out.jpg", img)


if __name__ == "__main__":
    write([
        ('this', 'green'),
        ('is', 'yellow'),
        ('a', 'orange'),
        ('test', 'red'),
        ('to', 'orange'),
        ('see', 'yellow'),
        ('if', 'yellow'),
        ('the', 'orange'),
        ('colors', 'red'),
        ('are', 'orange'),
        ('working', 'yellow'),
    ])
