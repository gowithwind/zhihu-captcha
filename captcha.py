#coding=utf-8
import random
import string
import sys
import math
from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageOps
from io import BytesIO


#字体的位置，不同版本的系统会有不同
font_path = 'simsun.ttc'
#生成几位数的验证码
number = 8
#生成验证码图片的高度和宽度
size = (200,30)
#背景颜色，默认为白色
bgcolor = (255,255,255)
#字体颜色，默认为蓝色
fontcolor = (0,0,255)

#用来随机生成一个字符串
def gene_text():
    source = list('用来随机生成一个字符串')
#     for index in range(0,10):
#         source.append(str(index))
    print(source)
    return ''.join(random.sample(source,number))#number是生成验证码的位数

#生成验证码
def gene_code():
    width,height = size #宽和高
    image = Image.new('RGBA',(width,height),bgcolor) #创建图片
    font = ImageFont.truetype(font_path,25) #验证码的字体
    draw = ImageDraw.Draw(image)  #创建画笔
    text = gene_text() #生成字符串
    print(text)
    font_width, font_height = font.getsize(text)
    # print(font_width, font_height)
    draw.text((0, (height - font_height) / 2),text,\
            font= font,fill=fontcolor) #填充字符串
    flip = random.sample([i for i in range(number)],2)
    flip.sort()
    mw = int(font_width/number)
    for i in flip:
        box = [i*mw,0,(i+1)*mw,30]
        region = image.crop(box)
        region = region.transpose(Image.ROTATE_180)
        image.paste(region, box)
    # image.save('idencode.gif') #保存验证码图片
    output = BytesIO()
    image.save(output, format="GIF")
    return flip, output.getvalue()
