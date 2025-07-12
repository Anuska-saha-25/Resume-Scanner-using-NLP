import fitz
import spacy
import re

nlp = spacy.load("en_core_web_sm")

SKILL_DB = ["Python", "Java", "C++", "Machine Learning", "SQL", "Data Analysis", "Excel", "AWS"]
EDU_KEYWORDS = ['B.Tech', 'Bachelor', 'B.Sc', 'M.Tech', 'Master', 'PhD', 'MBA']

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    return "\n".join([page.get_text() for page in doc])

def extract_name(doc):
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "Not Found"

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else "Not Found"

def extract_phone_number(text):
    phone_pattern = re.compile(r'(\+?\d[\d\s\-\(\)]{8,}\d)')
    match = phone_pattern.search(text)
    return match.group(0) if match else "Not Found"

def extract_skills(text):
    return [skill for skill in SKILL_DB if skill.lower() in text.lower()]

def extract_education(text):
    return [edu for edu in EDU_KEYWORDS if edu.lower() in text.lower()]

def extract_experience(text):
    keywords = ["experience", "worked at", "intern", "project", "role"]
    return [line.strip() for line in text.split('\n') if any(k in line.lower() for k in keywords)][:5]

def extract_resume_data(file_path):
    text = extract_text_from_pdf(file_path)
    doc = nlp(text)
    return {
        "Name": extract_name(doc),
        "Email": extract_email(text),
        "Phone": extract_phone_number(text),
        "Skills": extract_skills(text),
        "Education": extract_education(text),
        "Experience": extract_experience(text)
    }
