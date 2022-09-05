<?php


/*operadores logicos
 && AND Y
|| OR O
! NOT NO
and, or
*/
$edad1=18;
$edad2=64; 
$edad_oficial=20;

if($edad_oficial >= $edad1 && $edad_oficial<=$edad2){
echo "Esta en edad de trabajar";
}else{
  echo "No puede trabajar";  
}

echo '<br>';
$pais="España";

if($pais == "Mexico" || $pais == "España" || $pais =="Colombia"){
    echo "$pais, en este paí se habla español";
}else{
    echo "No se habla español";
}



?>