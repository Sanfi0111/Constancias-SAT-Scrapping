from pyzbar import pyzbar
from PIL import Image

''' Given an image with a QR Code, reads the QR code and returns the link
    String codeQR - The image with the QR code
    Return- The link from the QR code
'''
class ReadQR():
    
    urls = []
    def __init__(self, urls):
        self.urls = urls
    def readQr(self,listaImagenes):
        urls = []
        for imagenes in listaImagenes:   
            image = Image.open(imagenes)
            qr_code = pyzbar.decode(image)[0]
            #Convertir a String
            data= qr_code.data.decode("utf-8")
            type = qr_code.type
            url = f"{type}-->, {data}"
            print(url)
            urls.append(data)
            print("----")
        return urls
