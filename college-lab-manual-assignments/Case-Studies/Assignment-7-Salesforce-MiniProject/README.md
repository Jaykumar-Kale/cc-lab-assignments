# Cloud Computing Lab – Assignment 7
## Student Management System using Salesforce Cloud

---

## 📌 Assignment Title
Design and develop a custom application (Mini Project) using Salesforce Cloud.

---

## 🎯 Objective

To design and implement a cloud-based Student Management System using Salesforce Platform, demonstrating:

- Custom Objects
- Custom Fields
- Relationships
- Record Management
- Cloud-based application architecture

---

## ☁ Platform Used

- Salesforce Lightning Platform
- Salesforce Cloud (SaaS / PaaS)
- Custom Objects & Fields
- Declarative Development (No-Code / Low-Code)

---

## 🏗 System Overview

The Student Management System manages:

- Student Information
- Course Information
- Enrollment Details

The system is developed completely on Salesforce Cloud using custom objects.

---

## 🧱 Custom Objects Created

### 1️⃣ Student Object
Stores student details.

Fields:
- Student Name (Text)
- Roll Number (Text)
- Email (Email)
- Phone (Phone)
- Department (Picklist)
- Year (Picklist)

---

### 2️⃣ Course Object
Stores course details.

Fields:
- Course Name (Text)
- Course Code (Text)
- Credits (Number)
- Department (Picklist)

---

### 3️⃣ Enrollment Object
Used to create relationship between Student and Course.

Fields:
- Student (Lookup Relationship)
- Course (Lookup Relationship)
- Enrollment Date (Date)
- Status (Picklist)

---

## 🔗 Relationships Used

Enrollment Object acts as a junction object.

Relationships:
- Student → Enrollment (One-to-Many)
- Course → Enrollment (One-to-Many)

This models:

One Student can enroll in many Courses.
One Course can have many Students.

---

## 🧠 Architecture Type

This system follows:

SaaS Model (Software as a Service)

Salesforce provides:
- Hosting
- Database
- UI
- Security
- Authentication

We only configure business logic.

---

## 🛠 Development Steps (Step-by-Step)

1. Created new Salesforce Developer Account.
2. Opened Setup → Object Manager.
3. Created Custom Object: Student.
4. Added Custom Fields (Text, Email, Picklist, etc.).
5. Created Custom Object: Course.
6. Added required fields.
7. Created Custom Object: Enrollment.
8. Added Lookup relationships to Student and Course.
9. Created Tabs for each object.
10. Added objects to App Launcher.
11. Tested by inserting sample records.

---

## ⚠ Issue Faced – Text Style in Object

Problem:
While creating fields, text style or formatting was incorrect.

Reason:
Salesforce Text fields only store plain text.
They do not support rich text unless "Rich Text Area" field type is selected.

Solution:
If formatted text is required:
Use field type:
- Rich Text Area

Otherwise:
Use Text field for simple string storage.

---

## 🧪 Testing Procedure

1. Created Student record.
2. Created Course record.
3. Created Enrollment record.
4. Linked Student and Course via Lookup.
5. Verified relationship works.
6. Checked related lists inside Student object.

---

## 📊 Cloud Concepts Demonstrated

✔ SaaS (Software as a Service)
✔ Cloud Database
✔ Multi-Tenant Architecture
✔ Custom Object Modeling
✔ Relationship Management
✔ Low-Code Development

---

## 🔐 Security Model

Salesforce provides:

- Role-based access
- Object-level security
- Field-level security
- Record-level sharing

No manual backend required.

---

## 🎓 Viva Questions & Answers

Q1: What is Salesforce Cloud?
A: It is a cloud-based CRM platform providing SaaS and PaaS services.

Q2: What is a Custom Object?
A: A user-defined database table in Salesforce.

Q3: What is Lookup Relationship?
A: A relationship between two objects where one record references another.

Q4: What is a Junction Object?
A: An object used to create many-to-many relationships.

Q5: Which Cloud model is Salesforce?
A: SaaS (primary), also supports PaaS.

---

## 🧠 Viva Explanation (Short Version)

"We developed a Student Management System using Salesforce Cloud. We created custom objects for Student, Course, and Enrollment. Enrollment acts as a junction object to manage many-to-many relationships. The system demonstrates SaaS cloud architecture and relationship modeling."

---

## 🧠 Viva Explanation (Detailed Version)

"This project demonstrates how cloud platforms like Salesforce allow rapid application development using declarative tools. Instead of building backend manually, we use custom objects and relationships to design the data model. Salesforce handles infrastructure, security, and hosting."

---

## 🚀 Future Enhancements

- Add validation rules
- Add automation (Flow Builder)
- Add Reports & Dashboards
- Add Role-based permissions
- Add Triggers (Apex)

---

## ✅ Conclusion

This assignment demonstrates cloud-based application development using Salesforce Cloud.

It shows:

- Data modeling
- Relationship design
- SaaS architecture
- Low-code development
- Cloud deployment without infrastructure management

The Student Management System successfully runs on Salesforce Cloud.

---

END OF README