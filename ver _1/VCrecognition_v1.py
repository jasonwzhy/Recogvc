"""
version 1.0
date 2014-10-09
"""
#-*-coding:utf-8-*-
from PIL import Image
from PIL import ImageEnhance,ImageFilter
from pytesseract import image_to_string
class Recog(object):
	"""Rrecog"""
	def __init__(self,province = '', img_path = '', verify_type = ''):
		super(Recog, self).__init__()
		self.ret=''
		if province is '' or img_path is '' or verify_type is 0:
			raise Exception("The img path is error or verify_type is no define")
		try:
			self.img = Image.open(img_path)
		except IOError, e:
			raise e
		self.verify_type = int(verify_type)
		self.province = province
	def do_unverify(self):
		self.gsxtdic.get(self.province)(self)
		return self.ret
		"""try:
			self.gsxtdic.get('beijing')(self)
		except Exception, e:
			raise Exception("The province error")"""
	def do_ztxy(self):
		if self.verify_type is 1:	#recongnithion chinese
			cnoise_img = ClearNoise(self.img).clearNoise()
			ret = image_to_string(cnoise_img,lang="chi_sim")
			self.ret = ret.decode('utf-8')
		elif self.verify_type is 2:
			cnoise_img = ClearNoise(self.img).clearNoise()
			self.ret = ComputeTypeRecog(cnoise_img).doCount()
		return self.ret
	def do_mzImgexppwd(self):
		if self.verify_type is 1:
			self.img=self.img.convert("L")
			img_enhance = ImgEnhance(self.img)
			imgenh = img_enhance.smooth(4)
			imgenh = img_enhance.cutimg(20,5,145,45)
			imgenh = ClearNoise(imgenh).clearNoise()
			ret = image_to_string(imgenh)
			optim = OptimizeRet()
			self.ret = optim.lettersFormat(ret)
			self.ret = self.ret.decode('utf-8')
		return self.ret
	def do_undefined(self):
		return ''
	gsxtdic = {
		"sichuan":do_ztxy,
		"xinjiang":do_ztxy,
		"beijing":do_mzImgexppwd,
		"tianjin":do_undefined,
		"hebei":do_undefined,
		"shanghai":do_undefined,
		"fujian":do_undefined,
		"yunnan":do_undefined,
		"shanxi":do_undefined,#山西
		"neimenggu":do_undefined,
		"guangdong":do_undefined,
		"hainan":do_undefined,
		"liaoning":do_undefined,
		"jilin":do_undefined,
		"shandong":do_undefined,
		"heilongjiang":do_undefined,
		"anhui":do_undefined,
		"guangxi":do_undefined,
		"henan":do_undefined,
		"xizang":do_undefined,
		"qinghai":do_undefined,
		"jiangsu":do_undefined,
		"zhejiang":do_undefined,
		"jiangxi":do_undefined,
		"ningxia":do_undefined,
		"chongqing":do_undefined,
		"guizhou":do_undefined,
		"shaanxi":do_undefined,#陕西
		"gansu":do_undefined,
		"hubei":do_undefined,
		"hunan":do_undefined
	}
class ComputeTypeRecog(object):
	"""Reccompute"""
	def __init__(self, img_obj):
		super(ComputeTypeRecog, self).__init__()
		self.img_obj = img_obj
		self.__ret = self.imgToString()
		self.retlst = list(self.__ret)
		self.count_type = False
		self.count_index = 0
		#if not num text ,will rectify it
		self.rectify_num = {
			1:[u'l',u'、'],
			2:[u'二',u'Z'],
			3:[u'三',u'宝'],
			4:[u'《'],
			5:[u'S'],
			6:[],
			7:[u'>'],
			8:[u'菖'],
			9:[u'日'],
			0:[u'O']}
		self.rectifyCount()
		self.value_a = self.rectifyValue(self.retlst[:self.count_index])
		self.value_b = self.rectifyValue(self.retlst[self.count_index:])
		#self.doCount(value_a,value_b)
	def rectifyCount(self):
		count_add = [u'加',u'力',u'刀',u'口',u'灭',u'恤',u'瓜']
		count_mul = [u'乘',u'栗',u'冢',u'荚',u'寅',u'家',u'霁',u'宣']
		for ct in count_add:
			if ct in self.retlst:
				self.count_type=1
				self.count_index = self.retlst.index(ct)
				return self.count_type
		for cm in count_mul:
			if cm in self.retlst:
				self.count_type=2
				self.count_index = self.retlst.index(cm)
				return self.count_type
	def rectifyValue(self,rvalue_lst):
		for item in rvalue_lst:
			if item.isdecimal():
				return int(item)
		
		for num,rectify_values in self.rectify_num.items():
			for r_values in rectify_values:
				if r_values in rvalue_lst:
					return num
		return False
	def imgToString(self):
		ret = image_to_string(self.img_obj,lang="chi_sim")
		self.__ret = ret.decode('utf-8')
		return self.__ret
	def doCount(self):
		if self.count_type and self.value_a is not False and self.value_b is not False:
			if self.count_type is 1:  #sum
				return self.value_a + self.value_b
			elif self.count_type is 2: #multiplication
				return self.value_a*self.value_b
		else:
			return False
			
class ClearNoise(object):
	""" ClearNoise"""
	def __init__(self,img=''):
		super(ClearNoise, self).__init__()
		self.img = img
		if img is '':
			raise Exception('The img is error')
	def clearNoise(self):
		img = self.img.convert("RGBA")
		pixels = img.load()
		for rgb in range(0,3):
			for y in range(img.size[1]):
				for x in range(img.size[0]):
					if rgb == 0 and pixels[x,y][rgb] < 90:
						pixels[x,y] = (0,0,0)
					elif rgb == 1 and pixels[x,y][rgb] < 136:
						pixels[x,y] = (0,0,0)
					elif rgb == 2 and pixels[x,y][rgb] > 0:
						pixels[x,y] = (255,255,255)
		img = img.convert('L')
		return img

class ImgEnhance(object):
	"""The Enhance Image """
	def __init__(self,img):
		super(ImgEnhance,self).__init__()
		self.img = img
	def smooth(self,deep):
		for x in xrange(deep):
			self.img = self.img.filter(ImageFilter.SMOOTH)
		return self.img
	def cutimg(self,left, upper, right, lower):
		#box = (20,5,145,45)
		box = (left, upper, right, lower)
		self.img = self.img.crop(box)
		return self.img
class OptimizeRet(object):
	def __init__(self):
		super(OptimizeRet,self).__init__()
	def lettersFormat(self,ret):
		retlst = list(ret)
		return "".join([ritem for ritem in retlst if ritem.isalpha() or ritem.isdigit()])
		