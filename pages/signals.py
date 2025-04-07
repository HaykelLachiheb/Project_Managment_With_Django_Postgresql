from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Notification

@receiver(user_logged_in)
def create_login_notification(sender, request, user, **kwargs):
    full_name = user.get_full_name() or user.username  # Utilise `username` si le nom complet n'est pas défini
    Notification.objects.create(
        user=user,
        title="Connection Success",
        message=f"{full_name}, You Are Connected Successfully",
        is_read=False,
    )



from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.utils.timezone import now
from .models import Notification

@receiver(user_logged_out)
def create_logout_notification(sender, request, user, **kwargs):
    # Crée une notification de déconnexion pour l'utilisateur
    title = "Logout Notification"
    full_name = user.get_full_name() or user.username
    message = f"{full_name}, you have been successfully logged out on {now().strftime('%Y-%m-%d %H:%M:%S')}."
    Notification.objects.create(
        user=user,
        title=title,
        message=message,
        is_read=False
    )
