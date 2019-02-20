from pili import *

access_key = 'v_s4L4kwQ-er524cv0ByjdiU7KtwzcaTgb7-y_nU'
secret_key = 'e-m9s9sDqfVhFFblA8Xq9eQaMdBPoPJ9AMtrfFLm'
hub_name = 'imc-test'   # 七牛直播空间，需提前建立好
q = Credentials(access_key, secret_key)  # 密钥初始化
hub = Hub(q, hub_name)

stream_id='z1.imc-test.1dasdasdas'
stream = hub.get_stream(stream_id)
stream.delete()
