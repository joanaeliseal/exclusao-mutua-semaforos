from threading import Semaphore
from threading import Thread
import threading
import time

print('Aluna: Joana Elise Araújo Lopes')

numero = 0
troca = 0
semaforo = Semaphore(1)

def p(n):
    global numero
    global troca
    while True:
        semaforo.acquire()
        if troca == n:
            numero +=1
            time.sleep(1)
            if n == 0:
                print('P1:', numero)
            else:
                print('P2:', numero)
            troca = 1 - n
        semaforo.release()

def p1():
    p(0)
   

def p2():
    p(1)


t_p1 = threading.Thread(target=p1)
t_p2 = threading.Thread(target=p2)

t_p1.start()
t_p2.start()

time.sleep(5)