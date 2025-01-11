## Companies

Company Management System



### TODOS:
Create Data Models:
    - [] User Accounts
        - [] Username
        - [] Email Address (Login ID)
        - [] Role
    - [] Company (Naming: by field company_name)
        - [] Company Name (mandatory, unique)
        - [] Number of Departments (virtual)
        - [] Number of Employees (virtual)
        - [] Number of Projects (virtual)
    - [] Department (Naming: expression:{company}-{department_name})
        - [] Company (mandatory)
        - [] Department Name (mandatory)
        - [] Number of Employees (virtual)
        - [] Number of Projects (virtual)
    - [] Employee (Naming: auto-increment)
        - [] Company (Select)
        - [] Department (Select)
        - [] Employee Name
        - [] Email Address (unique)
        - [] Mobile Number (unique)
        - [] Address
        - [] Designation
        - [] Hired On (optional)
        - [] Days Employed (virtual)
    - [] Project
        - [] Company (Select)
        - [] Department (Select)
        - [] Project Name
        - [] Description
        - [] Start Date
        - [] End Date
        - [] Assigned Employees (Multi-Select)

#### License

mit