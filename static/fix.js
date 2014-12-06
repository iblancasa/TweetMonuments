var fixmeTop = $('#map-canvas').offset().top;

$(window).scroll(function() {

  var currentScroll = $(window).scrollTop();

  if (currentScroll >= fixmeTop) {
    $('#map-canvas').css({
      position: 'fixed',
      top: '0',
      left: '0'
    });
  } else {
    $('#map-canvas').css({                     
      position: 'static'
    });
  }

});
