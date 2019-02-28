#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 该脚本平均每小时提交 4万5千多条URL
# 推荐 0.3s,方便及时停止抓取， 一天提交10万~15万 URL  PS：因为URL一旦提交到队列中，就不可修改


import urlparse, hmac, hashlib, base64, commands, sys, time

def __token(data, secret_key):
		data = bytes(data)
		hashed = hmac.new(secret_key, data, hashlib.sha1)
		return base64.urlsafe_b64encode(hashed.digest())


def Qiniu_token(access_key, secret_key, method,host, url, content_type=None, body=None):
		"""
		<Method> <PathWithRawQuery>
		Host: <Host>
		Content-Type: <ContentType>
		[<X-Qiniu-*> Headers]
		[<Body>] #这里的 <Body> 只有在 <ContentType> 存在且不为 application/octet-stream 时才签进去。
		"""
		parsed_url = urlparse.urlsplit(url)
		netloc = parsed_url.netloc
		path = parsed_url.path
		query = parsed_url.query

		if not host:
			host = netloc

		path_with_query = path
		if query != '':
			path_with_query = ''.join([path_with_query, '?', query])
		data = ''.join(["%s %s" %
						(method, path_with_query), "\n", "Host: %s" %
						host, "\n"])

		if content_type:
			data += "Content-Type: %s" % (content_type) + "\n"+"\n"


		if content_type and content_type != "application/octet-stream" and body:
			data += body.decode(encoding='UTF-8')

		return '{0}:{1}'.format(access_key, __token(data, secret_key))


def post_fetch_request(Token, url, fetch_url, bucket_name, file_key, body):

	curl = """curl -d '%s' '%s' -H "Content-type: application/json"  -H 'Authorization:%s'""" % (body, url, Token)
	a,b = commands.getstatusoutput( curl )
	time.sleep( time_sleep )

if __name__ == '__main__':
	try:
		AccessKey = sys.argv[1]
		SecretKey = sys.argv[2]
		bucket_name= sys.argv[3]
		zone = sys.argv[4]  # z0,z1,z2,na0,as0 对应 华东，华北，华南，北美，东南亚
		file_name = sys.argv[5]  # 第一项为URL，保存的文件名默认为URI，每项用'\t'分割
		time_sleep = float(sys.argv[6])
	except Exception:
		print'version: 2018-11-21'
		print'./qiniu_big_fetch.py <ak> <sk> <bucket_name> <zone> <url_file_name> <time_sleep> \n'

	else:
		fout = open( file_name )
		while 1:
			line = fout.readline().strip()
			if not line:  break

			line_list=line.split('\t')
			fetch_url_single = line_list[0].strip()

			if len(line_list) == 1: file_key_single =  urlparse.urlsplit(fetch_url_single)[2].replace('/','',1)
			if len(line_list) > 1:  file_key_single=line_list[1].strip()

			path = '/sisyphus/fetch'

			host = 'api-%s.qiniu.com' % zone

			url = 'http://'+host+path

			body = '{"ignore_same_key":true, "url": "%s", "bucket": "%s", "key": "%s"  }' % (fetch_url_single, bucket_name, file_key_single  )

			if len(line_list) == 3:
				file_md5_check=line_list[2].strip()
				body = '{"ignore_same_key":true, "url": "%s", "bucket": "%s", "key": "%s", "md5": "%s" }' % (fetch_url_single, bucket_name, file_key_single , file_md5_check,  )

			try:
				Token = 'Qiniu ' + Qiniu_token( AccessKey, SecretKey, method='POST', host='', url=url, content_type='application/json' , body=body )
				post_fetch_request( Token, url, fetch_url_single, bucket_name, file_key_single , body)
			except Exception:
				print ("there must be error in token or post")


