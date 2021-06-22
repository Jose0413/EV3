// VALIDACIONES

function validar_envio(){
    // NOMBRE
    if(document.formulario.nombre.value.length==0){
        alert("Debe Ingresar El Nombre!")
        document.formulario.nombre.focus()
        return 0;
    }
    
    // APELLIDO
    if(document.formulario.apellido.value.length==0){
        alert("Debe Ingresar El Apellido!")
        document.formulario.apellido.focus()
        return 0;
    }

    // EDAD
    edad= parseInt(document.formulario.edad.value)
    if(isNaN(edad)){
        alert("Debe Ingresar Su Edad!")
        document.formulario.nombre.focus()
        return 0;

    }else{
        if(edad<18){
            alert("Debe Ser Mayor De Edad!")
            document.formulario.nombre.focus()
            return 0;
        }
    }

    // DIRECCION
    if(document.formulario.direccion.value.length==0){
        alert("Debe Ingresar Su Direccion!")
        document.formulario.direccion.focus()
        return 0;
    }

    // CORREO
    if(document.formulario.email.value.length==0){
        alert("Debe Ingresar Su Correo Electronico!")
        document.formulario.email.focus()
        return 0;
    }

    // CASILLA
    if (document.getElementById("casilla").checked){
        alert('Aceptar Condiciones Esta Seleccionado');
    }


    alert("Datos Ingresados!");
    document.formulario.submit();
}