import qrcode
from qrcode.image.pil import PilImage

# Create a customized QR code with different colors
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    # box_size=10,
    # border=4,
)
qr.add_data('https://www.linkedin.com/posts/rakeshdey007_geeksforgeeks-w3schools-jsmastery-activity-7217085433321574400-jQ43?utm_source=share&utm_medium=member_android')
qr.make(fit=True)

# Change the fill color to "blue" and the back color to "white"
img = qr.make_image(fill_color="white", back_color="black", image_factory=PilImage)
img.save("video.png")
