"""
This program is made by Kerem Aydın Güven
"""
import qrcode
import image
link = input("Enter URL:")
file_name = input("Enter file name: ")
code=qrcode.make(link)
code.save(f"{file_name}.png")
code.show(f"{file_name}.png")
