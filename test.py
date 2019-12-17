import cv2
import os
import numpy as np
pic_root = "./facades"
train_list = os.listdir(os.path.join(pic_root,"train"))
for each_pic in train_list:
    pic_path = os.path.join(pic_root,"train",each_pic)
    my_pic = cv2.imread(pic_path)
    cv2.imshow("result",my_pic)
    cv2.waitKey()
    break
