from pili import *
'''
SDK查看直播状态
'''

access_key = 'your_AK'
secret_key = 'your_SK'
hub_name = 'imc-test'   # 七牛直播空间，需提前建立好
q = Credentials(access_key, secret_key)  # 密钥初始化
hub = Hub(q, hub_name)

stream_id='z1.imc-test.yedandan'
stream = hub.get_stream(stream_id)
status = stream.status()
print(status)