# Smart Student Performance Prediction System

## **1. PROBLEM STATEMENT:**

- Students performance is influenced by multiple academic and behavioral factors.
- Faculty may find it difficult to identify student who are at risk at an early stage.
- A data-driven system can help predict student performance.
- The system can provide recommendation for improving student outcomes.

## **2. PROPOSED SOLUTION:**
- Collect student-related information.
- Process the entered data.
- Use a Machine Learning model to predict performance.
- Classify students based on predicted performance.
- Generate intelligent recommendations.
- Display the results through a user-friendly Tkinter interface.

## **3. PROCESS FLOW:**


```text
Start
  ↓
Enter Student Details
  ↓
Validate Input
  ↓
Preprocess Data
  ↓
ML Prediction
  ↓
Determine Performance Level
  ↓
Generate AI Recommendation
  ↓
Display Result
  ↓
End
```
## **4. PROJECT MAPPING:**

| **V-Model Stage**          | **Smart Student Project**                    |
|----------------------------|----------------------------------------------|
| Requirement Analysis       | Identify student performance problem         |
| System Design              | Design system architecture and UI            |
| Implementation             | Develop Python + ML application              |
| Integration                | Integrate UI, ML and AI                      |
| Testing                    | Test individual modules and complete system  |
| Validation                 | Check system against requirements            |
| Demonstration              | Present working capstone                     |

## **5. PROJECT - MODULAR APPLICATION DEVELOPMENT:**
Create separate functions:

```text
get_student_data()
calculate_average()
calculate_performance()
display_result()
```
## **6. REQUIREMENT ANALYSIS:**
## **6.1 FUNCTIONAL REQUIREMENTS:**
The system should:
- Accept student details.
- Validate user inputs.
- Store/process student information.
- Preprocess input data.
- Apply the trained ML model.
- Predict student performance.
- Generate recommendations.
- Display results through the GUI.
- Handle invalid inputs.
- Provide a reset/clear option.

## **6.2 NON-FUNCTIONAL REQUIREMENTS:**
- The application should be:
- User-friendly
- Easy to understand
- Fast in generating predictions
- Reliable
- Maintainable
- Scalable
- Secure with respect to student data
- Easy to test

## **6.3 IDENTIFY THE USER:**
Primary users may include:

- Faculty
- Academic coordinators
- Mentors
- Students
## **6.4 USER REQUIREMENT:**
The user should be able to:

- Enter student information.
- Submit the information for analysis.
- View predicted performance.
- Understand the student's risk level.
- Receive improvement recommendations.

## **6.5 IDENTIFY SYSTEM INPUTS:**
The initial system can use:

- Student ID
- Student Name
- Attendance Percentage
- Study Hours per Day
- Internal Assessment Marks
- Assignment Completion Percentage
- Previous Academic Performance

## **6.6 IDENTIFY SYSTEM OUTPUTS:**
### **6.6.1 PERFORMANCE PREDICTION:**
- Excellent
- Good
- Average
- At Risk
### **6.6.2 ADDITIONAL OUTPUT:**
- Prediction score/probability
- Risk level
- Key factors affecting performance
- Recommended actions
## **Example:**
Prediction: Good Performance

Risk Level: Low

Recommendation: Maintain current study pattern and attendance

## **7. SYSTEM DESIGN**
### **7.1 INPUTS**
- Student ID
- Student Name
- Attendance %
- Study Hours
- Internal Marks
- Assignment Completion %
- Previous Academic Performance
### **7.2 PROCESSING** 
- Validate input
- Preprocess data
- Send data to ML model
- Generate prediction
- Generate recommendation
### **7.3 OUTPUTS**
- Predicted performance
- Performance category
- Risk level
- Recommendation
## **8. SYSTEM ARCHITECTURE**
<img width="1600" height="800" alt="WhatsApp Image 2026-08-18 at 11 30 39 AM" src="https://github.com/user-attachments/assets/e4f937d4-530e-4dea-b859-2758e9d2535d" />

## **9. UI DESIGN REQUIREMENTS**
The application should contain:
### **9.1 STUDENT ACADEMIC SECTION**
- Student ID
- Student Name
### **9.2 ACADEMIC INFORMATION SECTION**
- Attendance
- Study Hours
- Internal Marks
- Assignment Completion
- Previous Performance
### **9.3 ACTION SECTION**
- Predict Performance
- Clear
- Exit
### **9.4 RESULT SECTION**
- Predicted Performance
- Risk Level
- Recommendation


