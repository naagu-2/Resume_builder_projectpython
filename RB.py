import streamlit as st
from fpdf import FPDF

def generate_resume(name, email, phone, job_role, skills, experience, education):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="YOUR RESUME ", ln=True, align='C')
    pdf.ln(10)
    
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Phone: {phone}", ln=True)
    pdf.cell(200, 10, txt=f"Job Role: {job_role}", ln=True)
    
    pdf.ln(5)
    pdf.cell(200, 10, txt="Skills:", ln=True)
    for skill in skills:
        pdf.cell(200, 10, txt=f"- {skill}", ln=True)
    
    pdf.ln(5)
    pdf.cell(200, 10, txt="Experience:", ln=True)
    pdf.multi_cell(0, 10, experience)
    
    pdf.ln(5)
    pdf.cell(200, 10, txt="Education:", ln=True)
    pdf.multi_cell(0, 10, education)
    
    pdf_filename = "resume.pdf"
    pdf.output(pdf_filename)
    return pdf_filename

st.title("Build Your Resume:")

name = st.text_input("Enter Your Full Name")
email = st.text_input("Enter your Email")
phone = st.text_input("Enter your Phone Number")
job_role = st.text_input("Enter Job Role")
skills = st.text_area("Skills (comma separated)").split(',')
experience = st.text_area("Enter Work Experience")
education = st.text_area("Enter your Education")

if st.button("Generate Resume"):
    resume_file = generate_resume(name, email, phone, job_role, skills, experience, education)
    with open(resume_file, "rb") as file:
        st.download_button(label="Download Resume", data=file, file_name="Your final Resume.pdf", mime="application/pdf")
