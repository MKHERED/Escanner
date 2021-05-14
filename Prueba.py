import timeit, time, os, win32api, win32con
"""
class P():
    def __init__(self):
        self.clic = win32api.GetAsyncKeyState(0x01)
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
                        break 
            time.sleep(.001)
            pass
        pass

P()
"""
count = int()

def validador_clic(count):
    clic = win32api.GetAsyncKeyState(0x01)
    temp_x, temp_y = win32api.GetCursorPos()
    
    while True:
        state_actual = win32api.GetAsyncKeyState(0x01)
        if state_actual != clic:
            clic = state_actual
            if state_actual < 0:
                x1, y1 = win32api.GetCursorPos()

                if (x1 != temp_x or y1 != temp_y):
                    count = count + 1
                    print('click se suma uno {}'.format(count))
                    
                    if count < 3:
                        validador_clic(count)
                        pass
                    pass

                if count == 3:
                    print('Boton clic presionado en: ' + str(x1) +", "+str(y1))
                    temp_x = x1
                    temp_y = y1
                    if count >= 3:
                        count = 0
                        print('reinicio')
                        pass
        time.sleep(0.0001)
        pass
    pass

validador_clic(count)