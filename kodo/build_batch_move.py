# 批量移动文件，测试域名过期也可以用，但是只能在区域内移动，不能跨区域

from qiniu import build_batch_move, Auth, BucketManager
access_key = 'your_AK'
secret_key = 'your_SK'

q = Auth(access_key, secret_key)
bucket = BucketManager(q)
# 原空间
src_bucket_name = 'hdtraining'
# 目标空间
target_bucket_name = 'qiniuxyy'


# 字典的键为原文件，值为目标文件
parse = {
    '111.m3u8': '1',
    '3333.m3u8': '2',
    '9.18.mp4': '3'
}

# force为true时强制同名覆盖,
ops = build_batch_move(src_bucket_name, parse,  target_bucket_name, force='true')
ret, info = bucket.batch(ops)
print(info)