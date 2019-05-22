# -*- coding: utf-8 -*-
# @Author  : pasca
# @mailbox : 1196738787@qq.com


from qiniu import QiniuMacAuth, http

# 需后台开通才可验证
access_key = 'your_AK'
secret_key = 'your_SK'
q = QiniuMacAuth(access_key, secret_key)

# 请求url
url = 'https://sms.qiniuapi.com/v1/signature'

"""
signature：签名 
source：签名来源，申请签名时必须指定签名来源。取值范围为：
       enterprises_and_institutions 企事业单位的全称或简称
       website 工信部备案网站的全称或简称
      app APP应用的全称或简称
public_number_or_small_program 公众号或小程序的全称或简称
store_name 电商平台店铺名的全称或简称
trade_name 商标名的全称或简称
pics：签名对应的资质证明图片进行 base64 编码格式转换后的字符串
"""

data = {"signature": "蛋蛋团",
        "source": "public_number_or_small_program"}

res, info = http._post_with_qiniu_mac(url, data, q)
print(res)

