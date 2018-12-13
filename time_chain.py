# -*- coding: utf-8 -*-
from qiniu import Auth,  create_timestamp_anti_leech_url
from qiniu.compat import is_py2
from qiniu.compat import is_py3
import time

def urlencode(str):
    if is_py2:
        import urllib2
        return urllib2.quote(str)
    elif is_py3:
        import urllib.parse
        return urllib.parse.quote(str)

def to_deadline(rang):
    return int(time.time()) + rang

if __name__ == '__main__':
    access_key = 'your_AK'
    secret_key = 'your_SK'
    q = Auth(access_key, secret_key)
    # 配置时间戳防盗链的参数
    host = '七牛空间绑定域名'
    file_name = '需要加密的文件名'
    encrypt_key = 'CDN后台生成key，主key和备key皆可'
    deadline = 3600  # 链接有效期时间戳（以秒为单位）
    time = to_deadline(deadline)
    query_string = ''
    try:
        '''
            create_timestamp_anti_leech_url(host, file_name, query_string, encrypt_key, deadline)
              Args:
                host:              带访问协议的域名
                file_name:         原始文件名，不需要urlencode
                query_string:      查询参数，不需要urlencode
                encrypt_key:       时间戳防盗链密钥
                deadline:          链接有效期时间戳（以秒为单位）
        
            Returns:
                带时间戳防盗链鉴权访问链接
        '''
        url_time = create_timestamp_anti_leech_url(host, file_name, query_string, encrypt_key, time)
        print('http://', url_time)
    except:
        print('生成防盗链url错误')
