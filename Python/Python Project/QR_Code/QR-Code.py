import qrcode
img = qrcode.make('https://www.linkedin.com/posts/rakeshdey007_geeksforgeeks-w3schools-jsmastery-activity-7217085433321574400-jQ43?utm_source=share&utm_medium=member_android')
type(img)  # qrcode.image.pil.PilImage
img.save("Password_Generator.png")