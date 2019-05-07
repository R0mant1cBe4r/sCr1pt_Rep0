# -*- coding: utf-8 -*-

#__Author__: Be4r

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QDir
import sys
import rsa
import base64
import datetime
import time
reload(sys)
sys.setdefaultencoding( "utf-8" )

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(448, 564)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("rsalogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.CreateKey = QtGui.QPushButton(self.centralwidget)
        self.CreateKey.setGeometry(QtCore.QRect(260, 20, 75, 23))
        self.CreateKey.setObjectName(_fromUtf8("CreateKey"))
        self.KeyName = QtGui.QLineEdit(self.centralwidget)
        self.KeyName.setGeometry(QtCore.QRect(120, 20, 121, 20))
        self.KeyName.setText(_fromUtf8(""))
        self.KeyName.setObjectName(_fromUtf8("KeyName"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.EncPlain = QtGui.QLineEdit(self.centralwidget)
        self.EncPlain.setGeometry(QtCore.QRect(120, 80, 121, 20))
        self.EncPlain.setObjectName(_fromUtf8("EncPlain"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.EncPubKey = QtGui.QLineEdit(self.centralwidget)
        self.EncPubKey.setGeometry(QtCore.QRect(120, 120, 121, 20))
        self.EncPubKey.setObjectName(_fromUtf8("EncPubKey"))
        self.Enc = QtGui.QPushButton(self.centralwidget)
        self.Enc.setGeometry(QtCore.QRect(350, 160, 75, 23))
        self.Enc.setObjectName(_fromUtf8("Enc"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 370, 111, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 250, 111, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 111, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.SignPriKey = QtGui.QLineEdit(self.centralwidget)
        self.SignPriKey.setGeometry(QtCore.QRect(120, 160, 121, 20))
        self.SignPriKey.setObjectName(_fromUtf8("SignPriKey"))
        self.SaveCipherAndSign = QtGui.QPushButton(self.centralwidget)
        self.SaveCipherAndSign.setGeometry(QtCore.QRect(350, 490, 75, 23))
        self.SaveCipherAndSign.setObjectName(_fromUtf8("SaveCipherAndSign"))
        self.Dec = QtGui.QPushButton(self.centralwidget)
        self.Dec.setGeometry(QtCore.QRect(350, 200, 75, 23))
        self.Dec.setObjectName(_fromUtf8("Dec"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 200, 111, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.Signature = QtGui.QLineEdit(self.centralwidget)
        self.Signature.setGeometry(QtCore.QRect(120, 200, 121, 20))
        self.Signature.setObjectName(_fromUtf8("Signature"))
        self.EncResult = QtGui.QTextEdit(self.centralwidget)
        self.EncResult.setGeometry(QtCore.QRect(120, 250, 301, 101))
        self.EncResult.setObjectName(_fromUtf8("EncResult"))
        self.SignResult = QtGui.QTextEdit(self.centralwidget)
        self.SignResult.setGeometry(QtCore.QRect(120, 370, 301, 101))
        self.SignResult.setObjectName(_fromUtf8("SignResult"))
        self.LoadPub = QtGui.QPushButton(self.centralwidget)
        self.LoadPub.setGeometry(QtCore.QRect(260, 120, 75, 23))
        self.LoadPub.setObjectName(_fromUtf8("LoadPub"))
        self.LoadPri = QtGui.QPushButton(self.centralwidget)
        self.LoadPri.setGeometry(QtCore.QRect(260, 160, 75, 23))
        self.LoadPri.setObjectName(_fromUtf8("LoadPri"))
        self.LoadSign = QtGui.QPushButton(self.centralwidget)
        self.LoadSign.setGeometry(QtCore.QRect(260, 200, 75, 23))
        self.LoadSign.setObjectName(_fromUtf8("LoadSign"))
        self.ClearInfo = QtGui.QPushButton(self.centralwidget)
        self.ClearInfo.setGeometry(QtCore.QRect(270, 490, 75, 23))
        self.ClearInfo.setObjectName(_fromUtf8("ClearInfo"))
        self.SpendTime = QtGui.QLineEdit(self.centralwidget)
        self.SpendTime.setGeometry(QtCore.QRect(270, 520, 151, 20))
        self.SpendTime.setText(_fromUtf8(""))
        self.SpendTime.setObjectName(_fromUtf8("SpendTime"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA-GUI By Be4r", None))
        self.CreateKey.setText(_translate("MainWindow", "生成", None))
        self.label.setText(_translate("MainWindow", "输入生成密钥名称：", None))
        self.label_2.setText(_translate("MainWindow", "加密明文/解密密文：", None))
        self.label_3.setText(_translate("MainWindow", "加密公钥/解密私钥：", None))
        self.Enc.setText(_translate("MainWindow", "加密", None))
        self.label_4.setText(_translate("MainWindow", "结果（签名/验证）：", None))
        self.label_5.setText(_translate("MainWindow", "结果（明文/密文）：", None))
        self.label_6.setText(_translate("MainWindow", "签名私钥/验证公钥：", None))
        self.SaveCipherAndSign.setText(_translate("MainWindow", "保存", None))
        self.Dec.setText(_translate("MainWindow", "解密", None))
        self.label_7.setText(_translate("MainWindow", "签名（解密使用）：", None))
        self.LoadPub.setText(_translate("MainWindow", "加载", None))
        self.LoadPri.setText(_translate("MainWindow", "加载", None))
        self.LoadSign.setText(_translate("MainWindow", "加载", None))
        self.ClearInfo.setText(_translate("MainWindow", "清空", None))

class MyForm(QtGui.QMainWindow):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.CreateKey,QtCore.SIGNAL("clicked()"),self.creat_rsa_key)
		QtCore.QObject.connect(self.ui.Enc,QtCore.SIGNAL("clicked()"),self.enc_and_sign)
		QtCore.QObject.connect(self.ui.Dec,QtCore.SIGNAL("clicked()"),self.dec_and_verify)
		QtCore.QObject.connect(self.ui.SaveCipherAndSign,QtCore.SIGNAL("clicked()"),self.save_cipher_sign)

		QtCore.QObject.connect(self.ui.LoadPub,QtCore.SIGNAL("clicked()"),self.get_pub_path)
		QtCore.QObject.connect(self.ui.LoadPri,QtCore.SIGNAL("clicked()"),self.get_pri_path)
		QtCore.QObject.connect(self.ui.LoadSign,QtCore.SIGNAL("clicked()"),self.get_sign_path)

		QtCore.QObject.connect(self.ui.ClearInfo,QtCore.SIGNAL("clicked()"),self.clear_info)	


	#get public key file path
	def get_pub_path(self):
		encpubkey_path = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '.',"pub files (*.pub);;key files (*.key)")
		if encpubkey_path:
			cur_path = QDir('.')
			encpubkey_path = cur_path.relativeFilePath(encpubkey_path)
			encpubkey_path = unicode(encpubkey_path,'utf-8')
			self.ui.EncPubKey.setText(encpubkey_path)
		#print encpubkey_path

	#get private key file path
	def get_pri_path(self):
		signprikey_path = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '.',"pub files (*.pub);;key files (*.key)")
		if signprikey_path:
			cur_path = QDir('.')
			signprikey_path = cur_path.relativeFilePath(signprikey_path)
			signprikey_path = unicode(signprikey_path,'utf-8')
			self.ui.SignPriKey.setText(signprikey_path)
		#print signprikey_path

	#get signature file path
	def get_sign_path(self):
		sign_path = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '.',"sign files (*.sign)")
		if sign_path:
			cur_path = QDir('.')
			sign_path = cur_path.relativeFilePath(sign_path)
			sign_path = unicode(sign_path,'utf-8')
			self.ui.Signature.setText(sign_path)
		#print sign_path

	#create rsa key button
	def creat_rsa_key(self):
		keyname = str(self.ui.KeyName.text())
		#print len(keyname)
		if keyname == '':
			self.ui.SpendTime.setText('Please input key name...')
		else:
			starttime = datetime.datetime.now()
			RsaMethod().creat_rsa_key(keyname)
			endtime = datetime.datetime.now()
			self.ui.SpendTime.setText('It takes time: '+ str((endtime-starttime).seconds) + 's.')

	#encrypt button
	def enc_and_sign(self):
		plain = str(self.ui.EncPlain.text())
		encpubkey_path = str(self.ui.EncPubKey.text())
		signprikey_path = str(self.ui.SignPriKey.text())

		starttime = datetime.datetime.now()

		encpubkey = RsaMethod().load_pub_key(encpubkey_path)
		signprikey = RsaMethod().load_pri_key(signprikey_path)

		cipher = RsaMethod().encrypt_plain(plain, encpubkey)
		signature = RsaMethod().sign(plain, signprikey)
		self.ui.EncResult.setText(str(cipher))
		self.ui.SignResult.setText(str(signature))

		endtime = datetime.datetime.now()
		self.ui.SpendTime.setText('It takes time: '+ str((endtime-starttime).seconds) + 's.')

	#decrypt button
	def dec_and_verify(self):
		cipher = str(self.ui.EncPlain.text())
		decprikey_path = str(self.ui.EncPubKey.text())
		verifypubkey_path = str(self.ui.SignPriKey.text())
		signature_path = str(self.ui.Signature.text())

		starttime = datetime.datetime.now()

		decprikey = RsaMethod().load_pri_key(decprikey_path)
		verifypubkey = RsaMethod().load_pub_key(verifypubkey_path)
		signature = RsaMethod().load_signature(signature_path)

		plain = RsaMethod().decrypt_cipher(cipher,decprikey)
		signverify = RsaMethod().verify(plain,signature,verifypubkey)
		self.ui.EncResult.setText(str(plain))
		self.ui.SignResult.setText(str(signverify))

		endtime = datetime.datetime.now()
		self.ui.SpendTime.setText('It takes time: '+ str((endtime-starttime).seconds) + 's.')

	#save cipher and signature button
	def save_cipher_sign(self):
		cipher = str(self.ui.EncResult.toPlainText())
		signature = str(self.ui.SignResult.toPlainText())

		starttime = datetime.datetime.now()

		RsaMethod().save(cipher,base64.b64decode(signature))

		endtime = datetime.datetime.now()
		self.ui.SpendTime.setText('It takes time: '+ str((endtime-starttime).seconds) + 's.')

	#clear
	def clear_info(self):

		starttime = datetime.datetime.now()
		
		self.ui.KeyName.setText("")
		self.ui.EncPlain.setText("")
		self.ui.EncPubKey.setText("")
		self.ui.SignPriKey.setText("")
		self.ui.Signature.setText("")
		self.ui.EncResult.setText("")
		self.ui.SignResult.setText("")

		endtime = datetime.datetime.now()
		self.ui.SpendTime.setText('It takes time: '+ str((endtime-starttime).seconds) + 's.')


class RsaMethod():
	#create rsa key
	def creat_rsa_key(self,keyname):
		(pubkey, prikey) = rsa.newkeys(2048, poolsize=4)
		f1 = open(keyname+".pub","w+")
		f2 = open(keyname+".key","w+")
		publickey = pubkey.save_pkcs1()
		privatekey = prikey.save_pkcs1()
		f1.write(publickey)
		f1.flush()
		f2.write(privatekey)
		f2.flush()
		f1.close()
		f2.close()

	#load public key
	def load_pub_key(self,path):
		#with open(path+".pub") as publicfile:
		path = unicode(path,'utf-8')
		with open(path, mode='rb') as publicfile:
			p = publicfile.read()
			publickey = rsa.PublicKey.load_pkcs1(p)
		return publickey

	#load private key
	def load_pri_key(self,path):
		#with open(path+".key") as privatefile:
		path = unicode(path,'utf-8')
		with open(path, mode='rb') as privatefile:
			p = privatefile.read()
			privatekey = rsa.PrivateKey.load_pkcs1(p)
		return privatekey

	#load signature
	def load_signature(self,path):
		path = unicode(path,'utf-8')
		with open(path) as f:
			signature = f.read()
			f.close()
		return signature

	#enc(plain,public key),base64 output
	def encrypt_plain(self,message, publickey):
		encode = rsa.encrypt(message.encode('utf-8'), publickey)
		cipher = base64.b64encode(encode)
		return cipher

	#dec(cipher,private key), base64 input
	def decrypt_cipher(self,cipher, privatekey):
		cipher = base64.b64decode(cipher)
		try:
			plain = rsa.decrypt(cipher, privatekey)
			return plain.decode('utf-8')
		except:
			return 'Decryption failure, Please confirm the private key.'

	#sign with the private key
	def sign(self,message, privatekey):
		signature = rsa.sign(message, privatekey, 'SHA-256')
		return base64.b64encode(signature)

	#verify with the public key
	def verify(self,plain, signature , publickey):
		try:
			verify_result = rsa.verify(plain, signature, publickey)
			return 'Verify success, the signature method is '+verify_result
		except:
			return 'Verify fail, the message is not trusted.'

	#save the cipher and signature
	def save(self,cipher,signature):
		f1 = open("Rsaresult","w+")
		f2 = open("Signature.sign","w+")
		f1.write(cipher)
		f1.flush()
		f2.write(signature)
		f2.flush()
		f1.close()
		f2.close()


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())
