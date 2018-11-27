from qiniu import Auth, CdnManager


access_key = 'v_s4L4kwQ-er524cv0ByjdiU7KtwzcaTgb7-y_nU'
secret_key = 'e-m9s9sDqfVhFFblA8Xq9eQaMdBPoPJ9AMtrfFLm'

q = Auth(access_key, secret_key)
cdn = CdnManager(q)
urls = ['http://phd6u0gel.bkt.clouddn.com/Geekbench-4.3.0-Linux.tar.gz', 'http://phd6u0gel.bkt.clouddn.com/super_pi.tgz']
refresh_urls_response = cdn.refresh_urls(urls=urls)
print(refresh_urls_response)





