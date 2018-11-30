from qiniu import QiniuMacAuth, http

# AK,SK，初始化
access_key = 'your_AK'
secret_key = 'your_SK'
q = QiniuMacAuth(access_key, secret_key)

url = 'http://qiniu.pasca.top/super_pi.tgz/?qhash/md5'

res = http._get_with_qiniu_mac(url=url, params=None, auth=q)
print(res)