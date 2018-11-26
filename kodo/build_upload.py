from qiniu import Auth, put_file
import os, sys
import urllib.parse
import datetime
import subprocess


__author__ = "pasca"

#  这里都是自己手动输入的一些信息，可以考虑图形化
access_key = 'cbjqXDJKDDy9wy2sRRq2NulALQKhE7l6EZv9XV3S'  #你的AK
secret_key = '6fZVQq_U4hxx-q6fQ69TfHUsBXlXACSoH9S2NToW'    #你的SK
bucket_name = '2018_11_16'  #待上传空间名
bucket_url = 'pia5c8gzf.bkt.clouddn.com'

img_suffix = ["JPG", "PNG", "jpg", "jpeg", "png", "bmp", "gif"]
result_file = "本次上传结果.txt"    #保存上传的结果到txt文件中

# 判断上传结果文件是否已经存在，存在就删除
if os.path.exists(result_file):
    os.remove(result_file)

class QiniuYun(object):
    # 初始化变量,AK,SK
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key
        self.q = Auth(access_key, secret_key)
    # 得到上传资源的url
    def get_url(self, bucket_url, filenames ):
        if not bucket_name in bucket_url.keys():
            raise ArithmeticError('空间名不对')   #加入异常处理，没有这个空间即返回错误
        url_prefix = bucket_url[bucket_name]
        url = url_prefix + urllib.parse.quote(filenames) #屏蔽特殊的字符、比如如果url里面的空格等。python2.X是urllib.quote(text)，python3.x是urllib.parse.quote(text)
        return url

    # 上传模块
    def uploads(self, bucket_name ,filenames, file_path):
        up_token = self.q.upload_token(bucket_name)
        ret, info = put_file(up_token, filenames, file_path)
        url = self.get_url(bucket_name, filenames)
        return ret, info, url

# 生成资源上传的时间
def Get_Upload_Time():
    now = datetime.datetime.now()
    tmp = tuple(now.timetuple())[:-3]
    tmp = map(str, tmp)
    return "/".join(tmp) + "/"

#  拖拽模块
# def Drag_File():


# 主函数
def main():
    if len(sys.argv) == 1:
        print(" 拖拽进入这里")
    sys.exit(0)
    files = sys.argv[1:]
    q = Qiniu(access_key, secret_key)
    up_time = Get_Upload_Time()

    for file in files:
        if os.path.isdir(file):
            print("暂不支持目录上传！")
            sys.exit(0)
        if os.path.isfile(file):
            suffix = os.path.splitext(file)[1][1:]
            prefix = "img/" if suffix in img_suffix else "file/"
            prefix += up_time
            name = os.path.split(file)[1]
            up_filename = prefix + name
            ret, info, url = q.upload_file(bucket, up_filename, file)
            print("已上传： %s " % name)
            save(name, url)
        subprocess.call(result_file, shell=True)  #打开文件


if __name__ == '__main__':
    main()





