import cv2
import pytesseract


class CuartaImagen:

    def __init__(self):

        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

        img = cv2.imread('text4.png')
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        print(pytesseract.image_to_string(img))

        f = open ('tesseract', 'w')
        f.write(pytesseract.image_to_string(img))
        f.close()

        cv2.imshow('Result',img)
        cv2.waitKey(0)

