/*Main Js for Ajedrez Nomada*/
$(document).foundation();

//Button clic
$('#welcome-button').click(function() {
  var name = $('#welcome').val()
  window.location.href = "/welcome/" + name;
});
