# 批量删除文件

from qiniu import build_batch_delete, Auth, BucketManager
access_key = 'cbjqXDJKDDy9wy2sRRq2NulALQKhE7l6EZv9XV3S'
secret_key = '6fZVQq_U4hxx-q6fQ69TfHUsBXlXACSoH9S2NToW'

#初始化
q = Auth(access_key, secret_key)
bucket = BucketManager(q)
bucket_name = 'qiniuxyy'

#这里不是字典形式，是列表形式
keys = ['1', '2', '3',]
# 返回的是数组，如【'delete/cWluaXV4eXk6NC5odG1s']形式
ops = build_batch_delete(bucket_name, keys)
print(ops)
# batch是将数组批量返回字典
ret, info = bucket.batch(ops)
print(info)