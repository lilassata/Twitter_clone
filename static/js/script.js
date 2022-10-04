///////////////////////////
// Javascript for Post page
///////////////////////////

// alert('hello');

$(function() {
    // Expected when js-menu-icon clicked
    $('.js-menu-icon').click(function() {
        // $(this): Self element, namely div.js-menu-icon
        // next() : Next to div.js-menu-icon, namely div.menu
        $(this).next().toggle();
    })
}) 