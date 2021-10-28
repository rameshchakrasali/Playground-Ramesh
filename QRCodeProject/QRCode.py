import qrcode
data = qrcode.make("https://www.youtube.com/")
print(type(data))
print(data.pixel_size)
data.save("YouTubeQR.jpg")

img = qrcode.make("Hi, I Love you!!!!!")
img.save("TextQR.jpg")

qr=qrcode.QRCode()
qr.add_data("Hi, I Love you!!!!")
qr.make()
img=qr.make_image()
img.save("TextQR1.jpeg")

qr=qrcode.QRCode(version=12,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=2,
    border=8)
qr.add_data("HKSJFKJSFJSFKJD")
qr.make()
img=qr.make_image(fill_color="red",back_color="#34fff0")
img.save("TextQR2.bmp")