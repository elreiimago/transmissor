import os



print("Accediendo al archivo...")
with open ("./a_source/prueba.dat",'r') as f_in:
    print("Accediendo al archivo... OK")
    print("Leyendo el archivo...")
    print("Datos leidos : ",f_in.read())
    print("Copiando archivo en la carpeta destino...")
    f_out = open("./b_dest/prueba_copia.dat",'w')
    f_in.seek(0)
    f_out.write(f_in.read())
    print("Archivo copiado con exito... OK")
    f_out.close()
    print("Saliendo del programa...")