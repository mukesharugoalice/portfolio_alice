import streamlit as st

import os
from zipfile import ZipFile
st.title("My Portfolio")
# Section: Profile
with st.expander("Profile"):
    st.header("Profile")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("alice.jpg", caption="Alice Maire Mukesharugo", width=200)

    with col2:
        st.markdown("""
        **Name:** Alice Maire Mukesharugo  
        **Role:** Project Lead  
        **Background:**  
        Mukesharugo Alice is a dedicated and visionary leader with a strong background in entrepreneurial leadership. With her passion for empowering communities and developing innovative solutions, she has actively worked to bring transformative ideas to life. Alice thrives in creating sustainable business models, fostering teamwork, and leading initiatives that positively impact society.  

        **Contact Information:**  
        - **Email:** mignonnealoice@gmail.com 
        - **Phone:** +250 788 415 066  
        - **LinkedIn:** [linkedin.com/in/mukesharugoalice](https://www.linkedin.com/in/mukesharugoalice-marie-916758270/)  
        """)

# Section 1: Scoping
with st.expander("1. Project Scoping"):
    st.header("1. Problem Statement")
    st.subheader("Project Name: Mindlift – Elevating Mental Well-being for Entrepreneurship and Employment")
    
    st.markdown("""
    **Key Issues Identified:**
    1.I see too many young people in Rwanda struggling to find jobs. 21.5% of youth
        (16-30 years old) are unemployed because their skills don’t match what the job
        market needs, and competition is tough.
  

    2.I also see the mental health struggles they face. 27.4% of youth (14-25 years old)
        suffer from anxiety and depression, often made worse by the stress of unemployment.
 

    3. I know these problems are connected. When young people can’t find work, their
        mental health declines, and when they struggle mentally, it’s even harder to secure
        and keep a job

    4.I believe this creates a cycle of poverty and emotional distress. Without real solutions,
        many will remain trapped, unable to reach their full potential.
 
    5. I am committed to breaking this cycle. We must tackle both the skills gap and mental
        health barriers to create lasting opportunities for youth.
 
    """)

    st.header("Mission")
    st.markdown("""
    My Mission: I am dedicated to eradicating youth unemployment in Rwanda through a
        comprehensive approach that integrates tailored training, entrepreneurship support, and
        mental health services. My project Mindlift, directly tackles the root causes of unemployment
        by:

    **Why Act Now?**  
     Without intervention, this will: 
                
     • Push more youth into extreme poverty
     • Widen gender inequalities (women face double discrimination)  
     • Create long-term societal burdens from untreated mental health issues
                

    **Mindlift's Transformational Impact:**  
    Impact on My Mission:
                
    • I will Break the unemployment-mental health cycle by equipping youth with both skills
    and emotional resilience.
                
    • I will Increase job placements and business startups, directly reducing unemployment
    rates.
                
    • I will Create a healthier, more stable community where young people can thrive
        economically and emotionally 
                
    """)
with st.expander("2. Project Planning"):
    st.markdown("### Summary of Project Planning")
    st.markdown("""
### Summary of Document
 

The Mindlift Project aims to empower youth through skills training, mental health support,
and job placement, with goals including certifying 300 participants annually, improving
mental health outcomes, and securing jobs for 65% of graduates within six months. The
project also focuses on transforming employer practices and building community networks
through alumni chapters.
My Key project management tools will include WhatsApp for communication, Google Sheets
for tracking progress, and Kobo Toolbox for secure data collection. My team will comprise
roles like Project Lead, Training Coaches, and Peer Mentors, and it will be supported by a
budget of $15,000 covering salaries, equipment, and participant support.
 Fundings will come from grants, donations, corporate partnerships, and modest training
fees, ensuring sustainability while addressing youth unemployment and mental health barriers
systematically.
    """)
    
    try:
        with open("PLANNING.pdf", "rb") as file:
            project_plan_bytes = file.read()
            st.download_button(label="📄 Download PLANNING", data=project_plan_bytes, file_name="PLANNING.pdf", mime="application/pdf")
    except FileNotFoundError:
        st.error("🚨 Project Plan file not found. Please upload the file named 'PLANNING.pdf'.")

            # Section 3: Structuring
with st.expander("3. Project Structuring"):
    st.header("3. Project Structuring")
    st.markdown("#### 3. STRUCTURING")

    st.markdown("""
    ### Mindlift Project Timeline  

    **Phase 1: Preparation (Months 1-2)**  
    1. Finalize partnerships with 2 local NGOs  
    2. Secure 1 main training venue + backup location  
    3. Recruit first cohort of 100 participants  
    **Milestone:** 100 enrolled participants by end Month 2  

    **Phase 2: Core Training (Months 3-4)**  
    1. Launch vocational skills training program  
    2. Begin weekly mental health sessions  
    3. Conduct initial skills assessments  
    **Milestone:** 70% completion of core training by Month 4  

    **Phase 3: Advanced Support (Months 5-6)**  
    1. Start entrepreneurship workshops  
    2. Distribute seed grants to top 20 business plans  
    3. Organize employer networking events  
    **Milestone:** 30 business plans finalized by Month 6  

    **Phase 4: Transition (Month 7)**  
    1. Conduct final job placements  
    2. Complete alumni network setup  
    3. Hold graduation ceremony  
    **Milestone:** First 60 graduates employed by Month 7  

    ---

    ### Key Dependencies  
    - NGO partnerships must be secured before recruitment  
    - Venue availability affects training start date  
    - Seed funding must be approved before business grants  

    ---

    ### Potential Challenges  
    - Participant transportation issues  
    - Power/internet outages during digital training  
    - Employer participation in networking events  

    ---

    ### KPIs & Metrics  
    1. **Employment Rate**  
        Success Outcome: 60% of graduates employed within 6 months  

    2. **New Businesses Started**  
        Success Outcome: 30 youth-led businesses launched  

    3. **Training Completion**  
        Success Outcome: 75% earn certifications  

    4. **Skills Improvement**  
        Success Outcome: 90% show better skills in tests  

    5. **Mental Health Progress**  
        Success Outcome: 50% drop in anxiety/depression reports  

    6. **Job Retention**  
        Success Outcome: 80% keep jobs after 1 year  

    7. **Employer Actions**  
        Success Outcome: 20+ companies adopt mental-health-friendly hiring  

    **Indicators of Outcomes:**  
    - Hard Data: Job contracts, business licenses, test scores  
    - Surveys: Anonymous mental health questionnaires  
    - Employer Proof: Letters/comments about graduate performance  
    """)

    # Section 4: Coordination
with st.expander("4. Project Coordination"):
    st.header("4. Project Coordination")
    st.markdown("### Document Summary")
    st.markdown("""
### **Summary of the Mindlift Coordination Plan**  

The **Mindlift Coordination Plan** outlines a structured approach to team engagement, participant involvement, and stakeholder management to support youth development. Key strategies include **weekly team check-ins**, collaborative planning, and peer mentorship to ensure progress. Participants provide feedback through forums and anonymous channels, while stakeholders like employers and donors receive tailored updates via reports, infographics, and meetings. The plan emphasizes **inclusive decision-making**, conflict resolution, and transparency. Additionally, it addresses challenges such as **skills mismatch, mental health stigma, and job access** through employer partnerships, counseling rebranding, and internship guarantees. Solutions like startup grants, caregiver stipends, and bias-reduction initiatives further enhance program sustainability. Overall, Mindlift fosters a supportive ecosystem by aligning training with market needs, empowering youth, and maintaining strong stakeholder relationships.
    """)

    try:
        with open("COORDINATION.pdf", "rb") as file:
            project_plan_bytes = file.read()
            st.download_button(label="📄 Download COORDINATION", data=project_plan_bytes, file_name="COORDINATION.pdf", mime="application/pdf")
    except FileNotFoundError:
        st.error("🚨 Project Plan file not found. Please upload the file named 'COORDINATION.pdf'.")


with st.expander("5. Project Execution"):
    st.header("5. Project Execution")
    st.markdown("### Document Summary")
    st.markdown("""
The Mindlift Execution Plan details a structured 7-month implementation process across four phases: Setup & Recruitment (securing venues, partnerships, and baseline assessments), Core Training (vocational skills, mental health counseling, and employer engagement events), Job Linkages (internships, seed grants, and mock interviews), and Transition (alumni tracking and graduation). Progress is tracked daily via attendance sheets and WhatsApp, weekly through mental health check-ins and employer SMS surveys, and monthly via visual dashboards. Success is measured by quantitative metrics (e.g., 60% job placement rate, 50% symptom reduction) and qualitative indicators (participant testimonials, employer feedback). Tools like Google Sheets and SMS ensure real-time monitoring, while contingencies like rural outreach and trial placements address challenges. The plan emphasizes community ownership, parallel skill/mental health support, and adaptive strategies to ensure sustainable outcomes.
    """)

    st.markdown("### Download Execution Document")
    try:
        with open("EXECUTION.pdf", "rb") as file:
            execution_plan_bytes = file.read()
            st.download_button(label="📄 Download Execution Document", data=execution_plan_bytes, file_name="EXECUTION.pdf", mime="application/pdf")
    except FileNotFoundError:
        st.error("🚨 Execution Document file not found. Please upload the file named 'EXECUTION.pdf'.")


    # Section 6: Trade-off Management
with st.expander("6. Trade-off Management"):
    st.header("6. Trade-off Management")
    
    st.markdown("### **Trade-off Management for Mindlift Project**")

    st.markdown("""
    #### **1. Possible Trade-offs in the Project**  
    In implementing Mindlift, several trade-offs must be considered due to resource constraints, time limitations, and competing priorities:  

    - **Quality vs. Scale**  
        - *Option A:* High-quality, intensive training for a smaller group (e.g., 100 participants with deep mentorship).  
        - *Option B:* Broader reach with lighter touch (e.g., 300 participants with basic training but less individual support).  

    - **Short-term Employment vs. Long-term Entrepreneurship**  
        - *Option A:* Focus on immediate job placements (vocational training for existing jobs).  
        - *Option B:* Prioritize entrepreneurship (business training, seed grants, but fewer quick job placements).  

    - **Mental Health Support vs. Skills Training Intensity**  
        - *Option A:* More counseling sessions (stronger mental health impact but fewer training hours).  
        - *Option B:* More skills training (better employability but potentially weaker mental health progress).  

    - **Cost Efficiency vs. Participant Accessibility**  
        - *Option A:* Centralized training (lower costs but excludes rural youth with transportation challenges).  
        - *Option B:* Decentralized training (higher reach but more expensive due to multiple venues).  
    """)

    st.markdown("""
    #### **2. Chosen Trade-offs & Justifications**  

    | **Trade-off**                | **Chosen Approach** | **Why?** |
    |------------------------------|---------------------|----------|
    | **Quality over Scale**        | Smaller cohorts (100) with deep support | Ensures higher success rates (certifications, job placements) and stronger mental health impact. |
    | **Balanced Employment & Entrepreneurship** | 60% job-focused, 40% entrepreneurship | Immediate income (jobs) stabilizes participants, while entrepreneurship creates long-term opportunities. |
    | **Moderate Mental Health Integration** | Weekly (not daily) counseling + resilience training | Ensures mental health is addressed without sacrificing critical skills training time. |
    | **Semi-Decentralized Model** | Main urban hub + select rural outreach | Balances cost and accessibility; urban focus first (higher employer connections), then expands. |
    """)

    st.markdown("""
    #### **3. Deep Analysis of How Trade-offs Support Success**  

    - **Quality over Scale** → Ensures measurable impact (75% certification rate, 60% employment) rather than superficial reach. High completion rates attract more partners/funders.  
    - **Balanced Job-Entrepreneurship Focus** → Mitigates risk: if job market weakens, entrepreneurship provides alternatives. Also aligns with Rwanda’s push for SME growth.  
    - **Moderate Mental Health Integration** → Avoids overwhelming participants with therapy at the cost of skills, but still achieves the **50% anxiety/depression reduction** target.  
    - **Semi-Decentralized Model** → Urban focus maximizes employer partnerships early (critical for job placements), while rural pilots test scalability for Phase 2.  

""")
# Footer and export option
st.markdown("---")
st.subheader("Export Options")
if st.button("Download Project Portfolio"):
    # Create a folder to store all files and texts
    folder_name = "Mindlift_Project_Portfolio"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Save all text content into a single file
    text_content = """
    Mission Project Portfolio
    -------------------------
    By MUKESHARUGO Alice Maire

    1. Project Scoping
    ------------------
    Project Name: Mindlift – Elevating Mental Well-being for Entrepreneurship and Employment

    Mission Statement:
    To eradicate youth unemployment in Rwanda by integrating skills training, entrepreneurship support, and mental health services.

    Problem Statement:
    In Rwanda, 21.5% of youth are unemployed, primarily due to a mismatch between their skills and labor market demands...

    (Include all other sections' text content here)
    """
    with open(f"{folder_name}/Project_Portfolio.txt", "w") as text_file:
        text_file.write(text_content)

    # Include PDF files if they exist
    pdf_files = ["PLANNING.pdf", "COORDINATION.pdf", "EXECUTION.pdf"]
    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            with open(pdf_file, "rb") as source_file:
                with open(f"{folder_name}/{pdf_file}", "wb") as dest_file:
                    dest_file.write(source_file.read())

    # Create a ZIP file containing the folder
    zip_file_name = f"{folder_name}.zip"
    with ZipFile(zip_file_name, "w") as zipf:
        for root, dirs, files in os.walk(folder_name):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_name))

    # Provide the ZIP file for download
    with open(zip_file_name, "rb") as zip_file:
        st.download_button(
            label="📦 Download Project Portfolio",
            data=zip_file,
            file_name=zip_file_name,
            mime="application/zip"
        )