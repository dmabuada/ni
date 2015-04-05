/** TODO: clean up this shitty code but get it to work for now*/


$(document).ready(function() {
$('a.login-window').click(function() {
    
  var popModal = $(this).attr('href');

  //fade in on click
  $(popModal).fadeIn(200);
  
  //center alignment padding + border 
    popMargTop = ($(popModal).height() + 24) / 2;
    popMargLeft = ($(popModal).width() + 24) / 2;
  
  $(popModal).css({
      'margin-top' : -popMargTop,
      'margin-left' : -popMargLeft
  });
  
  // append overlay to body
  $('body').append('<div id="overlay"></div>');
  $('#overlay').fadeIn(300);

  // open forgot password in same modal 
  $('a.forgot-window').click(function() {
      $('#login-box').remove();

      var forgotModal = $(this).attr('href');

      $(forgotModal).fadeIn(200);
  });
    return false;
  });
  
  return false;
});

$(function() {
  $(document).on('click','a.close, #overlay',function() {
    $('#overlay, #login-box').fadeOut('300',function() {
    $('#overlay').remove();
  });
    return false;
  });
  });
