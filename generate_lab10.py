from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# ── Title ─────────────────────────────────────────────────────────────────────
t = doc.add_heading('BN324 Enterprise Cyber Security and Management', 0)
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
s = doc.add_heading('Week 10 Laboratory – Information Security Governance Part C', level=1)
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# MODULE 1 – Access Control Policy Statement
# ══════════════════════════════════════════════════════════════════════════════
doc.add_heading('Module 1: Governance Documentation', level=1)
doc.add_heading('Activity 1: Access Control Policy Statement', level=2)

doc.add_paragraph(
    'All access to information systems, applications, and data assets owned or operated '
    'by the organisation must be granted on a least-privilege basis, ensuring that users, '
    'systems, and third parties receive only the minimum level of access required to '
    'perform their authorised functions. Access rights must be formally requested, approved '
    'by the relevant data owner, and documented prior to provisioning. Multi-factor '
    'authentication (MFA) is mandatory for all remote access, privileged accounts, and '
    'systems processing sensitive or confidential data. Access rights must be reviewed at '
    'least every six months; accounts belonging to employees who have changed roles or '
    'departed the organisation must be modified or revoked within 24 hours of notification. '
    'All access activity is subject to audit logging, and violations of this policy may '
    'result in disciplinary action, up to and including termination of employment or '
    'contract. This policy is aligned with ISO/IEC 27001:2022 Annex A.9 (Access Control) '
    'and the Australian Cyber Security Centre\'s Essential Eight baseline controls.'
)

doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# MODULE 2 – Governance Roles & Responsibilities
# ══════════════════════════════════════════════════════════════════════════════
doc.add_heading('Module 2: Governance Roles & Responsibilities', level=1)
doc.add_heading('Activity 2: Assign Responsibilities', level=2)

tbl = doc.add_table(rows=5, cols=3)
tbl.style = 'Table Grid'

headers = ['Responsibility', 'Role', 'Explanation']
for i, h in enumerate(headers):
    cell = tbl.rows[0].cells[i]
    cell.text = h
    for run in cell.paragraphs[0].runs:
        run.bold = True

role_rows = [
    (
        'Approves enterprise risk appetite',
        'Board of Directors',
        'Setting risk appetite is a strategic governance decision made at board level. '
        'The board is ultimately accountable to shareholders and regulators and must '
        'define how much risk the organisation is willing to accept '
        '(COBIT EDM03; ISO 27001 Clause 5.1).'
    ),
    (
        'Ensures security controls are implemented',
        'CIO / CISO',
        'The Chief Information Officer (CIO) or Chief Information Security Officer (CISO) '
        'translates governance policy into operational reality by overseeing the design, '
        'deployment, and maintenance of security controls across the organisation '
        '(ISO 27001 Clause 5.3).'
    ),
    (
        'Performs independent audit of controls',
        'Internal Audit',
        'Internal Audit provides independent, objective assurance that controls are '
        'operating effectively and that governance obligations are being met. '
        'Independence from operational management is essential for credibility '
        '(COBIT MEA02; ISO 27001 Clause 9.2).'
    ),
    (
        'Owns data classification decisions',
        'Data Owners',
        'Data Owners are senior business managers responsible for specific information '
        'assets. They determine the classification level (Public / Internal / Confidential) '
        'based on business impact, legal requirements, and sensitivity '
        '(ISO 27001 Annex A.8.2).'
    ),
]

for i, (resp, role, expl) in enumerate(role_rows, start=1):
    row = tbl.rows[i].cells
    row[0].text = resp
    row[1].text = role
    for para in row[1].paragraphs:
        for run in para.runs:
            run.bold = True
    row[2].text = expl

doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# MODULE 3 – Case Study: 5-Step Governance Improvement Plan
# ══════════════════════════════════════════════════════════════════════════════
doc.add_heading('Module 3: Case Study – Governance Improvement Plan', level=1)

doc.add_heading('Scenario Summary', level=2)
issues = [
    'No formal security governance structure.',
    'Increasing regulatory pressure (e.g. APRA CPS 234, Privacy Act 1988).',
    'Several recent security incidents indicating control gaps.',
    'No risk register — risks are unidentified and untracked.',
    'IT manages security informally with no defined roles or accountability.',
]
for issue in issues:
    doc.add_paragraph(issue, style='List Bullet')

doc.add_paragraph()
doc.add_heading('Proposed 5-Step Governance Improvement Plan', level=2)

steps = [
    (
        'Step 1: Establish a Formal Security Governance Structure',
        [
            'Appoint a Chief Information Security Officer (CISO) with board-level reporting authority.',
            'Establish a Security Steering Committee (or Risk Committee) comprising the CISO, CIO, CFO, Legal, and business unit leaders.',
            'Define and document governance roles and responsibilities: Board oversight, CISO operational leadership, Data Owners, and Internal Audit.',
            'Align the governance structure with COBIT 2019 (EDM01 – Ensure Governance Framework) and ISO 27001 Clause 5 (Leadership).',
        ],
        'Why: Without accountable leadership and defined roles, security remains reactive and informal. A governance structure provides the authority to enforce policy and the accountability to drive change.'
    ),
    (
        'Step 2: Develop Core Governance Documentation',
        [
            'Draft and have the board formally approve an Information Security Policy (top-level) that sets direction and risk appetite.',
            'Develop supporting standards and procedures: Access Control Policy, Incident Response Policy, Data Classification Standard, and Acceptable Use Policy.',
            'Establish a document management process — version control, review cycles (at least annually), and board/executive sign-off.',
            'Communicate policies to all staff and contractors with signed acknowledgement.',
        ],
        'Why: Formal documentation provides the legal and procedural baseline for compliance, audit, and enforcement. It demonstrates due diligence to regulators (e.g. APRA, OAIC).'
    ),
    (
        'Step 3: Build and Maintain a Risk Register',
        [
            'Conduct an organisation-wide information security risk assessment using ISO 27001 Clause 6.1 or NIST SP 800-30 methodology.',
            'Identify, record, and rate all significant risks (likelihood × impact) in a centralised risk register.',
            'Assign a risk owner to each entry and document the chosen treatment (accept, mitigate, transfer, or avoid).',
            'Review and update the risk register at least quarterly and after any significant incident or business change.',
        ],
        'Why: A risk register transforms security from guesswork into evidence-based management. It enables the board to make informed decisions about risk appetite and resource allocation.'
    ),
    (
        'Step 4: Implement Regulatory Compliance Alignment',
        [
            'Map current security controls against applicable regulations: APRA CPS 234 (information security for financial services), Privacy Act 1988 / NDB scheme, and the ACSC Essential Eight.',
            'Identify and remediate compliance gaps as a priority (particularly MFA, patch management, and access controls).',
            'Engage external legal and compliance advisors to assess exposure and obligations.',
            'Establish a compliance calendar with scheduled reviews, regulatory reporting deadlines, and audit preparation cycles.',
        ],
        'Why: As a financial services company, failure to meet APRA CPS 234 and Privacy Act obligations can result in significant regulatory penalties, enforcement action, and reputational damage.'
    ),
    (
        'Step 5: Establish KPIs, Monitoring, and Continuous Improvement',
        [
            'Define measurable Key Performance Indicators (KPIs) for security governance, e.g. % systems with MFA enabled, mean time to detect/respond to incidents, patch compliance rate, % staff completing security training.',
            'Implement a security dashboard reported to the board and Risk Committee on a monthly/quarterly basis.',
            'Engage Internal Audit to conduct annual independent reviews of the governance framework and control effectiveness.',
            'Run annual tabletop exercises and penetration tests to validate controls and update the risk register.',
            'Adopt a continuous improvement cycle (Plan–Do–Check–Act, per ISO 27001 Clause 10) to mature the governance programme over time.',
        ],
        'Why: Governance without measurement is ineffective. KPIs and regular reporting provide the feedback loop that enables leadership to track progress, identify emerging risks, and demonstrate accountability to regulators and stakeholders.'
    ),
]

for step_title, bullets, rationale in steps:
    doc.add_heading(step_title, level=3)
    for b in bullets:
        doc.add_paragraph(b, style='List Bullet')
    p = doc.add_paragraph()
    run = p.add_run('Rationale: ')
    run.bold = True
    p.add_run(rationale)
    doc.add_paragraph()

# Implementation Roadmap table
doc.add_heading('Implementation Roadmap Summary', level=2)
rtbl = doc.add_table(rows=6, cols=3)
rtbl.style = 'Table Grid'

rhdrs = ['Step', 'Action', 'Priority / Timeframe']
for i, h in enumerate(rhdrs):
    cell = rtbl.rows[0].cells[i]
    cell.text = h
    for run in cell.paragraphs[0].runs:
        run.bold = True

roadmap = [
    ('1', 'Establish governance structure (CISO, Risk Committee, roles)', 'Immediate – Month 1'),
    ('2', 'Develop and approve core security documentation', 'Short-term – Months 1–2'),
    ('3', 'Build and populate risk register', 'Short-term – Months 2–3'),
    ('4', 'Regulatory compliance gap analysis and remediation', 'Medium-term – Months 3–6'),
    ('5', 'Define KPIs, reporting dashboard, and audit cycle', 'Ongoing – from Month 3'),
]
for i, (step, action, timeline) in enumerate(roadmap, start=1):
    row = rtbl.rows[i].cells
    row[0].text = step
    row[1].text = action
    row[2].text = timeline

doc.add_paragraph()

# ── References ────────────────────────────────────────────────────────────────
doc.add_heading('References', level=1)
refs = [
    'ISO/IEC 27001:2022 – Information Security Management Systems Requirements.',
    'ISACA. COBIT 2019 Framework: Governance and Management Objectives.',
    'APRA. CPS 234 Information Security (2019). Australian Prudential Regulation Authority.',
    'Australian Cyber Security Centre (ACSC). Essential Eight Maturity Model. https://www.cyber.gov.au',
    'NIST SP 800-30 Rev. 1 – Guide for Conducting Risk Assessments.',
    'Office of the Australian Information Commissioner (OAIC). Privacy Act 1988 and NDB Scheme.',
]
for ref in refs:
    doc.add_paragraph(ref, style='List Bullet')

doc.save('/workspace/lab 10.docx')
print("lab 10.docx created successfully")
