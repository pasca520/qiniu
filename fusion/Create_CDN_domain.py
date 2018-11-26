from qiniu import auth,Auth
import requests

# 获取管理拼凭证
def token_of_request(q, url):
    QBoxToken = q.token_of_request(url=url)
    Authorization = 'QBox ' + QBoxToken
    return Authorization

# post请求
def requests_qiniu(url, Authorization):
    headers = {
        'Host': 'api.qiniu.com',
        'Content - Type': 'application/json',
        'Authorization': Authorization
    }
    data ={
        # 基本配置
        'type': 'normal',
        'platform': 'web',
        'geoCover': 'china',
        'protocol': 'http'
    }
    response = requests.post(url=url, data=data, headers=headers)
    return response


if __name__ == '__main__':
    access_key = 'your_AK'
    secret_key = 'your_SK'
    q = Auth(access_key, secret_key)
    url = 'http://api.qiniu.com/domain/create.pasca.top'
    uri = 'http://api.qiniu.com/domain/create.pasca.top/n'
    Authorization = token_of_request(q, uri)
    print(Authorization)
    response = requests_qiniu(url, Authorization)
    print(response)




