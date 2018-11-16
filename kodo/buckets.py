from qiniu import Auth, BucketManager


AK = Your_AK
SK = Your_SK
q = Auth(AK, SK)
c = BucketManager(q)
info = c.buckets()
print(info)