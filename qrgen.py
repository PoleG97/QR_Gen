import qrcode
import os
from colorama import Fore
import datetime

# URL del archivo PDF en Google Drive
pdf_url = input(f"{Fore.CYAN}Ingrese la URL\t: ")

# Definir la dirección donde se guardará el código QR
qr_path = os.path.join(os.path.dirname(__file__), "QR_Codes")

# Generar el código QR
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(pdf_url)
qr.make(fit=True)

# Preguntar al usuario si quiere dar un nombre personalizado al archivo
custom_name = input(f"{Fore.CYAN}¿Desea dar un nombre personalizado al archivo? (s/n)\t: ").lower()
if custom_name == "s":
    qr_filename = input(f"{Fore.CYAN}Ingrese el nombre del archivo\t: ")
    qr_filename = qr_filename + ".png"
else:
    # Guardar el código QR como imagen con el nombre basado en la fecha y hora de creación
    qr_filename = "QR_url_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"

qr_filepath = os.path.join(qr_path, qr_filename)

qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save(qr_filepath)

print(f"{Fore.GREEN}Código QR generado con éxito con el nombre {qr_filename}")
