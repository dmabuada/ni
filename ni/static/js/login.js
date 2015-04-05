/* TODO: Clean up this shitty code, but get it to work for now */

// Open login form modal
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
  
    return false;
  });
});

// Open forgot password modal 
$(function() {
  $(document).on('click','a.forgot-window',function() {
    $('#login-box').remove();

  var forgotModal = $(this).attr('href');
  //fade in on click
  $(forgotModal).fadeIn(200);

  });
    return false;
});

// Open registration modal 
$(function() {
  $(document).on('click','a.register-window',function() {
    $('#login-box').remove();

  var registrationModal = $(this).attr('href');
  //fade in on click
  $(registrationModal).fadeIn(200);

  });
    return false;
});

// Close out of all modals if user clicks overlay/close btn
$(function() {
  $(document).on('click','a.close, #overlay',function() {
    $('#overlay,.login-popup').fadeOut('300',function() {
    $('#overlay').remove();
  });
    return false;
  });
});
