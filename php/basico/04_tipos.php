<?php
/*
TIPOS DE DATOS
Entero (int/integer) = 99
Coma flotante / decimales (float / double) = 3.15
Cadenas (string) = "Hola soy un string";
Boleano (bool)= 1 0 true false
null
Array (Colección de datos)
Objetos
*/


$numero=100;
$decimal= 27.9;
$texto= "Soy un texto";
$verdadero=true;
$nula=null;
echo gettype($numero)."<br>";
echo gettype($decimal)."<br>";
echo gettype($texto)."<br>";
echo gettype($verdadero)."<br>";
echo $verdadero."<br>";
echo gettype($nula);


?>