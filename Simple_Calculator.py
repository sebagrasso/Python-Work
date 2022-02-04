import tkinter as tk
from math import sqrt, factorial, pi
 
 
# ventana de la calculadora
ventana = tk.Tk()
ventana.title("CALCULADORA")
ventana.config(
            width = 390,
            height = 600,
            bg = "Light Steel Blue"
            )
ventana.resizable(0,0)
 
##########  Funciones  ###########################
 
 
def clic(tecla):
    """
    Función que captura los clics en cada tecla de la calculadora
    y los muestra en pantalla
    """
    global calculo # almacena el calculo a realizar como str: "2+sqrt(3)"
    calculo = calculo + str(tecla)
    ingresa_texto.set(calculo)
    
 
 
def limpieza():
    """
    Función que limpia la pantalla de la calculadora (CLEAR)
    """
    global calculo
    ingresa_texto.set("0")
    calculo = ""
    
def hacer_calculo():
    """
    Función que realiza el cálculo y lo muestra en pantalla
    """
    global calculo
    try:
        total = str(eval(calculo))
    except Exception:
        limpieza()
        total = "ERROR"
    ingresa_texto.set(total)
    
    
    
 
############  Main ##############################
 
# definimos las dimensiones de las teclas
ancho = 10
alto = 3
 
# inicializo la variable que almacena el cálculo a realizar
calculo = ""
 
# creo una cadena de tkinter para mostrar en pantalla
ingresa_texto = tk.StringVar()
 
# inicializo la calculadora
limpieza()
 
 
#########  botones de la calculadora ###############
####### primera fila: 1,2,3,+
boton=tk.Button(text="1",width=ancho,height=alto,command=lambda:clic(1)) 
boton.place(x=17,y=180)
boton=tk.Button(text="2",width=ancho,height=alto,command=lambda:clic(2)) 
boton.place(x=107,y=180)
boton=tk.Button(text="3",width=ancho,height=alto,command=lambda:clic(3)) 
boton.place(x=197,y=180)
boton=tk.Button(text="+",width=ancho,height=alto,bg="white",command=lambda:clic('+')) 
boton.place(x=287,y=180)
 
####### segunda fila: 4,5,6,-
boton=tk.Button(text="4",width=ancho,height=alto,command=lambda:clic(4)) 
boton.place(x=17,y=240)
boton=tk.Button(text="5",width=ancho,height=alto,command=lambda:clic(5)) 
boton.place(x=107,y=240)
boton=tk.Button(text="6",width=ancho,height=alto,command=lambda:clic(6)) 
boton.place(x=197,y=240)
boton=tk.Button(text="-",width=ancho,height=alto,bg="white",command=lambda:clic('-')) 
boton.place(x=287,y=240)
 
####### tercera fila: 7,8,9,*
boton=tk.Button(text="7",width=ancho,height=alto,command=lambda:clic(7)) 
boton.place(x=17,y=300)
boton=tk.Button(text="8",width=ancho,height=alto,command=lambda:clic(8)) 
boton.place(x=107,y=300)
boton=tk.Button(text="9",width=ancho,height=alto,command=lambda:clic(9)) 
boton.place(x=197,y=300)
boton=tk.Button(text="*",width=ancho,height=alto,bg="white",command=lambda:clic('*')) 
boton.place(x=287,y=300)
 
####### cuarta fila: (,0,),/
boton=tk.Button(text="(",width=ancho,height=alto,bg="gainsboro",command=lambda:clic('(')) 
boton.place(x=17,y=360)
boton=tk.Button(text="0",width=ancho,height=alto,command=lambda:clic(0)) 
boton.place(x=107,y=360)
boton=tk.Button(text=")",width=ancho,height=alto,bg="gainsboro",command=lambda:clic(')')) 
boton.place(x=197,y=360)
boton=tk.Button(text="/",width=ancho,height=alto,bg="white",command=lambda:clic('/')) 
boton.place(x=287,y=360)
 
####### quinta fila: raiz, coma decimal, potencia, factorial
boton=tk.Button(text="RAIZ",width=ancho,height=alto,bg="gainsboro",command=lambda:clic('sqrt(')) 
boton.place(x=17,y=420)
boton=tk.Button(text=".",width=ancho,height=alto,command=lambda:clic('.')) 
boton.place(x=107,y=420)
boton=tk.Button(text="POW",width=ancho,height=alto,bg="gainsboro",command=lambda:clic('**')) 
boton.place(x=197,y=420)
boton=tk.Button(text="!",width=ancho,height=alto,bg="gainsboro",command=lambda:clic('factorial(')) 
boton.place(x=287,y=420)
 
####### sexta fila: clear,%,PI,=
boton=tk.Button(text="CL",width=ancho,height=alto,bg="cadet blue",command=limpieza) 
boton.place(x=17,y=480)
boton=tk.Button(text="%",width=ancho,height=alto,bg="gainsboro",command=lambda:clic('%')) 
boton.place(x=107,y=480)
boton=tk.Button(text="PI",width=ancho,height=alto,bg="gainsboro",command=lambda:clic(pi)) 
boton.place(x=197,y=480)
boton=tk.Button(text="=",width=ancho,height=alto,bg="cadet blue",command=hacer_calculo) 
boton.place(x=287,y=480)
 
#####  PANTALLA  ########
pantalla = tk.Entry(
            font = ('arial',20,'bold'),
            width = 17,
            textvariable = ingresa_texto, # variable que se muestra
            state = tk.DISABLED,          # bloquea el ingreso de datos
            bd = 20,                      # grosor del borde 
            bg = "powder blue",
            justify = "right"
            )
pantalla.place(x=20, y=60)
 
ventana.mainloop()
