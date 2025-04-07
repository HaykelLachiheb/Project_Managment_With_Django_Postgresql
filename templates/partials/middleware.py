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
