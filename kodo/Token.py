from qiniu import Auth, put_file
import requests

# 验证上传token
def Check_Upload_Token(upload_token, key, file_path):
    upload = put_file(upload_token, key, file_path, progress_handler=True)
    return upload

# 验证管理token
def Check_AccessToken(url, accessToken ):
    headers = {
        'Host': 'rs.qbox.me',
        'Content - Type': 'application / x - www - form - urlencoded',
        'Authorization': 'QBox '+ accessToken
    }
    response = requests.get(url=url, headers=headers)
    return response.text

def main():
    # 需要填写你的 Access Key 和 Secret Key
    access_key = 'your_AK'
    secret_key = 'your_SK'

    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = '2018_11_16'

    # 上传到七牛后保存的文件名
    key = '1'

    # 本地要上传的文件
    file_path = '/Users/pasca/Desktop/七牛文档/1.txt'

    # 管理凭证的url，这里是列举空间的bucket
    url = 'http://rs.qbox.me/buckets?'
    # 生成上传 Token，可以指定过期时间等
    # 上传策略示例
    # https://developer.qiniu.com/kodo/manual/1206/put-policy
    policy = {
     # 'callbackUrl':'https://requestb.in/1c7q2d31',
     # 'callbackBody':'filename=$(fname)&filesize=$(fsize)'
     # 'persistentOps':'imageView2/1/w/200/h/200'
     }

    # 3600为token过期时间，秒为单位。3600等于一小时
    upload_token = q.upload_token(bucket_name, key, 3600, policy)
    accessToken = q.token_of_request(url)
    # 执行上传token
    info = Check_Upload_Token(upload_token, key, file_path)
    print('上传凭证：', upload_token, info)

    #执行管理token
    info1 = Check_AccessToken(url, accessToken)
    print('管理凭证：', accessToken, info1)

if __name__ == '__main__':
    main()


