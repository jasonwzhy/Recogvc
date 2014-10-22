#-*-coding:utf-8-*-
from PIL import Image
from PIL import ImageEnhance,ImageFilter
from pytesseract import image_to_string

class Recog(object):
	"""Rrecog"""
	def __init__(self, img_path = '', verify_type = 0):
		super(Recog, self).__init__()
		self.ret=''
		if img_path is '' or verify_type is 0:
			raise Exception("The img path is error or verify_type is no define")
		try:
			self.img = Image.open(img_path)
		except IOError, e:
			raise e
		#self.verify_type(verify_type)
		self.verify_type = int(verify_type)
	def do_unverify(self):
		if self.verify_type is 1:	#recongnithion chinese
			cnoise_img = ClearNoise(self.img).clearNoise()
			ret = image_to_string(cnoise_img,lang="chi_sim")
			self.ret = ret.decode('utf-8')
		elif self.verify_type is 2:
			cnoise_img = ClearNoise(self.img).clearNoise()
			self.ret = ComputeTypeRecog(cnoise_img).doCount()
		return self.ret
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
