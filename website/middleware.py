from django.http import HttpResponsePermanentRedirect


class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().partition(':')[0]
        if host in ('www.schafercondoncarter.com','www.weworkforhumans.com','www.sccadv.com', 'sccadv.com', 'weworkforhumans.com') :
            return HttpResponsePermanentRedirect(
                "https://schafercondoncarter.com" + request.path
            )
        else:
            return self.get_response(request)
