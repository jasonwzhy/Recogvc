"""
version 1.0
date 2014-10-09
"""
#-*-coding:utf-8-*-
import VCrecognition
#img_path = "/Users/jasonwzhy/work/brandbigdata/verifycode/gsxt.saic.gov.cn/sichuan/ztxy4.jpeg"#图片路径
img_path = "/Users/jasonwzhy/tmp/t9.jpg"
rec= VCrecognition.Recog('beijing',img_path,1)
print rec.do_unverify()#成功会返回内容(unicode)，失败返回False
img_path = "/Users/jasonwzhy/work/brandbigdata/verifycode/gsxt.saic.gov.cn/sichuan/ztxy4.jpeg"#图片路径
rec2= VCrecognition.Recog('sichuan',img_path,2)
print rec2.do_unverify()