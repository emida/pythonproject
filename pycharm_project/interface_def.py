import requests
from config import *
import rsa
import base64
import re
import pickle


def get_dataandpost():
	with open("data.txt","r",encoding='utf-8') as fp:
		str=fp.read()
		list=str.split('\n')
		for i in list:
			#print('I=',i)
			url,header,data,keyword=i.split('||')
			#print('url=%s\nheader=%s\ndata=%s\nkeyword=%s\n'%(url,header,data,keyword))
			assert_word(keyword,post(url,header,data))

		
#反序列化
def get_unique_number():
	#你得先是用pickle写的，才能读出来
	
	try:
		with open("uniquenumber.txt","rb") as fp:
			unique_number = pickle.load(fp)  #序列化，将文件中的数字读取出来
	except Exception as e:
		print(e,'\n')
		with open("uniquenumber.txt","wb") as fp:
			pickle.dump(1,fp)
	else:
		with open("uniquenumber.txt","wb") as fp:
			pickle.dump(unique_number+1,fp)   #反序列化，将数字+1后，写到文件中覆盖原有的值！
	print(unique_number)
	return unique_number

def rsa2(jiamichuan):
	pubKey_str2 = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCTIlemLUY83iDZ+GlzA0QorkojUulAbXkGkXhqa98EoMmyKExVJRwgE6ZVn997FnRS5hiis5Q/CrxxcZtcJpCDRg1Ww68y90fHW/1Hv4HbKWO6d8jsxXRGo+NsMhRCb+Ne4zXKKIoMXJHLgY+BVD2gu0PgJq4Ys0Vw6oM+0hxfZwIDAQAB"
	pubKey_str1 = '''-----BEGIN PUBLIC KEY-----
	MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCTIlemLUY83iDZ+GlzA0QorkojUulAbXkGkXhqa98EoMmyKExVJRwgE6ZVn997FnRS5hiis5Q/CrxxcZtcJpCDRg1Ww68y90fHW/1Hv4HbKWO6d8jsxXRGo+NsMhRCb+Ne4zXKKIoMXJHLgY+BVD2gu0PgJq4Ys0Vw6oM+0hxfZwIDAQAB
	-----END PUBLIC KEY-----
	'''
	# 3、生成publicKey对象
	#key = rsa.PublicKey.load_pkcs1(pubKey_str2)
	key = rsa.PublicKey.load_pkcs1_openssl_pem(pubKey_str1)
	#key=rsa.PublicKey.load_pkcs1(pubKey_str)
	#private_key = rsa.PrivateKey.load_pkcs1(privateKey)
	message=jiamichuan
	#要加密的明文必须得转为字节类型哇
	#a = bytes(message, encoding='utf-8')
	a=message.encode('utf-8')#和上面作用一样将str转为字节
	cryptedMessage=rsa.encrypt(a,key)
	#加密之后需要对结果进行base64转码,后utf-8转码,并去掉换行和回车CRLF
	aa = base64.encodestring(cryptedMessage).decode('utf-8').strip().replace('\n','')
	#print("我写的程序：",aa)
	'''
	aa_ noB=re.findall(r"b\'(.+?)\'",aa)
	print("我写的程序：",aa_noB[0])
	'''
	return(aa)


def post(url,header,data):
	#通过eval获取配置的ip，并将字符串转换为字典
	response=requests.post(url=eval(url),headers=eval(header),data=data)
	#print(response.text)
	return(response.text)	

def assert_word(keyword,response_text):
	if re.search(keyword,response_text):
		print('断言成功')
	else:
		print('断言失败')


