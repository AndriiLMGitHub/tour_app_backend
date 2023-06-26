from django.http import JsonResponse


def info(request):
    return JsonResponse({"message": "Info page"})
