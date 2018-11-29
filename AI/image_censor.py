from qiniu import QiniuMacAuth, http

#  密钥队初始化
access_key = 'your_AK'
secret_key = 'your_SK'
q = QiniuMacAuth(access_key, secret_key)

url = 'http://ai.qiniuapi.com/v1/image/censor'   # 请求url
data = {"data": {"uri": "http://oayjpradp.bkt.clouddn.com/Audrey_Hepburn.jpg"}, "params": {"type": ["pulp", "terror", "politician"]}}
ret, info = http._post_with_qiniu_mac(url, data, q)
if ret['code'] == 0:
    print('检测成功\n结果是：', ret['result'])
else:
    print('检测出错')


