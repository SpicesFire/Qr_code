import qrcode
import image
link = input("Enter URL:")
file_name = input("Enter file name: ")
code=qrcode.make(link)
code.save(file_name)
