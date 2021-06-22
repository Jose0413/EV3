// VALIDACIONES

function validar_envio(){
    // CORREO
    if(document.formulario.email.value.length==0){
        alert("Debe Ingresar Su Correo Electronico!")
        document.formulario.email.focus()
        return 0;
    }

    alert("Correo Electronico Ingresado!");
    document.formulario.submit();
}