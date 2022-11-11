import pyqrcode
import png
from pyqrcode import QRCode

#string which will be in QR
QR="https://www.instagram.com"

#calling the method to generate qr
url=pyqrcode.create(QR)

#creating and saving png file
url.png('qrcode.png',scale=7)
