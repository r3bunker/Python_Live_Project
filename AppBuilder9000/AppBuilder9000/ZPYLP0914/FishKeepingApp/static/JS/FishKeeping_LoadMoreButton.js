
  /********************/
 /* Load More button */
/********************/
/*
    Initially displays four
    database elements, then
    four more each time button
    is pressed.
*/
$(function () {
    $(".js-selector-div").slice(0, 4).show();
    $("#loadMore").on('click', function (e) {
        e.preventDefault();
        $(".js-selector-div:hidden").slice(0, 4).slideDown();
        if ($(".js-selector-div:hidden").length == 0) {
            $("#load").fadeOut('slow');
        }
        $('html,body').animate({
            scrollTop: $(this).offset().top
        }, 1500);
    });
});



  /*****************/
 /* To Top button */
/*****************/
/*
    Takes user back to top of
    wish list.
*/
$('.js-selector-a[href=\\#top]').click(function () {
    $('body,html').animate({
        scrollTop: 0
    }, 600);
    return false;
});
$(window).scroll(function () {
    if ($(this).scrollTop() > 50) {
        $('.totop a').fadeIn();
    } else {
        $('.totop a').fadeOut();
    }
});
