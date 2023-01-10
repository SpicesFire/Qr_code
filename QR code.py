import qrcode
import image
link = input("URL'yi giriniz:")
code=qrcode.make(link)
code.save("reis.png")