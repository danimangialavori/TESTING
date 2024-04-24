$(document).ready(function()
{

alert("Entro a la funcion");

insertar_registro()


}
)
function insertar_registro()
{
$(document).on('click', '#btn_register', function() 

{
var user = $('#nombre').val();
var email= $('#email').val();

if(nombre == "" || email == "")
{
    $('#Message').html ("Llenar los campos en blanco");
}
else
{

    $.ajax(
        {
            URL: 'insertar.php',
            method: 'post',
            data: {Uname:UserActivation, UEmail:Email},
            success: function (data)
        {
            $('#message').html (data);
           // $('#Registration').modal ('show');
           // $('form').trigger ('reset')
           // Mostrar_registro();
        } 
        }
    )
}
})
}
