# -*- coding: utf-8 -*-
# @Author  : pasca
# @mailbox : 1196738787@qq.com


from qiniu import QiniuMacAuth, http

# 需后台开通才可验证
access_key = 'your_AK'
secret_key = 'your_SK'
q = QiniuMacAuth(access_key, secret_key)

# 请求url
url = 'https://sms.qiniuapi.com/v1/message'

"""
template_id：模板 ID
mobiles：手机号，示例：["15900000000","13500000000"]

"""

data = {
    "template_id": "1131042429772763136",
    "mobiles": ["15900000000","13500000000"]
}
res, info = http._post_with_qiniu_mac(url, data, q)
print(res)