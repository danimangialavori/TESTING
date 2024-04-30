<?php

require_once('conexion.php');

function insertarRegistro()
{


//    echo 'Entro bien';

global $con;

$UserName= $_POST ['Uname'];

$query= "insert into form_login (Nombre, Apellido, Dni,  values('$UserName', "





}





?>