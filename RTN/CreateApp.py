from qiniu import QiniuMacAuth, RtcServer


access_key = 'your_AK'
secret_key = 'your_SK'

# 密钥初始化
auth = QiniuMacAuth(access_key, secret_key)
res = RtcServer(auth)
"""
CreateApp 创建一个应用

Hub: 绑定的直播 hub，可选，使用此 hub 的资源进行推流等业务功能，hub 与 app 必须属于同一个七牛账户。

Title: app 的名称，可选，注意，Title 不是唯一标识，重复 create 动作将生成多个 app。

MaxUsers: int 类型，可选，连麦房间支持的最大在线人数。

NoAutoKickUser: bool 类型，可选，禁止自动踢人（抢流）。默认为 false ，即同一个身份的 client (app/room/user) ，新的连麦请求可以成功，旧连接被关闭。

"""
create_app = {
    "hub": "imc-test",
    "title": "pasca-qiniu",
    "maxUsers": 9
}

CreateApp = res.create_app(create_app)
print(CreateApp)






