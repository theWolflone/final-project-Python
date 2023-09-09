from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"},{"item_name": "Bar"},{"item_name": "Baz"}]
@app.get("/item/")
async def read_item(skip : int = 0, limit : int = 10):
    return fake_items_db[skip : skip +  limit]

from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi import Request
from pydantic import BaseModel

from obra import *
from user import *

class ItemUser(BaseModel):
    cedula: str
    nombre : str
    primerapellido : str
    segundoapellido : str
    direccion : str
    correo : str
    tipo : str
    clave : str

class ItemObra(BaseModel):
    id: str
    nombre: str
    creador: str
    calificacion: str

@app.get("/")
async def root():
    return FileResponse('login.html')

@app.get("/archivouser")
async def root():
    return FileResponse('user.html')

@app.get("/archivoobra")
async def root():
    return FileResponse('obra.html')

@app.get("/userjs")
async def root():
    return FileResponse('userFrontend.js')

@app.get("/obrajs")
async def root():
    return FileResponse('obraFrontend.js')

@app.get("/users")
async def root():
    usuario = User()
    
    listausersarchivo = usuario.listar()
    for elemento in listausersarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificausuarioprimerpaso(\''+ elemento.cedula +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminausuario(\''+ elemento.cedula +'\')"></input>'
    return listausersarchivo 

@app.get("/obras")
async def root():
    obra = Obra()
    
    listaobrasarchivo = obra.listar()
    for elemento in listaobrasarchivo:
        elemento.creador = elemento.creador.nombre
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaobraprimerpaso(\''+ elemento.id +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminaobra(\''+ elemento.id +'\')"></input>'
    return listaobrasarchivo 

@app.put("/users")
async def root(item:ItemUser):
    usuario  = User()
    usuario.cedula = item.cedula
    usuario.nombre = item.nombre
    usuario.primerapellido = item.primerapellido
    usuario.segundoapellido = item.segundoapellido
    usuario.direccion =  item.direccion
    usuario.correo= item.correo
    usuario.tipo = item.tipo
    usuario.clave = item.clave
    usuario.guardar()
    listausersarchivo = usuario.listar()
    for elemento in listausersarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificausuarioprimerpaso(\''+ elemento.cedula +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminausuario(\''+ elemento.cedula +'\')"></input>'
    return listausersarchivo


@app.put("/obras")
async def root(item:ItemObra):
    obra  = Obra()
    obra.id = item.id
    obra.nombre = item.nombre
    usuario = User()
    usuario.nombre = item.creador
    obra.creador = usuario
    obra.calificacion = item.calificacion

    obra.guardar()
    listaobrasarchivo = obra.listar()
    for elemento in listaobrasarchivo:
        elemento.creador = elemento.creador.nombre
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaobraprimerpaso(\''+ elemento.id +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminaobra(\''+ elemento.id +'\')"></input>'
    return listaobrasarchivo

@app.delete("/users")
async def root(item:ItemUser):
    usuario  = User()
    usuario.cedula = item.cedula
    usuario.nombre = item.nombre
    usuario.primerapellido = item.primerapellido
    usuario.segundoapellido = item.segundoapellido
    usuario.direccion =  item.direccion
    usuario.correo= item.correo
    usuario.tipo = item.tipo
    usuario.clave = item.clave
    usuario.eliminar()
    listausersarchivo = usuario.listar()
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
    return listaobrasarchivo

@app.post("/users")
async def root(item:ItemUser):
    usuario  = User()
    usuario.cedula = item.cedula
    usuario.nombre = item.nombre
    usuario.primerapellido = item.primerapellido
    usuario.segundoapellido = item.segundoapellido
    usuario.direccion =  item.direccion
    usuario.correo= item.correo
    usuario.tipo = item.tipo
    usuario.clave = item.clave
    usuario.modificar()

    listausersarchivo = usuario.listar()
    for elemento in listausersarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificausuarioprimerpaso(\''+ elemento.cedula +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminausuario(\''+ elemento.cedula +'\')"></input>'
    return listausersarchivo

@app.post("/obras")
async def root(item:ItemObra):
    obra  = Obra()
    obra.id = item.id
    obra.nombre = item.nombre
    obra.calificacion = item.calificacion
    
    obra.modificar()

    listaobrasarchivo = obra.listar()
    for elemento in listaobrasarchivo:
        elemento.creador = elemento.creador.nombre
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaobraprimerpaso(\''+ elemento.id +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminaobra(\''+ elemento.id +'\')"></input>'
    return listaobrasarchivo




@app.post("/loginusers")
async def root(item:ItemUser):
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