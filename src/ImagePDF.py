import os
import fitz   
from tqdm import tqdm 

class ImagePDF():
    nomImagenes = []
    def __init__(self, nomImagenes):
        self.nomImagenes = nomImagenes


    '''Given a PDF, takes a snapshot at the exact position of the QR code.
    String dir- The direction of the file with the PDf´s
    Return - The images from PDF'''
    def getQRSFromPDF(self, dir,nomImagenes):
        for each_path in os.listdir(dir):
            if ".pdf" in each_path:
                doc = fitz.Document((os.path.join(dir, each_path)))
                num = 0
                for i in tqdm(range(len(doc)), desc="pages"):
                    for img in tqdm(doc.get_page_images(i), desc="page_images"):
                        xref = img[0]
                        image = doc.extract_image(xref)
                        pix = fitz.Pixmap(doc, xref)
                        if(num == 3):
                            print("Lista de imagenes  ")
                            print()
                            nomImagenes.append(str(os.path.join(dir, "%s_p%s-%s.png" % (each_path[:-4], i, xref))))
                            print(nomImagenes)
                            pix.save(os.path.join(dir, "%s_p%s-%s.png" % (each_path[:-4], i, xref)))
                            num = num+1
                        else: num = num+1
        print("Completed")
        return nomImagenes            
