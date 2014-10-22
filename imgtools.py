#-*-coding:utf-8-*-
from PIL import Image
from PIL import ImageEnhance,ImageFilter
from pytesseract import image_to_string

#img = Image.open("/Users/jasonwzhy/Desktop/captcha.jpg")
img = Image.open("/Users/jasonwzhy/work/brandbigdata/verifycode/gsxt.saic.gov.cn/sichuan/ztxy6.jpeg")
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
	ret = image_to_string(img,lang="chi_sim")
	print ret
	ret = ret.decode('utf-8')
	lst = [u'乘']
	print lst
	print type(ret)
	print list(ret)
def tvalue(img):
	return img.convert("L")

#imgt = clearNoise(img)
#imgt = midvalue(img)
imgt = tvalue(img)
imgt = clearNoise(imgt)
#imgt = tvalue(img)
#imgt.show()

tessertact(imgt)
