from flask import Flask, render_template, request
from PyPDF2 import PdfReader
from resume_model import clean_text, get_similarity, extract_skills, get_suggestions

app = Flask(__name__)

def extract_text(file):
    try:
        pdf = PdfReader(file)
        text=""
        for p in pdf.pages:
            if p.extract_text():
                text+=p.extract_text()
        return text
    except:
        return "Invalid PDF"

@app.route("/", methods=["GET","POST"])
def home():
    score=None
    missing=[]
    suggestions=[]   # 👉 yaha add hua

    if request.method=="POST":
        file=request.files["resume"]
        jd=request.form["jd"]

        r_text = extract_text(file)

        if r_text == "Invalid PDF":
            return "❌ Please upload a valid PDF"

        r=clean_text(r_text)
        j=clean_text(jd)

        score=get_similarity(r,j)
        missing=list(set(extract_skills(jd))-set(extract_skills(r)))

        suggestions = get_suggestions(missing)
        print("Missing:", missing)
        print("Suggestions:", suggestions)  # 👉 yaha add hua

    return render_template(
        "index.html",
        score=score,
        missing_skills=missing,
        suggestions=suggestions   # 👉 yaha add hua
    )

app.run(debug=True)