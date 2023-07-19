import qrcode
import os

# URL del archivo PDF en Google Drive
pdf_url = input("Introduce la direccion para generar:: ")

# Definir la dirección donde se guardará el código QR
qr_path = "/home/jairo/Pictures"

# Generar el código QR
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(pdf_url)
qr.make(fit=True)

# Guardar el código QR como imagen
qr_filename = "qr_code.png"
qr_filepath = os.path.join(qr_path, qr_filename)
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save(qr_filepath)

print(f"Código QR generado y guardado en: {qr_filepath}")
