
import timeit, time, os, win32api, win32con, sys

# ---------------------------------------------
# Este es El codigo principal.... ahora a hacer un hilo
tiempo_v = int()
contador = int()
val = int() #Val es la variable que activa y desativa la funcion
class inicio():
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
                    inicio_t = time.time() # Aqui tomamos el tiempo
                    tiempo_v = 1
                    pass

                if (state_actual < 0) and (contador <= 3 ) :
                    print('Es menor')
                    contador += 1
                    print(contador)
                    break
                pass
            elif (val == 1): #seguir con la operacion principal
                print('fin del comprobador')
                # aqui seguimos validando el tiempo
                
                sys.exit() # esto es temporal
                break
            
            pass
###############################################################################
            if contador >= 3:
                val = 1
                contador = 0
                tiempo_v = 0

                fin_t = time.time()

                t_trans = float(fin_t - inicio_t)

                print(t_trans)

                if t_trans <= 1:
                    print('pasa')
                    #Ejecutar aque las demas funciones XD de capture
                    pass
                elif t_trans >= 1:
                    print('no pasa')
                    pass
                break
                pass
################################################################################        

        time.sleep(0.1)
        print(val)
        inicio(contador, val, tiempo_v)

inicio(contador, val, tiempo_v)
