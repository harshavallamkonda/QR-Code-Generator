import pyqrcode
from pyqrcode import QRCode


# String which represent the QR code
s = "https://harshaportfolio.netlify.app"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "filename.svg"
url.svg("myportfolio.svg", scale=8)
