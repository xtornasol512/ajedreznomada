/*Main Js for Ajedrez Nomada*/
$(document).foundation();

//Button clic
$('#welcome-button').click(function() {
  var name = $('#welcome').val()
  window.location.href = "/welcome/" + name;
});

$( document ).ready(function() {
  var burst = new mojs.Burst({
    top: 20,
    left: 70,
    parent: main_title,
    radius: {15 : 50},
    children : {
      fill : ['deeppink', 'cyan', 'orange']
    }
  });

  $('#main_title').click(function(e){
    burst
      .replay()
  });
});

