from PIL import Image
x = 503
y = 122 #y坐标    只需要保证 x * y = 行数  就ok

im = Image.new("RGB",(x,y))#创建图片
file = open('C:/Users/HP/Desktop/1.txt') #打开rbg值文件

#通过一个个rgb点生成图片
for i in range(0,x):
  for j in range(0,y):
    line = file.readline()#获取一行
    rgb = line.split(",")#分离rgb
    im.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2])))#rgb转化为像素
im.show()
