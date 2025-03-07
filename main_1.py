import qrcode 
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4)

qr.add_data("https://www.linkedin.com/in/virendragoura?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app")
qr.make(fit=True)
img = qr.make_image(fill_color="blue",back_color="white")
img.save("Virendra_Linkedin.png")
