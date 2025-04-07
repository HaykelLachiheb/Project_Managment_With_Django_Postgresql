UPDATE "Employee" e
SET "List_Tasks" = (
    SELECT ARRAY(
        SELECT t."TaskDesc"
        FROM "pages_tasks" t
        WHERE t."Responsible" = e."EmployeeName"
    )
);
