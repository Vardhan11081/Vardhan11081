from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

# Title
title = doc.add_heading('BN324 Enterprise Cyber Security and Management', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

subtitle = doc.add_heading('Week 5 Workshop/Laboratory – Information Security Governance', level=1)
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph()

# ── MODULE 1 ──────────────────────────────────────────────────────────────────
doc.add_heading('Module 1: Foundations of Information Security Governance', level=1)
doc.add_heading('Activity 1: Governance vs. Management', level=2)

doc.add_paragraph(
    'Each statement is classified below with a brief explanation based on '
    'ISO 27001, NIST CSF, and COBIT 2019.'
)

act1_table = doc.add_table(rows=6, cols=2)
act1_table.style = 'Table Grid'

# Header row
hdr = act1_table.rows[0].cells
hdr[0].text = 'Statement'
hdr[1].text = 'Answer (Governance or Management?)'
for cell in hdr:
    for para in cell.paragraphs:
        run = para.runs[0] if para.runs else para.add_run(cell.text)
        run.bold = True

rows_data = [
    (
        '1. Approves the enterprise information security policy',
        'Governance – This is a board/executive-level decision that sets the direction '
        'and authorises the overall security posture of the organisation '
        '(ISO 27001 Clause 5.1; COBIT EDM01).'
    ),
    (
        '2. Implements firewall rules',
        'Management – This is a day-to-day operational/technical activity carried out '
        'by IT/security staff to enforce security controls '
        '(NIST CSF – Protect; ISO 27001 Annex A.13).'
    ),
    (
        '3. Defines risk appetite',
        'Governance – Setting the risk appetite is a strategic governance responsibility '
        'of senior leadership that guides all risk-related decisions '
        '(ISO 27001 Clause 6.1; COBIT EDM03).'
    ),
    (
        '4. Conducts vulnerability scanning',
        'Management – This is an operational security task performed by the security '
        'team to identify technical weaknesses '
        '(NIST CSF – Identify/Detect; ISO 27001 Annex A.12.6).'
    ),
    (
        '5. Monitors compliance with security KPIs',
        'Governance – Monitoring KPIs against policy objectives is an oversight '
        'function that provides assurance to leadership '
        '(ISO 27001 Clause 9.1; COBIT MEA01; NIST CSF – Detect).'
    ),
]

for i, (stmt, ans) in enumerate(rows_data, start=1):
    row = act1_table.rows[i].cells
    row[0].text = stmt
    row[1].text = ans

doc.add_paragraph()

# ── MODULE 2 ──────────────────────────────────────────────────────────────────
doc.add_heading('Module 2: Governance Frameworks', level=1)
doc.add_heading('Activity 2: Framework Mapping', level=2)

doc.add_paragraph(
    'Each governance activity is mapped to the most relevant component '
    'of ISO 27001, NIST CSF, and COBIT 2019.'
)

act2_table = doc.add_table(rows=5, cols=4)
act2_table.style = 'Table Grid'

hdr2 = act2_table.rows[0].cells
headers = ['Governance Activity', 'ISO 27001', 'NIST CSF', 'COBIT 2019']
for cell, text in zip(hdr2, headers):
    cell.text = text
    for para in cell.paragraphs:
        for run in para.runs:
            run.bold = True

act2_data = [
    (
        'Define security roles and responsibilities',
        'Clause 5.3 & Annex A.6.1 – Organisational roles, responsibilities and authorities',
        'Identify – Governance (ID.GV): Organisational cybersecurity policies and roles are established',
        'EDM01 – Ensure Governance Framework Setting and Maintenance'
    ),
    (
        'Conduct risk assessment',
        'Clause 6.1.2 – Information security risk assessment',
        'Identify – Risk Assessment (ID.RA): Asset vulnerabilities, threats and risk responses identified',
        'APO12 – Manage Risk'
    ),
    (
        'Monitor security performance',
        'Clause 9.1 – Monitoring, measurement, analysis and evaluation',
        'Detect – Security Continuous Monitoring (DE.CM): Networks and assets are monitored',
        'MEA01 – Monitor, Evaluate and Assess Performance and Conformance'
    ),
    (
        'Develop incident response plan',
        'Annex A.16.1 – Management of information security incidents',
        'Respond – Response Planning (RS.RP): Response processes and procedures are executed',
        'DSS02 – Manage Service Requests and Incidents'
    ),
]

for i, row_data in enumerate(act2_data, start=1):
    row = act2_table.rows[i].cells
    for cell, text in zip(row, row_data):
        cell.text = text

doc.add_paragraph()

# ── References ────────────────────────────────────────────────────────────────
doc.add_heading('References', level=2)
refs = [
    'ISO/IEC 27001:2022 – Information Security Management Systems Requirements.',
    'NIST Cybersecurity Framework v1.1 (2018), National Institute of Standards and Technology.',
    'ISACA, COBIT 2019 Framework: Governance and Management Objectives.',
]
for ref in refs:
    p = doc.add_paragraph(ref, style='List Bullet')

doc.save('/workspace/lab 5.docx')
print("lab 5.docx created successfully")
