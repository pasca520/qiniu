from qiniu import Auth, urlsafe_base64_encode, PersistentFop

# AK,SK，初始化
access_key = 'your_AK'
secret_key = 'your_SK'
q = Auth(access_key, secret_key)


# 参数给定
bucket_name = ''   #空间名
key = '' #索引文件
fops = 'mkzip/4'
save_key = urlsafe_base64_encode('')  #保存的空间和名字
fops = fops + '|saves/' + save_key
pipline = ''   # 指定私有队列



# 开始执行
pfops = PersistentFop(q, bucket_name, pipline)
ops = []
ops.append(fops)
ret, info = pfops.execute(key, ops, 1)
print('本次处理结果的作业ID', ret)
print('返回结果：', info)