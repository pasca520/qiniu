from qiniu import RtcServer, QiniuMacAuth

access_key = 'your_AK'
secret_key = 'your_SK'

# 密钥初始化
auth = QiniuMacAuth(access_key, secret_key)
res = RtcServer(auth)

DeleteApp = res.delete_app(app_id= 'dip4r0w8t')
print(DeleteApp)