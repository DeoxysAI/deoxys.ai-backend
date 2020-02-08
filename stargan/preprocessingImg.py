from PIL import Image
import sys
import os


image = Image.open(os.path.abspath(os.path.dirname(sys.argv[0]))+'/images/'+sys.argv[1])
image = image.resize((128, 128))
image = image.save('newImg.jpg')

with open(os.path.abspath(os.path.dirname(sys.argv[0]))+'/attributes.txt', 'r') as f:
    attr = list(map(str, f.readline().split()))
    convert = [-1 for i in range(len(attr))]
    sel_attr = sys.argv[2].split()
    for i in range(len(attr)):
        for j in sel_attr:
            if attr[i] == j:
                convert[i] = 1
    with open('newAttr.txt', 'w') as f2:
        f2.write(str(1))
        f2.write('\n')
        for i in attr:
            f2.write(str(i) + ' ')
        f2.write('\n')
        f2.write('newImg.jpg ')
        for i in convert:
            f2.write(str(i)+' ')

    

