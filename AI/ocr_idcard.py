from qiniu import QiniuMacAuth, http

#  密钥队初始化
access_key = 'your_AK'
secret_key = 'your_SK'
q = QiniuMacAuth(access_key, secret_key)

url = 'http://ai.qiniuapi.com/v1/ocr/idcard'   # 请求url
data = {"data": {"uri": "身份证的网址"}}
ret, info = http._post_with_qiniu_mac(url, data, q)
if ret['code'] == 0:
    print(ret.get('result').get('res'))
else:
    print('检测出错')