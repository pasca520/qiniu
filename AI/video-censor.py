from qiniu import QiniuMacAuth, http
import requests, time

#  密钥队初始化
access_key = 'your_AK'
secret_key = 'your_SK'
q = QiniuMacAuth(access_key, secret_key)

url = 'http://ai.qiniuapi.com/v3/video/censor'   # 请求url
data = {"data": {"uri": "http://cdn.vcore.hk/1528336770927592712019-02-181550474493.mp4"}, "params": {"scenes": ["pulp", "terror", "politician"]}}
ret, info = http._post_with_qiniu_mac(url, data, q)
job = ret['job']

time.sleep(10)
# 根据job得到结果
url1 = 'http://ai.qiniuapi.com/v3/jobs/video/{}'.format(job)
token = "Qiniu " + q.token_of_request("GET", "ai.qiniuapi.com", url1, "")
r = requests.get(url1, headers={'Authorization': token})
print(r.text)


