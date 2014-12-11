var directionsDisplay;
var directionsService = new google.maps.DirectionsService();
var map;

function initialize() {
  directionsDisplay = new google.maps.DirectionsRenderer();
  var inicio = new google.maps.LatLng(40.4378271, -3.6795367);
  var mapOptions = {
    zoom: 6,
    center: inicio
  }
  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
  directionsDisplay.setMap(map);


  var image = 'static/iconos/sevilla.png';
  var sevilla = new google.maps.LatLng(37.3753708, -5.9550582);
  var giralda = new google.maps.Marker({
    position: sevilla,
    map: map,
    icon: image
  });

  google.maps.event.addListener(giralda, 'click', function() {
    $(".monumento").hide(500);
    $("#giralda").show(500);
  });

  image = 'static/iconos/granada.png';
  var granada = new google.maps.LatLng(37.1809462, -3.5922032);
  var alhambra = new google.maps.Marker({
    position: granada,
    map: map,
    icon: image
  });

  google.maps.event.addListener(alhambra, 'click', function() {
    $(".monumento").hide(500);
    $("#alhambra").show(500);
  });

  image = 'static/iconos/cordoba.png';
  var cordoba = new google.maps.LatLng(37.891586, -4.7844853);
  var mezquita = new google.maps.Marker({
    position: cordoba,
    map: map,
    icon: image
  });

  google.maps.event.addListener(mezquita, 'click', function() {
    $(".monumento").hide(500);
    $("#mezquitacordoba").show(500);
  });

  image = 'static/iconos/madrid.png';
  var madrid = new google.maps.LatLng(40.4378271, -3.6795367);
  var puertaalcala = new google.maps.Marker({
    position: madrid,
    map: map,
    icon: image
  });

  google.maps.event.addListener(puertaalcala, 'click', function() {
    $(".monumento").hide(500);
    $("#puertaalcala").show(500);
  });


  image = 'static/iconos/barcelona.png';
  var barcelona = new google.maps.LatLng(41.39479,2.1487679);
  var sagradafamilia = new google.maps.Marker({
    position: barcelona,
    map: map,
    icon: image
  });

  google.maps.event.addListener(sagradafamilia, 'click', function() {
    $(".monumento").hide(500);
    $("#sagradafamilia").show(500);
  });
}
