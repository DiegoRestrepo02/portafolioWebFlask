$(document).ready(function(){
	$('.ir-arriba').click(function(){
		$('body, html').animate({
			scrollTop: '0px'
		}, 300);
	});

	$(window).scroll(function(){
		if( $(this).scrollTop() > 0 ){
			$('.ir-arriba').slideDown(300);
		} else {
			$('.ir-arriba').slideUp(300);
		}
	});

});

function enviarContacto() {
    let nombre = $("#nombre").val();
    let correo = $('#correo').val();
	let mensaje = $('#mensaje').val();

    if (nombre == "" || nombre == " " || nombre == null || nombre == undefined) {
        alert("ERROR:\nEl nombre no puede estar vacio.");
        return;
    }

    if (correo == "" || correo == " " || correo == null || correo == undefined) {
        alert("ERROR:\nEl correo no puede estar vacio.");
        return;
    }

	if (mensaje == "" || mensaje == " " || mensaje == null || mensaje == undefined) {
        alert("ERROR:\nEl mensaje no puede estar vacio.");
        return;
    }

    $.ajax({
        url: "/enviarMensajeContacto",
        type: "POST",
        data: { "nombre": nombre, "correo": correo, "mensaje": mensaje },
        success: function (response) {
            alert(response);
        },
        error: function (error) {
            //console.log(error);
        },
    });
}