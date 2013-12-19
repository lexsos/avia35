$ = jQuery
$(document).ready =>
    $('#top-slider').carousel(interval: 10000)
    $('.doc-type').popover()

    $('.inner-galery').hover ->
        img_url = $(this).attr 'img-url'
        $('#main-img-galery').attr 'src', img_url

    $('#accordion-job .btn').click ->
        $('#JobModal .job-name').html $(this).attr('job-name')

    $('.schedule-table .btn').click ->
        $('#OrderModal .modal-body').load $(this).attr('agents')
        $('#OrderModal .order-name').html $(this).attr('order-name')
