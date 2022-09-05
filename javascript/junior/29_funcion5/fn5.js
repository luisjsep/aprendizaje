

//otra forma de crear una función

const saludar = function(nombre){
    let frase= `¡Hola ${nombre}! ¿Cómo estas?<br>`;
    document.write(frase);
}
//función flecha
const saludar2 = nombre =>{
    let frase= `¡Hola ${nombre}! ¿Cómo estas?<br>`;
    document.write(frase);
}
//retornando automaticamente
const saludar3 = (nombre,apellido) =>document.write(frase);


saludar("Pedro");
saludar("Juan");
saludar("Santiago");