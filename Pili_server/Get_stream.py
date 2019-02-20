from pili import *
'''
SDK为得到一个流的信息，返回python对象内存地址
'''
access_key = 'your_AK'
secret_key = 'your_SK'
hub_name = 'imc-test'   # 七牛直播空间，需提前建立好
q = Credentials(access_key, secret_key)  # 密钥初始化
hub = Hub(q, hub_name)

# ID：z1.imc-test.pasca  测试
stream = hub.get_stream(stream_id=id)
print("\n得到一个流（为python对象内存地址）：\n", stream)