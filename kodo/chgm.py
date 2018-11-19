from qiniu import Auth
from qiniu import BucketManager

# 前置准备
access_key = 'AK'
secret_key = 'SK'
q = Auth(access_key, secret_key)
bucket = BucketManager(q)
bucket_name = '2018_11_16'
key = 'test11.png'

# 将一个文件的元信息修改为png，原来是image/jpeg
ret, info = bucket.change_mime(bucket_name, key, 'image/png')
print(info)