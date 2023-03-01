#Librerias
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib


# Iniciamos los parámetros del script
remitente = 'cjuarez@creze.com'
destinatarios = ['cjuarez@creze.com']
# destinatarios = ['bprum@creze.com','stabares@creze.com','jahedo@creze.com','sgazca@creze.com','ecervantes@creze.com','caguilar@creze.com','apedroza@creze.com','celine@creze.com','jmartinez@creze.com','cjuarez@creze.com','asantiago@creze.com','pislas@creze.com']
asunto = f'PAGO PUNTUAL CREZE_DOMICILIACIÓN_MAQUINARIA Y EQUIPOS DE TERRACERIA SA DE CV'
cuerpo = f'Buena tarde. \n\nEstimado Benjamin Enrique Perez Sandi Martinez esperamos se encuentre muy bien, le recordamos que su crédito Creze con contrato C12137CC6358 a nombre de MAQUINARIA Y EQUIPOS DE TERRACERIA SA DE CV , tiene programado su pago puntual el día 28/02/2023 por un monto de $55,985.43; es importante mantener el saldo en la cuenta para que podamos realizar la domiciliación correspondiente; con esto evitar intereses moratorios y mala calificación ante buró de crédito \n\n ¡Agradecemos el compromiso con su crédito! \n\nEn caso de preferir aplicar su pago por transferencia, recuerda que también contamos con esta forma de pago, compartimos los datos bancarios: \n\nNúmero de Cuenta: 0114736958 \nBanco: BBVA BANCOMER S.A. IBM \nBeneficiario: BANCO ACTINVER SA POR CT DEL FID 4353 \nCLABE: 012180001147369582 \nRFC: PSC091014U80 \nConcepto: C12137CC6358 \nPago: $55,985.43 \nArea de Cobranza' 

ruta_adjunto = 'cb.jpg'
nombre_adjunto = 'cb.jpg'

# # Creamos el objeto mensaje
mensaje = MIMEMultipart()

# # Establecemos los atributos del mensaje
mensaje['From'] = remitente
mensaje['To'] = ", ".join(destinatarios)
mensaje['Subject'] = asunto

# # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
mensaje.attach(MIMEText(cuerpo, 'plain'))

# # Abrimos el archivo que vamos a adjuntar
archivo_adjunto = open(ruta_adjunto, 'rb')

# # Creamos un objeto MIME base
adjunto_MIME = MIMEBase('application', 'octet-stream')
# Y le cargamos el archivo adjunto
adjunto_MIME.set_payload((archivo_adjunto).read())
# Codificamos el objeto en BASE64
encoders.encode_base64(adjunto_MIME)
# Agregamos una cabecera al objeto
adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
# Y finalmente lo agregamos al mensaje
mensaje.attach(adjunto_MIME)

# Creamos la conexión con el servidor
sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)

# Ciframos la conexión
sesion_smtp.starttls()

# Iniciamos sesión en el servidor
sesion_smtp.login() 

# Convertimos el objeto mensaje a texto
texto = mensaje.as_string()

# Enviamos el mensaje
sesion_smtp.sendmail(remitente, destinatarios, texto)

# Cerramos la conexión
sesion_smtp.quit()

print("Correo enviado con exito")