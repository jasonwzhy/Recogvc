#-*-coding:utf-8-*-
from PIL import Image
from PIL import ImageEnhance,ImageFilter
from pytesseract import image_to_string
import time

#img = Image.open("/Users/jasonwzhy/Desktop/captcha.jpg")
img = Image.open("/Users/jasonwzhy/tmp/t4.jpg")
class clearNoise:
	def __init__(self,img):
		self.img = img
	def clearNoise(self,img):
		img = img.convert("RGBA")
		pixdata = img.load()
		for y in xrange(img.size[1]):
		    for x in xrange(img.size[0]):
		        if pixdata[x, y][0] < 90:
		            pixdata[x, y] = (0, 0, 0, 255)
		for y in xrange(img.size[1]):
		    for x in xrange(img.size[0]):
		        if pixdata[x, y][1] < 136:
		            pixdata[x, y] = (0, 0, 0, 255)
		for y in xrange(img.size[1]):
		    for x in xrange(img.size[0]):
		        if pixdata[x, y][2] > 0:
		            pixdata[x, y] = (255, 255, 255, 255)
		#im_orig = Image.open('input-black.gif')
		#img = img.resize((80, 35), Image.NEAREST)
		img = img.convert('1')
		img.show()
		return img

def clearNoise(img):
	#img = img.convert("L")
	img = img.convert("RGBA")
	pixdata = img.load()
	for y in range(img.size[1]):
	    for x in range(img.size[0]):
	        if pixdata[x, y][0] < 90:
	            pixdata[x, y] = (0, 0, 0)
	for y in range(img.size[1]):
	    for x in range(img.size[0]):
	        if pixdata[x, y][1] < 136:
	            pixdata[x, y] = (0, 0, 0)
	for y in range(img.size[1]):
	    for x in range(img.size[0]):
	        if pixdata[x, y][2] > 0:
	            pixdata[x, y] = (255, 255, 255)
	#im_orig = Image.open('input-black.gif')
	#img = img.resize((106, 40), Image.NEAREST)
	img = img.convert('L')
	#img = img.filter(ImageFilter.SHARPEN)
	img.show()

	return img
def midvalue(img):
	img = img.filter(ImageFilter.MedianFilter())
	enhancer = ImageEnhance.Contrast(img)
	img = img.convert('L')
	img = enhancer.enhance(1)
	img.show()
	return img
def tessertact(img):
	#ret = image_to_string(img,lang="chi_sim")
	ret = image_to_string(img)
	print ret
	#ret = ret.decode('utf-8')
	#lst = [u'乘']
	#print lst
	#print type(ret)
	#print list(ret)
def tvalue(img):
	return img.convert("L")
def smooth(img):
	#time.sleep(1)
	retimg = img.filter(ImageFilter.SMOOTH)
	#retimg.show()
	return retimg
def roll(image, delta):
    "Roll an image sideways"

    image = image.copy() #复制图像
    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))
    return image

def cutimg(img):
	print img.size
	box = (20,5,145,45)
	p = img.crop(box)
	p.show()
	#img.paste(p,box)
	return p
#imgt = clearNoise(img)
#imgt = midvalue(img)
imgt = tvalue(img)
#imgt=img

imgt=smooth(imgt)
imgt=smooth(imgt)
imgt=smooth(imgt)
imgt=smooth(imgt)
imgt = cutimg(imgt)
imgt = clearNoise(imgt)
#imgt = tvalue(img)
#imgt.show()

tessertact(imgt)
