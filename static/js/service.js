$(document).ready(function()
{
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $("#learn").click(function () 
    {
        var estatura = $('#height').val();
        var peso = $('#weight').val();
        $.ajax({
            type: "POST",
            url: 'http://localhost:8000/descubrir',
            data: {height:estatura, weight:peso},
            success: function(data){
                console.log(data["result"])
                if(data["result"] == 1){
                    genero = "Mujer"
                }
                else{
                    genero = "Hombre"
                }
                swal("Gracias!", "Segun nuestro sistema de IA tu eres: " + genero, "");
            },
        })
    });
    
});
