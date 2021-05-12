
import os, time, pytesseract, win32api, win32con, time, math, pyautogui, hunspell, pyperclip

class process():
    def __init__(self, x1, y1, x2, y2):
        #Posicion 1
        self.x1, self.y1 = (x1, y1)
        #Posicion 2
        self.x2, self.y2 = (x2, y2)
        
        #print("x1 = {}, y1 = {}, x2 = {}, y2 ={}".format(self.x1, self.y1, self.x2, self.y2))
        #Distancia desde x2 hasta x1 y y2 hasta y1
        distancia = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
        
        #Distancia entre cada punto
        #print(distancia) 
        self.ancho, self.alto = (self.x2 - self.x1, self.y2 - self.y1)
        #print(str(self.ancho) + " Y " + str(self.alto) )
        #self.name = Nombre.jpeg

        self.name = str('x{}y{}x{}y{}M.jpeg').format(self.x1, self.y1, self.x2, self.y2)
        time.sleep(0.5)

        #Direccion a donde se va a guardar la foto
        self.url = str(os.getcwd() + "\Escanner\img\{}").format(self.name)
        #Fin del init
        self.capture()

    def capture(self):
        #Especificacion del tamaño de la foto 
        screenshot = pyautogui.screenshot(region=(self.x1, self.y1, self.ancho, self.alto))
        #print('paso')
        #Se guarda la folo en self.url... 
        screenshot.save(self.url)

        #Tiempo miemtras se guarda la foto para continuar
        time.sleep(0.5)
        #fin de capture
        self.analis()

    def analis(self):
        #Variable donde va el texto y a iterar como lista
        self.text_sep = str()

        #Definicion de ruta para el analizador
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        
        #Tiempo de espera mietras se ubica la foto
        time.sleep(0.5)

        #Comprobando que la foto ya este guardada en self.url...
        if os.path.isabs("\Escanner\img\{}".format(self.name)) == True:
            #print('Verdadero')

            try:
                from PIL import Image
            except ImportError:
                import Image
                pass
            #print('analizando busqueda')

            #Variable de Foto-texto a pasar
            img_text = pytesseract.image_to_string(Image.open(self.url))
            
            #Texto con errores
            #print(img_text)

            #Capture tomada, y eliminada despues de obtener los datos
            print('foto eliminada: {}'.format(self.name))
            os.remove(self.url)

            #Limpiando los caracteres que tenga el texto
            img_text.replace('\x0c', ' ')
            img_text.replace('\n', ' ')
            
            #Dividiendo el texto en palabras y agregandolas a una lista para ser iteradas
            self.text_sep = img_text.split()

            #print(self.text_sep)
            
            #Ubicacion del diccionario a usar para corregir palabras
            dic = str(os.getcwd()) + '\Escanner\dic'
            dictionary = hunspell.Hunspell(dic + '\es_Es', dic + '\es_ES')
            #Fin de analis
            self.corregir_palabras(dictionary, self.text_sep)
            

    def corregir_palabras(self, corrector, palabras):
        #Variables a usar como diccionario, el Texto de la foto
        self.corrector = corrector
        self.palabras = palabras

        #Lista de palabras corregidas
        self.corregida = []

        #Iterar self.palabras para comprobar si esta bien escrita o tiene errores
        for p in self.palabras:

            #comprobar si pasa o no la verificacion
            ok = self.corrector.spell(p)
            if not ok:
                #Sugerencias del diccionario
                suge = self.corrector.suggest(p)
                #Evitar poner sugerencias de menor tamaño que la palabra del texto
                if len(suge) > 0:
                    #Tomar la primera sugerencia
                    mejor_sugerencia = suge[0]
                    #agendarla a palabras corregidas
                    self.corregida.append(mejor_sugerencia)
                    #Buscar el indice de la palabra mala para sustituir
                    find = int(self.palabras.index(p))
                    #Eliminar la palabra mala
                    texto = self.palabras.pop(find)
                    #Sustituir con el indice de la palabra mala, por la sugerencia
                    texto = self.palabras.insert(find, mejor_sugerencia)

        #Crear una cadena de texto con la lista ya corregida
        texto = str(" ").join(self.palabras)
        
        #print(self.corregida)
        #print('--'*50)
        #print(texto)
        
        print('Texto Copiado')
        pyperclip.copy(texto)
        
class inicio():
    def __init__(self):
        self.clic = win32api.GetAsyncKeyState(0x01)
        self.Primera_OP()

    #Funcion para tomar la posicion del primer click(x1 , y1) del mouse
    def Primera_OP(self):
        temp_x, temp_y = win32api.GetCursorPos()
        while True:
            state_actual = win32api.GetAsyncKeyState(0x01)
            if state_actual != self.clic:
                self.clic = state_actual
                if state_actual < 0:
                    x1, y1 = win32api.GetCursorPos()
                    if (x1 != temp_x or y1 != temp_y):
                        print('Boton clic presionado en: ' + str(x1) +", "+str(y1))
                        temp_x = x1
                        temp_y = y1
                        self.Segundo_OP(x1, y1)
                        break 
            time.sleep(.001)
            pass
        pass
    
    #Funcion para tomar la posicion del segundo click(x2, y2) del mouse
    def Segundo_OP(self, x1, y1):
        temp_x2, temp_y2 = win32api.GetCursorPos()
        while True:
            state_actual = win32api.GetAsyncKeyState(0x01)
            if state_actual != self.clic:
                self.clic = state_actual
                if state_actual < 0:
                    x2, y2 = win32api.GetCursorPos()
                    if (x2 != temp_x2 or y2 != temp_y2):
                        print('Boton clic presionado en: ' + str(x2) +", "+str(y2))
                        temp_x2 = x2
                        temp_y2 = y2
                        process(x1, y1, x2, y2)
                        break 
            time.sleep(.001)
            pass
    pass

inicio()
            



