from app.utils.skill_dictionary import SKILLS

def extract_skills(jd_text: str):
    jd_text_lower = jd_text.lower()
    found = [skill for skill in SKILLS if skill in jd_text_lower]
    return list(set(found))

def detect_role(jd_text: str):
    jd = jd_text.lower()

    roles = [
        "data analyst",
        "data scientist",
        "machine learning engineer",
        "software engineer",
        "frontend developer",
        "backend developer",
        "full stack developer"
    ]

    for role in roles:
        if role in jd:
            return role.title()

    return "Unknown"

def analyze_jd(jd_text: str):
    return {
        "role": detect_role(jd_text),
        "skills": extract_skills(jd_text)
    }