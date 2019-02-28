from qiniu import RtcServer, QiniuMacAuth

access_key = 'your_AK'
secret_key = 'your_SK'

# 密钥初始化
auth = QiniuMacAuth(access_key, secret_key)
res = RtcServer(auth)

"""
AppID: app 的唯一标识，创建的时候由系统生成。

Title: app 的名称， 可选。

Hub: 绑定的直播 hub，可选，用于合流后 rtmp 推流。

MaxUsers: int 类型，可选，连麦房间支持的最大在线人数。

NoAutoKickUser: bool 类型，可选，禁止自动踢人。

MergePublishRtmp: 连麦合流转推 RTMP 的配置，可选择。其详细配置包括如下

Enable: 布尔类型，用于开启和关闭所有房间的合流功能。
AudioOnly: 布尔类型，可选，指定是否只合成音频。
Height, Width: int64，可选，指定合流输出的高和宽，默认为 640 x 480。
OutputFps: int64，可选，指定合流输出的帧率，默认为 25 fps 。
OutputKbps: int64，可选，指定合流输出的码率，默认为 1000 。
URL: 合流后转推旁路直播的地址，可选，支持魔法变量配置按照连麦房间号生成不同的推流地址。如果是转推到七牛直播云，不建议配置。
StreamTitle: 转推七牛直播云的流名，可选，支持魔法变量配置按照连麦房间号生成不同的流名。例如，配置 Hub 为 qn-zhibo ，配置 StreamTitle 为 $(roomName) ，则房间 meeting-001 的合流将会被转推到 rtmp://pili-publish.qn-zhibo.***.com/qn-zhibo/meeting-001 地址。详细配置细则，请参考 portal.qiniu,com 配置页面，或咨询七牛技术支持。
备注：以上关于合流画面的配置项仅用于配置合流的输出效果，对某一个特定输入的画面的配置（例如位置、大小、层级等），请参考相关客户端 sdk 说明文档。

"""

data = {
    "hub": "imc_test",
    "title": "qiniu",
    "maxUsers": 7,
    "mergePublishRtmp": {
        "enable": True,
        "audioOnly": False,
        "height": 700 ,
        "width": 700,
        "fps": 30,
        "kbps": 500,
    }
}

UpdateApp = res.update_app(app_id= 'dhr2vd5pe', data=data)
print(UpdateApp)