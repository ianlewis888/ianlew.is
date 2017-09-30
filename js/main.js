$(document).ready(loadFunctionality);

function loadFunctionality() {
  var menuIcon = $('#menu-icon');
  var menuClose = $('#menu-close');
  var nav = $('#navigation');

  menuIcon.on('click', function() {
    nav.css('display', 'inline');
    this.style.setProperty('display', 'none', 'important');
    menuClose.css('display', 'inline');
    $('#navigation li').css('opacity', '0');
    $('#navigation li').css('opacity', '1');
  });

  menuClose.on('click', function() {
    nav.css('display', 'none');
    this.style.setProperty('display', 'none', 'important');
    menuIcon.css('display', 'inline');
  });
}
