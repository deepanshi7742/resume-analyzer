import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

SKILLS = ["python","java","sql","machine learning","html","css","javascript","flask","data analysis","communication"]

def clean_text(text):
    doc = nlp(text.lower())
    return " ".join([t.lemma_ for t in doc if not t.is_stop and t.is_alpha])

def get_similarity(a,b):
    v = TfidfVectorizer()
    vec = v.fit_transform([a,b])
    return round(cosine_similarity(vec[0],vec[1])[0][0]*100,2)

def extract_skills(text):
    return [s for s in SKILLS if s in text.lower()]


# 🔥 IMPORTANT FUNCTION (indentation correct)
def get_suggestions(missing_skills):
    suggestions = []

    if not missing_skills:
        return ["Great! Your resume matches the job description well."]

    for skill in missing_skills:
        suggestions.append(f"Add {skill} to your resume.")

    suggestions.append("Improve your resume by adding more relevant projects.")
    suggestions.append("Include measurable achievements (e.g., increased accuracy by 20%).")

    return suggestions