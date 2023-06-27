'''GithubLink'''
import qrcode 
from PIL import Image

qr=qrcode.QRCode(version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=20, border=4)
qr.add_data("https://github.com/swapnilwaghmare96")
qr.make(fit=True)
img=qr.make_image(fill_color="red", back_color="white")
img.save("Github_swapnilwaghmare96.png")
