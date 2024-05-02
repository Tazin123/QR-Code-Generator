import qrcode
from django.core.mail import mail_managers

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = "https://www.youtube.com/@TechieCoder/playlists"
qr.add_data(data)
qr.make(fit=True)  # Change `true` to `True`
img = qr.make_image(fill="black", back_color="white")
img.save("test.png")
