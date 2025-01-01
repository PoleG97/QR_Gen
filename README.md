# Introducción
Este script esá pensado para la generación de código QR de 
manera sencilla y rápida. Exportando una imagen del código 
en formato PNG.

# Objetivo
Generar QR de manera sencilla y rápida, pero sobretodo duradera.
La mayoría de sitios de generación de QR implican un tiempo de
vida limitado, por lo que se busca una solución que permita
generar códigos QR que no caduquen.

# Uso
## Instalar los requisitos
```bash
pip install -r requirements.txt
```

## Ejecutar el script
```bash
python qr_gen.py
```
o
```bash
python3 qr_gen.py
```

## Uso del script
Ahora sólo habrá que seguir lo que pida el script.

1. La URL completa que se quiere codificar.
2. Si se quiere o no dar un nombre personalizado al archivo.

>[!WARNING]
> EL nombre no debe incluir espacios ni caracteres especiales.

> En caso de querer dar un nombre personalizado, no hace falta 
> incluir la extensión `.png`, ya que el script la añadirá
> automáticamente.

> Si no se da un nombre personalizado, el script generará un
> nombre automático basado en la fecha y hora de generación.