import qrcode


url = "https://github.com/AMOOLYASHETTYYY/PythonPrograms"


qrimg = qrcode.make(url)


qrimg.save("githubqr.png")

print("QR code saved as githubqr.png")
