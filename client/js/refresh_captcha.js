function refresh_captcha(btn) {

    var parent = $(btn).parent()
    var url = $(btn).attr('url')

    $.getJSON(url, function(json) {
        var img_url = json['captcha_image'];
        var captcha_key = json['captcha_key'];

        parent.find('#id_captcha_0').val(captcha_key);
        parent.find('#id_captcha_1').val('');
        parent.find('.captcha').attr('src', img_url);
    });
};
