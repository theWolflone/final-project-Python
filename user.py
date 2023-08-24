from persona import *
import os.path


class User(persona):
    tipo= ""
    clave = ""
    def guardar(self):
         bandera = True
         with open("User.txt", "a+") as myfile:
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
                    
                        if(self.cedula == sublista[0]):
                            print("Cedula ingresada ya existe en nuestros registros")
                            bandera= False
                            break
                        else:
                            self.cedula = sublista[0]
                            self.nombre = sublista[1]
                            self.primerapellido= sublista[2]
                            self.segundoapellido = sublista[3]
                            self.direccion= sublista[4]
                            self.correo= sublista[5]
                            self.tipo= sublista[6]
                            self.clave = sublista[7]
                            
                    
                    except Exception:
                        pass
         if bandera:
             file_name = 'User.txt'#cargamos el archivo de texto en una variable
             with open(file_name, 'a') as x_file:
                    x_file.write(self.cedula + '*' + self.nombre + '*' + self.primerapellido + '*' + self.segundoapellido + '*' + self.direccion + '*' + self.correo + '*' + self.tipo +'*' + self.clave +'>')
             print("Dato Guardado correctamente")
             
         
            #en la liena anterior le guardamos al archivo de texto ademas de lo que ya tiene una nueva linea de texto, notese que para separar
            #cada campo de la categoria le agregamos un '*', y al final agregamos un '@', para decir que ahi termina el objeto

    def listar(self):
           
           with open("User.txt", "r") as myfile:

            data = myfile.readlines()
            #el archivo de texto guarda los clientes sin formato, es decir en texto puro, entonces separamos los datos con caracteres comodines
            #, cada objeto tipo categoria guardado en el texto, tendra al final un carcater '@', para saber que estamos ante un nuevo objeto
            #y dentro de cada objeto se separa cada campo del mismo por un caracter '*', el orden siempre del guardado es:nombre,descripcion,identificacion
            #en la siguiente linea, creamos una lista de cadenas de texto, pero ya separando cada objeto tipo categoria
            if(len(data) > 0):

                ft = data[0].split('>')
                listadeusuarios=[]
                for elemento in ft:  # iteramos cada elemento en la lista
                    try:  # este comando evita que se caiga en sistema si hay errores
                        sublista = elemento.split('*')  # creamos una nueva lista por cada objeto de la lista anterior, esta vez separandola por el campo
                    
                   
                        nuevousuario = User()
                    
                        nuevousuario.cedula = sublista[0]
                        nuevousuario.nombre = sublista[1]
                        nuevousuario.primerapellido= sublista[2]
                        nuevousuario.segundoapellido = sublista[3]
                        nuevousuario.direccion= sublista[4]
                        nuevousuario.correo= sublista[5]
                        nuevousuario.tipo= sublista[6]
                        nuevousuario.clave = sublista[7]
                        listadeusuarios.append(nuevousuario)
                    except Exception:
                        pass
            return listadeusuarios
    def login(self):
           if(self.correo != "" and self.clave != ""):
               nuevousuario = User()
               nuevousuario.cedula = "-1"
               with open("User.txt", "r") as myfile:

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
                                nuevousuario.cedula = sublista[0]
                                nuevousuario.nombre = sublista[1]
                                nuevousuario.primerapellido= sublista[2]
                                nuevousuario.segundoapellido = sublista[3]
                                nuevousuario.direccion= sublista[4]
                                nuevousuario.correo= sublista[5]
                                nuevousuario.tipo= sublista[6]
                                nuevousuario.clave = sublista[7]
                                if (self.correo == nuevousuario.correo and self.clave == nuevousuario.clave):
                                    
                                    break
                                else:
                                    nuevousuario.cedula = "-1"
                        

                        except Exception:
                            pass
                return nuevousuario
           else:
                print("Escriba el correo y la clave")


    def rellenaarchivoconlalista(self,lista):
        datosentexto=""
        for elemento in lista:
            datosentexto +=  elemento.cedula + '*' + elemento.nombre + '*' + elemento.primerapellido + '*' + elemento.segundoapellido + '*' + elemento.direccion + '*' + elemento.correo + '*' + elemento.tipo +'*' + elemento.clave +'>'
        file_name = 'Cliente.txt'#cargamos el archivo de texto en una variable
        with open(file_name, 'w') as x_file:
            x_file.write(datosentexto)
    
            

    def eliminar(self):
           listadeusuarios=[]
           if(self.cedula != "" ):
               with open("Cliente.txt", "r") as myfile:

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
                                nuevousuario = User()
                                nuevousuario.cedula = sublista[0]
                                nuevousuario.nombre = sublista[1]
                                nuevousuario.primerapellido= sublista[2]
                                nuevousuario.segundoapellido = sublista[3]
                                nuevousuario.direccion= sublista[4]
                                nuevousuario.correo= sublista[5]
                                nuevousuario.tipo= sublista[6]
                                nuevousuario.clave = sublista[7]
                               
                                listadeusuarios.append(nuevousuario)
                        except Exception:
                            pass
                    for dato in listadeusuarios:
                        if(self.cedula == dato.cedula):
                            listadeusuarios.remove(dato)
                    self.rellenaarchivoconlalista(listadeusuarios)
                    print("Usuario con cedula: " + self.cedula + " ha sido eliminado")
                    return listadeusuarios
                
           else:
                print("Escriba la cedula a eliminar")   
    def modificar(self):
           listadeusuarios=[]
           if(self.cedula != "" ):
               with open("User.txt", "r") as myfile:

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
                                nuevousuario = User()
                                nuevousuario.cedula = sublista[0]
                                nuevousuario.nombre = sublista[1]
                                nuevousuario.primerapellido= sublista[2]
                                nuevousuario.segundoapellido = sublista[3]
                                nuevousuario.direccion= sublista[4]
                                nuevousuario.correo= sublista[5]
                                nuevousuario.tipo= sublista[6]
                                nuevousuario.clave = sublista[7]
                                listadeusuarios.append(nuevousuario)
                        except Exception:
                            pass
                    for dato in listadeusuarios:
                        if(self.cedula == dato.cedula):
                            listadeusuarios.remove(dato)
                            dato.cedula = self.cedula 
                            dato.nombre=self.nombre 
                            dato.primerapellido= self.primerapellido
                            dato.segundoapellido = self.segundoapellido
                            dato.direccion=self.direccion
                            dato.correo= self.correo
                            dato.tipo= self.tipo
                            dato.clave = self.clave
                            listadeusuarios.append(dato)
                    self.rellenaarchivoconlalista(listadeusuarios)
                    print("Usuario con cedula: " + self.cedula + " ha sido actualizado")
                    return listadeusuarios
                
           else:
                print("Escriba la cedula a modificar")