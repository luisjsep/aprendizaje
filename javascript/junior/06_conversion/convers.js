

num1=parseFloat(prompt("Ingresa el primer número: "));
num2=parseFloat(prompt("Ingresa el segundo número: "));

suma=num1 + num2;
resta= num1 - num2;
division= num1 / num2;
multiplicacion= num1 * num2;
potencia= num1 ** num2;
resto= num1 % num2;

document.writeln("<h2>El resultado de la suma es: "+ suma + "</h2>");
document.writeln("<h2>El resultado de la resta es: "+ resta + "</h2>");
document.writeln("<h2>El resultado de la división es: "+ division + "</h2>");
document.writeln("<h2>El resultado de la multiplicación es: "+ multiplicacion + "</h2>");
document.writeln("<h2>El resultado de "+ num1+ " elevado a "+num2+ " es: "+multiplicacion + "</h2>");
document.writeln("<h2>El resultado del resto: "+ resto + "</h2>");

