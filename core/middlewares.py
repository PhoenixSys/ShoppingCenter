from django.shortcuts import redirect, render

from core.models import IpManagerDb


class IpManager:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        import requests
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        request_ip = requests.get("https://api.ipify.org?format=json").json()["ip"]
        IpManagerDb.objects.get_or_create(ip=request_ip)
        ip = IpManagerDb.objects.get(ip=request_ip)
        if ip.access is True:
            ip.views += 1
            ip.save()
            response = self.get_response(request)
            return response
        else:
            return render(request, "_layout/access_denied.html")
