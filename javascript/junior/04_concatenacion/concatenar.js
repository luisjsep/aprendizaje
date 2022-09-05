saludo= "¡hola pedro!";
pregunta= " ¿Cómo estas?";

frase= saludo + pregunta;
document.write(frase+"<br>");


//concatenar string con numeros

numero1=52;
numero2=8;
frase= "" + numero1 + numero2;
//se crea una cadena de caracteres
document.write(frase+"<br>");


//método concat
//concat necesita al menos una variable string para concatenar
num1="52";
num2=8;
frase = num1.concat(num2);

document.write(frase + "<br>");

 //backtick 

 frase1="lucas dalto"
 frase= `soy ${frase1} y estoy caminando`;
 document.write(frase);


 //escape de commillas simples;

 frase="hola mi nombre es 'Luis' y soy un genio";

 //escape de comillas dobles

 frase= 'hola mi nombre es "Javier" y soy un genio';


 
