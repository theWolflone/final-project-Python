class Obra {
      constructor(
        id,
        nombre,
        creador,
      ) {
        this.id = id;
        this.nombre = nombre;
        this.creador = creador;
      }
    
      Guardar() {
        var objetoaenviar = this;
    
        return new Promise(function (resolve, reject) {
          try {
            var xhr = new XMLHttpRequest();
            xhr.open("PUT", "/obras");
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.onload = function () {
              if (xhr.status == 200) {
                resolve(JSON.parse(xhr.responseText));
              } else {
                reject(xhr);
              }
            };
            xhr.send(JSON.stringify(objetoaenviar));
          } catch (err) {
            reject(err.message);
          }
        });
      }
      Modificar() {
        var objetoaenviar = this;
    
        return new Promise(function (resolve, reject) {
          try {
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/obras");
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.onload = function () {
              if (xhr.status == 200) {
                resolve(JSON.parse(xhr.responseText));
              } else {
                reject(xhr);
              }
            };
            xhr.send(JSON.stringify(objetoaenviar));
          } catch (err) {
            reject(err.message);
          }
        });
      }
      Eliminar() {
        var objetoaenviar = this;
    
        return new Promise(function (resolve, reject) {
          try {
            var xhr = new XMLHttpRequest();
            xhr.open("DELETE", "/obras");
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.onload = function () {
              if (xhr.status == 200) {
                resolve(JSON.parse(xhr.responseText));
              } else {
                reject(xhr);
              }
            };
            xhr.send(JSON.stringify(objetoaenviar));
          } catch (err) {
            reject(err.message);
          }
        });
      }
    
      Seleccionartodos() {
        var objetoaenviar = this;
    
        return new Promise(function (resolve, reject) {
          try {
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "/obras");
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.onload = function () {
              if (xhr.status == 200) {
                resolve(JSON.parse(xhr.responseText));
              } else {
                reject(xhr);
              }
            };
            xhr.send(JSON.stringify(objetoaenviar));
          } catch (err) {
            reject(err.message);
          }
        });
      }
    }
    