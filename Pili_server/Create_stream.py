from pili import *
'''
SDK为创建一路流
'''
access_key = 'your_AK'
secret_key = 'your_SK'
hub_name = 'imc-test'   # 七牛直播空间，需提前建立好
q = Credentials(access_key, secret_key)  # 密钥初始化
hub = Hub(q, hub_name)

stream = hub.create_stream(title=None, publishKey=None, publishSecurity="static")
print("\ncreate_stream():\n", stream.to_json())

