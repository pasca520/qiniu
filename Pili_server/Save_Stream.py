from pili import *
import time

'''
SDK为保存直播回放
'''
access_key = 'your_AK'
secret_key = 'your_SK'
hub_name = 'imc-test'   # 七牛直播空间，需提前建立好
q = Credentials(access_key, secret_key)  # 密钥初始化
hub = Hub(q, hub_name)

stream_id='z1.imc-test.yedandan'
stream = hub.get_stream(stream_id)

start = '2019-02-19 16:22'
end = '2019-02-19 16:41'

timeArray = time.strptime(start, "%Y-%m-%d %H:%M")
timeArray1 = time.strptime(end, "%Y-%m-%d %H:%M")
start = time.mktime(timeArray)
end = time.mktime(timeArray1)

res = stream.save_as(name="videoName.mp4", format="mp4", start=int(start), end=int(end), notifyUrl=None)
print(res)