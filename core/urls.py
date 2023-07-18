from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views import View
from django.http import JsonResponse


class RedirectSocial(View):
    def get(self, request, *args, **kwargs):
        code, state = str(request.GET['code']), str(request.GET['state'])
        json_obj = {'code': code, 'state': state}
        print(json_obj)
        return JsonResponse(json_obj)


urlpatterns = [
  path('admin/', admin.site.urls),

  path('api/auth/', include('djoser.urls')),
  path('api/auth/', include('djoser.urls.jwt')),
  path('api/auth/', include('djoser.social.urls')),

  path('api/account/', include('account.urls')),
  path('api/', include('travel_tours.urls')),
  path('api/', include('travel_tours_info.urls')),


  re_path('^.*$', TemplateView.as_view(template_name="index.html")),
  # path('', RedirectSocial.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
