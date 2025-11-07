"""
Static job roles database with skills, demand scores, and learning resources
"""

JOB_ROLES_DB = {
    "Data Analyst": {
        "required_skills": [
            "SQL", "Excel", "Python", "Data Visualization", "Statistics",
            "Tableau", "Power BI", "Data Cleaning", "Business Intelligence"
        ],
        "demand_score": 85,
        "description": "Analyze data to help businesses make informed decisions",
        "learning_resources": {
            "SQL": {
                "youtube": "https://www.youtube.com/results?search_query=SQL+tutorial+for+beginners",
                "estimated_hours": 40
            },
            "Python": {
                "youtube": "https://www.youtube.com/results?search_query=Python+for+data+analysis",
                "estimated_hours": 60
            },
            "Data Visualization": {
                "youtube": "https://www.youtube.com/results?search_query=Data+visualization+tutorial",
                "estimated_hours": 30
            },
            "Tableau": {
                "youtube": "https://www.youtube.com/results?search_query=Tableau+tutorial",
                "estimated_hours": 25
            },
            "Statistics": {
                "youtube": "https://www.youtube.com/results?search_query=Statistics+for+data+analysis",
                "estimated_hours": 50
            }
        },
        "career_path": ["Junior Data Analyst", "Data Analyst", "Senior Data Analyst", "Data Scientist"]
    },
    
    "Data Scientist": {
        "required_skills": [
            "Python", "R", "Machine Learning", "Statistics", "SQL",
            "Deep Learning", "Data Visualization", "Pandas", "NumPy", "Scikit-learn"
        ],
        "demand_score": 92,
        "description": "Build predictive models and extract insights from complex data",
        "learning_resources": {
            "Machine Learning": {
                "youtube": "https://www.youtube.com/results?search_query=Machine+learning+course",
                "estimated_hours": 100
            },
            "Deep Learning": {
                "youtube": "https://www.youtube.com/results?search_query=Deep+learning+tutorial",
                "estimated_hours": 80
            },
            "Python": {
                "youtube": "https://www.youtube.com/results?search_query=Python+for+data+science",
                "estimated_hours": 60
            },
            "Statistics": {
                "youtube": "https://www.youtube.com/results?search_query=Statistics+for+data+science",
                "estimated_hours": 50
            },
            "Scikit-learn": {
                "youtube": "https://www.youtube.com/results?search_query=Scikit+learn+tutorial",
                "estimated_hours": 40
            }
        },
        "career_path": ["Data Analyst", "Junior Data Scientist", "Data Scientist", "Senior Data Scientist", "ML Engineer"]
    },
    
    "ML Engineer": {
        "required_skills": [
            "Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
            "MLOps", "Docker", "Kubernetes", "Cloud Platforms", "Model Deployment"
        ],
        "demand_score": 88,
        "description": "Design and deploy machine learning systems at scale",
        "learning_resources": {
            "TensorFlow": {
                "youtube": "https://www.youtube.com/results?search_query=TensorFlow+tutorial",
                "estimated_hours": 60
            },
            "PyTorch": {
                "youtube": "https://www.youtube.com/results?search_query=PyTorch+tutorial",
                "estimated_hours": 60
            },
            "MLOps": {
                "youtube": "https://www.youtube.com/results?search_query=MLOps+tutorial",
                "estimated_hours": 50
            },
            "Docker": {
                "youtube": "https://www.youtube.com/results?search_query=Docker+tutorial",
                "estimated_hours": 30
            },
            "Model Deployment": {
                "youtube": "https://www.youtube.com/results?search_query=ML+model+deployment",
                "estimated_hours": 40
            }
        },
        "career_path": ["Data Scientist", "Junior ML Engineer", "ML Engineer", "Senior ML Engineer", "AI Architect"]
    },
    
    "Software Engineer": {
        "required_skills": [
            "Python", "Java", "JavaScript", "Git", "Data Structures",
            "Algorithms", "SQL", "REST APIs", "Testing", "Agile"
        ],
        "demand_score": 90,
        "description": "Design, develop, and maintain software applications",
        "learning_resources": {
            "Data Structures": {
                "youtube": "https://www.youtube.com/results?search_query=Data+structures+tutorial",
                "estimated_hours": 80
            },
            "Algorithms": {
                "youtube": "https://www.youtube.com/results?search_query=Algorithms+tutorial",
                "estimated_hours": 80
            },
            "Java": {
                "youtube": "https://www.youtube.com/results?search_query=Java+programming+tutorial",
                "estimated_hours": 70
            },
            "REST APIs": {
                "youtube": "https://www.youtube.com/results?search_query=REST+API+tutorial",
                "estimated_hours": 30
            },
            "Git": {
                "youtube": "https://www.youtube.com/results?search_query=Git+tutorial",
                "estimated_hours": 20
            }
        },
        "career_path": ["Junior Software Engineer", "Software Engineer", "Senior Software Engineer", "Tech Lead", "Engineering Manager"]
    },
    
    "Full Stack Developer": {
        "required_skills": [
            "JavaScript", "React", "Node.js", "HTML", "CSS",
            "MongoDB", "SQL", "REST APIs", "Git", "TypeScript"
        ],
        "demand_score": 87,
        "description": "Build complete web applications from frontend to backend",
        "learning_resources": {
            "React": {
                "youtube": "https://www.youtube.com/results?search_query=React+tutorial",
                "estimated_hours": 50
            },
            "Node.js": {
                "youtube": "https://www.youtube.com/results?search_query=Node.js+tutorial",
                "estimated_hours": 50
            },
            "JavaScript": {
                "youtube": "https://www.youtube.com/results?search_query=JavaScript+tutorial",
                "estimated_hours": 60
            },
            "MongoDB": {
                "youtube": "https://www.youtube.com/results?search_query=MongoDB+tutorial",
                "estimated_hours": 30
            },
            "TypeScript": {
                "youtube": "https://www.youtube.com/results?search_query=TypeScript+tutorial",
                "estimated_hours": 40
            }
        },
        "career_path": ["Junior Full Stack Developer", "Full Stack Developer", "Senior Full Stack Developer", "Tech Lead"]
    },
    
    "DevOps Engineer": {
        "required_skills": [
            "Linux", "Docker", "Kubernetes", "CI/CD", "AWS",
            "Terraform", "Ansible", "Git", "Python", "Monitoring"
        ],
        "demand_score": 86,
        "description": "Automate and optimize software development and deployment processes",
        "learning_resources": {
            "Docker": {
                "youtube": "https://www.youtube.com/results?search_query=Docker+tutorial",
                "estimated_hours": 40
            },
            "Kubernetes": {
                "youtube": "https://www.youtube.com/results?search_query=Kubernetes+tutorial",
                "estimated_hours": 60
            },
            "AWS": {
                "youtube": "https://www.youtube.com/results?search_query=AWS+tutorial",
                "estimated_hours": 80
            },
            "Terraform": {
                "youtube": "https://www.youtube.com/results?search_query=Terraform+tutorial",
                "estimated_hours": 40
            },
            "CI/CD": {
                "youtube": "https://www.youtube.com/results?search_query=CI+CD+tutorial",
                "estimated_hours": 35
            }
        },
        "career_path": ["Junior DevOps Engineer", "DevOps Engineer", "Senior DevOps Engineer", "DevOps Architect"]
    },
    
    "Business Analyst": {
        "required_skills": [
            "Business Intelligence", "SQL", "Excel", "Requirements Analysis", "JIRA",
            "Process Modeling", "Stakeholder Management", "Data Analysis", "Documentation"
        ],
        "demand_score": 82,
        "description": "Bridge business needs with technical solutions",
        "learning_resources": {
            "Business Intelligence": {
                "youtube": "https://www.youtube.com/results?search_query=Business+intelligence+tutorial",
                "estimated_hours": 50
            },
            "Requirements Analysis": {
                "youtube": "https://www.youtube.com/results?search_query=Requirements+analysis+tutorial",
                "estimated_hours": 40
            },
            "SQL": {
                "youtube": "https://www.youtube.com/results?search_query=SQL+for+business+analysts",
                "estimated_hours": 40
            },
            "Process Modeling": {
                "youtube": "https://www.youtube.com/results?search_query=Business+process+modeling",
                "estimated_hours": 30
            },
            "JIRA": {
                "youtube": "https://www.youtube.com/results?search_query=JIRA+tutorial",
                "estimated_hours": 20
            }
        },
        "career_path": ["Junior Business Analyst", "Business Analyst", "Senior Business Analyst", "Product Manager"]
    }
}

# Common technical skills for keyword extraction
COMMON_SKILLS = [
    # Programming Languages
    "Python", "Java", "JavaScript", "C++", "C#", "R", "Go", "Ruby", "PHP", "Swift",
    "Kotlin", "TypeScript", "Scala", "Rust", "MATLAB",
    
    # Web Technologies
    "HTML", "CSS", "React", "Angular", "Vue.js", "Node.js", "Django", "Flask",
    "Express.js", "Spring Boot", "REST APIs", "GraphQL",
    
    # Databases
    "SQL", "MySQL", "PostgreSQL", "MongoDB", "Redis", "Oracle", "NoSQL",
    "Cassandra", "DynamoDB",
    
    # Data Science & ML
    "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Scikit-learn",
    "Pandas", "NumPy", "Data Visualization", "Statistics", "NLP", "Computer Vision",
    
    # Cloud & DevOps
    "AWS", "Azure", "GCP", "Docker", "Kubernetes", "CI/CD", "Jenkins", "Git",
    "Terraform", "Ansible", "Linux", "MLOps",
    
    # Analytics & BI
    "Tableau", "Power BI", "Excel", "Data Analysis", "Business Intelligence",
    "Data Cleaning", "ETL",
    
    # Other
    "Agile", "Scrum", "JIRA", "Testing", "Debugging", "Problem Solving",
    "Communication", "Team Collaboration", "Project Management"
]