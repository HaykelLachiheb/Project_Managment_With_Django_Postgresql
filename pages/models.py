





# models.py
from django.db import models


class Phases(models.Model):
       PhaseID = models.IntegerField(db_column='PhaseID')
       PhaseName = models.CharField(max_length=50,db_column='PhaseName')
       Pourcentage = models.IntegerField(db_column='Pourcentage')

       def __str__(self):
           return str(self.Pourcentage)
       
       class Meta:
        db_table = 'Phases'





from django.contrib.postgres.fields import ArrayField

class Employee(models.Model):
    EmployeeID = models.IntegerField(db_column='EmployeeID')
    EmployeeName = models.CharField(max_length=50, db_column='EmployeeName')
    List_Tasks = ArrayField(models.CharField(max_length=100), default=list)  # Liste des descriptions de tâches
    
    def __str__(self):
        return str(self.EmployeeID)
    
    class Meta:
        db_table = 'Employee'



class Tasks(models.Model):
    TaskID = models.IntegerField(db_column='TaskID')
    Responsible = models.CharField(max_length=100, db_column='Responsible')
    TaskDaysAllowed = models.IntegerField(db_column='TaskDaysAllowed', null=False, blank=False, default=0)
    TaskDaysWorked = models.IntegerField(db_column='TaskDaysWorked', null=False, blank=False, default=0)
    TaskDesc = models.CharField(max_length=50, db_column='TaskDesc')
    StartingDay = models.DateField()
    State = models.CharField(max_length=50, db_column='State', default="Assigned To")
   

  

    
    
    
   
    def save(self, *args, **kwargs):
        # Sauvegarde de la tâche (avant la sauvegarde)
        super().save(*args, **kwargs)
        
        # Ajout de la description de la tâche dans la liste des tâches de l'employé
        try:
            employee = Employee.objects.get(EmployeeName=self.Responsible)
            
            # Ajoute la description de la tâche dans la liste des tâches de l'employé si elle n'est pas déjà présente
            if self.TaskDesc not in employee.List_Tasks:
                employee.List_Tasks.append(self.TaskDesc)
                employee.save()
        except Employee.DoesNotExist:
            pass  # Si l'employé n'existe pas, vous pouvez gérer l'erreur ici si nécessaire

    def __str__(self):
        return str(self.TaskID)
    



from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255, default="Default Title")
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message[:20]}"


# models.py
class Invoice(models.Model):
    Bill_ID = models.CharField(max_length=255, db_column='Bill_ID')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='invoices/pdfs/', null=True, blank=True)  # Nouveau champ

