# import random
# from faker import Faker
# from datetime import datetime, timedelta

# fake = Faker()

# def generate_employee_data(num_employees=5):
#     employees = []
#     for _ in range(num_employees):

#         employee = {
#             "employee_id": fake.uuid4(),
#             "name": fake.first_name(),
#             "lastname": fake.last_name(),
#             "email": fake.email(),
#             "phone_number": fake.phone_number(),
#             "position": random.choice([
#                 "Research Scientist", 
#                 "Software Engineer", 
#                 "Operations Manager", 
#                 "HR Specialist", 
#                 "Security Officer"
#             ]),
#             "department": random.choice([
#                 "R&D", 
#                 "IT", 
#                 "Operations", 
#                 "HR", 
#                 "Security"
#             ]),
#             "skills": random.sample([
#                 "Python", "Project Management", "Data Analysis", 
#                 "Genetic Research", "Cybersecurity", "Machine Learning",
#                 "Leadership", "Database Management", "Public Speaking"
#             ], k=random.randint(2, 5)),
#             "location": random.choice([
#                 "Raccoon City HQ", 
#                 "Umbrella Europe", 
#                 "Umbrella Asia", 
#                 "Umbrella North America", 
#                 "Umbrella South America"
#             ]),
#             "hire_date": (
#                 datetime.now() - timedelta(days=random.randint(1, 365 * 10))
#             ).strftime("%Y-%m-%d"),
#             "supervisor": fake.name(),
#             "salary": round(random.uniform(40000, 120000), 2),
#         }

#         employees.append(employee)

#     return employees




# import random 

# def generate_employee_data(num_employees=1):
#     """
#     Returns a fixed, detailed profile for the user to fill in.
#     The list format is maintained to match the structure expected by app.py.
#     """
#     # === BEGIN: USER-EDITABLE PROFILE ===
#     # Please replace the placeholder values below with your own details.
#     user_profile = {
#         "employee_id": "A354145024004",
#         "name": "Kuldeep",
#         "lastname": "Mandal",
#         "email": "kuldeepmandal175514@gmail.com",
#         "phone_number": "6299689984",
#         "position": "Fresher",
#         "department": "Information technology",
#         "skills": [
#             "Python", "Javascript", "WebDev", 
#             "Data Analysis", "Leadership", "Technical Writing"
#         ],
#         "location": "Remote",
#         "hire_date": "2020-01-15",
#         "supervisor": "-",
#         "salary_range": "Any",
#         # Custom field for your goals
#         "current_goal": "Get familiar with Gen-Ai",
#     }
#     # === END: USER-EDITABLE PROFILE ===

#     # Return only the single profile required by the application
#     # The list wrapper is needed because app.py calls generate_employee_data(1)[0]
#     return [user_profile] * num_employees





import random 

def generate_employee_data(num_employees=1):
    """
    Returns a fixed, detailed profile for the user to fill in.
    The list format is maintained to match the structure expected by app.py.
    """
    # === BEGIN: USER-EDITABLE PROFILE ===
    # This profile is now customized to Kuldeep Mandal's professional data.
    user_profile = {
        "employee_id": "A354145024004",
        "name": "Kuldeep",
        "lastname": "Mandal",
        "email": "kuldeepmandal175514@gmail.com",
        "phone_number": "6299689984",
        "position": "Fresher",
        "department": "Information technology",
        "skills": [
            # Updated based on your CV/website analysis
            "Python", 
            "Java (basic)", 
            "Javascript",
            "React", 
            "HTML", 
            "CSS", 
            "MySQL", 
            "SQL",
            "Power BI", 
            "Data Analysis", 
            "Leadership", 
            "Problem Solving"
        ],
        "location": "Remote",
        "supervisor": "-",
        "salary_range": "Any",
        # Custom field for your goals
        "current_goal": "Get familiar with Gen-Ai",
        "education": "Pursuing MCA at Amity University", # Added for context
    }
    # === END: USER-EDITABLE PROFILE ===

    # Return only the single profile required by the application
    # The list wrapper is needed because app.py calls generate_employee_data(1)[0]
    return [user_profile] * num_employees

