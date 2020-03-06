import threading #Uso de hilos
import time # medir t de ejecucion
from queue import Queue
import RPi.GPIO as GPIO


def blink():
    GPIO.setmode(GPIO.BCM) #Configura GPIO
    GPIO.setup(4, GPIO.OUT)#Configura puerto como salida
    GPIO.output(4, True) # enciende el LED
    time.sleep(10) #Pausa
    GPIO.output(4, False) #apaga el LED
    return

def power2():
    Elementos = [] #array
    start = time.time() # La variable start incia  cronometro
    for x in range(0,100): 
        Elementos.append(x/10)#se introducen los nuevos datos al array
    for x in Elementos:
        x=pow(x,2)
        print (threading.current_thread().name,x) #Se imprime el nombre del hilo junto con el valor nuevo que se está introduciendo
    for x in Elementos:
        x=pow(x,2)
        print (threading.current_thread().name,x) 
    return print('tiempo de ejecución:', time.time()-start)#Se imprime el tiempo de ejecución

def unhilo():
    hilo = threading.Thread(target=power2) # se adjunta la funcion al hilo
    hilo.start() #Se inicia el hilo
    return

def printing(x): # se introducen los nuevos datos al array
    with print_lock: # con lock en el print
        return print(threading.current_thread().name, x**2) #Se imprime el nombre del hilo junto con el valor nuevo que se está introduciendo
def task(): #
    while True:
        elemento = cola.get() #se obtiene dgito de la cola
        printing(elemento)   
        cola.task_done()   #objeto de cola listo
    return

def cuatrohilos():
    for x in range(4):
        hilo = threading.Thread(target = task) # se adjunta funcion
        hilo.daemon = True # se usa la función .daemon para finalizar el hilo tras haberlo utilizado
        hilo.start() # se inicia el hilo
    start = time.time() # se inicia timer
    for x in range(100):
        cola.put(x/10) # Se introducen elementos a la cola
    cola.join() 
    for x in range(100):
        cola.put(x/10)
        cola.join() # Acomoda los elementos y los separa por comas (arrray)
    print('tiempo de ejecución:', time.time()-start)#Se imprime el tiempo de ejecución
    return

print_lock= threading.Lock()
cola = Queue() # La variable cola, es utilizada para ir introduciendo los valores al array
cuatrohilos()
unhilo()
blink()

