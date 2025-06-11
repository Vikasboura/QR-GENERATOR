import qrcode

# Take input from user
data = input("Enter the text or URL to convert into a QR code: ")

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Create the image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
filename = "qr_code.png"
img.save(filename)

print(f"✅ QR Code saved as '{filename}'")
# Display the QR code
