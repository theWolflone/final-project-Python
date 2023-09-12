# Importamos FastAPI
from fastapi import FastAPI

# Instanciamos FastAPI
app = FastAPI()

fake_items_db = [{"item_name": "Foo"},{"item_name": "Bar"},{"item_name": "Baz"}]
@app.get("/item/")

async def read_item(skip : int = 0, limit : int = 10):
    return fake_items_db[skip : skip +  limit]

# Importamos las diferentes librerias necesarias para procesar HTML, archivos y modelos
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi import Request
from pydantic import BaseModel

# Importamos las clases que vamos a utilizar
from obra import *
from user import *

# Creamos la clase del usuario
class ItemUser(BaseModel):
    cedula: str
    nombre : str
    primerapellido : str
    segundoapellido : str
    direccion : str
    correo : str
    tipo : str
    clave : str

# Creamos la clase de la obra
class ItemObra(BaseModel):
    id: str
    nombre: str
    creador: str
    calificacion: str

# Llamamos al archivo login
@app.get("/")
async def root():
    return FileResponse('login.html')

# Llamamos al archivo del usuario
@app.get("/archivouser")
async def root():
    return FileResponse('user.html')

# Cargamos el archivo de las obras
@app.get("/archivoobra")
async def root():
    return FileResponse('obra.html')

# Cargamos el archivo del frontend de user
@app.get("/userjs")
async def root():
    return FileResponse('userFrontend.js')

# Cargamos el archivo del frontend de user
@app.get("/obrajs")
async def root():
    return FileResponse('obraFrontend.js')

# Enrutamos la función para listar
@app.get("/users")
async def root():
    # Declaramos al usuario
    usuario = User()
    
    # Llamamos a la función listar
    listausersarchivo = usuario.listar()
    #Recorremos con un ciclo la lista de usuario
    for elemento in listausersarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificausuarioprimerpaso(\''+ elemento.cedula +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminausuario(\''+ elemento.cedula +'\')"></input>'
    return listausersarchivo 

# Enrutamos la función para listar
@app.get("/obras")
async def root():
    # Declaramos la obra
    obra = Obra()
    
    # Llamamos a la función listar
    listaobrasarchivo = obra.listar()
    #Recorremos con un ciclo la lista de obras
    for elemento in listaobrasarchivo:
        elemento.creador = elemento.creador.nombre
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaobraprimerpaso(\''+ elemento.id +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminaobra(\''+ elemento.id +'\')"></input>'
        elemento.calificar = '<input type="button" value="calificar" onclick="calificaobra(\''+ elemento.id +'\')"></input>'
    return listaobrasarchivo 

# Creamos la función en la cual guardamos los usuarios
@app.put("/users")
async def root(item:ItemUser):
    # Instanciamos al usuario
    usuario  = User()
    # Igualamos los valores a las entidades para dirigirlo al archivo
    usuario.cedula = item.cedula
    usuario.nombre = item.nombre
    usuario.primerapellido = item.primerapellido
    usuario.segundoapellido = item.segundoapellido
    usuario.direccion =  item.direccion
    usuario.correo= item.correo
    usuario.tipo = item.tipo
    usuario.clave = item.clave

    # Llamamos a la función de guardar correspondiente del usuario
    usuario.guardar()
    # Volvemos a listar los archivos ya modificados
    listausersarchivo = usuario.listar()
    # Recorremos los elementos de la lista de los usuarios con un for
    for elemento in listausersarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificausuarioprimerpaso(\''+ elemento.cedula +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminausuario(\''+ elemento.cedula +'\')"></input>'
    return listausersarchivo

# Creamos la función en la cual guardamos las obras
@app.put("/obras")
async def root(item:ItemObra):
    # Instanciamos la obra
    obra  = Obra()
    # Igualamos los valores a las entidades para dirigirlo al archivo
    obra.id = item.id
    obra.nombre = item.nombre
    #En este caso, llamamos a la entidad de usuario que nos permitirá dirigir una obra al creador o a la persona que registró dicha obra
    usuario = User()
    usuario.nombre = item.creador
    obra.creador = usuario
    obra.calificacion = item.calificacion

    # Llamamos a la función de guardar correspondiente de la obra
    obra.guardar()
    # Volvemos a listar los archivos ya modificados
    listaobrasarchivo = obra.listar()
    # Recorremos los elementos de la lista de las obras con un for
    for elemento in listaobrasarchivo:
        elemento.creador = elemento.creador.nombre
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaobraprimerpaso(\''+ elemento.id +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminaobra(\''+ elemento.id +'\')"></input>'
        elemento.calificar = '<input type="button" value="calificar" onclick="calificaobra(\''+ elemento.id +'\')"></input>'
    return listaobrasarchivo

# Enrutamos la función para eliminar algún usuario deseado
@app.delete("/users")
async def root(item:ItemUser):
    # Instanciamos al usuario
    usuario  = User()
    # Igualamos los valores a las entidades para dirigirlo al archivo
    usuario.cedula = item.cedula
    usuario.nombre = item.nombre
    usuario.primerapellido = item.primerapellido
    usuario.segundoapellido = item.segundoapellido
    usuario.direccion =  item.direccion
    usuario.correo= item.correo
    usuario.tipo = item.tipo
    usuario.clave = item.clave
    # Llamamos a la función de eliminar correspondiente del usuario
    usuario.eliminar()
    # Volvemos a listar los archivos ya modificados
    listausersarchivo = usuario.listar()
    # Recorremos los elementos de la lista de los usuarios con un for
    for elemento in listausersarchivo:
       elemento.modificar = '<input type="button" value="modificar" onclick="modificausuarioprimerpaso(\''+ elemento.cedula +'\')"></input>'
       elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminausuario(\''+ elemento.cedula +'\')"></input>'
    return listausersarchivo

@app.delete("/obras")
async def root(item:ItemObra):
    obra  = Obra()
    obra.id = item.id
    obra.nombre = item.nombre
    usuario = User()
    usuario.nombre = item.creador
    obra.creador = usuario
    obra.calificacion = item.calificacion
    obra.eliminar()
    listaobrasarchivo = obra.listar()
    for elemento in listaobrasarchivo:
       elemento.creador = elemento.creador.nombre
       elemento.modificar = '<input type="button" value="modificar" onclick="modificaobraprimerpaso(\''+ elemento.id +'\')"></input>'
       elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminaobra(\''+ elemento.id +'\')"></input>'
       elemento.calificar = '<input type="button" value="calificar" onclick="calificaobra(\''+ elemento.id +'\')"></input>'
    return listaobrasarchivo

# Enrutamos la función de los usuarios a modificar con el verbo correspondiente, en este caso, POST
@app.post("/users")
async def root(item:ItemUser):
    # Instanciamos la obra
    usuario  = User()
    usuario.cedula = item.cedula
    usuario.nombre = item.nombre
    usuario.primerapellido = item.primerapellido
    usuario.segundoapellido = item.segundoapellido
    usuario.direccion =  item.direccion
    usuario.correo= item.correo
    usuario.tipo = item.tipo
    usuario.clave = item.clave
    # Llamamos la función de la obra en la petición http
    usuario.modificar()

    # Volvemos a listar los archivos ya modificados
    listausersarchivo = usuario.listar()
    # Recorremos los elementos de la lista de las obras con un for
    for elemento in listausersarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificausuarioprimerpaso(\''+ elemento.cedula +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminausuario(\''+ elemento.cedula +'\')"></input>'
    return listausersarchivo

# Enrutamos la función de las obras a modificar con el verbo correspondiente, en este caso, POST
@app.post("/obras")
async def root(item:ItemObra):
    # Instanciamos la obra
    obra  = Obra()
    obra.id = item.id
    obra.nombre = item.nombre
    obra.calificacion = item.calificacion
    
    # Llamamos la función de la obra en la petición http
    obra.modificar()

    # Volvemos a listar los archivos ya modificados
    listaobrasarchivo = obra.listar()
    
    # Recorremos los elementos de la lista de las obras con un for
    for elemento in listaobrasarchivo:
        elemento.creador = elemento.creador.nombre
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaobraprimerpaso(\''+ elemento.id +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminaobra(\''+ elemento.id +'\')"></input>'
        elemento.calificar = '<input type="button" value="calificar" onclick="calificaobra(\''+ elemento.id +'\')"></input>'
    return listaobrasarchivo

# Enrutamos la función para calificar las obras
@app.post("/obrascalif")
# Creamos la función asincrona de la obra
async def root(item:ItemObra):
    # Instanciamos la obra
    obra  = Obra()
    # Igualamos cada item del model con cada atributo de la entidad y devolvemos la petición http que se le realiza al servidor, en este caso para calificar
    obra.id = item.id
    obra.nombre = item.nombre
    obra.calificacion = item.calificacion
    
    obra.calificar()

    # Tras haber calificado, la lista de obras en el archivo las listaremos para seguidamente imprimir ya teniendo los datos actualizados
    listaobrasarchivo = obra.listar()
    for elemento in listaobrasarchivo:
        # Llamamos el atributo creador con el creador de la persona registrada.
        elemento.creador = elemento.creador.nombre
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaobraprimerpaso(\''+ elemento.id +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminaobra(\''+ elemento.id +'\')"></input>'
        elemento.calificar = '<input type="button" value="calificar" onclick="calificaobra(\''+ elemento.id +'\')"></input>'
    return listaobrasarchivo



# Generamos el login
@app.post("/loginusers")
async def root(item:ItemUser):
    # En la función asincrona hacemos el llamado de usuarios

    # Igualamos cada item del model con cada atributo de la entidad y devolvemos la petición http que se le realiza al servidor
    usuario = User()
    usuario.cedula = item.cedula
    usuario.clave = item.clave
    usuario.correo = item.correo
    usuario.direccion= item.direccion
    usuario.nombre = item.nombre
    usuario.primerapellido = item.primerapellido
    usuario.segundoapellido = item.segundoapellido
    usuario.tipo = item.tipo
    return usuario.login()