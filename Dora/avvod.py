# 该功能目前支持华东和华北的bucket。

from qiniu import Auth, PersistentFop, build_op, op_save, urlsafe_base64_encode

# 自己的密钥对
access_key = 'your_AK'
secret_key = 'your_SK'

# 初始化Auth状态
q = Auth(access_key, secret_key)

# 你要测试的空间， 并且这个key在你空间中存在
bucket_name = 'test222'
key = 'test.mp4'
# 是使用的队列名称,不设置代表不使用私有队列，使用公有队列。
pipeline = 'gloria_trial'


# 设置转码参数,利用format格式化函数传参,这里实现的是非持久化的存储。即生成一个m3u8的文件。以流形式播放，
# /autosave/0 （默认）: 表示avvod使用服务端缓存，短期内有效，即不会发生二次转码，无额外存储费用，但七牛不承诺缓存期限，一旦失效，就会重新转码
# /atuosave/1 ：表示avvod的结果持久化，即转码后的结果存储在源bucket，永久不发生二次转码，有额外存储费用（转码后持久化的结果是有组织的一个m3u8文件+N个ts文件，以原文件名作为前缀命名）
fops = 'avvod/m3u8/autosave/0'


# 通过添加'|saveas'参数，指定处理后的文件保存的bucket和key，不指定默认保存在当前空间，bucket_saved为目标bucket，name_saved为目标key
# saveas_key = urlsafe_base64_encode('')
# fops = fops+'|saveas/'+saveas_key

# 执行持久化处理
pfop = PersistentFop(q, bucket_name, pipeline)

# fops参数拼接
ops = []
ops.append(fops)
# 1代表强制执行
ret, info = pfop.execute(key, ops, 1)
print('info信息：', info)
print('dora的persistentId:', ret)
assert ret['persistentId'] is not None
