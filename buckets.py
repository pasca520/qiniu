from qiniu import Auth, BucketManager
import My_AKSK

AK = My_AKSK.Your_AK
SK = My_AKSK.Your_SK
q = Auth(AK, SK)
c = BucketManager(q)
info = c.buckets()
print(info)


