# -*- coding: utf-8 -*-

import rsa
import base64

#生成rsa公私钥
def creat_rsa_key(key_lenth):
	(pubkey, prikey) = rsa.newkeys(key_lenth)
	f1 = open("public.pub","w+")
	f2 = open("private.key","w+")
	publickey = pubkey.save_pkcs1()
	privatekey = prikey.save_pkcs1()
	f1.write(publickey)
	f1.flush()
	f2.write(privatekey)
	f2.flush()
	f1.close()
	f2.close()

#装载公私钥
def load_pub_key():
	with open("public.pub") as publicfile:
		p = publicfile.read()
		publickey = rsa.PublicKey.load_pkcs1(p)
	return publickey

def load_pri_key():
	with open("private.key") as privatefile:
		p = privatefile.read()
		privatekey = rsa.PrivateKey.load_pkcs1(p)
	return privatekey	

#公钥、明文加密，base64输出
def encrypt_plain(message, publickey):
	encode = rsa.encrypt(message, publickey)
	cipher = base64.b64encode(encode)
	return cipher

#私钥、密文解密，密文base64输入
def decrypt_cipher(cipher, privatekey):
	cipher = base64.b64decode(cipher)
	plain = rsa.decrypt(cipher, privatekey)
	return plain

#使用私钥进行签名
def sign(message, privatekey):
	signature = rsa.sign(message, privatekey, 'SHA-256')
	return signature

#使用公钥进行签名验证
def verify(plain, signature , publickey):
	verify_result = rsa.verify(plain, signature, publickey)
	return verify_result


if __name__== "__main__":

	message = "sectest"
	#creat_rsa_key(2048)
	publickey = load_pub_key()
	privatekey = load_pri_key()
	cipher = encrypt_plain(message, publickey)
	plain = decrypt_cipher(cipher, privatekey)
	print "密文: "+cipher
	print "明文："+plain
	signature = sign(message, privatekey)
	print "签名: "+signature
	print "签名验证: "+verify(plain, signature, publickey)
