$ = jQuery
$(document).ready =>
    $('#top-slider').carousel(interval: 10000)
    $('.doc-type').popover()

    $('.inner-galery').hover ->
        img_url = $(this).attr 'img-url'
        $('#main-img-galery').attr 'src', img_url

    $('.schedule-table .btn').click ->
        $('#OrderModal .modal-body').load $(this).attr('agents')
        $('#OrderModal .order-name').html $(this).attr('order-name')

    $('#accordion-job .btn').click ->
        form_url = $(this).attr('form-url')
        $('#JobModal').load form_url, ->
            set_ajax_job = ->
                $('#job_response_form').ajaxForm
                    success: (data) ->
                        $('#JobModal').html data
                        set_ajax_job()
                    beforeSubmit: ->
                        $('#job_response_form .send-progress').css('display', 'inline')
                        true
            set_ajax_job()

    set_ajax_feedback = ->
        $('#feedback_response_form').ajaxForm
            success: (data) ->
                $('#FeedbackModal').html data
                set_ajax_feedback()
            beforeSubmit: ->
                $('#feedback_response_form .send-progress').css('display', 'inline')
                true
    set_ajax_feedback()


    $('.doc-type').mouseleave ->
        $('.accordion-group .in').removeClass('no-overflow')

    $('.doc-type').mouseenter ->
        $('.accordion-group .in').addClass('no-overflow')
