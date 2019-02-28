from qiniu import Auth, RtcServer,QiniuMacAuth

access_key = 'your_AK'
secret_key = 'your_SK'

# 密钥初始化
auth = QiniuMacAuth(access_key, secret_key)
res = RtcServer(auth)

Getapp = res.get_app(app_id= 'dip4r0w8t')
print(Getapp)


"""
返回信息：
AppID: app 的唯一标识。

UID: 客户的七牛帐号。

Hub: 绑定的直播 hub，使用此 hub 的资源进行推流等业务功能，hub 与 app 必须属于同一个七牛账户。

Title: app 的名称，注意，Title 不是唯一标识。

MaxUsers: int 类型，连麦房间支持的最大在线人数。

NoAutoKickUser: bool 类型，禁止自动踢人。

MergePublishRtmp: 连麦合流转推 RTMP 的配置。

CreatedAt: time 类型，app 创建的时间。

UpdatedAt: time 类型，app 更新的时间。

"""