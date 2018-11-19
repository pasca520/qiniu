from qiniu import auth, urlsafe_base64_encode
import hmac
import requests
from hashlib import sha1

# 生成管理凭证
def get_authorization(Your_AK, Your_SK, url):
    signingStr = url.encode('utf-8')
    sign = hmac.new(signingStr, Your_SK.encode('utf-8'), sha1).digest()
    encodedSign = urlsafe_base64_encode(sign)
    accessToken = Your_AK + ':' +encodedSign
    return accessToken
# 构造header， 发送get请求
def get_result(url, host, Content_Type, QboxToken):
    headers = {
        'Host': host,
        'Content-Type': Content_Type,
        'Authorization': QboxToken
    }
    response = requests.get(url, headers=headers)
    return response.text

def main():
    Your_AK = 'Your_ak'
    Your_SK = 'Your_sk'
    # q = Auth(Your_AK, Your_SK)
    token_url = '/v6/domain/list?tbl=2018_11_16\n '
    url = 'http://api.qiniu.com/v6/domain/list?tbl=2018_11_16'
    host = 'api.qiniu.com'
    Content_Type = 'application/x-www-form-urlencoded'
    accessToken = get_authorization(Your_AK, Your_SK, token_url)
    QboxToken = 'QBox ' + accessToken
    response = get_result(url, host, Content_Type, QboxToken)
    print(response)
   # print(QboxToken)

if __name__ == '__main__':
    main()