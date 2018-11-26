from qiniu import Auth, PersistentFop, build_op, op_save, urlsafe_base64_encode
# 自己的密钥对
access_key = 'your_AK'
secret_key = 'your_SK'

# 初始化Auth状态
q = Auth(access_key, secret_key)

# 你要测试的空间， 并且这个key在你空间中存在
bucket_name = '2018_11_16'
key = 'test.mp4'
# 是使用的队列名称,不设置代表不使用私有队列，使用公有队列。
pipeline = 'gloria_trial'

video1 = urlsafe_base64_encode('http://qiniu.pasca.top/test1')
video2 = urlsafe_base64_encode('http://qiniu.pasca.top/test31')


# 设置转码参数,利用format格式化函数传参
fops = 'avconcat/2/format/mp4/index/1/{}/{}'.format(video1, video2)


# 通过添加'|saveas'参数，指定处理后的文件保存的bucket和key，不指定默认保存在当前空间，bucket_saved为目标bucket，name_saved为目标key
saveas_key = urlsafe_base64_encode('2018_11_16:test——pinjie')
fops = fops+'|saveas/'+saveas_key

# 执行持久化处理
pfop = PersistentFop(q, bucket_name, pipeline)

# fops参数拼接
ops = []
ops.append(fops)
print(ops)
# 1代表强制执行
ret, info = pfop.execute(key, ops, 1)
print('info信息：', info)
print('dora的persistentId:', ret)
assert ret['persistentId'] is not None
