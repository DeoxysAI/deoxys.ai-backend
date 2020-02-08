from PIL import Image
import sys
import os

image = Image.open('../images/'+sys.argv[1])
image = image.resize((128, 128))
image = image.save('newImg.jpg')

with open('attributes.txt', 'r') as f:
    attr = list(map(str, f.readline().split()))
    convert = [-1 for i in range(len(attr))]
    for i in range(len(attr)):
        if str(attr[i]) == str(sys.argv[2]):
                convert[i] = 1
    1
    with open('newAttr.txt', 'w') as f2:
        f2.write(1)
        f2.write('\n')
        f2.write('newImg.jpg')
        for i in attr:
            f2.write(i + ' ')
        f2.write('\n')
        for i in convert:
            f2.write(i+' ')


    

