import sys
from PIL import Image
import StringIO
import struct
import os

prependTag = "thumbnail_"
maxHeight_2x = 300.0

def main():    
    imgPath = '/Users/sunilkumar/Documents/MomJWebsite/local/Photos_Project/Paintings_Usable/FullSize'
    imageFileNames = []
    writeStrs = []

    for root, dirs, files in os.walk(imgPath):
        for name in files:
            imageFileNames.append(os.path.join(root, name))
    for imgFile in imageFileNames:
        try:
            img = Image.open(imgFile)
            width, height = img.size
            scaleFactor = maxHeight_2x/height

            newW_2x = int(width * scaleFactor)
            newH_2x = int(height * scaleFactor)
            
            newW_1x = int(width * scaleFactor)/2
            newH_1x = int(height * scaleFactor)/2
            
            baseNameOnly = prependTag + os.path.basename(imgFile.split(".")[0])
    #<canvas id="thumbnail_Blossom" height="231" width="157" largeH='576' largeW='392' style="cursor: pointer;z-index: 9;">

            writeStr = "<canvas id=\"" + baseNameOnly + "\" "
            writeStr += "height=\"" + str(newH_2x) + "\" "
            writeStr += "width=\"" + str(newW_2x) + "\" "
            writeStr += "largeH=\"" + str(newH_1x) + "\" "
            writeStr += "largeW=\"" + str(newW_1x) + "\" "
            writeStr += "style=\"cursor: pointer;z-index: 9;\">"
            writeStrs.append(writeStr)
        except Exception, e:
            print str(e)
    # Open a file
    fo = open(os.path.join(imgPath, "foo.txt"), "wb")
    for wStr in writeStrs:
        print "Writing: '%s'"%(wStr)
        fo.write(wStr + '\n')
    # Close opend file
    fo.close()


if __name__ == "__main__":
    main()