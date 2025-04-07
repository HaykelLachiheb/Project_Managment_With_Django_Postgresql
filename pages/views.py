from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout




#********************************** Index View *****************************************************

def index(request):
    return render(request , 'partials/Login.html')

# **********************************Main View **************************************  ************** 

def main(request):
    return render(request , 'partials/main.html')

# **********************************Resulat View ***************************************************

def resultat(request):
    return render(request , 'partials/resultat.html')

# **********************************Reset view *****************************************************

def reset(request):
    return render(request , 'partials/ResetPass.html')

# *********************************Dashboard View *************************************************


def dashboard(request):
    return render(request , 'partials/Dashboard.html')

# *********************************phasesCompleted View *******************************************

def phasesCompleted(request):
    return render(request , 'partials/PhasesCompleted.html')

# *********************************roadmap View ***************************************************


def roadmap(request):
    return render(request , 'partials/Roadmap.html')


# *********************************todolist View **************************************************

def todolist(request):
    return render(request , 'partials/ToDoList.html')

# *********************************signup View ****************************************************


def signup(request):
    return render(request , 'partials/SignUp.html')

# ********************************about View ******************************************************

def about(request):
    return render(request , 'pages/about.html')

# ********************************DisplaySreach View **********************************************

def DisplaySreach(request):
    return render(request , 'partials/Display_Search.html')


# ********************************home View *******************************************************

def home(request):
    return render(request, 'partials/index.html')


# ********************************page_user View *************************************************

def page_user(request):
    return render(request, 'partials/page-user.html')


# ********************************page_user View *************************************************

def Notification(request):
    return render(request, 'partials/add_notification.html')

# *********************************Billing View *******************************************

def Billing(request):
    return render(request , 'partials/Billing.html')


# *********************************Ftech Bills View *******************************************

def List_Bills(request):
    return render(request , 'partials/List_Bills.html')

# *********************************Add Bills View *******************************************

def Add_Bill(request):
    return render(request , 'partials/Add_Bill.html')



# *********************************Delete Bills View *******************************************

def Delete_Bill(request):
    return render(request , 'partials/Delete_Bills.html')

# *********************************Search Bills View *******************************************

def Search_Bill(request):
    return render(request , 'partials/Search_Bill.html')

# *********************************Update Bills View *******************************************

def Update_Bill(request):
    return render(request , 'partials/Update_Bill.html')



# *********************************Update Bills View *******************************************

def CreateProject(request):
    return render(request , 'partials/CreateProject.html')








# **********************************update_user View ***********************************************

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

@login_required
def update_user(request):
    # Update User from the form 

    if request.method == 'POST':
        user = request.user  
        user.username = request.POST.get('UserName', user.username)
        user.email = request.POST.get('UserEmail', user.email)
        user.first_name = request.POST.get('UserFirstName', user.first_name)
        user.last_name = request.POST.get('UserLastName', user.last_name)
        
        user.save()

         # Créez la notification
        Notification.objects.create(
            user=request.user, 
            message=f"Your Profile has been updated",
            title=f"User {user.username}",
        )

        
    return render(request, 'partials/page-user.html', {'user': request.user})




#***********************************                      ******************************************
#*********************************** Authentication Views ******************************************
#***********************************                      ******************************************





# ***********************************Login View ****************************************************

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def Login(request):

   # Extract User data from the form 

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Try to authenticate

        user = authenticate(request, username=username, password=password)        

        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Invalid Username or Password.Please Try Again')
    return render(request, 'partials/Login.html')





# ***********************************Logout View **************************************************

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
@never_cache
def logout_view(request):
    logout(request)
    return redirect('Login') 






#***************************                      ************************************************
#*************************** Task Managment Views ************************************************
#***************************                      ************************************************

# *****************************Add_Task View **********************************************

from django.shortcuts import render
from .models import Employee, Tasks
from django.utils.timezone import now

def Add_Task(request):
    # Get Employees List
    employees = Employee.objects.values_list('EmployeeName', flat=True)

    if request.method == "POST":
        # Get the Employee Data
        TaskID = request.POST.get('TaskID')
        Responsible = request.POST.get('Responsible', '').strip().capitalize()
        TaskDaysAllowed = request.POST.get('TaskDaysAllowed')
        StartingDay = request.POST.get('StartingDay')
        TaskDesc = request.POST.get('TaskDesc', '').strip().capitalize()
        State = request.POST.get('State')
        TaskDaysWorked = 0 

        errors = []

        # Test if all fields are entred

        if not TaskID or not Responsible or not TaskDaysAllowed or not StartingDay or not TaskDesc or not State:
            errors.append("All fields must be filled.")

        # Test if TaskID is a number and positive
        try:
            TaskID = int(TaskID)
            if TaskID <= 0:
                errors.append("TaskID must be a positive number.")
        except ValueError:
            errors.append("TaskID must be a number.")

        # Test if TaskDaysAllowed is a number and positive
        try:
            TaskDaysAllowed = int(TaskDaysAllowed)
            if TaskDaysAllowed <= 0:
                errors.append("TaskDaysAllowed must be a positive number.")
        except ValueError:
            errors.append("TaskDaysAllowed must be a number.")

        # Test if StartingDay is a valid date
        try:
            StartingDay = now().strptime(StartingDay, "%Y-%m-%d").date()
        except ValueError:
            errors.append("StartingDay must be a valid date (YYYY-MM-DD).")

        # Test if the Employee requested does exist
        try:
            responsible_employee = Employee.objects.get(EmployeeName=Responsible)
        except Employee.DoesNotExist:
            errors.append(f"The Employee {Responsible} does not exist.")

        # Calculate automatically the TaskDaysWorked
        if not errors:
            today = now().date()
            days_worked = (today - StartingDay).days
            TaskDaysWorked = min(max(0, days_worked), TaskDaysAllowed)

        # Send the errors to the template
        if errors:
            return render(request, 'partials/Task_Managments.html', {'employees': employees, 'errors': errors})

        # Create a task if everything is OK
        task = Tasks(
            TaskID=TaskID,
            Responsible=Responsible,
            TaskDaysAllowed=TaskDaysAllowed,
            TaskDaysWorked=TaskDaysWorked,
            TaskDesc=TaskDesc,
            StartingDay=StartingDay,
            State=State
        )
        task.save()

        # Create a notification telling that the User has created the task 
        Notification.objects.create(
            user=request.user,  
            message=f"New Task Has Been Created: {task.TaskID}",
        )

        # Create a success message
        success_message = f"Task {TaskID} has been added successfully."

        # Render the template and send data to it
        return render(request, 'partials/Task_Managments.html', {'employees': employees, 'success_message': success_message})

    
    return render(request, 'partials/Task_Managments.html', {'employees': employees})


# *********************************task_list View *************************************************

from django.shortcuts import render
from .models import Tasks

def task_list(request):
    
    # Collect all tasks ordered by their TaskID
    tasks = Tasks.objects.all().order_by('TaskID')  

    # Render the template and send data to it
    return render(request, 'partials/task_list.html', {'tasks': tasks})


# **********************************search_task View **********************************************


from django.shortcuts import render
from .models import Tasks

def search_task(request):
    task = None
    error_message = ""

    # Get the taskId entred from the Form

    if request.method == "GET":
        task_id = request.GET.get('TaskID')  
        
        # Extract the Task by its TaskID if exist or create and error

        if task_id:
            try:
                task = Tasks.objects.get(task_id=task_id) 
            except Tasks.DoesNotExist:
                error_message = "No task found with the given Task ID."
    
    return render(request, 'partials/Display_Search.html', {'task': task, 'error_message': error_message})


# ****************************************update_task View ****************************************


from django.shortcuts import render, get_object_or_404
from .models import Tasks, Employee
from datetime import datetime

def update_task(request):

    # Extract the hole list of Employees
    employees = Employee.objects.values_list('EmployeeName', flat=True)


    valid_states = ['Assigned', 'In Progress', 'Completed', 'In Review', 'Overdue']

    # Create variables of all data gathered from Form
    if request.method == "POST":
        TaskID = request.POST.get('TaskID', '').strip()
        Responsible = request.POST.get('Responsible', '').strip().capitalize()
        TaskDaysAllowed = request.POST.get('TaskDaysAllowed', '').strip()
        TaskDesc = request.POST.get('TaskDesc', '').strip().capitalize()
        StartingDay = request.POST.get('StartingDay', '').strip()
        State = request.POST.get('State', '').strip()

        errors = []

        # Validate TaskID
        if not TaskID:
            errors.append("TaskID is required.")
        else:
            # Check if the task exists
            task = Tasks.objects.filter(TaskID=TaskID).first()
            if not task:
                errors.append(f"No task found with TaskID '{TaskID}'.")

        # Test if TaskDaysAllowed is a number and be positive
        if not TaskDaysAllowed:
            errors.append("TaskDaysAllowed is required and must be a positive number.")
        else:
            try:
                TaskDaysAllowed = int(TaskDaysAllowed)
                if TaskDaysAllowed <= 0:
                    errors.append("TaskDaysAllowed must be a positive number.")
            except ValueError:
                errors.append("TaskDaysAllowed must be a valid number.")

        # Test if TaskDesc has been entred
        if not TaskDesc:
            errors.append("TaskDesc should not be empty.")

        # Test if Responsible has been entred
        if not Responsible:
            errors.append("Responsible is required.")
        else:
            try:
                Employee.objects.get(EmployeeName=Responsible)
            except Employee.DoesNotExist:
                errors.append(f"The employee '{Responsible}' does not exist.")

        # Test if StartingDay has been entred
        if not StartingDay:
            errors.append("StartingDay is required.")
        else:
            try:
                starting_day = datetime.strptime(StartingDay, '%Y-%m-%d')  # Format YYYY-MM-DD
            except ValueError:
                errors.append("StartingDay must be in the format YYYY-MM-DD.")

        # Test if State has been entred
        if not State:
            errors.append("State is required.")
        elif State not in valid_states:
            errors.append(f"State must be one of the following: {', '.join(valid_states)}.")

        # If errors exist, return them to the template
        if errors:
            return render(request, 'partials/update_task.html', {'employees': employees, 'errors': errors})

        # Calculate TaskDaysWorked (current date - StartingDay)
        if not errors:
            today = datetime.today()
            days_worked = (today - starting_day).days

            # Ensure TaskDaysWorked does not exceed TaskDaysAllowed
            if days_worked > TaskDaysAllowed:
                days_worked = TaskDaysAllowed

            # Update the existing task
            task.Responsible = Responsible
            task.TaskDaysAllowed = TaskDaysAllowed
            task.TaskDaysWorked = days_worked  # Update the calculated value
            task.TaskDesc = TaskDesc
            task.StartingDay = StartingDay
            task.State = State
            task.save()
            
            # Create Notification of updating a Task
            Notification.objects.create(
            user=request.user,  # l'utilisateur connecté
            title=f"Task {task.TaskID} Has Been Updated Successfully",
            message=f"{task.TaskDesc}",
        )
            
            success_message = f"Task {TaskID} has been updated successfully."
            return render(request, 'partials/FetchTask.html', {'employees': employees, 'success_message': success_message})

    return render(request, "partials/FetchTask.html", {'employees': employees})


# *************************************display_tasks View ******************************************

from .models import Tasks  
from datetime import datetime ,timedelta 
from datetime import date

def display_tasks(request):  
  
   # Extract the Number of Tasks
   total_tasks = Tasks.objects.count()


   # Extract the list of tasks classified by TaskID

   today = datetime.today().date()


   # Calculate the lasting working days 

   tasks = Tasks.objects.all().order_by('TaskID') 
  
   for task in tasks:
     task_due_date = task.StartingDay + timedelta(days=task.TaskDaysAllowed)
        
       
     task.days_left = (today - task.StartingDay).days

       
     task.is_valid = task_due_date >= today  




   return render(request, 'partials/TasksList.html', {'tasks': tasks,'today': today,'tasks': tasks,'range_obj': range(1,total_tasks),'total_tasks': total_tasks})



# *****************************************Delete_Task View ***************************************

from django.shortcuts import get_object_or_404, render
from .models import Tasks

def Delete_Task(request):
    error_message = None

    # Get the entered TaskId from the Form
   
    if request.method == "POST":
        task_id = request.POST.get('TaskID') 
        success_message3 = f"Task {task_id} Has Been Deleted Successfully"    
        
      
        if task_id:

            # Test if the TaskId Entred is a positif number

            try:
                task_id = int(task_id) 
                if task_id <= 0:
                    error_message = "TaskID must be a positive number."
                else:
                   
                    task = get_object_or_404(Tasks, TaskID=task_id)
                    
                    # Delete the task

                    task.delete()

                    Notification.objects.create(
                        user=request.user,  # l'utilisateur connecté
                        title=f"Task {task.TaskID} Has Been Deleted Successfully",
                        message=f"Task {task.TaskID} Has Been Deleted Successfully",
                    )
                    return render(request, 'partials/Task_Managments.html', {'task': task, 'error_message': error_message,'success_message2':success_message2})
            except ValueError:
                error_message = "TaskID must be a valid number."
            except Exception as e:
                error_message = f"Delete Error: {e}"
        else:
            error_message = "TaskID is not valid."
    
    return render(request, 'partials/DeleteTask.html', {'error_message': error_message,'success_message3':success_message3})



# *****************************************fetch_task View *****************************************

from django.shortcuts import render
from django.http import JsonResponse

def fetch_task(request, template_name=None):
    task = None
    error = None

    if request.method == "POST":
        task_id = request.POST.get('TaskID')
        
        # Test if the TaskID input is filled or not and is a positif number

        if not task_id:
            error = "TaskID must be filled"
        elif not task_id.isdigit() or int(task_id) <= 0:
            error = "TaskID must be a positif number"
        else:

            # Fetch the Task 

            task = Tasks.objects.filter(TaskID=task_id).first()
            return render(request, 'partials/FetchTask.html', {'task': task, 'error': error})
            if not task:
                error = "No Task FOUND for this task ID"

    
    if not template_name:
        template_name = 'partials/FetchTask.html'

    return render(request, 'partials/Task_Managments.html', {'task': task, 'error': error})



# ***************************************taskManagment View ****************************************

def taskManagment(request):
    return render(request , 'partials/TaskManagment.html')

# u**************************************pdatetask View *******************************************

def updatetask(request):
    return render(request , 'partials/update_task.html')

# ***************************************TasksList View *******************************************

def TasksList(request):
    return render(request, 'partials/TasksList.html')

# ***************************************Employee_Tasks View ***************************************

def Employee_Tasks(request):
    return render(request, 'partials/Employee_Tasks.html')



#***************************                          ************************************************
#*************************** Employee Managment Views ************************************************
#***************************                          ************************************************


# ****************************EmployeesManagment View **********************************************


def EmployeesManagment(request):
    return render(request , 'partials/EmployeesManagment.html')



# ****************************EmployeesList View ***************************************************

def EmployeesList(request):
    return render(request, 'partials/EmployeesList.html')

# ****************************Employee_Managments View *********************************************

def Employee_Managments(request):
    return render(request, 'partials/Employee_Managments.html')



# *****************************DeleteEmployee View *************************************************



from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from .models import Employee  

def DeleteEmployee(request):

    # Extract the EmployeeId from the Form

    if request.method == "POST":
        Employee_id = request.POST.get('EmployeeID') 
        if Employee_id:

            # Test if the requested Employee Exist or not
          
            try:
                employee = get_object_or_404(Employee, EmployeeID=Employee_id)

                # Delete the Employee

                employee.delete()

                success_message = f"Employee {Employee_id} has been deleted successfully."

                Notification.objects.create(
                user=request.user,  # l'utilisateur connecté
                title=f"Employee {employee.EmployeeID} Has Been Deleted Successfully",
                message=f"Employee {employee.EmployeeID} Has Been Deleted Successfully",
        )
                


                return render(request, 'partials/Employee_Managments.html', {'employee': employee, 'success_message': success_message})



                return render(request, 'partials/Employee_Managments.html',{'employee': employee})
            except Exception as e:
                return HttpResponse(f"Delete Error {e}")
        else:
            return HttpResponse(" EmployeeID is not valid")
    else:
        return HttpResponse("Unallowed method.")


# *************************************fetch_employee View ****************************************


from django.shortcuts import render
from .models import Employee 

def fetch_employee(request):
    employee = None
    
    # Extract the EmployeeID from the Form 

    if request.method == "POST":
        employee_id = request.POST.get('EmployeeID') 
       
        # Ftech the Employee if exist  

        if employee_id:
          
            employee = Employee.objects.filter(EmployeeID=employee_id).first() 

    # Count the total number of Employees        
    
    total_employees = Employee.objects.count()

    return render(request, 'partials/FetchEmployee.html', {'employee': employee,'total_employees':total_employees})


# *********************************update_employee View ********************************************

from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee

def update_employee(request):
    employee = None

    # Extract the Data  from the Form

    if request.method == "POST":
        employee_id = request.POST.get("EmployeeID")
        employee_name = request.POST.get('EmployeeName', '').lower().capitalize()       

        # Test if the requested Employee already Exist

        employee = get_object_or_404(Employee, EmployeeID=employee_id)

        # Update the Employee Data

        employee.EmployeeID = employee_id
        employee.EmployeeName = employee_name
       
        employee.save()

        Notification.objects.create(
            user=request.user,  # l'utilisateur connecté
            title=f"A New Employee Has Been Updated Successfully",
            message=f"{employee.EmployeeName}",
        )
 
        success_message = f"Employee {employee_id} has been updated successfully."
        return render(request, 'partials/Employee_Managments.html', {'employee': employee, 'success_message': success_message})


        return redirect("update_employee") 

    elif request.method == "GET":
       
        employee_id = request.GET.get("EmployeeID")
        if employee_id:
            try:
                employee = Employee.objects.get(id=employee_id)
            except Employee.DoesNotExist:
                employee = None

    return render(request, "partials/update_employee.html", {"employee": employee})




# ************************************employee_list View *******************************************
from django.shortcuts import render
from .models import Employee, Tasks

def employee_list(request):
    employees = Employee.objects.all().order_by('EmployeeID')
    tasks = Tasks.objects.all()
    
    # Liste des employés avec leurs tâches détaillées
    employees_with_tasks = []

    total_tasks = 0  # Variable pour le nombre total de tâches

    for employee in employees:
        employee_tasks = []
        
        # Récupérer les tâches liées à cet employé
        for task_desc in employee.List_Tasks:
            task = tasks.filter(TaskDesc=task_desc).first()  # Cherche la tâche par description
            if task:
                # Ajouter la tâche avec ses détails
                employee_tasks.append({
                    'task': task,
                    'task_desc': task.TaskDesc,
                    'task_days_allowed': task.TaskDaysAllowed,
                    'task_days_worked': task.TaskDaysWorked,
                    'starting_day': task.StartingDay,
                    'state': task.State,
                    'task_ID' : task.TaskID,
                })
                total_tasks += 1  # Incrémenter le total des tâches
    
        # Ajouter l'employé avec ses tâches
        employees_with_tasks.append({
            'employee': employee,
            'tasks': employee_tasks
        })
    
    return render(request, 'partials/EmployeesList.html', {
        'employees_with_tasks': employees_with_tasks,
        'employees': employees,
        'total_tasks': total_tasks,  # Ajouter la variable total_tasks
    })








# ***************************************search_employee View **************************************

from django.shortcuts import render
from .models import Employee, Tasks

def search_employee(request):
    tasks = None
    employee_name = None
    error_message = None

    # Extract the data from the Form

    if request.method == "POST":
        employee_id = request.POST.get("employee_id")

        # test if the employee already exist 

        if employee_id:
            try:
              
                employee = Employee.objects.get(EmployeeID=employee_id)
                employee_name = employee.EmployeeName

                # List the Employees

                tasks = Tasks.objects.filter(Responsible=employee_name)
                List_Assigned = []
                List_Assigned_TaskID = []
                List_Completed = []
                List_In_Progress = []
                List_In_Review = []
                List_Overdue = []

                # List the Employee's state 


                for task in tasks :

                     if task.State == "Assigned" :
                         
                         List_Assigned.append([task.TaskID, task.TaskDesc])
                         
                     if task.State == "Completed" :
                         
                         List_Completed.append([task.TaskID, task.TaskDesc]) 

                     if task.State == "In Progress" :
                         
                         List_In_Progress.append([task.TaskID, task.TaskDesc])     

                     if task.State == "In Review" :
                         
                         List_In_Review.append([task.TaskID, task.TaskDesc]) 

                     if task.State == "Overdue" :
                         
                         List_Overdue.append([task.TaskID, task.TaskDesc])         


            except Employee.DoesNotExist:
                error_message = "Employee not found. Please check the ID and try again."
        else:
            error_message = "Employee ID cannot be empty."

    return render(request, "partials/Employee_Tasks.html", {
        "tasks": tasks,
        "employee_name": employee_name,
        "error_message": error_message,
        "List_Assigned" : List_Assigned,
        "List_Completed" : List_Completed,
        "List_In_Progress" : List_In_Progress,
        "List_In_Review" : List_In_Review,
        "List_Overdue" : List_Overdue,
        "List_Assigned_TaskID" : List_Assigned_TaskID
    })



# **************************************AddEmployee View *******************************************


from django.shortcuts import render, redirect
from .models import Employee

def AddEmployee(request):

    nouveau_objet = None

    # Get the data from the Form

    if request.method == "POST":
        EmployeeID = request.POST.get('EmployeeID')
        EmployeeName = request.POST.get('EmployeeName', '').lower().capitalize()
        List_Tasks = []
        
        # Create a New Employee
       
        nouveau_objet = Employee(id=EmployeeID,EmployeeID=EmployeeID, EmployeeName=EmployeeName,List_Tasks=List_Tasks)
        nouveau_objet.save()

         # Créez la notification
        Notification.objects.create(
            user=request.user,  # l'utilisateur connecté
            message=f"New Employee Has Been Created",
            title=f"Employee {nouveau_objet.EmployeeName}",
        )

        
        # Message de succès
        success_message = f"Employee {EmployeeID} has been added successfully."
        return render(request, 'partials/Employee_Managments.html', {'nouveau_objet': nouveau_objet, 'success_message': success_message})

        
    return render(request, 'partials/Employee_Managments.html',{'nouveau_objet': nouveau_objet})


# ************************************** User Profile View *******************************************



def user_profile(request):
    context = {
        'segment': 'page_user'
    }
    return render(request, 'partials/page-user.html', context)


# ************************************** Reset Password View *******************************************




from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def reset_password_request_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        associated_users = User.objects.filter(email=email)
        if associated_users.exists():
            for user in associated_users:
                # Utilisez le formulaire de réinitialisation de mot de passe intégré
                form = PasswordResetForm({'email': email})
                if form.is_valid():
                    form.save(
                        request=request,
                        use_https=True,
                        email_template_name='partials/reset_email_template.html',  # Créez ce template
                    )
                messages.success(request, "Un email a été envoyé pour réinitialiser votre mot de passe.")
        else:
            messages.error(request, "Aucun utilisateur n'est associé à cet email.")
        return redirect('reset_password')
    return render(request, 'partials/reset_password.html')

# ***************************** ******calendar_view **********************************************

import calendar
from django.shortcuts import render
from django.utils import timezone
from .models import Tasks

def calendar_view(request):
    # Récupérer la date actuelle
    current_date = timezone.localdate()
    
    # Obtenir l'année et le mois actuels
    year = current_date.year
    month = current_date.month
    
    # Utiliser calendar pour obtenir le calendrier du mois (une liste de semaines)
    month_calendar = calendar.monthcalendar(year, month)
    
    # Récupérer les tâches pour ce mois
    tasks = Tasks.objects.filter(StartingDay__year=year, StartingDay__month=month)
    
    # Créer une liste de jours sous forme de "semaine"
    weeks = []
    for week in month_calendar:
        days = []
        for day in week:
            if day == 0:
                days.append(None)  # Ajouter None pour les jours vides
            else:
                days.append(day)
        weeks.append(days)
    
    # Passer les données au template
    return render(request, 'partials/calendar.html', {
        'current_date': current_date,
        'weeks': weeks,
        'tasks': tasks
    })


 #***************************                      ************************************************
#*************************** Notifications Views ************************************************
#***************************                      ************************************************
   


# ************************** Notifications View *********************************************


from django.shortcuts import render, redirect
from .models import Notification
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_notification(request):
    success_message = ""
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        title = request.POST.get('title')
        message = request.POST.get('message')
        
        # Assure-toi que tu as un utilisateur valide
        try:
            user = User.objects.get(id=user_id)
            notification = Notification.objects.create(
                user=user,
                title=title,
                message=message
            )
            notification.save()
            success_message = f"notification has been created successfully"
        except User.DoesNotExist:
         return HttpResponse("Utilisateur non trouvé", status=400)
    else:
        return render(request, 'partials/create_notification.html')
    return render(request, 'partials/create_notification.html',{'success_message':success_message})

# ***********************************  Unread Notifications View ********************************
from django.http import JsonResponse

def get_unread_count(request):
    return Notification.objects.filter(user=request.user, is_read=False).count()

# ********************************** notifications_view *****************************************
def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    
    unread_count = Notification.objects.filter(user=request.user, is_read=False).count()
    read_count = Notification.objects.filter(user=request.user, is_read=True).count()

    # Débogage - affichez la valeur dans la console
    print(f"Unread notifications count: {unread_count}")

    total_count = notifications.count()

    context = {
        'notifications': notifications,
        'unread_count': unread_count,  # Passer la variable au template
        'read_count' : read_count,
        'total_count': total_count,
    }
    
    return render(request, 'partials/notifications.html', context)

# ******************************* mark_notification_as_read *************************************

from django.shortcuts import redirect
from .models import Notification

def mark_notification_as_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    if notification.user == request.user:
        notification.is_read = True
        notification.save()
    return redirect('notifications_view')

 #***************************                      ************************************************
#***************************    Billing Views      ************************************************
#***************************                      ************************************************
   


# *********************************Add Bills View *******************************************
from django.shortcuts import render
from django.core.files.storage import default_storage
import openpyxl
from datetime import date

def Add_Bill(request):
    today = date.today().isoformat()

    if request.method == 'POST' and 'file' in request.FILES:
        # Charger le fichier Excel
        file = request.FILES['file']
        file_path = default_storage.save(file.name, file)

        rows = []
        try:
            # Lire le fichier Excel
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                Bill_ID, amount, due_date = row
                if not Bill_ID or not amount or not due_date:
                    continue
                rows.append({
                    'Bill_ID': Bill_ID,
                    'amount': amount,
                    'due_date': due_date.isoformat()
                })

            # Sauvegarder les données des factures en session
            request.session['excel_rows'] = rows
            return render(request, 'partials/Add_Bill.html', {
                'rows': rows,
                'today': today
            })
        except Exception as e:
            return render(request, 'partials/Add_Bill.html', {
                'error': f"Error processing the file: {e}",
                'today': today
            })
        finally:
            default_storage.delete(file_path)

    return render(request, 'partials/Add_Bill.html', {
        'today': today
    })

# **************************************** Upload_PDFs ******************************************
from django.shortcuts import render
from decimal import Decimal
from datetime import datetime
from .models import Invoice

def Upload_PDFs(request):
    rows = request.session.get('excel_rows', [])

    if request.method == 'POST' and 'pdf_files[]' in request.FILES:
        pdf_files = request.FILES.getlist('pdf_files[]')

        # Vérifier que le nombre de fichiers PDF correspond au nombre de factures
        if len(pdf_files) != len(rows):
            return render(request, 'partials/Add_Bill.html', {
                'error': f"Number of PDF files ({len(pdf_files)}) does not match the number of invoices ({len(rows)}).",
                'rows': rows
            })

        try:
            # Créer les factures et associer les fichiers PDF
            for index, row in enumerate(rows):
                Bill_ID = row['Bill_ID']
                amount = Decimal(row['amount'])
                due_date = datetime.fromisoformat(row['due_date']).date()

                # Créer une nouvelle facture
                invoice = Invoice.objects.create(
                    Bill_ID=Bill_ID,
                    amount=amount,
                    due_date=due_date,
                    paid=False
                )

                # Associer le fichier PDF
                pdf_file = pdf_files[index]
                invoice.pdf_file.save(pdf_file.name, pdf_file, save=True)

            success_message = "Invoices and PDF files have been uploaded successfully."
            request.session.pop('excel_rows', None)  # Nettoyer les données de session
            return render(request, 'partials/Add_Bill.html', {
                'success_message': success_message
            })
        except Exception as e:
            return render(request, 'partials/Add_Bill.html', {
                'error': f"Error processing the PDFs: {e}",
                'rows': rows
            })

    return render(request, 'partials/Add_Bill.html', {
        'rows': rows
    })

# ***************************************** List_Bills ******************************************

from django.shortcuts import render
from .models import Invoice

def List_Bills(request):
    # Récupérer toutes les factures
    invoices = Invoice.objects.all().order_by('Bill_ID')

    return render(request, 'partials/List_Bills.html', {
        'invoices': invoices
    })


# ***************************************** Delete Bills View ************************************

import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice

def Delete_Bills(request):
    invoices = Invoice.objects.all().order_by('Bill_ID')

    if request.method == 'POST':
        bill_id = request.POST.get('bill_id')
        if bill_id:
            invoice = get_object_or_404(Invoice, Bill_ID=bill_id)

            # Supprimer le fichier associé si il existe
            if invoice.pdf_file:
                file_path = os.path.join(settings.MEDIA_ROOT, invoice.pdf_file.name)
                if os.path.exists(file_path):
                    os.remove(file_path)

            # Supprimer la facture
            invoice.delete()

            return redirect('Delete_Bills')

    return render(request, 'partials/Delete_Bills.html', {
        'invoices': invoices
    })

# ********************************* update_invoice **********************************************

import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Invoice
from django.http import HttpResponseRedirect

def update_invoice(request):
    if request.method == 'POST':
        bill_id = request.POST.get('Bill_ID')  # Récupérer Bill_ID depuis le formulaire
        amount = request.POST.get('Amount')
        due_date = request.POST.get('Due_Date')
        pdf_file = request.FILES.get('pdf_file')  # Récupérer le fichier PDF

        # Récupérer la facture existante en utilisant le champ correct `Bill_ID`
        invoice = get_object_or_404(Invoice, Bill_ID=bill_id)

        # Mettre à jour les informations de la facture
        invoice.amount = amount
        invoice.due_date = due_date

        if pdf_file:
            # Vérifiez si un fichier existe déjà et supprimez-le
            if invoice.pdf_file:
                existing_file_path = os.path.join(settings.MEDIA_ROOT, str(invoice.pdf_file))
                if os.path.isfile(existing_file_path):
                    os.remove(existing_file_path)  # Supprimer l'ancien fichier
            
            # Ajouter le nouveau fichier
            invoice.pdf_file = pdf_file

        invoice.save()  # Enregistrez les modifications

        return HttpResponseRedirect('/update_invoice/')  # Rediriger après mise à jour

    return render(request, 'partials/Update_Bill.html')

# ********************************** search_invoice ********************************************

from django.shortcuts import render, get_object_or_404
from .models import Invoice

def search_invoice(request):
    invoice = None
    searched = False

    if 'Bill_ID' in request.GET:
        bill_id = request.GET.get('Bill_ID')
        searched = True
        try:
            invoice = Invoice.objects.get(Bill_ID=bill_id)
        except Invoice.DoesNotExist:
            invoice = None

    return render(request, 'partials/Search_Invoice.html', {'invoice': invoice, 'searched': searched})

# ************************************** pay_bill ***********************************************

from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice

def bill_payment(request):
    invoices = Invoice.objects.filter(paid=False).order_by('Bill_ID')

    if request.method == 'POST':
        bill_id = request.POST.get('Bill_ID')
        if bill_id:
            invoice = get_object_or_404(Invoice, Bill_ID=bill_id)
            invoice.paid = True
            invoice.save()
            return redirect('bill_payment')  # Redirige après le paiement

    return render(request, 'partials/Bill_Payment.html', {'invoices': invoices})

