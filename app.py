"""
Streamlit UI: upload a resume (PDF/DOCX/TXT), see everything extracted from it
in a clean structured layout.

Run with:  streamlit run app.py
"""

import json
import tempfile
import os

import streamlit as st
from parser import parse_resume

st.set_page_config(page_title="Resume Extractor", page_icon="📄", layout="wide")

st.title("📄 Resume Detail Extractor")
st.caption(
    "Upload a resume (PDF, DOCX, or TXT) and this will extract the name, "
    "contact info, education, experience, skills, projects, and certifications. "
    "Works regardless of font, font size, or styling used in the resume."
)

uploaded_file = st.file_uploader("Upload a resume", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    suffix = "." + uploaded_file.name.split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    try:
        with st.spinner("Reading and extracting resume details..."):
            data = parse_resume(tmp_path)
    except Exception as e:
        st.error(f"Couldn't parse this file: {e}")
        st.stop()
    finally:
        os.unlink(tmp_path)

    st.success("Extraction complete.")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("👤 Basic Info")
        st.write(f"**Name:** {data['name'] or '_Not detected_'}")
        c = data["contact_info"]
        st.write(f"**Email:** {c['email'] or '_Not found_'}")
        st.write(f"**Phone:** {c['phone'] or '_Not found_'}")
        st.write(f"**LinkedIn:** {c['linkedin'] or '_Not found_'}")
        st.write(f"**GitHub:** {c['github'] or '_Not found_'}")

        if data["summary"]:
            st.subheader("📝 Summary")
            st.write(data["summary"])

        st.subheader("🎓 Education")
        if data["education"]:
            for edu in data["education"]:
                st.markdown(f"- {edu['raw']}")
                meta = []
                if edu["degree"]:
                    meta.append(f"Degree: {edu['degree']}")
                if edu["year"]:
                    meta.append(f"Year: {edu['year']}")
                if edu["cgpa"]:
                    meta.append(f"CGPA: {edu['cgpa']}")
                if edu["percentage"]:
                    meta.append(f"%: {edu['percentage']}")
                if meta:
                    st.caption(" | ".join(meta))
        else:
            st.write("_No education section detected_")

        st.subheader("🏆 Certifications")
        if data["certifications"]:
            for cert in data["certifications"]:
                st.markdown(f"- {cert}")
        else:
            st.write("_None detected_")

    with col2:
        st.subheader("💼 Experience")
        if data.get("total_experience"):
            st.info(f"**Total experience:** {data['total_experience']['human_readable']}")
        if data["experience"]:
            for exp in data["experience"]:
                st.markdown(f"**{exp['raw_header']}**")
                if exp["duration"]:
                    calc = exp.get("duration_calculated")
                    if calc:
                        st.caption(f"{exp['duration']}  →  **{calc['human_readable']}**")
                    else:
                        st.caption(exp["duration"])
                if exp["details"]:
                    for d in exp["details"]:
                        st.markdown(f"  - {d}")
                st.markdown("---")
        else:
            st.write("_No experience section detected_")

        st.subheader("🚀 Projects")
        if data["projects"]:
            for proj in data["projects"]:
                st.markdown(f"**{proj['title']}**")
                for d in proj["details"]:
                    st.markdown(f"  - {d}")
        else:
            st.write("_No projects section detected_")

        st.subheader("🛠️ Skills")
        if data["skills"]:
            for category, skills in data["skills"].items():
                st.markdown(f"**{category}:** {', '.join(skills)}")
        else:
            st.write("_No recognizable skills found_")

    with st.expander("🔍 View sections detected & raw structured JSON"):
        st.write("**Sections detected in this resume:**", data["sections_detected"])
        st.json(data)

    st.download_button(
        "⬇️ Download extracted data as JSON",
        data=json.dumps(data, indent=2),
        file_name=f"{uploaded_file.name.rsplit('.', 1)[0]}_extracted.json",
        mime="application/json",
    )
else:
    st.info("Upload a resume above to get started.")