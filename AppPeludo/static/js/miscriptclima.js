// JQ
$(document).ready(function(){
    $('#consultaclima').hide();

});

// JS
function buscar(){
    
    // JS

    // VARIABLES
    var clima = new XMLHttpRequest();
    var ciudad = document.getElementById("ciudad").value;
    
    // API
    clima.open('GET','https://api.openweathermap.org/data/2.5/weather?q=' + ciudad + '&appid=8fefcdc4f65e87fdd7c08f9e34215dc5&units=metric', false);
    clima.send(null);

    // DATOS
    var datos = JSON.parse(clima.response);
    var ciudad = datos.name;
    var temperatura = datos.main.temp_min;
    var humedad = datos.main.humidity;
    var velocidadviento = datos.wind.speed;

    // JQUERY

    // DISTRIBUIR DATOS
    $('#ubicacion').html(ciudad);
    $('#temperatura').html(temperatura);
    $('#humedad').html(humedad);
    $('#velocidadviento').html(velocidadviento);

    $('#ciudad').val('');
    $('#consultaclima').show();

}

