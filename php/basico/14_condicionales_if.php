<?php
/*
//CONDICIONALES
if (condicion){
instrucciones
}else{
otras intrucciones
}

//Operadores de comparación
== igual
=== identico
!= diferente
<> diferente
!== no identico
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que 

*/
$color="rojo";
if($color=="rojo")
{
    echo "El color es rojo";
}else{
    echo "El color No es rojo";
}
echo '<br>';
$color="verde";
if($color=="rojo")
{
    echo "El color es rojo";
}else{
    echo "El color No es rojo";
}
echo '<br>';

$nombre="Luis Sepulveda";
$ciudad="Madrid";
$continente="Europa";
$edad=49;
$mayoria_edad=18;

if ($edad >= $mayoria_edad){
    echo "<h1>$nombre es mayor de edad</edad>";

    if ($continente=="Europa"){
        echo "<h2>Y es de $ciudad</h2>";
    }else{
        echo "No es Europeo";
    }
}else {
    echo "<h2>$nombre No es mayor de edad </edad>";
}




?>