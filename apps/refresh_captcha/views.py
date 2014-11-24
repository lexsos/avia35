import json
from django.http import HttpResponse
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url


def refresh_captcha(request):

    captcha_data = dict()
    captcha_key = CaptchaStore.generate_key()
    captcha_data['captcha_key'] = captcha_key
    captcha_data['captcha_image'] = captcha_image_url(captcha_key)

    response_data = json.dumps(captcha_data)
    return HttpResponse(response_data, content_type='application/json')
