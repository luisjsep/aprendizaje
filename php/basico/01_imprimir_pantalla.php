<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Imprimir por pantalla - Master en PHP</title>

</head>

<body>
    <h1>Master en PHP</h1>
    <?="Esto es otra forma de imprimir en pantalla"?>

</body>

</html>


<?php

//imprimir en pantalla
echo '<h1>Listado de videojuegos</h1>';
echo '<ul>'
      .'<li>MArio Bros</li>'
      .'<li>Zelda</li>'
      .'<li>Donkey kong</li>'
      .'<li>Fifa</li>'
      .'</ul>';

$numero= 10;


echo '<p>Esto es una '.'concatenacion</p>';

//las comillas simples no recononcen una variable
//por eso se tiene que concatenar
//la comilla doble son más lentas, ya que php espera una variable
//para imprimirla

echo 'esta es la variable: $numero'.'<br>';

echo 'esta es la variable numero:'.$numero .'<br>';

echo "esta es la variable: $numero";


?>