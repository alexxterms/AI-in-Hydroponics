from fpdf import FPDF

# Create a PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Top 10 Q1 Journals and Why They Rank High", ln=True, align="C")
        self.ln(10)

    def chapter_title(self, num, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, f"{num}. {title}", ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 10, body)
        self.ln()

# Content for each journal
journals_info = [
    ("CA: A Cancer Journal for Clinicians", 
     "Highest impact factor globally. Offers review-style articles on cancer that influence clinical practice and public health policy."),
    ("Nature Reviews Molecular Cell Biology", 
     "Publishes comprehensive reviews on molecular and cell biology. Widely cited for summarizing cutting-edge research."),
    ("New England Journal of Medicine (NEJM)", 
     "Premier clinical medicine journal publishing landmark clinical trials and medical research affecting global healthcare."),
    ("Cell", 
     "High-impact life sciences journal. Known for pioneering discoveries in genetics, neuroscience, and immunology."),
    ("Nature Medicine", 
     "Bridges biomedical research with clinical application. Focused on disease mechanisms and therapeutic developments."),
    ("Nature Reviews Materials", 
     "Leading reviews journal in materials science and nanotechnology. Synthesizes research in a fast-growing field."),
    ("Nature Reviews Cancer", 
     "Provides expert reviews on cancer biology and therapy. Influences research direction and clinical strategies."),
    ("Nature", 
     "Renowned multidisciplinary journal. Known for publishing groundbreaking research across all scientific disciplines."),
    ("Chemical Reviews", 
     "Essential for chemists. Publishes in-depth, highly cited reviews covering all areas of chemistry."),
    ("Nature Energy", 
     "Focuses on sustainable energy technologies and policy. Highly relevant due to global energy challenges."),
]

# Create PDF
pdf = PDF()
pdf.add_page()

for i, (title, content) in enumerate(journals_info, 1):
    pdf.chapter_title(i, title)
    pdf.chapter_body(content)

# Save PDF
pdf_path = "/home/ali/Documents/work.pdf"
pdf.output(pdf_path)
pdf_path
