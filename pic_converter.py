#!/usr/bin/python3

import sys
from PIL import Image
import json


def getPxs(filenameIn):
    srcImg = Image.open(filenameIn)
    pxs = srcImg.load()
    if(srcImg.height != 11):
        raise Exception("Image has to have a size of 11")
    pxsar = []
    for x in range(srcImg.width):
        col = []
        for y in range(srcImg.height):
            col.append(pxs[x,y])
        pxsar.append(col)
    return pxsar

        

if __name__ == "__main__": 
    if(len(sys.argv) < 4):
        print("Usage: python3 {} pathToImageFile pathToSave name".format(sys.argv[0]))
        exit()
    filenameIn = sys.argv[1]
    filenameOut = sys.argv[2]
    name = sys.argv[3]

    pxs = getPxs(filenameIn)
    data = {"name": name, "pxs": pxs}
    with open("{}.json".format(filenameOut), "w") as fo:
        fo.write(json.dumps(data, indent=4))



