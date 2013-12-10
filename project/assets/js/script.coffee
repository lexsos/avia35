$ = jQuery
$(document).ready =>
    $('#top-slider').carousel(interval: 10000)

    $('.inner-galery').hover ->
        img_url = $(this).attr 'img-url'
        $('#main-img-galery').attr 'src', img_url
