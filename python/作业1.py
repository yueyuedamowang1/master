import random
n = random.randint(1,8)
import urllib.request
name = 'name'
web1 = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596823900026&di=56d9945df232e86068a7934c6e1e6679&imgtype=0&src=http%3A%2F%2Fpics1.baidu.com%2Ffeed%2F8b82b9014a90f603e0304156d382131eb151edb2.jpeg%3Ftoken%3D14a5b4b92518a1e92cc5103e1d083a73%26s%3DB82CEE161B436ECC0ACBC06D0300707B'
web2 = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596824207039&di=afb97316d0c3a3d412a6a0e704170a74&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201802%2F09%2F20180209203423_lgldt.jpg'
web3 = 'http://www.ifavart.com/UploadFile/big/201802/20180208125338_76140.jpg'
web4 = 'http://www.ifavart.com/UploadFile/big/201802/20180208125344_50671.jpg'
web5 = 'http://www.ifavart.com/UploadFile/big/201802/20180208125349_15596.jpg'
web6 = 'http://www.ifavart.com/UploadFile/big/201802/20180208125353_40466.jpg'
web7 = 'http://www.ifavart.com/UploadFile/big/201801/20180130112050_39220.jpg'
web8 = 'http://www.ifavart.com/UploadFile/big/201709/20170927174156_29595.jpg'
if n == 1:
    web = web1
    name = 'pic1'
if n == 2:
    web = web2

    name = 'pic2'
if n == 3:
    web = web3
    name = 'pic3'
if n == 4:
    web = web4
    name = 'pic4'
if n == 5:
    
    web = web5
    name = 'pic5'
if n == 6:
    web = web6
    name = 'pic6'
if n == 7:
    web = web7
    name = 'pic7'
if n == 8:
    web = web8
    name = 'pic8'
response = urllib.request.urlopen(web)
img1 = response.read()

with open(name+'.jpg.jpg','wb')as f:
    f.write(img1)
print("图片已保存")
