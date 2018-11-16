from qiniu import BucketManager, Auth
# from My_AKSK import Your_AK, Your_SK    #这里是为了隐私，单独设置了个AK，SK文件，然后导入

ak = Your_AK
sk = Your_SK
# 认证初始化
q = Auth(ak, sk)

# 空间初始化
a = BucketManager(q)

# 空间名称的URL安全的Base64编码，空间名称仅支持字母、短划线-、下划线_、数字的组合。
Bucket_name = '2018_11_16'

# 存储区域，默认华东, z0 华东 z1 华北 z2 华南 na0 北美 as0 东南亚
info = a.mkbucketv2(bucket_name=Bucket_name, region='z2')
print(info)


