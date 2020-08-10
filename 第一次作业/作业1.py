import random
n = random.randint(1,8)
import urllib.request
name = 'name'
tep1 = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596823900026&di=56d9945df232e86068a7934c6e1e6679&imgtype=0&src=http%3A%2F%2Fpics1.baidu.com%2Ffeed%2F8b82b9014a90f603e0304156d382131eb151edb2.jpeg%3Ftoken%3D14a5b4b92518a1e92cc5103e1d083a73%26s%3DB82CEE161B436ECC0ACBC06D0300707B'
tep2 = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596824207039&di=afb97316d0c3a3d412a6a0e704170a74&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201802%2F09%2F20180209203423_lgldt.jpg'
tep3 = 'http://www.ifavart.com/UploadFile/big/201802/20180208125338_76140.jpg'
tep4 = 'http://www.ifavart.com/UploadFile/big/201802/20180208125344_50671.jpg'
tep5 = 'http://www.ifavart.com/UploadFile/big/201802/20180208125349_15596.jpg'
tep6 = 'http://www.ifavart.com/UploadFile/big/201802/20180208125353_40466.jpg'
tep7 = 'http://www.ifavart.com/UploadFile/big/201801/20180130112050_39220.jpg'
tep8 = 'http://www.ifavart.com/UploadFile/big/201709/20170927174156_29595.jpg'
if n == 1:
    tep = tep1
    name = 'tep1'
if n == 2:
    tep = tep2

    name = 'tep2'
if n == 3:
    tep = tep3
    name = 'tep3'
if n == 4:
    tep = tep4
    name = 'tep4'
if n == 5:
    
    tep = tep5
    name = 'tep5'
if n == 6:
    tep = tep6
    name = 'tep6'
if n == 7:
    tep = tep7
    name = 'tep7'
if n == 8:
    tep = tep8
    name = 'tep8'
response = urllib.request.urlopen(tep)
img1 = response.read()

with open(name+'.jpg.jpg','wb')as f:
    f.write(img1)
