# -*- coding:utf-8 -*-
# 简单示例一
import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import matplotlib.pyplot as plt
import numpy as np
# from skimage import morphology,data,color

class ImageHander:
    # def __init__(self):
    #     self.path = "C:\Users\君莫笑\PycharmProjects\pythonTest\pythonImage\zhixiao.jpg"
    '''将图片旋转45度，然后显示'''

    def Image0(self, path):
        im0 = Image.open(path)
        plt.figure("beauty")
        plt.subplot(1, 2, 1)
        plt.title("before image")
        plt.imshow(im0)
        plt.axis("off")

        im1 = im0.rotate(45)
        plt.subplot(1, 2, 2)
        plt.title("after rotate image")
        plt.imshow(im1)
        plt.axis("off")
        plt.show()

    '''创建缩略图'''

    def Image1(self, path, size):
        file, index = os.path.splitext(path)  # 将文件的文件名和拓展名分开，用于之后的保存重命名
        im1 = Image.open(path)
        plt.figure("beauty")

        plt.subplot(1, 2, 1)
        plt.title("before image")
        plt.imshow(im1)
        plt.axis("off")

        im1.thumbnail(size, Image.ANTIALIAS)  # 等比例缩放
        im1.save(file + ".thumbnail", "JPEG")
        plt.subplot(1, 2, 2)
        plt.title("after thumbnail image")
        plt.imshow(im1)
        plt.axis("off")
        plt.show()

    '''
    图片合成
    将图二合成到图一为newim1,如果图一透明才能看到结果不然最终显示图二
    '''

    def Image2(self, path1, path2):
        im1 = Image.open(path1)
        plt.figure("beauty one")

        plt.subplot(1, 3, 1)
        plt.title("The First Image")
        plt.imshow(im1)
        plt.axis("off")

        im2 = Image.open(path2)
        plt.subplot(1, 3, 2)
        plt.title("The Second Image")
        plt.imshow(im2)
        plt.axis("off")

        # newim1 = Image.alpha_composite(im1,im2)
        # newim1.show()
        # alpha为透明度
        newim2 = Image.blend(im1, im2, 0.5)
        plt.subplot(1, 3, 3)
        plt.title("The Combine Image")
        plt.imshow(newim2)
        plt.axis("off")
        plt.show()

    '''将图片像素点都乘2返回一个Image对象'''

    def Image3(self, path):
        im3 = Image.open(path)
        plt.figure("beauty")
        plt.subplot(1, 2, 1)
        plt.title("before Image")
        plt.imshow(im3)
        plt.axis("off")

        imnew = Image.eval(im3, lambda x: x * 2)
        plt.subplot(1, 2, 2)
        plt.title("after Image")
        plt.imshow(imnew)
        plt.axis("off")
        plt.show()

    '''创建图像'''

    def Image4(self):
        # 创建图像
        # 创建一个灰度图像
        newL = Image.new("L", (56, 56), 255)
        plt.figure("beauty")
        plt.subplot(1, 3, 1)
        plt.title("newL Image")
        plt.imshow(newL)
        plt.axis("off")

        # 创建一个RGb图像
        newrgb = Image.new("RGB", (56, 56), (20, 200, 45))
        plt.subplot(1, 3, 2)
        plt.title("newrgb Image")
        plt.imshow(newrgb)
        plt.axis("off")

        newrgba = Image.new("RGBA", (56, 56), (20, 200, 45, 255))
        plt.subplot(1, 3, 3)
        plt.title("newrgba Image")
        plt.imshow(newrgba)
        plt.axis("off")
        plt.show()

    '''
    其他形式创建图像
    PIL.image.fromarray(obj,mode=None)
    obj -图像的数组，类型可以是numpy.array()
    mode -如果不给出，会自动判断
    fromarray()函数实现图像的灰度化
    '''

    def Image5(self, path):
        a = Image.open(path)
        plt.figure("beauty")

        plt.subplot(1, 3, 1)
        plt.title("before image")

        plt.imshow(a)
        plt.axis("off")

        b = a.resize((156, 156))
        datab = list(b.getdata())
        obj1 = []
        obj2 = []
        for i in range(len(datab)):
            obj1.append([sum(datab[i]) / 3])  # 灰度化方法一：RGB三个分量的均值
            obj2.append([0.3 * datab[i][0] + 0.59 * datab[i][1] + 0.11 * datab[1][2]])
            # 灰度化方法2：根据亮度与RGB三个分量的对应关系：Y=0.3*R+0.59*G+0.11*B
        obj1 = np.array(obj1).reshape((156, 156))
        obj2 = np.array(obj2).reshape((156, 156))
        arrayimg1 = Image.fromarray(obj1)
        arrayimg2 = Image.fromarray(obj2)
        plt.subplot(1, 3, 2)
        plt.title("arrayimg1 image")
        plt.imshow(arrayimg1)
        plt.axis("off")

        plt.subplot(1, 3, 3)
        plt.title("arrayimg2 image")
        plt.imshow(arrayimg2)
        plt.axis("off")
        plt.show()

    '''图片上面加文字'''

    def Image6(self, path, fontpath):
        im = Image.open(path)
        plt.figure("beauty")

        plt.subplot(1, 2, 1)
        plt.title("before image")

        plt.imshow(im)
        plt.axis("off")

        im1 = im
        draw = ImageDraw.Draw(im1)
        width, height = im1.size
        # 选择文字字体和大小
        setFont = ImageFont.truetype(fontpath, 36)
        # 设置文字颜色
        fillColor = "black"
        # 写入文字
        draw.text((40, height - 100), u'宋智孝', font=setFont, fill=fillColor)

        plt.subplot(1, 2, 2)
        plt.title("after image")
        plt.imshow(im1)
        plt.axis("off")
        plt.show()

    def Image7(self, path):
        img = Image.open(path)
        plt.figure("zhixiao")
        plt.figure(num=1, figsize=(8, 5), )
        plt.title('The image title')
        plt.axis('off')  # 不显示坐标轴
        plt.imshow(img)
        plt.show()

    # 通道分离与合并
    def Image8(self, path):
        img = Image.open(path)
        gray = img.convert('L')  # 转换成灰度
        r, g, b = img.split()  # 分离三通道
        pic = Image.merge('RGB', (r, g, b))  # 合并三通道
        plt.figure("beauty")
        plt.subplot(2, 3, 1)
        plt.title('origin')
        plt.imshow(img)
        plt.axis('off')

        plt.subplot(2, 3, 2), plt.title('gray')
        plt.imshow(gray, cmap='gray'), plt.axis('off')

        plt.subplot(2, 3, 3)
        plt.title('merge')
        plt.imshow(pic)
        plt.axis('off')

        plt.subplot(2, 3, 4)
        plt.title('r')
        plt.imshow(r, cmap='gray')
        plt.axis('off')

        plt.subplot(2, 3, 5)
        plt.title('g')
        plt.imshow(g, cmap='gray')
        plt.axis('off')

        plt.subplot(2, 3, 6)
        plt.title('b')
        plt.imshow(b, cmap='gray')
        plt.axis('off')
        plt.show()

    '''裁剪图片'''

    def Image9(self, path):

        img = Image.open(path)  # 打开图像
        plt.figure("beauty")
        plt.subplot(1, 2, 1), plt.title('origin')
        plt.imshow(img), plt.axis('off')
        # box变量是一个四元组(左，上，右，下)。
        box = (80, 100, 860, 500)
        roi = img.crop(box)
        plt.subplot(1, 2, 2)
        plt.title('roi')
        plt.imshow(roi)
        plt.axis('off')
        plt.show()

    '''图片添加椒盐噪声'''

    def Image10(self, path):
        origin = Image.open(path)
        plt.figure("beauty")
        plt.subplot(1, 2, 1)
        plt.title("before title")
        plt.imshow(origin)
        plt.axis("off")

        img = np.array(Image.open(path))
        # 随机生成5000个椒盐
        rows, cols, dims = img.shape
        for i in range(5000):
            x = np.random.randint(0, rows)
            y = np.random.randint(0, cols)
            img[x, y, :] = 255

        plt.subplot(1, 2, 2)
        plt.title("after title")
        plt.imshow(img)
        plt.axis("off")
        plt.show()

    '''画灰度直方图'''

    def Image11(self, path):
        before = Image.open(path)
        plt.figure("beauty")

        plt.subplot(1, 3, 1)
        plt.title("before image")
        plt.imshow(before)
        plt.axis("off")

        covert = Image.open(path).convert('L')
        plt.subplot(1, 3, 2)
        plt.title("convertT image")
        plt.imshow(before)
        plt.axis("off")

        img = np.array(Image.open(path).convert('L'))
        plt.subplot(1, 3, 3)
        arr = img.flatten()
        n, bins, patches = plt.hist(arr, bins=256, normed=1, facecolor='blue', alpha=0.75)
        plt.title("The flatten Title")
        plt.show()

    '''画彩色图片直方图'''

    def Image12(self, path):
        img = Image.open(path)
        plt.figure("beauty")
        plt.subplot(1, 2, 1)
        plt.title("before image")
        plt.imshow(img)
        plt.axis("off")

        r, g, b = img.split()

        ar = np.array(r).flatten()
        plt.hist(ar, bins=256, normed=1, facecolor='r', edgecolor='r', hold=1)

        ag = np.array(g).flatten()
        plt.hist(ag, bins=256, normed=1, facecolor='b', edgecolor='b')

        plt.subplot(1, 2, 2)
        plt.title("after image")
        plt.imshow(img)
        plt.axis("off")
        plt.show()

    '''
    ImageEnhance模块图像增强
    亮度加强brightness用于调整图片的明暗平衡。
    对比度加强contrast用于调整图片的对比度，相当于彩色电视机的对比度调整。
    锐化度加强sharpness用于锐化/钝化图片。
    颜色加强color用于调整图片的色彩平衡
    '''

    def Image13(self, path):
        img = Image.open(path)
        img = ImageEnhance.Color(img)  # 获得色彩加强器实例
        img.enhance(1).show()
        plt.figure("beauty")
        plt.title("The ImageEnhance")
        plt.imshow(img)
        plt.show()

    '''ImageFilter模块图像滤镜'''

    def Image14(self, path):
        img = Image.open(path)
        plt.figure("beauty")
        plt.subplot(4, 3, 1)
        plt.title('origin')
        plt.imshow(img)
        plt.axis('off')
        # img.resize((width/2,height/2))
        # img = img.filter(ImageFilter.SHARPEN)
        img1 = img.filter(ImageFilter.BLUR)
        plt.figure("beauty")
        plt.subplot(4, 3, 2)
        plt.title('BLUR')
        plt.imshow(img1)
        plt.axis('off')

        img2 = img.filter(ImageFilter.SHARPEN)
        plt.figure("beauty")
        plt.subplot(4, 3, 3)
        plt.title('SHARPEN')
        plt.imshow(img2)
        plt.axis('off')

        img3 = img.filter(ImageFilter.CONTOUR)
        plt.figure("beauty")
        plt.subplot(4, 3, 4)
        plt.title('CONTOUR')
        plt.imshow(img3)
        plt.axis('off')

        img4 = img.filter(ImageFilter.EDGE_ENHANCE)
        plt.figure("beauty")
        plt.subplot(4, 3, 5)
        plt.title('EDGE_ENHANCE')
        plt.imshow(img4)
        plt.axis('off')

        img5 = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        plt.figure("beauty")
        plt.subplot(4, 3, 6)
        plt.title('EDGE_ENHANCE_MORE')
        plt.imshow(img5)
        plt.axis('off')

        img6 = img.filter(ImageFilter.EMBOSS)
        plt.figure("beauty")
        plt.subplot(4, 3, 7)
        plt.title('EMBOSS')
        plt.imshow(img6)
        plt.axis('off')

        img7 = img.filter(ImageFilter.FIND_EDGES)
        plt.figure("beauty")
        plt.subplot(4, 3, 8)
        plt.title('FIND_EDGES')
        plt.imshow(img7)
        plt.axis('off')

        img8 = img.filter(ImageFilter.SMOOTH)
        plt.figure("beauty")
        plt.subplot(4, 3, 9)
        plt.title('SMOOTH')
        plt.imshow(img8)
        plt.axis('off')

        img9 = img.filter(ImageFilter.SMOOTH_MORE)
        plt.figure("beauty")
        plt.subplot(4, 3, 10)
        plt.title('SMOOTH_MORE')
        plt.imshow(img9)
        plt.axis('off')

        plt.show()

    def Image15(self):
        image = color.rgb2gray(data.horse())
        image = 1 - image  # 反相
        # 实施骨架算法
        skeleton = morphology.skeletonize(image)

        # 显示结果
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

        ax1.imshow(image, cmap=plt.cm.gray)
        ax1.axis('off')
        ax1.set_title('original', fontsize=20)

        ax2.imshow(skeleton, cmap=plt.cm.gray)
        ax2.axis('off')
        ax2.set_title('skeleton', fontsize=20)

        fig.tight_layout()
        plt.show()


if __name__ == '__main__':
    path = r"C:\Users\君莫笑\PycharmProjects\pythonTest\pythonImage\zhixiao.jpg"
    path2 = r"C:\Users\君莫笑\PycharmProjects\pythonTest\pythonImage\zhixiao2.jpg"
    fontpath = r"C:\Users\君莫笑\PycharmProjects\pythonTest\pythonImage\malgun.ttf"
    img = ImageHander()
    # img.Image0(path)
    # size = 128, 128
    # img.Image1(path, size)
    # img.Image2(path, path2)
    # img.Image3(path)
    # img.Image4()
    # img.Image5(path)
    # img.Image6(path, fontpath)
    # img.Image7(path)
    # img.Image8(path)
    # img.Image9(path)
    # img.Image10(path)
    # img.Image11(path)
    img.Image12(path)
    # img.Image13(path)

    # img.Image14(path)
