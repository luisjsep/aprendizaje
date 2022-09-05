<?php
//Variables super globables

//Variables del servidor

//Dirección ip de mi servidor
echo '<h1>';
echo $_SERVER['SERVER_ADDR'];
echo '<h1>';
//Nombre de dominio
echo '<h1>';
echo $_SERVER['SERVER_NAME'];
echo '<h1>';

//Software que usa el servidor
echo '<h1>';
echo $_SERVER['SERVER_SOFTWARE'];
echo '<h1>';


//Navegador web desde que estoy accediendo al servidor
echo '<h1>';
echo $_SERVER['HTTP_USER_AGENT'];
echo '<h1>';
//Dirección ip del cliente
echo '<h1>';
echo $_SERVER['REMOTE_ADDR'];
echo '<h1>';


?>