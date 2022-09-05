<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario en php</title>
</head>
<body>
    <h1>Formulario en PHP</h1>
    <form method="GET" action="recibir.php">
    <p>
    <label for="nombre">Nombre</label>
    <input type="text" name="nombre">
    </p>
    <p>
    <label for="Apellido">Apellido</label>
    <input type="text" name="apellido">
    </p>

    <input type="submit" value="Enviar">
    </form>
</body>
</html>