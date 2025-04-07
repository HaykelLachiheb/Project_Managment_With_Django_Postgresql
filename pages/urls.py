from django.urls import path
from . import views

urlpatterns = [
    

    # Main View
    path('main/', views.main, name='main'),

 

    # Reset View
    path('reset/', views.reset, name='reset'),

    # Dashboard View
    path('dashboard/', views.dashboard, name='dashboard'),

    # PhasesCompleted View
    path('phases_completed/', views.phasesCompleted, name='phasesCompleted'),

    # Roadmap View
    path('roadmap/', views.roadmap, name='roadmap'),

    # TodoList View
    path('todolist/', views.todolist, name='todolist'),

    # Signup View
    path('signup/', views.signup, name='signup'),

    # About View
    path('about/', views.about, name='about'),

    # DisplaySearch View
    path('display_search/', views.DisplaySreach, name='DisplaySreach'),

    # Home View
    path('', views.home, name='home'),

    # Page User View
    path('page_user/', views.page_user, name='page_user'),

    # Notification View
    path('notification/', views.Notification, name='notification'),

    # Billing View
    path('billing/', views.Billing, name='Billing'),

    # List Bills View
    path('List_Bills/', views.List_Bills, name='List_Bills'),

    # Add Bill View
    path('Add_Bill/', views.Add_Bill, name='Add_Bill'),

   
    # Delete Bill View
    path('Delete_Bill/', views.Delete_Bills, name='Delete_Bills'),

   


    


    # Resultat View
    path('resultat/', views.resultat, name='resultat'),

   





    


    # Search Bill View
    path('Search_Bill/', views.Search_Bill, name='Search_Bill'),

    # Update Bill View
    path('Update_Bill/', views.Update_Bill, name='Update_Bill'),

   

    # Update User View (requires login)
    path('update_user/', views.update_user, name='update_user'),

    # Login View
    path('Login/', views.Login, name='Login'),
   


   

 


  





    


    # Logout View
    path('logout/', views.logout_view, name='logout'),

    # Add Task View
    path('add_task/', views.Add_Task, name='Add_Task'),

   

    



  


   

   

   

    # Logout View
    path('logout/', views.logout, name='Logout'),


    # Task List View
    path('task_list/', views.task_list, name='task_list'),

    # Search Task View
    path('search_task/', views.search_task, name='search_task'),

    # Update Task View
    path('update_task/', views.update_task, name='update_task'),

 
   




    

    


    # Task List View
    path('task_list/', views.task_list, name='task_list'),

    # Search Task View
    path('search_task/', views.search_task, name='search_task'),

    # Update Task View
    path('update_task/', views.update_task, name='update_task'),

    # Display Tasks View
    path('display_tasks/', views.display_tasks, name='display_tasks'),

    # Delete Task View
    path('delete_task/', views.Delete_Task, name='Delete_Task'),

    # Fetch Task View
    path('fetch_task/', views.fetch_task, name='fetch_task'),

    # Task Management View
    path('task_management/', views.taskManagment, name='taskManagment'),

    # Update Task View
    path('update_task/', views.updatetask, name='updatetask'),



  









   

    # Task List View
    path('task_list/', views.task_list, name='task_list'),

    # Search Task View
    path('search_task/', views.search_task, name='search_task'),

    # Update Task View
    path('update_task/', views.update_task, name='update_task'),

    # Display Tasks View
    path('display_tasks/', views.display_tasks, name='display_tasks'),

    # Delete Task View
    path('delete_task/', views.Delete_Task, name='Delete_Task'),

    # Fetch Task View
    path('fetch_task/', views.fetch_task, name='fetch_task'),

    # Task Management View
    path('task_management/', views.taskManagment, name='taskManagment'),

    # Update Task View
    path('update_task/', views.updatetask, name='updatetask'),

    # Tasks List View
    path('tasks_list/', views.TasksList, name='TasksList'),

    # Employee Tasks View
    path('employee_tasks/', views.Employee_Tasks, name='Employee_Tasks'),

    # Employees Management View
    path('employees_management/', views.EmployeesManagment, name='EmployeesManagment'),

    # Employees List View
    path('employees_list/', views.EmployeesList, name='EmployeesList'),

    # Employee Management View
    path('employee_management/', views.Employee_Managments, name='Employee_Managments'),

    # Delete Employee View
    path('delete_employee/', views.DeleteEmployee, name='DeleteEmployee'),

    # Fetch Employee View
    path('fetch_employee/', views.fetch_employee, name='fetch_employee'),

    # Update Employee View
    path('update_employee/', views.update_employee, name='update_employee'),

   

    




   

    # Task List View
    path('task_list/', views.task_list, name='task_list'),

    # Search Task View
    path('search_task/', views.search_task, name='search_task'),

    # Update Task View
    path('update_task/', views.update_task, name='update_task'),

    # Display Tasks View
    path('display_tasks/', views.display_tasks, name='display_tasks'),

    # Delete Task View
    path('delete_task/', views.Delete_Task, name='Delete_Task'),

    # Fetch Task View
    path('fetch_task/', views.fetch_task, name='fetch_task'),

    # Task Management View
    path('task_management/', views.taskManagment, name='taskManagment'),

    # Update Task View
    path('update_task/', views.updatetask, name='updatetask'),

    # Tasks List View
    path('tasks_list/', views.TasksList, name='TasksList'),

    # Employee Tasks View
    path('employee_tasks/', views.Employee_Tasks, name='Employee_Tasks'),

    # Employees Management View
    path('employees_management/', views.EmployeesManagment, name='EmployeesManagment'),

    # Employees List View
    path('employees_list/', views.EmployeesList, name='EmployeesList'),

    # Employee Management View
    path('employee_management/', views.Employee_Managments, name='Employee_Managments'),

    # Delete Employee View
    path('delete_employee/', views.DeleteEmployee, name='DeleteEmployee'),

    # Fetch Employee View
    path('fetch_employee/', views.fetch_employee, name='fetch_employee'),

    # Update Employee View
    path('update_employee/', views.update_employee, name='update_employee'),

    # Employee List View
    path('employee_list/', views.employee_list, name='employee_list'),

    # Search Employee View
    path('search_employee/', views.search_employee, name='search_employee'),

    # Add Employee View
    path('add_employee/', views.AddEmployee, name='AddEmployee'),


   

  
   




    # User Profile View
    path('user_profile/', views.user_profile, name='user_profile'),



    
    

    # Task List View
    path('task_list/', views.task_list, name='task_list'),

    # Search Task View
    path('search_task/', views.search_task, name='search_task'),

    # Update Task View
    path('update_task/', views.update_task, name='update_task'),

    # Display Tasks View
    path('display_tasks/', views.display_tasks, name='display_tasks'),

    # Delete Task View
    path('delete_task/', views.Delete_Task, name='Delete_Task'),

    # Fetch Task View
    path('fetch_task/', views.fetch_task, name='fetch_task'),

    # Task Management View
    path('task_management/', views.taskManagment, name='taskManagment'),

    # Update Task View
    path('update_task/', views.updatetask, name='updatetask'),

    # Tasks List View
    path('tasks_list/', views.TasksList, name='TasksList'),

    # Employee Tasks View
    path('employee_tasks/', views.Employee_Tasks, name='Employee_Tasks'),

    # Employees Management View
    path('employees_management/', views.EmployeesManagment, name='EmployeesManagment'),

    # Employees List View
    path('employees_list/', views.EmployeesList, name='EmployeesList'),

    # Employee Management View
    path('employee_management/', views.Employee_Managments, name='Employee_Managments'),

    # Delete Employee View
    path('delete_employee/', views.DeleteEmployee, name='DeleteEmployee'),

    # Fetch Employee View
    path('fetch_employee/', views.fetch_employee, name='fetch_employee'),

    # Update Employee View
    path('update_employee/', views.update_employee, name='update_employee'),

    # Employee List View
    path('employee_list/', views.employee_list, name='employee_list'),

    # Search Employee View
    path('search_employee/', views.search_employee, name='search_employee'),

    # Add Employee View
    path('add_employee/', views.AddEmployee, name='AddEmployee'),

    # Reset Password Request View
    path('reset_password/', views.reset_password_request_view, name='reset_password'),

    # Calendar View
    path('calendar/', views.calendar_view, name='calendar'),

    # Create Notification View
    path('create_notification/', views.create_notification, name='create_notification'),




   


    # User Profile View
    path('user_profile/', views.user_profile, name='user_profile'),

    


    # Task List View
    path('task_list/', views.task_list, name='task_list'),

    # Search Task View
    path('search_task/', views.search_task, name='search_task'),

    # Update Task View
    path('update_task/', views.update_task, name='update_task'),

    # Display Tasks View
    path('display_tasks/', views.display_tasks, name='display_tasks'),

    # Delete Task View
    path('delete_task/', views.Delete_Task, name='Delete_Task'),

    # Fetch Task View
    path('fetch_task/', views.fetch_task, name='fetch_task'),

    # Task Management View
    path('task_management/', views.taskManagment, name='taskManagment'),

    # Update Task View
    path('update_task/', views.updatetask, name='updatetask'),

    # Tasks List View
    path('tasks_list/', views.TasksList, name='TasksList'),

    # Employee Tasks View
    path('employee_tasks/', views.Employee_Tasks, name='Employee_Tasks'),

    # Employees Management View
    path('employees_management/', views.EmployeesManagment, name='EmployeesManagment'),

    # Employees List View
    path('employees_list/', views.EmployeesList, name='EmployeesList'),

    # Employee Management View
    path('employee_management/', views.Employee_Managments, name='Employee_Managments'),

    # Delete Employee View
    path('delete_employee/', views.DeleteEmployee, name='DeleteEmployee'),

    # Fetch Employee View
    path('fetch_employee/', views.fetch_employee, name='fetch_employee'),

    # Update Employee View
    path('update_employee/', views.update_employee, name='update_employee'),

    # Employee List View
    path('employee_list/', views.employee_list, name='employee_list'),

    # Search Employee View
    path('search_employee/', views.search_employee, name='search_employee'),

    # Add Employee View
    path('add_employee/', views.AddEmployee, name='AddEmployee'),

    # Reset Password Request View
    path('reset_password/', views.reset_password_request_view, name='reset_password'),

    # Calendar View
    path('calendar/', views.calendar_view, name='calendar'),

    # Create Notification View
    path('create_notification/', views.create_notification, name='create_notification'),

    # Unread Notifications Count View
    path('unread_notifications_count/', views.get_unread_count, name='unread_notifications_count'),

    # Notifications View
    path('notifications/', views.notifications_view, name='notifications_view'),

    # Mark Notification as Read View
    path('mark_notification_as_read/<int:notification_id>/', views.mark_notification_as_read, name='mark_notification_as_read'),

    

    # Upload PDFs View
    path('upload_pdfs/', views.Upload_PDFs, name='Upload_PDFs'),

   
    # Update Invoice View
    path('update_invoice/', views.update_invoice, name='update_invoice'),

    # Search Invoice View
    path('search_invoice/', views.search_invoice, name='search_invoice'),

    # Bill Payment View
    path('bill_payment/', views.bill_payment, name='bill_payment'),






]
