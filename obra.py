import os.path
from user import *

class Obra():
    id = ""
    nombre= ""
    calificacion=""
    creador= User()
    def guardar(self):
         bandera = True
         with open("Obras.txt", "a+") as myfile:
            data = myfile.readlines()
            #el archivo de texto guarda las categorias sin formato, es decir en texto puro, entonces separamos los datos con caracteres comodines
            #, cada objeto tipo categoria guardado en el texto, tendra al final un carcater '@', para saber que estamos ante un nuevo objeto
            #y dentro de cada objeto se separa cada campo del mismo por un caracter '*', el orden siempre del guardado es:nombre,descripcion,identificacion
            #en la siguiente linea, creamos una lista de cadenas de texto, pero ya separando cada objeto tipo categoria
            if(len(data) > 0):
                ft = data[0].split('>')
                identificadormayor=0
                for elemento in ft:  # iteramos cada elemento en la lista
                    try:  # este comando evita que se caiga en sistema si hay errores
                        sublista = elemento.split('*')  # creamos una nueva lista por cada objeto de la lista anterior, esta vez separandola por el campo
                    
                        if(self.id == sublista[0]):
                            print("Id ingresado ya existe en nuestros registros")
                            bandera= False
                            break
                        else:
                            self.id = sublista[0]
                            self.nombre = sublista[1]
                            self.calificacion = sublista[2]
                            user = User()
                            user.nombre = sublista[3]
                            self.creador= user
                            
                            
                    
                    except Exception:
                        pass
         if bandera:
             file_name = 'Obras.txt'#cargamos el archivo de texto en una variable
             with open(file_name, 'a') as x_file:
                    x_file.write(self.id + '*' + self.nombre + self.calificacion +'*' + self.creador + '*' +'>')
             print("Dato Guardado correctamente")
             
         
            #en la liena anterior le guardamos al archivo de texto ademas de lo que ya tiene una nueva linea de texto, notese que para separar
            #cada campo de la categoria le agregamos un '*', y al final agregamos un '@', para decir que ahi termina el objeto

    def listar(self):
           
           with open("Obras.txt", "r") as myfile:

            data = myfile.readlines()
            #el archivo de texto guarda los clientes sin formato, es decir en texto puro, entonces separamos los datos con caracteres comodines
            #, cada objeto tipo categoria guardado en el texto, tendra al final un carcater '@', para saber que estamos ante un nuevo objeto
            #y dentro de cada objeto se separa cada campo del mismo por un caracter '*', el orden siempre del guardado es:nombre,descripcion,identificacion
            #en la siguiente linea, creamos una lista de cadenas de texto, pero ya separando cada objeto tipo categoria
            if(len(data) > 0):

                ft = data[0].split('>')
                listadeobras=[]
                for elemento in ft:  # iteramos cada elemento en la lista
                    try:  # este comando evita que se caiga en sistema si hay errores
                        sublista = elemento.split('*')  # creamos una nueva lista por cada objeto de la lista anterior, esta vez separandola por el campo
                    
                   
                        nuevaobra = Obra()
                    
                        nuevaobra.id = sublista[0]
                        nuevaobra.nombre = sublista[1]
                        nuevaobra.calificacion = sublista[2]
                        user = User()
                        user.nombre = sublista[3]
                        nuevaobra.creador= user
                        listadeobras.append(nuevaobra)
                    except Exception:
                        pass
            return listadeobras
           
    def rellenaarchivoconlalista(self,lista):
        datosentexto=""
        for elemento in lista:
            datosentexto +=  elemento.id + '*' + elemento.nombre + elemento.calificacion + '*' + elemento.creador + '*' +'>'
        file_name = 'Obras.txt'#cargamos el archivo de texto en una variable
        with open(file_name, 'w') as x_file:
            x_file.write(datosentexto)
    
            

    def eliminar(self):
           listadeobras=[]
           if(self.id != "" ):
               with open("Obras.txt", "r") as myfile:

                data = myfile.readlines()
                #el archivo de texto guarda los clientes sin formato, es decir en texto puro, entonces separamos los datos con caracteres comodines
                #, cada objeto tipo categoria guardado en el texto, tendra al final un carcater '@', para saber que estamos ante un nuevo objeto
                #y dentro de cada objeto se separa cada campo del mismo por un caracter '*', el orden siempre del guardado es:nombre,descripcion,identificacion
                #en la siguiente linea, creamos una lista de cadenas de texto, pero ya separando cada objeto tipo categoria
                if(len(data) > 0):

                    ft = data[0].split('>')
            
                    for elemento in ft:  # iteramos cada elemento en la lista
                        try:  # este comando evita que se caiga en sistema si hay errores
                            
                            sublista = elemento.split('*')  # creamos una nueva lista por cada objeto de la lista anterior, esta vez separandola por el campo
                            if(len(sublista) > 1):
                                nuevaobra = Obra()
                                nuevaobra.id = sublista[0]
                                nuevaobra.nombre = sublista[1]
                                nuevaobra.calificacion = sublista[2]
                                user = User()
                                user.nombre = sublista[3]
                                nuevaobra.creador= user.nombre
                                
                               
                                listadeobras.append(nuevaobra)
                        except Exception:
                            pass
                    for dato in listadeobras:
                        if(self.id == dato.id):
                            listadeobras.remove(dato)
                    self.rellenaarchivoconlalista(listadeobras)
                    print("Obra con id: " + self.id + " ha sido eliminado")
                    return listadeobras
                
           else:
                print("Escriba el id a eliminar")   
    def modificar(self):
           listadeobras=[]
           if(self.id != "" ):
               with open("Obras.txt", "r") as myfile:

                data = myfile.readlines()
                #el archivo de texto guarda los clientes sin formato, es decir en texto puro, entonces separamos los datos con caracteres comodines
                #, cada objeto tipo categoria guardado en el texto, tendra al final un carcater '@', para saber que estamos ante un nuevo objeto
                #y dentro de cada objeto se separa cada campo del mismo por un caracter '*', el orden siempre del guardado es:nombre,descripcion,identificacion
                #en la siguiente linea, creamos una lista de cadenas de texto, pero ya separando cada objeto tipo categoria
                if(len(data) > 0):

                    ft = data[0].split('>')
            
                    for elemento in ft:  # iteramos cada elemento en la lista
                        try:  # este comando evita que se caiga en sistema si hay errores
                            
                            sublista = elemento.split('*')  # creamos una nueva lista por cada objeto de la lista anterior, esta vez separandola por el campo
                            if(len(sublista) > 1):
                                nuevaobra = Obra()
                                nuevaobra.id = sublista[0]
                                nuevaobra.nombre = sublista[1]
                                nuevaobra.calificacion = sublista[2]
                                user = User()
                                user.nombre = sublista[3]
                                nuevaobra.creador= user.nombre
                                listadeobras.append(nuevaobra)
                        except Exception:
                            pass
                    for dato in listadeobras:
                        if(self.id == dato.id):
                            listadeobras.remove(dato)
                            dato.id = self.id 
                            dato.nombre=self.nombre 
                            dato.calificacion = self.calificacion
                            user = User()
                            user.nombre = self.creador
                            dato.creador= user.nombre
                            listadeobras.append(dato)
                    self.rellenaarchivoconlalista(listadeobras)
                    print("Obra con id: " + self.id + " ha sido actualizado")
                    return listadeobras
                
           else:
                print("Escriba el id a modificar")