UPDATE pages_tasks
SET "State" = 'Completed'
WHERE "State" = 'Assigned' AND "TaskDaysWorked" > "TaskDaysAllowed";
