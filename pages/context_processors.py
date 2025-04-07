# context_processors.py

from .models import Employee

def employee_list(request):
    if request.path == '/update_task/':  # Vérifier si on est sur la page de mise à jour
        return {
            'employees': Employee.objects.all()
        }
    return {}
