from geoavalanche import settings


def geoavalanche_settings(request):
    # return any necessary values
    return {
        'NORECAPTCHA_SITE_KEY': settings.NORECAPTCHA_SITE_KEY
    }
