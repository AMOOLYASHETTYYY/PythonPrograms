import qrcode

upi_id = "amoolyashetty10@okicici"
name = "amoolya shetty"
amount = "100"
currency = "INR"


upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}"


img = qrcode.make(upi_url)


img.save("gpay_qr.png")

print("QR Code saved as gpay_qr.png")
