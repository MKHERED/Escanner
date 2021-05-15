
import os, sys, time, pytesseract, win32api, win32con, math, pyautogui, hunspell, pyperclip

l_Pos = list()

class process():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        print(l_Pos)




        
        
        self.ancho = self.x2 - self.x1
        self.alto = self.y2 - self.y1
        
        

        self.name = str('{}{}{}{}M.png').format(self.x1, self.y1, self.x2, self.y2)
        time.sleep(0.5)

        
        self.url = str(os.getcwd() + "\Escanner\img\{}").format(self.name)
        
        self.capture()

    def capture(self):
         
        screenshot = pyautogui.screenshot(region=(self.x1, self.y1, self.ancho, self.alto))
        
         
        screenshot.save(self.url)

        
        time.sleep(0.5)
        
        self.analis()

    def analis(self):
        
        self.text_sep = str()

        
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        
        
        time.sleep(0.5)

        
        if os.path.isabs("\Escanner\img\{}".format(self.name)) == True:
            print('Verdadero')
            
            try:
                from PIL import Image
            except ImportError:
                import Image
                pass
            
            print('analizando busqueda')

            
            img_text = pytesseract.image_to_string(Image.open(self.url))
            
            
            

            
            print('foto eliminada: {}'.format(self.name))
            os.remove(self.url)

            
            img_text.replace('\x0c', ' ')
            img_text.replace('\n', ' ')
            
            
            self.text_sep = img_text.split()

            
            
            
            dic = str(os.getcwd()) + '\Escanner\dic'
            dictionary = hunspell.Hunspell(dic + '\es_Es', dic + '\es_ES')
            
            self.corregir_palabras(dictionary, self.text_sep)
            

    def corregir_palabras(self, corrector, palabras):
        
        self.corrector = corrector
        self.palabras = palabras

        
        self.corregida = []

        
        for p in self.palabras:

            
            ok = self.corrector.spell(p)
            if not ok:
                
                suge = self.corrector.suggest(p)
                
                if len(suge) > 0:
                    
                    mejor_sugerencia = suge[0]
                    
                    self.corregida.append(mejor_sugerencia)
                    
                    find = int(self.palabras.index(p))
                    
                    texto = self.palabras.pop(find)
                    
                    texto = self.palabras.insert(find, mejor_sugerencia)

        
        texto = str(" ").join(self.palabras)
        
        
        
        
        
        print('Texto Copiado')
        pyperclip.copy(texto)
        
class inicio():
    def __init__(self):
        self.clic = win32api.GetAsyncKeyState(0x01)
        self.Segundo_OP()
    
    
    def Segundo_OP(self):
        temp_x2, temp_y2 = win32api.GetCursorPos()
        while True:
            state_actual = win32api.GetAsyncKeyState(0x01)
            if state_actual != self.clic:
                self.clic = state_actual
                if state_actual < 0:
                    x2, y2 = win32api.GetCursorPos()
                    if (x2 != temp_x2 or y2 != temp_y2):
                        print('Boton clic presionado en: ' + str(x2) +", "+str(y2))
                        l_Pos.append(x2)
                        l_Pos.append(y2)
                        
                        process(l_Pos[0], l_Pos[1], l_Pos[2], l_Pos[3])
                        break 
            time.sleep(.001)
            pass
    pass



tiempo_v = int()
contador = int()
val = int()

class validacion():
    def __init__(self, contador, val, tiempo_v):
        self.tiempo_v = tiempo_v
        self.contador = contador
        self.rueda(self.contador, val, self.tiempo_v)

    def rueda(self, contador, val, tiempo_v):
        while True:
            state_actual = win32api.GetAsyncKeyState(0x01)
            if val <= 0:
                if tiempo_v == 0:
                    print('tomando tiempo')
                    global inicio_t
                    inicio_t = time.time()  
                    tiempo_v = 1
                    pass
                if (state_actual < 0) and (contador <= 3):
                    contador += 1
                    print('mas uno, estado actual del contador: {}'.format(contador))
                    break
                        
                pass
            if contador >= 3:  
                
                val = 1
                contador = 0
                tiempo_v = 0
                
                fin_t = time.time()
                
                t_transc = float(fin_t - inicio_t)
                print(t_transc)

                if t_transc <= 1:
                    print('paso')
                    
                    def Primera_OP():
                        temp_x, temp_y = win32api.GetCursorPos()
                        l_Pos.append(temp_x)
                        l_Pos.append(temp_y)

                        print('posicion {}, {}'.format(l_Pos[0], l_Pos[1]))
                        inicio()
                        
                    Primera_OP()
                    pass
                elif t_transc >= 1:
                    print('no paso')

                    validacion(contador=0, val=0, tiempo_v=0)
                    
                    pass
                print('Fin del comprobador')

                sys.exit()
                break
            pass
        time.sleep(0.1)
        print(val)
        validacion(contador, val, tiempo_v)

validacion(contador, val, tiempo_v)



