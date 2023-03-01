
import os
import cv2
for filename in os.listdir("./"):
    if filename.endswith(".pgm"):
        input_path = filename
        output_path =  os.path.splitext(filename)[0] + ".png"
        img=cv2.imread(input_path)
        cv2.imwrite(output_path,img)
