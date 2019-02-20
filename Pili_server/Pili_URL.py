from pili import *
'''
SDK为根据流，输出推拉流地址
'''
access_key = 'your_AK'
secret_key = 'your_SK'
hub_name = 'imc-test'   # 七牛直播空间，需提前建立好
q = Credentials(access_key, secret_key)  # 密钥初始化
hub = Hub(q, hub_name)

stream_id='z1.imc-test.5c6cf9b7a3d5ec32580ebc2f'
stream = hub.get_stream(stream_id)
PublishUrl = stream.rtmp_publish_url()
RtmpUrl = stream.rtmp_live_urls()
HlspUrl = stream.hls_live_urls()
FlvUrl = stream.http_flv_live_urls()
SnapshotPlay = stream.snapshot(name="imageName.jpg", format="jpg", time=None, notifyUrl=None)


print('推流地址：', PublishUrl)
print('RTMP拉流地址：', RtmpUrl)
print('HLS拉流地址：', HlspUrl)
print('Flv拉流地址：', FlvUrl)
print('直播封面：', SnapshotPlay)

