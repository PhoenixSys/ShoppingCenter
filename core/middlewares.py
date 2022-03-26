from django.shortcuts import redirect, render

from core.models import IpManagerDb


class IpManager:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        import requests
        try:
            request_ip = requests.get("https://api.ipify.org?format=json").json()["ip"]
            resp = requests.get(
                f"http://ip-api.com/json/{request_ip}?fields=status,message,country,city,lat,lon,proxy").json()
            country = resp["country"]
            city = resp["city"]
            lat = resp["lat"]
            lon = resp["lon"]
            proxy = resp["proxy"]
            if not proxy:
                IpManagerDb.objects.get_or_create(ip=request_ip, country=country, city=city, lat=lat, lon=lon)
                ip = IpManagerDb.objects.get(ip=request_ip)
                if (ip.access is True) and (ip.country == "Iran" or ip.country == "Netherlands"):
                    ip.views += 1
                    ip.save()
                    response = self.get_response(request)
                    return response
                else:
                    context = {
                        "ip": request_ip,
                        "region": country
                    }
                    return render(request, "_layout/access_denied.html", context=context)
            else:
                context = {
                    "ip": request_ip,
                    "region": country
                }
                return render(request, "_layout/access_denied.html", context=context)
        except:
            return render(request, "_layout/error_page.html")
