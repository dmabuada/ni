$(document).ready(function() {
$('a.login-window').click(function() {
    
  var loginBox = $(this).attr('href');

  //fade in on click
  $(loginBox).fadeIn(200);
  
  //center alignment padding + border 
  var popMargTop = ($(loginBox).height() + 24) / 2;
  var popMargLeft = ($(loginBox).width() + 24) / 2;
  
  $(loginBox).css({
      'margin-top' : -popMargTop,
      'margin-left' : -popMargLeft
  });
  
  // append overlay to body
  $('body').append('<div id="overlay"></div>');
  $('#overlay').fadeIn(300);
  
  return false;
});

$(function() {
  $(document).on('click','a.close, #overlay',function() {
    $('#overlay,.login-popup').fadeOut('300',function() {
    $('#overlay').remove();
  });
    return false;
  });
  });
});
