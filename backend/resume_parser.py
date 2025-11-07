"""
Resume parsing utilities to extract text and skills from PDF/text files
"""

import re
from typing import List, Set
try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

from backend.data.job_roles_data import COMMON_SKILLS


def extract_text_from_pdf(pdf_file) -> str:
    """
    Extract text content from a PDF file
    
    Args:
        pdf_file: Uploaded PDF file object from Streamlit
        
    Returns:
        Extracted text as string
    """
    if PdfReader is None:
        raise ImportError("PyPDF2 is required for PDF parsing. Install it with: pip install PyPDF2")
    
    try:
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")


def extract_text_from_txt(txt_file) -> str:
    """
    Extract text content from a text file
    
    Args:
        txt_file: Uploaded text file object from Streamlit
        
    Returns:
        Extracted text as string
    """
    try:
        text = txt_file.read().decode('utf-8')
        return text
    except Exception as e:
        raise Exception(f"Error reading text file: {str(e)}")


def extract_skills_from_text(text: str) -> Set[str]:
    """
    Extract skills from resume text using keyword matching
    
    Args:
        text: Resume text content
        
    Returns:
        Set of identified skills
    """
    text_lower = text.lower()
    found_skills = set()
    
    for skill in COMMON_SKILLS:
        # Create pattern to match skill as whole word (case-insensitive)
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.add(skill)
    
    return found_skills


def parse_resume(uploaded_file) -> dict:
    """
    Main function to parse resume and extract information
    
    Args:
        uploaded_file: Streamlit uploaded file object
        
    Returns:
        Dictionary containing:
            - text: Full resume text
            - skills: Set of identified skills
            - skill_count: Number of skills found
    """
    file_type = uploaded_file.name.split('.')[-1].lower()
    
    # Extract text based on file type
    if file_type == 'pdf':
        text = extract_text_from_pdf(uploaded_file)
    elif file_type in ['txt', 'text']:
        text = extract_text_from_txt(uploaded_file)
    else:
        raise ValueError(f"Unsupported file type: {file_type}. Please upload PDF or TXT file.")
    
    # Extract skills
    skills = extract_skills_from_text(text)
    
    return {
        'text': text,
        'skills': skills,
        'skill_count': len(skills)
    }