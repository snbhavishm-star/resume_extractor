# Resume Detail Extractor

Upload a resume (PDF, DOCX, or TXT) and it extracts, in structured form:

- Name, email, phone, LinkedIn, GitHub
- Summary/objective
- Education (degree, institution, year, CGPA/%)
- Experience (role, company, duration, bullet points)
- Projects
- Skills (auto-categorized: languages, AI/ML, cloud, databases, etc.)
- Certifications & achievements

**Font size doesn't matter.** Text is pulled from the PDF/DOCX at the
character level using `pdfplumber` / `python-docx`, not by reading pixels —
so a resume in 8pt or 24pt font extracts identically. What *does* matter is
having clear section headers (e.g. "Education", "Experience", "Skills") —
the parser looks for those to segment the document.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

### Option 1 — Web UI (recommended)
```bash
streamlit run app.py
```
Opens a browser page where you drag-and-drop a resume and see everything
extracted, plus a JSON download button.

### Option 2 — Command line
```bash
python parser.py path/to/resume.pdf
```
Prints the extracted structured data as JSON.

### Option 3 — Use as a library
```python
from parser import parse_resume

data = parse_resume("resume.pdf")
print(data["skills"])
print(data["education"])
```

## How it works

1. **Text extraction** — `pdfplumber` (PDF) or `python-docx` (DOCX) pulls
   raw text + table content, independent of font/styling.
2. **Section segmentation** — scans for known headers (Education,
   Experience, Skills, Projects, Certifications, Summary, Achievements)
   and splits the document accordingly.
3. **Field extraction** — regex for email/phone/links/dates/CGPA, a
   150+ term skills dictionary (`skills_db.py`) for skill detection
   organized by category, and heuristics for degree/job-block parsing.
4. **Output** — a single structured dict/JSON with every category above,
   plus `sections_detected` telling you exactly what the resume did and
   didn't contain.

## Extending it

- Add more skills to `SKILLS_DB` in `skills_db.py` (grouped by category).
- Add more section header synonyms to `SECTION_HEADERS` if a resume uses
  unusual headings (e.g. "Relevant Coursework" instead of "Education").
- For scanned/image-only PDFs (no selectable text), you'd need OCR
  (e.g. `pytesseract`) as a preprocessing step — not included here since
  most resumes are text-based PDFs or DOCX.
#echo resume_extractor
