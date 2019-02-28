from qiniu import Auth, get_room_token



access_key = 'your_AK'
secret_key = 'your_SK'

auth = Auth(access_key, secret_key)


## 定义房间管理凭证信息
roomAccess = {
    "appId": "dhr2vd5pe",
    "roomName": "test1232",
    "userId": "pasca",
    "expireAt": 51437808000,
    "permission": "user"
}
# 调用接口版生成token
roomToken = get_room_token(access_key, secret_key, roomAccess)


