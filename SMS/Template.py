# -*- coding: utf-8 -*-
# @Author  : pasca
# @mailbox : 1196738787@qq.com

from qiniu import QiniuMacAuth, http

# 需后台开通才可验证
access_key = 'your_AK'
secret_key = 'your_SK'
q = QiniuMacAuth(access_key, secret_key)

# 请求url
url = 'https://sms.qiniuapi.com/v1/template'

"""
name：模板名称
template：模板内容
type：模板类型，取值范围为: notification (通知类短信), verification (验证码短信), marketing (营销类短信)
description：申请理由简述
signature_id ：已经审核通过的签名

"""

data = {
    "name": "蛋蛋团",
    "template": "【蛋蛋团】您正在申请手机注册，验证码为：${code}，5分钟内有效！",
    "type": "verification",
    "description": "test",
    "signature_id": "1131035480654090240"
}
res, info = http._post_with_qiniu_mac(url, data, q)
print(res)