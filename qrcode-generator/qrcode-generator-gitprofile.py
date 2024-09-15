import qrcode
from PIL import Image

# Data to encode
data = "https://github.com/sachiniwathudura"

# Create an instance of QRCode
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border thickness
)

# Add the data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the QR code image
img.save("qrcode_with_pillow.png")

# Optionally, open and display the image
img.show()
