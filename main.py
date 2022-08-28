import qrcode
from PIL import Image, ImageDraw

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size= 10, border=4)
qr.add_data("https://www.facebook.com/sandy.singh.944023")
qr.make(fit=True)
img=qr.make_image()
img.save("My_profile_qrcode.png")
