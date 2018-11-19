from qiniu import Auth, put_file, etag


access_key = 'your_ak'
secret_key = 'your_sk'
q = Auth(access_key, secret_key)
bucket_name = '2018_11_16'
key = 'test11.png'

# 上传文件到七牛后， 七牛将文件名和文件大小回调给业务服务器。
policy={
 'callbackUrl':' pasca.top',
 'callbackBody':'filename=$(fname)&filesize=$(fsize)'
 }
token = q.upload_token(bucket_name, key, 3600, policy)
localfile = '/Users/pasca/Desktop/1.jpg'
ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)