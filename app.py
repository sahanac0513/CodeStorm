"""
Career Compass AI - Main Streamlit Application
A web app that analyzes resumes and provides career guidance
"""

import streamlit as st
import pandas as pd
from backend.resume_parser import parse_resume
from backend.career_analyzer import analyze_career_fit, get_learning_plan, generate_career_roadmap


# Page configuration
st.set_page_config(
    page_title="Career Compass AI",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
    .score-excellent {
        color: #28a745;
        font-size: 2.5rem;
        font-weight: bold;
    }
    .score-good {
        color: #ffc107;
        font-size: 2.5rem;
        font-weight: bold;
    }
    .score-fair {
        color: #fd7e14;
        font-size: 2.5rem;
        font-weight: bold;
    }
    .score-poor {
        color: #dc3545;
        font-size: 2.5rem;
        font-weight: bold;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-size: 1.2rem;
        padding: 0.75rem;
        border-radius: 10px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #155a8a;
    }
    </style>
""", unsafe_allow_html=True)


# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'landing'
if 'resume_data' not in st.session_state:
    st.session_state.resume_data = None
if 'career_matches' not in st.session_state:
    st.session_state.career_matches = None
if 'selected_role' not in st.session_state:
    st.session_state.selected_role = None


def landing_page():
    """Landing page with introduction and Get Started button"""
    st.markdown('<div class="main-header">🧭 Career Compass AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Navigate Your Career Journey with AI-Powered Insights</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        ### Welcome to Career Compass AI
        
        Your intelligent career guidance platform that helps you:
        
        ✅ **Analyze Your Resume** - Upload your resume and get instant insights
        
        ✅ **Discover Career Paths** - Find job roles that match your skills
        
        ✅ **Identify Skill Gaps** - See what skills you need to learn
        
        ✅ **Get Learning Resources** - Access curated learning paths with time estimates
        
        ✅ **Plan Your Career** - Visualize your career progression roadmap
        
        ---
        
        ### How It Works
        
        1. **Upload** your resume (PDF or TXT format)
        2. **Analyze** your skills and get a career fit score
        3. **Explore** recommended job roles and career paths
        4. **Learn** with personalized skill development resources
        
        ---
        """)
        
        if st.button("🚀 Get Started", key="get_started"):
            st.session_state.page = 'upload'
            st.rerun()


def upload_page():
    """Resume upload and analysis page"""
    st.markdown('<div class="main-header">📄 Upload Your Resume</div>', unsafe_allow_html=True)
    
    # Back button
    if st.button("← Back to Home"):
        st.session_state.page = 'landing'
        st.rerun()
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        ### Upload Your Resume
        
        Please upload your resume in **PDF** or **TXT** format. 
        Our AI will analyze your skills and match them with relevant career opportunities.
        """)
        
        uploaded_file = st.file_uploader(
            "Choose a file",
            type=['pdf', 'txt'],
            help="Upload your resume in PDF or TXT format"
        )
        
        if uploaded_file is not None:
            st.success(f"✅ File uploaded: {uploaded_file.name}")
            
            if st.button("🔍 Analyze Resume", key="analyze"):
                with st.spinner("Analyzing your resume... This may take a moment."):
                    try:
                        # Parse resume
                        resume_data = parse_resume(uploaded_file)
                        st.session_state.resume_data = resume_data
                        
                        # Analyze career fit
                        career_matches = analyze_career_fit(resume_data['skills'])
                        st.session_state.career_matches = career_matches
                        
                        # Move to results page
                        st.session_state.page = 'results'
                        st.rerun()
                        
                    except Exception as e:
                        st.error(f"❌ Error analyzing resume: {str(e)}")
                        st.info("Please make sure your file is a valid PDF or TXT file.")


def get_score_class(score):
    """Return CSS class based on score"""
    if score >= 80:
        return "score-excellent"
    elif score >= 60:
        return "score-good"
    elif score >= 40:
        return "score-fair"
    else:
        return "score-poor"


def results_page():
    """Display analysis results and top career matches"""
    st.markdown('<div class="main-header">📊 Your Career Analysis</div>', unsafe_allow_html=True)
    
    # Back button
    if st.button("← Upload New Resume"):
        st.session_state.page = 'upload'
        st.session_state.resume_data = None
        st.session_state.career_matches = None
        st.rerun()
    
    st.markdown("---")
    
    if st.session_state.resume_data and st.session_state.career_matches:
        resume_data = st.session_state.resume_data
        career_matches = st.session_state.career_matches
        
        # Display skills found
        st.markdown("### 🎯 Skills Identified in Your Resume")
        st.info(f"**{resume_data['skill_count']} skills** detected from your resume")
        
        # Display skills in columns
        skills_list = sorted(list(resume_data['skills']))
        cols = st.columns(4)
        for idx, skill in enumerate(skills_list):
            with cols[idx % 4]:
                st.markdown(f"✓ {skill}")
        
        st.markdown("---")
        
        # Display top 3 career matches
        st.markdown("### 🎯 Top Career Matches")
        st.markdown("Based on your skills, here are your best career opportunities:")
        
        for idx, match in enumerate(career_matches[:3], 1):
            with st.expander(f"**#{idx} {match['role_name']}** - Score: {match['combined_score']}/100", expanded=(idx==1)):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown("#### Match Score")
                    score_class = get_score_class(match['match_score'])
                    st.markdown(f'<div class="{score_class}">{match["match_score"]}%</div>', unsafe_allow_html=True)
                    st.caption("Skills match")
                
                with col2:
                    st.markdown("#### Industry Demand")
                    st.markdown(f'<div class="score-excellent">{match["demand_score"]}/100</div>', unsafe_allow_html=True)
                    st.caption("Market demand")
                
                with col3:
                    st.markdown("#### Overall Score")
                    score_class = get_score_class(match['combined_score'])
                    st.markdown(f'<div class="{score_class}">{match["combined_score"]}/100</div>', unsafe_allow_html=True)
                    st.caption("Combined rating")
                
                st.markdown(f"**Description:** {match['description']}")
                
                st.markdown(f"**✅ Skills You Have ({len(match['known_skills'])}):** {', '.join(match['known_skills']) if match['known_skills'] else 'None'}")
                st.markdown(f"**📚 Skills to Learn ({len(match['missing_skills'])}):** {', '.join(match['missing_skills']) if match['missing_skills'] else 'None'}")
                
                if st.button(f"View Learning Path for {match['role_name']}", key=f"view_{idx}"):
                    st.session_state.selected_role = match
                    st.session_state.page = 'learning'
                    st.rerun()
        
        st.markdown("---")
        
        # Next button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("📚 View Detailed Learning Paths", key="next_to_learning"):
                st.session_state.selected_role = career_matches[0]  # Default to top match
                st.session_state.page = 'learning'
                st.rerun()


def learning_page():
    """Display detailed learning path and career roadmap"""
    st.markdown('<div class="main-header">📚 Your Learning Path</div>', unsafe_allow_html=True)
    
    # Back button
    if st.button("← Back to Results"):
        st.session_state.page = 'results'
        st.rerun()
    
    st.markdown("---")
    
    if st.session_state.selected_role:
        role = st.session_state.selected_role
        
        # Role selector
        st.markdown("### Select a Career Role")
        role_names = [match['role_name'] for match in st.session_state.career_matches]
        selected_role_name = st.selectbox(
            "Choose a role to explore:",
            role_names,
            index=role_names.index(role['role_name'])
        )
        
        # Update selected role if changed
        if selected_role_name != role['role_name']:
            for match in st.session_state.career_matches:
                if match['role_name'] == selected_role_name:
                    st.session_state.selected_role = match
                    role = match
                    break
        
        st.markdown(f"## {role['role_name']}")
        st.markdown(f"*{role['description']}*")
        
        st.markdown("---")
        
        # Skills comparison
        st.markdown("### 🎯 Skills Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### ✅ Skills You Already Have")
            if role['known_skills']:
                for skill in role['known_skills']:
                    st.success(f"✓ {skill}")
            else:
                st.info("Start building your skills for this role!")
        
        with col2:
            st.markdown("#### 📚 Skills You Need to Learn")
            if role['missing_skills']:
                for skill in role['missing_skills']:
                    st.warning(f"○ {skill}")
            else:
                st.success("You have all required skills!")
        
        st.markdown("---")
        
        # Learning plan table
        if role['missing_skills']:
            st.markdown("### 📖 Personalized Learning Plan")
            st.markdown("Here's your roadmap to acquire the missing skills:")
            
            learning_plan = get_learning_plan(role)
            
            # Create DataFrame for better display
            df_data = []
            total_hours = 0
            for item in learning_plan:
                df_data.append({
                    'Skill': item['skill'],
                    'Learning Resource': f"[YouTube Tutorial]({item['youtube_link']})",
                    'Estimated Time': f"{item['estimated_hours']} hours"
                })
                total_hours += item['estimated_hours']
            
            df = pd.DataFrame(df_data)
            
            # Display as table with clickable links
            st.table(df)
            
            st.info(f"**Total Learning Time:** Approximately {total_hours} hours ({total_hours//40} weeks at 40 hours/week)")
        else:
            st.markdown("### 📖 Personalized Learning Plan")
            st.success("🎉 You have all the required skills for this role! No learning plan needed.")
        
        st.markdown("---")
        
        # Career roadmap
        st.markdown("### 🚀 Career Progression Roadmap")
        st.markdown("Your potential career path in this field:")
        
        roadmap = generate_career_roadmap(role)
        st.success(roadmap)
        
        st.markdown("---")
        
        # Download report button (placeholder)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.download_button(
                label="📥 Download Career Report",
                data=generate_report(role),
                file_name=f"career_report_{role['role_name'].replace(' ', '_')}.txt",
                mime="text/plain"
            )


def generate_report(role: dict) -> str:
    """Generate a text report for download"""
    report = f"""
CAREER COMPASS AI - CAREER ANALYSIS REPORT
==========================================

Career Role: {role['role_name']}
Description: {role['description']}

SCORES
------
Skills Match: {role['match_score']}%
Industry Demand: {role['demand_score']}/100
Overall Score: {role['combined_score']}/100

SKILLS YOU HAVE ({len(role['known_skills'])})
-----------------
{chr(10).join('✓ ' + skill for skill in role['known_skills']) if role['known_skills'] else 'None'}

SKILLS TO LEARN ({len(role['missing_skills'])})
---------------
{chr(10).join('○ ' + skill for skill in role['missing_skills']) if role['missing_skills'] else 'None'}

LEARNING PLAN
-------------
"""
    
    if role['missing_skills']:
        learning_plan = get_learning_plan(role)
        total_hours = 0
        for item in learning_plan:
            report += f"\nSkill: {item['skill']}\n"
            report += f"Resource: {item['youtube_link']}\n"
            report += f"Estimated Time: {item['estimated_hours']} hours\n"
            total_hours += item['estimated_hours']
        
        report += f"\nTotal Learning Time: {total_hours} hours ({total_hours//40} weeks)\n"
    
    report += f"""
CAREER PROGRESSION ROADMAP
--------------------------
{generate_career_roadmap(role)}

---
Generated by Career Compass AI
"""
    
    return report


# Main app logic
def main():
    """Main application controller"""
    if st.session_state.page == 'landing':
        landing_page()
    elif st.session_state.page == 'upload':
        upload_page()
    elif st.session_state.page == 'results':
        results_page()
    elif st.session_state.page == 'learning':
        learning_page()


if __name__ == "__main__":
    main()
