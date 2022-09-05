
/**
 * script que simule el sistema de validación de una plataforma
 * digital. El usuario deberá proporcionar tanto su nombre como la contraseña-
 * Si los valores coinciden con los previamente almacenados, entonces se le dará
 * la bienvenida, sino se le indicará que hubo un error-
 */

const USER='Pep2';
const PASSWORD= '123456';

alert('Proporciona los siguientes datos: ');
user=prompt("Usuario: ");
pass=prompt("Contraseña: ");

if (user == USER && pass==PASSWORD)
{
    document.write('Felicidades lograste ingresar');
    document.write('<br>------------------------------<br>');
}else{
    alert('Datos incorrectos');
}

document.write('Que tengas un buen día');
    
