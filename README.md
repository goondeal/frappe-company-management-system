# **Company Management System**  


## **📚 Table of Contents**  
- [Overview](#-overview)  
- [Installation](#-installation)  
- [Approach and Implementation Details](#-1-approach-and-implementation-details)  
- [Task Completion Checklist](#-2-task-completion-checklist)  
- [Security Measures](#-3-security-measures)  
- [API Documentation](#-4-api-documentation)  
- [Future Work](#-5-future-work)  
- [Assumptions and Considerations](#-6-assumptions-and-considerations)  

---
## 📖 **Overview**  
This is a backend application built on the Frappe framework that provides CRUD operations for managing companies, departments, employees, and projects. It includes a workflow for employee performance reviews and implements role-based access control for secure data handling.  

## ⚙️ **Installation**  
Setting up the application is straightforward. Follow these steps to install and add the app to your Frappe site:
from your frappe-bench folder:
1. **Clone the Repository**:  
   ```bash  
   bench get app https://github.com/goondeal/frappe-company-management-system.git 
   ```
2. **Add it to your site**:  
   ```bash  
   bench --site <your-site-name> install-app companies
   bench restart
   ```

## **1. 🛠️ Approach and Implementation Details**  

### **Approach**  
1. **Frappe Framework**: Leveraged for its modularity and support for workflows, role-based access, and RESTful APIs.  
2. **Entities**: Designed Doctypes for `Company`, `Department`, `Employee`, `Project`, and `Performance Review`.  
3. **Workflow**: Implemented a structured employee performance review process with transitions and state-based control.  
4. **Role-Based Access Control**: Applied granular permissions for `Admin`, `Manager`, and `Employee` roles, where **Admin** has control over company, **Manager** has control over his department, and **Employee** can read his own data.
5. Manual integration testing.


### **Implementation Details**  
- **Data Models**: Created Doctypes with relationships and auto-calculated fields (e.g., `days_employed`).  
- **Workflow**: A `Performance Review` workflow manages transitions (e.g., Pending Review → Review Scheduled).  
- **Custom Scripts**:  
  - Restricted the selection of employees in `Performance Review` based on the Admin's company or manager's department.  
  - Auto-created user accounts when adding new employees.
- **API**: Provided RESTful endpoints for all entities.  
- **Security**: Enforced role-based access control that was achieved by combining doctype permissions and `permission_query_conditions` and `has_permission` to restrict unauthorized data access.  
     
---

## **2. ✅ Task Completion Checklist**  

### **Mandatory Tasks**  
- [x] Data Models for `Company`, `Department`, `Employee`, `Project`, and `Performance Review`.  
    - [x] Company (Naming: by field company_name)
        - [x] Company Name (mandatory, unique)
        - [x] Number of Departments (virtual)
        - [x] Number of Employees (virtual)
        - [x] Number of Projects (virtual)
    - [x] Department (Naming: expression:{company}-{department_name})
        - [x] Company (mandatory)
        - [x] Department Name (mandatory)
        - [x] Number of Employees (virtual)
        - [x] Number of Projects (virtual)
    - [x] Employee (Naming: auto-increment)
        - [x] Company (Select, mandatory)
        - [x] Department (Select, mandatory)
        - [x] Employee Name
        - [x] Email Address (unique)
        - [x] Mobile Number (unique)
        - [x] Address
        - [x] Designation (Data)
        - [x] Hired On (optional)
        - [x] Days Employed (virtual)
    - [x] Project (Naming: Expression {company}-{department}-{project_name})
        - [x] Company (Select, mandatory)
        - [x] Department (Select, mandatory)
        - [x] Project Name (mandatory)
        - [x] Description
        - [x] Start Date (mandatory)
        - [x] End Date (mandatory)
        - [x] Assigned Employees (Multi-Select)
    - [x] Performance Review (Naming: Autoincreament)
        - [x] Status (Select)
        - [x] Employee (Link)
        - [x] Review Date
        - [x] Feedback
        - [x] Manager Comments
        - [x] Company (link, hidden, to control access for admins)
        - [x] department (link, hidden, to control access for managers)

- [x] Workflow for Performance Review (handled only by **managers** for now).  
- [x] Role-based access control for admins, managers and employees.  
- [x] CRUD operations for all entities with API support.

### **Bonus Tasks**  
- [x] CRUD operations for Projects via API.  
- [ ] Advanced data visualization for reports (pending).  

---

## **3. 🔐 Security Measures**  
1. **Role-Based Access Control**:  
   - `Admin`: Full access to all entities related to his company.  
   - `Manager`: Restricted to managing employees, departments, and performance reviews within their department.  
   - `Employee`: View-only access to their performance review and related data.  

2. **Data Protection**:  
   - Sensitive data like passwords are hashed using Frappe's secure authentication mechanism.  

---

## **4. 📡 API Documentation**  

The API depends on frappe API approach. Visit **https://docs.frappe.io/framework/v14/user/en/api/rest** to see more rich examples. 

### **Base URL**  
http://`<site-name>`/


### **Endpoints**: 
- Full **CRUD** endpoints for all entities.
- customize the request with query parameters: `fields`, `filters`, `order_by`, `limit_start`, `limit_page_length`, and `limit`.
- For more information visit: **https://docs.frappe.io/framework/v14/user/en/api/rest**

#### **Authentication**: Session-based authentication.
- **POST /api/method/login**
- **Headers**: `Content-Type: application/json`, `Accept: application/json`
- **Body**:  
  ```json  
  {  
    "usr": "<username or email>",
    "pwd": "<password>" 
  }  
    ```

#### **Company**  
- **GET /api/resource/Company**: Retrieve all companies.  
- **GET /api/resource/Company/<name>**: Retrieve a single company by name.  

#### **Department**  
- **GET /api/resource/Department**: Retrieve all departments.  
- **GET /api/resource/Department/<name>**: Retrieve a single department.  

#### **Employee**  
- **POST /api/resource/Employee**: Create a new employee.  
  **Body**:  
  ```json  
  {  
    "employee_name": "John Doe",  
    "email": "<user.email>",  
    "company": "<company_name>",  
    "department": "<department_name>"  
  }  
    ```
- **GET**: Retrieve a single employee by ID or list all employees.  
- **PATCH**: Update an existing employee.  
- **DELETE**: Remove an employee.  

### **Project**  
- **POST**: Create a new project.  
- **GET**: Retrieve a single project by ID or list all projects.  
- **PATCH**: Update an existing project.  
- **DELETE**: Remove a project.  

## Future Work
Note: the task took only 2 working days of 3 due to my heavy schedule.

1. Automate the integration tests.
2. Write validations on the full detailed scenarios on the different entities.
3. After knowing the full requirements, The `Performance Review` life cycle can be improved. For examble separate the **feedback** cycle from the **Review** and automate the process, and customize the access control over it to prevent human errors.
4. After knowing the full requirements, Improve Access Control over all entities.
5. Give **admins** access to handle `Performance Review`.


#### License
mit