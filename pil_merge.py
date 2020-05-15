#!/usr/bin/python
# -*- coding: utf-8 -*-


import math
from PIL import Image

column = 3
width = 802
height = 286
size = (802, 286)

list_im = [r'D:\python\code\code.png', r'D:\python\code\code.png', r'D:\python\code\code.png', r'D:\python\code\code.png', 
           r'D:\python\code\code.png', r'D:\python\code\code.png', r'D:\python\code\code.png', r'D:\python\code\code.png',
           r'D:\python\code\code.png']
list_im = list_im
imgs = [Image.open(i) for i in list_im]

row_num = math.ceil(len(imgs)/column)
target = Image.new('RGB', (width*column, height*row_num))
for i in range(len(list_im)):
    if i % column == 0:
        end = len(list_im) if i + column > len(list_im) else i + column 
        for col, image in enumerate(imgs[i:i+column]):
            target.paste(image, (width*col, height*(i//column), 
                                 width*(col + 1), height*(i//column + 1)))   
target.show()
target.save('D:\python\code\code2.png')