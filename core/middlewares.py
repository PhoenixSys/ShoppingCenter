from django.shortcuts import redirect, render

from core.models import IpManagerDb


class IpManager:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        import requests
        request_ip = requests.get("https://api.ipify.org?format=json").json()["ip"]
        region = requests.get("http://ip-api.com/json/24.48.0.1?fields=status,message,country").json()["country"]
        IpManagerDb.objects.get_or_create(ip=request_ip)
        ip = IpManagerDb.objects.get(ip=request_ip)
        if (ip.access is True) and (region == "Iran"):
            ip.views += 1
            ip.save()
            response = self.get_response(request)
            return response
        else:
            context = {
                "ip": request_ip,
                "region": region
            }
            return render(request, "_layout/access_denied.html", context=context)
