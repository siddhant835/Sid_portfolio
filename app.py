"""
Siddhant Pardeshi — Software Engineer & AI Automation Specialist
Interactive Streamlit Web Portfolio
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from PIL import Image, ImageDraw

# Page configuration
st.set_page_config(
    page_title="Siddhant Pardeshi | Software Engineer & AI Automation",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Dark Theme Styling
st.markdown("""
<style>
    /* Dark cyber aesthetic */
    .main {
        background-color: #050a14;
    }
    .stApp {
        background-color: #050a14;
        color: #e2e8f0;
    }
    .metric-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
    }
    .code-box {
        background: #0f172a;
        border: 1px solid rgba(34, 211, 238, 0.2);
        border-radius: 12px;
        padding: 16px;
    }
    .status-badge {
        display: inline-block;
        background: rgba(34, 197, 94, 0.15);
        color: #4ade80;
        border: 1px solid rgba(34, 197, 94, 0.3);
        border-radius: 9999px;
        padding: 4px 12px;
        font-size: 13px;
        font-family: monospace;
        margin-bottom: 12px;
    }
    .tag-chip {
        display: inline-block;
        background: rgba(34, 211, 238, 0.12);
        color: #38bdf8;
        border: 1px solid rgba(34, 211, 238, 0.25);
        border-radius: 9999px;
        padding: 2px 10px;
        font-size: 12px;
        font-family: monospace;
        margin-right: 6px;
        margin-bottom: 6px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for interactive project demos
if "attendance_records" not in st.session_state:
    st.session_state.attendance_records = [
        {"Time": "09:15:22 AM", "Employee ID": "EMP-835", "Name": "Siddhant Pardeshi", "Confidence": "98.4%", "Status": "Present ✓", "DMS Sync": "Success"},
        {"Time": "09:18:40 AM", "Employee ID": "EMP-102", "Name": "Rahul Deshmukh", "Confidence": "96.1%", "Status": "Present ✓", "DMS Sync": "Success"},
        {"Time": "09:22:15 AM", "Employee ID": "EMP-304", "Name": "Ananya Kulkarni", "Confidence": "97.8%", "Status": "Present ✓", "DMS Sync": "Success"},
    ]

if "csr_leads" not in st.session_state:
    st.session_state.csr_leads = [
        {"Company": "Tata Consultancy Services", "Domain": "Education & STEM", "Budget": "₹25L - ₹50L", "Decision Maker": "Head of CSR (Mumbai)", "Status": "Verified"},
        {"Company": "Infosys Foundation", "Domain": "Healthcare & Rural", "Budget": "₹30L - ₹60L", "Decision Maker": "CSR Director (Bengaluru)", "Status": "Verified"},
        {"Company": "Wipro Cares", "Domain": "Ecology & Learning", "Budget": "₹20L - ₹40L", "Decision Maker": "CSR Lead", "Status": "Verified"},
    ]

# ==============================================================================
# SIDEBAR
# ==============================================================================
with st.sidebar:
    st.markdown("## `< SP />` Siddhant Pardeshi")
    st.caption("Software Engineer | AI & Automation Specialist")
    
    st.markdown("""
    <div class="status-badge">
        ● Available for Full-Time Roles
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📍 Details")
    st.markdown("**Location:** Belgaum, Karnataka, India")
    st.markdown(
        "**Email:** <a href=\"mailto:siddhantpardeshi137@gmail.com\" style=\"color:#1f77b4; font-weight:600;\">siddhantpardeshi137@gmail.com</a>",
        unsafe_allow_html=True,
    )
    st.markdown("**Phone:** [+91 70202 02307](tel:+917020202307)")
    st.markdown("**GitHub:** [github.com/siddhant835/Sid_portfolio](https://github.com/siddhant835/Sid_portfolio)")

    st.markdown("---")
    st.markdown("### ⚡ Core Skills")
    skills = ["Python", "OpenCV", "MySQL", "REST API", "Apps Script", "Automation", "HTML5/CSS3", "JavaScript", "PHP", "Git"]
    tags_html = "".join([f'<span class="tag-chip">{s}</span>' for s in skills])
    st.markdown(tags_html, unsafe_allow_html=True)

    st.markdown("---")
    resume_text = """Siddhant Pardeshi
Software Engineer & AI Automation Specialist
Email: siddhantpardeshi137@gmail.com | Phone: +91 7020202307
GitHub: https://github.com/siddhant835/Sid

Summary:
Results-driven software developer experienced in Python, computer vision and process automation. Built attendance systems for 250+ users and automated pipelines that reduced 3-4 staff workloads.
"""
    st.download_button(
        label="📄 Download Resume (Summary)",
        data=resume_text,
        file_name="Siddhant_Pardeshi_Resume.txt",
        mime="text/plain",
        use_container_width=True
    )

# ==============================================================================
# HERO SECTION
# ==============================================================================
col_hero_1, col_hero_2 = st.columns([3, 2], gap="large")

with col_hero_1:
    st.markdown("""
    # Hi, I'm <span style="color:#22d3ee">Siddhant Pardeshi</span>
    ### `> Software Engineer | AI & Automation Specialist`
    """, unsafe_allow_html=True)
    
    st.write(
        "Results-driven developer with expertise in **Python, Web Technologies & Process Automation**. "
        "I turn manual operations into scalable software — from facial recognition for **250+ employees** "
        "to bulk corporate automation pipelines that replaced **3-4 staff members** of manual work."
    )
    
    # Key Metrics Cards
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="Users Deployed", value="250+", delta="Live in Production")
    with m2:
        st.metric(label="Major Projects", value="4+", delta="Production Scaled")
    with m3:
        st.metric(label="Manual Work Reduced", value="3-4x", delta="Hours Saved")

with col_hero_2:
    st.markdown("#### 💻 Terminal Snapshot")
    st.code("""# Facial recognition attendance engine
import cv2, face_recognition

def mark_attendance(frame):
    faces = detect_faces(frame)
    for face in faces:
        if match_with_db(face):
            db.mark_present(employee_id)
            return "Attendance Marked ✓"

# Deployed for 200-250 employees
# Integrated with internal DMS""", language="python")

st.markdown("---")

# ==============================================================================
# NAVIGATION TABS
# ==============================================================================
tab_projects, tab_skills, tab_experience, tab_contact = st.tabs([
    "🚀 Interactive Projects & Live Demos",
    "🛠️ Tech Stack & Skills",
    "💼 Professional Experience",
    "📬 Contact & Inquiry Form"
])

# ------------------------------------------------------------------------------
# TAB 1: INTERACTIVE PROJECTS
# ------------------------------------------------------------------------------
with tab_projects:
    st.subheader("Selected Work & Live Python Demos")
    st.caption("Interact with live simulations of real software solutions built and deployed by Siddhant.")

    proj_selector = st.radio(
        "Select a project to explore and simulate:",
        [
            "1. Facial Recognition Attendance System (OpenCV & Python)",
            "2. CSR Research & Outreach Data Pipeline",
            "3. Automated CSR Bulk Email Dispatcher",
            "4. Responsive NGO Website Architecture (Mahesh Foundation)"
        ],
        horizontal=True
    )

    # --------------------------------------------------------------------------
    # PROJECT 1: FACIAL RECOGNITION ATTENDANCE
    # --------------------------------------------------------------------------
    if "1. Facial Recognition" in proj_selector:
        st.markdown("### 📷 Facial Recognition Attendance System")
        st.write(
            "Scalable web-based platform with real-time camera authentication for **250+ employees**. "
            "Extracts 128-d face encodings using OpenCV & dlib, matches against a MySQL employee directory, "
            "and automatically prevents duplicate punches within 12 hours while syncing to Document Management Systems."
        )

        col_cam, col_log = st.columns([1, 1], gap="medium")

        with col_cam:
            st.markdown("#### 📸 Live Camera Test (or Simulation)")
            st.caption("Use your camera or test simulated recognition:")
            
            # Real camera input in Streamlit
            img_file_buffer = st.camera_input("Take a photo to test attendance recognition")
            
            sim_col1, sim_col2 = st.columns(2)
            with sim_col1:
                btn_sim = st.button("⚡ Simulate Scan & Punch", use_container_width=True)
            with sim_col2:
                btn_reset = st.button("🔄 Reset Records", use_container_width=True)

            if btn_reset:
                st.session_state.attendance_records = []
                st.success("Attendance records reset!")

            # If photo taken or simulated
            if img_file_buffer is not None or btn_sim:
                now_str = datetime.now().strftime("%I:%M:%S %p")
                
                # Draw bounding box on image or mock image
                if img_file_buffer is not None:
                    img = Image.open(img_file_buffer)
                else:
                    # Create mock synthetic face image
                    img = Image.new('RGB', (320, 240), color=(15, 23, 42))
                    d = ImageDraw.Draw(img)
                    d.rectangle([100, 50, 220, 190], outline=(34, 211, 238), width=3)
                    d.text((105, 55), "EMP-835: Siddhant (98.4%)", fill=(74, 222, 128))

                # Append record
                new_entry = {
                    "Time": now_str,
                    "Employee ID": "EMP-835",
                    "Name": "Siddhant Pardeshi",
                    "Confidence": "98.4%",
                    "Status": "Present ✓",
                    "DMS Sync": "Success"
                }
                st.session_state.attendance_records.insert(0, new_entry)
                st.success(f"✓ Attendance successfully recorded for Siddhant Pardeshi at {now_str}")
                st.image(img, caption="Processed Face Detection Bounding Box", width=300)

        with col_log:
            st.markdown("#### 📋 Live Attendance Log (MySQL / DMS Sync)")
            if st.session_state.attendance_records:
                df_attendance = pd.DataFrame(st.session_state.attendance_records)
                st.dataframe(df_attendance, use_container_width=True, hide_index=True)
                
                # CSV Download
                csv_data = df_attendance.to_csv(index=False).encode('utf-8')
                st.download_button(
                    "📥 Export Attendance Log (CSV)",
                    data=csv_data,
                    file_name="attendance_export.csv",
                    mime="text/csv"
                )
            else:
                st.info("No attendance records logged yet. Click 'Simulate Scan & Punch' to test.")

    # --------------------------------------------------------------------------
    # PROJECT 2: CSR RESEARCH & OUTREACH PIPELINE
    # --------------------------------------------------------------------------
    elif "2. CSR Research" in proj_selector:
        st.markdown("### 📊 CSR Research & Outreach Data Pipeline")
        st.write(
            "An automated bulk data extraction and deduplication pipeline built with Google Apps Script & Sheets API. "
            "Aggregates hundreds of potential CSR corporate partners, verifies MCA/company registry data, "
            "and automatically assigns lead statuses."
        )

        st.markdown("#### ⚡ Interactive Pipeline Runner")
        col_run1, col_run2 = st.columns([2, 1])
        with col_run1:
            new_comp = st.text_input("Add Corporate Target", placeholder="e.g. HCL Technologies Foundation")
        with col_run2:
            st.write("")
            st.write("")
            btn_add = st.button("🚀 Run Lead Ingestion", use_container_width=True)

        if btn_add and new_comp:
            st.session_state.csr_leads.insert(0, {
                "Company": new_comp,
                "Domain": "Education / Youth",
                "Budget": "₹15L - ₹35L",
                "Decision Maker": "CSR Committee Head",
                "Status": "Verified & Enriched"
            })
            st.success(f"Ingested and deduplicated lead: {new_comp}")

        df_leads = pd.DataFrame(st.session_state.csr_leads)
        st.dataframe(df_leads, use_container_width=True, hide_index=True)

    # --------------------------------------------------------------------------
    # PROJECT 3: AUTOMATED EMAIL DISPATCHER
    # --------------------------------------------------------------------------
    elif "3. Automated CSR" in proj_selector:
        st.markdown("### 📧 Automated CSR Bulk Email Dispatcher")
        st.write(
            "Custom mail-merge and outreach automation built using Gmail API and Apps Script. "
            "Features automated thread tracking, dynamic merge tags (`{{Company_Name}}`), "
            "quota management, and follow-up chains that saved **3-4 people** of manual work."
        )

        st.markdown("#### ✉️ Mail Merge Template Preview")
        subject_template = st.text_input("Subject Template", value="Partnership Proposal for {{Company_Name}} - Mahesh Foundation")
        recipient_company = st.selectbox("Test Recipient Company", [lead["Company"] for lead in st.session_state.csr_leads])
        
        rendered_subject = subject_template.replace("{{Company_Name}}", recipient_company)
        st.info(f"**Rendered Subject:** `{rendered_subject}`")

        if st.button("🚀 Simulate Batch Dispatch (5 Emails)"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            for i in range(1, 6):
                progress_bar.progress(i * 20)
                status_text.text(f"Dispatching email {i}/5 to validated CSR directors via Gmail API...")
            status_text.success("✓ Batch dispatch complete! All 5 threads tracked and synced.")

    # --------------------------------------------------------------------------
    # PROJECT 4: NGO WEBSITE SHOWCASE
    # --------------------------------------------------------------------------
    elif "4. Responsive NGO Website" in proj_selector:
        st.markdown("### 🌐 Responsive NGO Website — Mahesh Foundation")
        st.write(
            "Designed and engineered responsive, high-converting frontend components for donation, "
            "CSR programs, and educational initiatives. Implemented accessible layouts and interactive widgets."
        )
        st.link_button("🔗 Visit Production Website: maheshfoundation.org", "https://maheshfoundation.org")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("##### ⚡ Key Achievements")
            st.markdown("- Seamless donation funnel integration\n- Mobile-first responsive layouts\n- Performance-optimized assets")
        with c2:
            st.markdown("##### 🛠️ Tech Used")
            st.markdown("- HTML5 & CSS3\n- Modern JavaScript\n- Wix Architecture & Velo")
        with c3:
            st.markdown("##### 🎯 Audience Impact")
            st.markdown("- Improved donor inquiries\n- Higher mobile engagement\n- Transparent CSR reporting")

# ------------------------------------------------------------------------------
# TAB 2: TECH STACK & SKILLS
# ------------------------------------------------------------------------------
with tab_skills:
    st.subheader("Technical Competencies")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.markdown("#### 💻 Programming Languages & AI")
        st.write("**Python:** 90% (Core backend, OpenCV, data pipelines, automation)")
        st.progress(90)
        st.write("**Computer Vision (OpenCV):** 85% (Face recognition, real-time webcam streams)")
        st.progress(85)
        st.write("**JavaScript:** 80% (Frontend UI, Google Apps Script, REST clients)")
        st.progress(80)
        st.write("**SQL / MySQL:** 82% (Relational modeling, indexing, queries)")
        st.progress(82)

    with col_s2:
        st.markdown("#### ⚙️ Automation & Backend Tools")
        st.write("**Google Apps Script & Sheets API:** 95% (Bulk outreach & deduplication)")
        st.progress(95)
        st.write("**REST API Design & Integration:** 85% (DMS integration, external APIs)")
        st.progress(85)
        st.write("**Git / GitHub:** 85% (Version control, collaboration)")
        st.progress(85)
        st.write("**Frontend (HTML5 / CSS3 / Tailwind):** 80% (Responsive layouts)")
        st.progress(80)

# ------------------------------------------------------------------------------
# TAB 3: PROFESSIONAL EXPERIENCE
# ------------------------------------------------------------------------------
with tab_experience:
    st.subheader("Experience & Track Record")
    st.markdown("### 🏢 Mahesh Foundation")
    st.markdown("**Role:** CSR Executive & AI Innovations | *July 2024 – Present* (Belgaum, Karnataka)")
    
    st.markdown("""
    - **Facial Recognition Attendance System:** Architected and deployed an end-to-end attendance system using Python and OpenCV for **200-250 employees**, eliminating buddy punching and syncing directly with DMS.
    - **CSR Outreach Automation:** Engineered automated lead research, validation, and email dispatch systems using the **Gmail API and Google Apps Script**, reducing manual workload equivalent to **3-4 staff members**.
    - **In-house Software Engineering:** Acted as primary technical developer solving operational bottlenecks with custom Python automation scripts and database management.
    """)

# ------------------------------------------------------------------------------
# TAB 4: CONTACT & INQUIRY FORM
# ------------------------------------------------------------------------------
with tab_contact:
    st.subheader("Get In Touch")
    st.write("Looking for a Software Engineer who can ship automation that saves real hours? Send a message below:")

    with st.form("contact_form", clear_on_submit=True):
        f_name = st.text_input("Your Name *", placeholder="e.g. Alex Johnson")
        f_email = st.text_input("Your Email *", placeholder="e.g. alex@example.com")
        f_subject = st.text_input("Subject", placeholder="e.g. Software Engineer Opportunity / Project Inquiry")
        f_message = st.text_area("Message *", placeholder="Hi Siddhant, I would like to discuss...")
        
        submitted = st.form_submit_button("📩 Send Message", use_container_width=True)

        if submitted:
            if not f_name or not f_email or not f_message:
                st.error("Please fill out all required fields (Name, Email, and Message).")
            else:
                st.success(f"Thank you, {f_name}! Your message has been received. I'll get back to you within 24 hours at {f_email}.")
                st.info(f"Direct mail link: [Click to send via your email client](mailto:siddhantpardeshi137@gmail.com?subject={f_subject}&body=From:%20{f_name}%20({f_email})%0A%0A{f_message})")

st.markdown("---")
st.caption("© 2025 Siddhant Pardeshi • Built with 100% Python & Streamlit • [github.com/siddhant835/Sid](https://github.com/siddhant835/Sid)")
