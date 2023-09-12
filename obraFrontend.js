// Creamos la clase de obra
class Obra {
      constructor(
        id,
        nombre,
        creador,
        calificacion,
      ) {
        this.id = id;
        this.nombre = nombre;
        this.creador = creador;
        this.calificacion = calificacion;
      }
    
      // Metodos de la clase

      // Metodo para guardar una obra
      Guardar() {
        var objetoaenviar = this;
    

        return new Promise(function (resolve, reject) {
          try {
            var xhr = new XMLHttpRequest();
            // Enviamos la petición con el verbo correspondiente
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

      // Método para modificar una obra
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

      // Metodo para eliminar una obra
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

      // Método para calificar las obras
      Calificar() {
        var objetoaenviar = this;
    
        return new Promise(function (resolve, reject) {
          try {
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/obrascalif");
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
    
      // Metodo para obtener todas las obras
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
    