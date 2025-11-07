"""
Career analysis and job role matching logic
"""

from typing import List, Dict, Set
from backend.data.job_roles_data import JOB_ROLES_DB


def calculate_match_score(user_skills: Set[str], required_skills: List[str]) -> float:
    """
    Calculate match percentage between user skills and required skills
    
    Args:
        user_skills: Set of skills from user's resume
        required_skills: List of skills required for a job role
        
    Returns:
        Match score as percentage (0-100)
    """
    if not required_skills:
        return 0.0
    
    # Convert to lowercase for case-insensitive matching
    user_skills_lower = {skill.lower() for skill in user_skills}
    required_skills_lower = [skill.lower() for skill in required_skills]
    
    # Count matching skills
    matching_skills = sum(1 for skill in required_skills_lower if skill in user_skills_lower)
    
    # Calculate percentage
    match_percentage = (matching_skills / len(required_skills)) * 100
    
    return round(match_percentage, 1)


def analyze_career_fit(user_skills: Set[str]) -> List[Dict]:
    """
    Analyze user skills against all job roles and return ranked matches
    
    Args:
        user_skills: Set of skills from user's resume
        
    Returns:
        List of job role matches sorted by score (highest first)
        Each match contains: role_name, match_score, demand_score, 
        combined_score, description, required_skills, missing_skills
    """
    matches = []
    
    for role_name, role_data in JOB_ROLES_DB.items():
        required_skills = role_data['required_skills']
        match_score = calculate_match_score(user_skills, required_skills)
        demand_score = role_data['demand_score']
        
        # Combined score: 70% match + 30% demand
        combined_score = (match_score * 0.7) + (demand_score * 0.3)
        
        # Identify missing skills
        user_skills_lower = {skill.lower() for skill in user_skills}
        missing_skills = [
            skill for skill in required_skills 
            if skill.lower() not in user_skills_lower
        ]
        
        # Identify known skills
        known_skills = [
            skill for skill in required_skills 
            if skill.lower() in user_skills_lower
        ]
        
        matches.append({
            'role_name': role_name,
            'match_score': match_score,
            'demand_score': demand_score,
            'combined_score': round(combined_score, 1),
            'description': role_data['description'],
            'required_skills': required_skills,
            'known_skills': known_skills,
            'missing_skills': missing_skills,
            'learning_resources': role_data['learning_resources'],
            'career_path': role_data['career_path']
        })
    
    # Sort by combined score (highest first)
    matches.sort(key=lambda x: x['combined_score'], reverse=True)
    
    return matches


def get_learning_plan(role_match: Dict) -> List[Dict]:
    """
    Generate a learning plan for missing skills
    
    Args:
        role_match: Dictionary containing role match information
        
    Returns:
        List of learning items with skill, resource, and time estimate
    """
    learning_plan = []
    missing_skills = role_match['missing_skills']
    learning_resources = role_match['learning_resources']
    
    for skill in missing_skills:
        if skill in learning_resources:
            resource = learning_resources[skill]
            learning_plan.append({
                'skill': skill,
                'youtube_link': resource['youtube'],
                'estimated_hours': resource['estimated_hours']
            })
        else:
            # Fallback for skills without specific resources
            learning_plan.append({
                'skill': skill,
                'youtube_link': f"https://www.youtube.com/results?search_query={skill.replace(' ', '+')}+tutorial",
                'estimated_hours': 30  # Default estimate
            })
    
    return learning_plan


def generate_career_roadmap(role_match: Dict) -> str:
    """
    Generate a career progression roadmap
    
    Args:
        role_match: Dictionary containing role match information
        
    Returns:
        Formatted career path string
    """
    career_path = role_match['career_path']
    return " → ".join(career_path)