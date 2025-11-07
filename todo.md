# Career Compass AI - MVP Development Plan

## Project Overview
A Streamlit web application that analyzes resumes and provides career guidance with job role suggestions, skills gap analysis, and learning resources.

## File Structure
```
/workspace/streamlit_template/
├── app.py                          # Main Streamlit application (landing + main pages)
├── backend/
│   ├── __init__.py                 # Package initializer
│   ├── resume_parser.py            # Resume text extraction from PDF
│   ├── career_analyzer.py          # Job role matching and scoring logic
│   └── data/
│       └── job_roles_data.py       # Static job roles dictionary with skills
├── requirements.txt                # Python dependencies
└── template_config.json            # Template configuration
```

## Core Files to Create (6 files total)

### 1. backend/__init__.py
- Empty package initializer

### 2. backend/data/job_roles_data.py
- Static dictionary with 5-7 job roles
- Each role contains: required skills, demand score, learning resources, career progression
- Roles: Data Analyst, Data Scientist, ML Engineer, Software Engineer, Full Stack Developer

### 3. backend/resume_parser.py
- Function to extract text from PDF using PyPDF2
- Function to extract text from plain text
- Simple keyword extraction for skills

### 4. backend/career_analyzer.py
- Function to match resume skills with job roles
- Calculate match score (0-100) based on skills overlap
- Identify missing skills
- Generate career roadmap suggestions

### 5. app.py
- Page 1: Landing page with "Get Started" button
- Page 2: Resume upload and analysis with score display
- Page 3: Skills comparison table with learning resources and roadmap
- Use Streamlit session state for navigation

### 6. requirements.txt
- streamlit
- PyPDF2
- pandas

## Implementation Strategy
- Use simple keyword matching for skills extraction
- Static data for job roles (no ML model needed)
- Session state for page navigation
- Minimalistic UI with cards and tables

## Status
- [ ] Create backend package structure
- [ ] Implement job roles data
- [ ] Implement resume parser
- [ ] Implement career analyzer
- [ ] Create main Streamlit app
- [ ] Update requirements.txt
- [ ] Test and lint