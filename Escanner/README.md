# Explicacion del procedimiento 
## __Definicion__
    Un escáner de palabras hecho con código python para escanear fotos o contenido no copiable al portapapeles tradicionalmente, solo necesita ejecutar desde el archivo principal main  

Luego solo presione el primer punto de un cuadro y el segundo del mismo cuadro, ej:  
__punto1(x = 0, y = 0)__ y __punto2(x=10, y=10)__.  

:-----------------------------------------------------------:
``` 
        (0.0)<-----------------10px-------------------->
            ^
            |           Texto texto texto
            |           Texto texto texto
            |           Texto texto texto
            |           Texto texto texto
            |           Texto texto texto
            10px            
            |
            |
            |
            |
            |
            |
            |
                                                        (10, 10)
```

Formando un cuadro de 10x10, el texto que se encuentre dentro de ese cuadro será analizado y corregido (no traducido) al idioma español para luego ser copiado al portapapeles del mouse.  
By Thefeniz

#### preguntar a David como el mide el tiempo del usuario para evaluar un if 
#### osea ejemplo: si la persona hace clic en menos de 5 segundo pasa sino el boton se desactiva 