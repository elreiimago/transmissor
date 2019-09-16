
import sh
import socket
from time import sleep
from threading import Thread
import time
import sys

###############################
##  Name: 
##  Arguments: 
##  Comments: 
###############################

class Device_discovery:
     
    ###############################
    ##  Name: Init
    ##  Arguments: Ip_range -> # of ips it will look for
    ##  Comments: 
    ###############################
    def __init__(self,ip_range=64):
        self.ip_range = ip_range
        self.avalibles_ips={}
        self.threads = []  
       



    def get_local_ip(self):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        #print("Direccion ip local obtenida con exito! : ",local_ip)
        return local_ip




    def scan_ips(self,ip):
            try:
                sh.ping(ip, "-c 1",_out="/dev/null")  
                 
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
                self.avalibles_ips[ip]=0
            except sh.ErrorReturnCode_1:  
                exit()
        

    def make_scan(self):
        print("Obteniendo direccion ip local...")
        #localip -> 10.0.0.1
        local_ip = self.get_local_ip()
        #ip_range -> 10.0.0.
        ip_range= local_ip[0:-1] 

        print("Iniciando scaneo de dispositivos en la misma red...")

        for num in range(1,self.ip_range):
            ip=ip_range+str(num)
            thread = Thread(target = self.scan_ips,args=(ip,))
            thread.start()
            self.threads.append(thread)
            

        for thread in self.threads:
            thread.join()
        self.threads.clear()

        self.ips_with_transmissor()

        print("Scaner realizado con exito! Resultados:")
        for ip in self.avalibles_ips.keys():
            if self.avalibles_ips[ip] == 1:
                print(ip," [  OK  ]")
            else: 
                print(ip," [      ]")


    def ips_with_transmissor(self):
        if len(self.avalibles_ips) == 0 :
            self.make_scan()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        for ip in self.avalibles_ips.keys():
            try:
                s.connect((ip, 8080))
                
                self.avalibles_ips[ip]=1

            except:
                self.avalibles_ips[ip]=0

            s.close()



    def start_listening(self):
        print("Abriendo socket...")
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind the socket to a public host, and a well-known port
        serversocket.bind((self.get_local_ip(), 8080))
        # become a server socket
        serversocket.listen(1)
        print("Socket abierto correctamente!")
        try:
            client_sock, addres =serversocket.accept()
            print("Se ha conectado alguien!")
            client_sock.close()
            exit()
        except KeyboardInterrupt:
            print("Cerrando el programa...!")
            exit()

        





if __name__ == "__main__":
    a = Device_discovery(32)
    a1 = time.time()

    a.make_scan()

    #a.start_listening()   
    print(time.time() - a1," s")
    
    
    exit()









   










