from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# ── Title ─────────────────────────────────────────────────────────────────────
t = doc.add_heading('BN324 Enterprise Cyber Security and Management', 0)
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
s = doc.add_heading('Week 9 Laboratory – Information Security Governance Part B', level=1)
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# MODULE 1
# ══════════════════════════════════════════════════════════════════════════════
doc.add_heading('Module 1: Asset Identification & Classification', level=1)
doc.add_heading('Activity 3: Classify Information Assets', level=2)

doc.add_paragraph(
    'The following assets are classified using a three-tier model '
    '(Public / Internal / Confidential) based on sensitivity, '
    'business impact if disclosed, and ISO 27001 Annex A.8 asset management principles.'
)

# Classification table
tbl = doc.add_table(rows=5, cols=3)
tbl.style = 'Table Grid'

headers = ['Asset', 'Classification', 'Justification']
for i, h in enumerate(headers):
    cell = tbl.rows[0].cells[i]
    cell.text = h
    for run in cell.paragraphs[0].runs:
        run.bold = True

rows_data = [
    (
        'Marketing brochure',
        'PUBLIC',
        'Intentionally created for external audiences; disclosure causes no harm. '
        'No access restrictions required.'
    ),
    (
        'Customer database',
        'CONFIDENTIAL',
        'Contains personal information protected under the Privacy Act 1988 and the NDB scheme. '
        'Unauthorised disclosure risks regulatory penalties, reputational damage, and harm to individuals.'
    ),
    (
        'Internal HR procedures',
        'INTERNAL',
        'For employee use only; not intended for public release but not highly sensitive. '
        'Disclosure outside the organisation could embarrass the business or enable policy exploitation.'
    ),
    (
        'Proprietary source code',
        'CONFIDENTIAL',
        'Core intellectual property that provides competitive advantage. '
        'Disclosure could enable competitors to replicate products or attackers to find vulnerabilities.'
    ),
]

for i, (asset, cls, just) in enumerate(rows_data, start=1):
    row = tbl.rows[i].cells
    row[0].text = asset
    row[1].text = cls
    # Bold the classification tier
    for para in row[1].paragraphs:
        for run in para.runs:
            run.bold = True
    row[2].text = just

doc.add_paragraph()

# Classification tier explanation
doc.add_heading('Classification Tier Definitions', level=3)
tiers = [
    ('Public', 'Information approved for unrestricted external distribution. Loss or '
     'disclosure has no significant business impact.'),
    ('Internal', 'Information for internal use only. Not harmful if disclosed but should '
     'not be shared outside the organisation without approval.'),
    ('Confidential', 'Sensitive information whose unauthorised disclosure could cause significant '
     'harm — legal, financial, reputational, or competitive. Requires strict access controls, '
     'encryption, and audit logging.'),
]
for tier, defn in tiers:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(tier + ': ')
    run.bold = True
    p.add_run(defn)

doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# MODULE 2
# ══════════════════════════════════════════════════════════════════════════════
doc.add_heading('Module 2: Risk Assessment', level=1)
doc.add_heading('Activity 4: Risk Scenario Analysis', level=2)

doc.add_paragraph(
    'Scenario: A company stores customer data in a cloud CRM. '
    'Multi-factor authentication (MFA) is not enabled. '
    'A phishing attack could compromise credentials.'
)
doc.add_paragraph()

# Risk formula note
p = doc.add_paragraph()
run = p.add_run('Risk = Threat × Vulnerability × Impact')
run.bold = True
run.italic = True

doc.add_paragraph()

# Risk assessment table
rtbl = doc.add_table(rows=5, cols=2)
rtbl.style = 'Table Grid'

risk_rows = [
    (
        'Threat',
        'A malicious external actor (e.g. cybercriminal or nation-state group) launches '
        'a targeted phishing campaign to steal employee login credentials for the cloud CRM. '
        'Phishing remains the leading initial access vector in Australian cyber incidents '
        '(ACSC Annual Cyber Threat Report).'
    ),
    (
        'Vulnerability',
        'Multi-factor authentication (MFA) is not enabled on the CRM platform. '
        'The system relies solely on username and password, making it susceptible to '
        'credential stuffing, password spraying, and phishing attacks. '
        'Additionally, employees may not have received phishing-awareness training.'
    ),
    (
        'Impact',
        'Unauthorised access to the cloud CRM could result in:\n'
        '• Mass exposure of customer personal information (names, addresses, payment details).\n'
        '• Regulatory penalties under the Privacy Act 1988 / NDB scheme (mandatory breach notification).\n'
        '• Significant reputational damage and loss of customer trust.\n'
        '• Potential financial loss through fraud or ransom demands.\n'
        '• Legal liability if customer data is misused by the attacker.'
    ),
    (
        'Risk Rating (High / Med / Low)',
        'HIGH\n'
        'Rationale: The threat (phishing) is common and well-resourced; the vulnerability '
        '(no MFA) is a critical control gap; and the impact (customer data breach, regulatory '
        'penalties) is severe. All three factors are elevated, producing a High overall risk rating.'
    ),
    (
        'Recommended Controls',
        '1. Enable MFA immediately on all CRM accounts (priority control — reduces credential '
        'compromise risk by ~99%).\n'
        '2. Conduct phishing-awareness training and simulated phishing exercises for all staff.\n'
        '3. Deploy email filtering and anti-phishing tools (e.g. DMARC, SPF, DKIM) to block '
        'malicious emails before they reach users.\n'
        '4. Apply least-privilege access — restrict CRM access to only employees who need it.\n'
        '5. Enable login audit logging and anomaly detection to identify suspicious access patterns.\n'
        '6. Develop and test an incident response plan specific to CRM/cloud data breaches.\n'
        '7. Review third-party CRM provider security controls and SLAs.'
    ),
]

for i, (field, answer) in enumerate(risk_rows):
    row = rtbl.rows[i].cells
    row[0].text = field
    for para in row[0].paragraphs:
        for run in para.runs:
            run.bold = True
    row[1].text = answer

doc.add_paragraph()

# Summary note
doc.add_heading('Key Takeaway', level=3)
doc.add_paragraph(
    'This scenario illustrates that a single missing control (MFA) can dramatically '
    'elevate overall risk even when other safeguards are in place. Under ISO 27001 '
    'Annex A.9 (Access Control) and the ACSC Essential Eight, MFA is a mandatory '
    'baseline control. Enabling MFA is the single highest-impact, lowest-cost '
    'remediation action available to the organisation.'
)

doc.add_paragraph()

# ── References ────────────────────────────────────────────────────────────────
doc.add_heading('References', level=1)
refs = [
    'ISO/IEC 27001:2022 – Annex A.8 (Asset Management) and A.9 (Access Control).',
    'Australian Cyber Security Centre (ACSC). Essential Eight Maturity Model. https://www.cyber.gov.au',
    'Office of the Australian Information Commissioner (OAIC). Notifiable Data Breaches Scheme. https://www.oaic.gov.au',
    'NIST SP 800-30 Rev. 1 – Guide for Conducting Risk Assessments.',
]
for ref in refs:
    doc.add_paragraph(ref, style='List Bullet')

doc.save('/workspace/lab 9.docx')
print("lab 9.docx created successfully")
