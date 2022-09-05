<?php

$dia=3;
//Esto no es lo más optimo
if ($dia == 1)
{
    echo "Es lunes";
}else{
    if($dia==2){
        echo "Es martes";
    }else{
        if ($dia==3)
        {
           echo "Es miercoles"; 
        }else {
            if($dia==4)
            {
                echo "Es jueves";
            }else {
                if ($dia==5){
                    echo "Es Viernes";
                }
            }
        }   
    }
}
echo "<br>";
//Forma correcta

if ($dia == 1){
    echo "Lunes";
}elseif ($dia== 2)
{
    echo "Martes";
}else if ($dia==3){
    echo "Miercoles";
}elseif($dia==4){
    echo "Jueves";
}elseif($dia==5){
    echo "Viernes";
}
?>