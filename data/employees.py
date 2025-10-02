import random 

def generate_employee_data(num_employees=1):
    """
    Returns a fixed, detailed profile for the user to fill in.
    The list format is maintained to match the structure expected by app.py.
    """

    user_profile = {
        "employee_id": "A354145024004",
        "name": "Kuldeep",
        "lastname": "Mandal",
        "email": "kuldeepmandal175514@gmail.com",
        "phone_number": "6299689984",
        "position": "Fresher",
        "department": "Information technology",
        "skills": [

            "Python", 
            "Java",
            "Node.js",
            "Pandas",
            "Numpy",
            "Langchain",
            "Vector Database(ChromaDB)",
            "Streamlit cloud",
            "Git/Github Version Control",
            "MS Office",
            "Serverless/Zero cost architecture",
            "Puter cloud",
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

        "current_goal": "Get familiar with Gen-Ai",
        "education": "Pursuing MCA at Amity University",
    }

    return [user_profile] * num_employees

