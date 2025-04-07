from django.utils.cache import patch_cache_control

class DisableCacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if not request.user.is_authenticated:
            patch_cache_control(response, no_store=True, no_cache=True, must_revalidate=True)
        return response

from django.utils.cache import patch_response_headers

class DisableCacheOnAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Appliquer les en-têtes de cache uniquement si l'utilisateur est authentifié
        if request.user.is_authenticated:
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
        
        return response


from .models import Notification

def unread_count_middleware(get_response):
    def middleware(request):
        # Ajoutez le `unread_count` au contexte global
        if request.user.is_authenticated:
            unread_count = Notification.objects.filter(user=request.user, is_read=False).count()
            request.unread_count = unread_count
        else:
            request.unread_count = 0
        response = get_response(request)
        return response
    return middleware
