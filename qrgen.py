import qrcode
import os
from colorama import Fore
import datetime
from PIL import Image

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

# Preguntar al usuario por el color del código QR
fill_color = input(
    f"{Fore.CYAN}Ingrese el color de relleno del código QR en formato RGB (por ejemplo: 255,0,0 para rojo)\t: ").lower()

qr_filepath = os.path.join(qr_path, qr_filename)

qr_img = qr.make_image(fill_color=tuple(map(int, fill_color.split(','))), back_color="white")

# Preguntar al usuario si quiere agregar una imagen en el centro del QR
add_logo = input(f"{Fore.CYAN}¿Desea agregar una imagen en el centro del QR? (s/n)\t: ").lower()
if add_logo == "s":
    logo_path = input(f"{Fore.CYAN}Ingrese el nombre de la imagen PNG (sin extensión)\t: ")
    logo = Image.open(os.path.join(os.path.dirname(__file__), "Images", logo_path + ".png"))

    # Calcular el tamaño del logo
    qr_width, qr_height = qr_img.size
    logo_size = qr_width // 4
    logo = logo.resize((logo_size, logo_size))

    # Crear un nuevo QR con espacio en el centro
    qr_center = qrcode.QRCode(version=1, box_size=10, border=4)
    qr_center.add_data(pdf_url)
    qr_center.make(fit=True)
    qr_center_img = qr_center.make_image(fill_color=tuple(map(int, fill_color.split(','))), back_color="white")

    # Calcular la posición para centrar el logo
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
    qr_center_img.paste(logo, pos, mask=logo)

    qr_center_img.save(qr_filepath)
else:
    qr_img.save(qr_filepath)

print(f"{Fore.GREEN}Código QR generado con éxito con el nombre {qr_filename}")