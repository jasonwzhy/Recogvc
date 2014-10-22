#-*-coding:utf-8-*-
import VCrecognition
img_path = ""#图片路径
rec= VCrecognition.Recog(img_path,2)#2为数字运算 1为中文识别
print rec.do_unverify()#成功会返回内容(unicode)，失败返回False
