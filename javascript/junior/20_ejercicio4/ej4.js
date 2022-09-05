

/**
 * script que solicita la edad del usuario
 * y si es mayor o igual a 18 indicarle que ya es mayor
 * de edad
 */

edad= parseInt(prompt("Ingresa tu edad: "));

if (edad>=18){
    document.write("<h1>Felicidades eres mayor de edad<br>");
    document.write("Un gran poder conlleva una gran responsabilidad.</h1");
}else{
    document.write("<h1>Lo siento, No eres mayor de edad</h1>");
}

document.write("<br><h2>Que tengas buen día</h2>");