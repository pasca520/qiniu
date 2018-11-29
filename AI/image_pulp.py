from qiniu import QiniuMacAuth
from qiniu import http

# 初始化AK,SK
access_key = 'your_AK'
secret_key = 'your_SK'
q = QiniuMacAuth(access_key, secret_key)

# 包体和接口
data = {'data': {'uri': 'http://7xlv47.com1.z0.glb.clouddn.com/pulpsexy.jpg'}}
# body = json.dumps(data).encode('utf-8')
# url = 'http://ai.qiniuapi.com/v1/image/censor'
url = 'http://ai.qiniuapi.com/v1/pulp'
# # 生成七牛鉴权，专门用来数据处理的鉴权
# token = q.token_of_request(method='POST', host='ai.qiniuapi.com', url=url, qheaders='', content_type='application/json', body=body)
#
# headers= {
#     'Content-Type': 'application/json',
#     'Authorization': 'Qiniu {0}'.format(token)
# }
# print(headers)

res1 = http._post_with_qiniu_mac(url=url, data=data, auth=q)
# res = requests.post(url=url, headers=headers, data=json.dumps(data))
print(res1)

