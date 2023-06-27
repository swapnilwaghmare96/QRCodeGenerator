'''Youtube Channel Link'''
import qrcode 
from PIL import Image

qr=qrcode.QRCode(version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=20, border=4)
qr.add_data("https://www.youtube.com/channel/UCTP_n3YvtKWiPw0QlRw6npg")
qr.make(fit=True)
img=qr.make_image(fill_color="red", back_color="white")
img.save("yt_swapnilwaghmare96.png")
