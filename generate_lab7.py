from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# ── Title ─────────────────────────────────────────────────────────────────────
t = doc.add_heading('BN324 Enterprise Cyber Security and Management', 0)
t.alignment = WD_ALIGN_PARAGRAPH.CENTER

s = doc.add_heading('Week 7 Laboratory – Major Recent Cybersecurity Incidents in Australia', level=1)
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_paragraph()

# ── Incident Summary ──────────────────────────────────────────────────────────
doc.add_heading('Overview of Incidents', level=1)
incidents = [
    ('1. Defence Industry Supply Chain Breaches (Late 2025)',
     'Cyber-attacks on defence contractors exposed sensitive material linked to submarine '
     'programs and the $7 billion Redback infantry fighting vehicle contract, highlighting '
     'critical vulnerabilities in Australia\'s defence supply chain.'),
    ('2. University of Sydney Data Breach (December 2025)',
     'Hackers stole personal data of 13,000+ staff, donors and alumni, triggering mandatory '
     'breach notifications under the Notifiable Data Breaches (NDB) scheme.'),
    ('3. BECKS Jewellery Cyber Incident (December 2025)',
     'The SafePay ransomware group claimed responsibility for an attack on Australian jeweller '
     'BECKS, illustrating the growing ransomware threat to SMBs.'),
    ('4. Dodo & iPrimus Customer Data Exposure',
     'Personal information of customers was exposed, continuing a trend of escalating attacks '
     'on Australian telcos and service providers.'),
]
for title, detail in incidents:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(title + ': ')
    run.bold = True
    p.add_run(detail)

doc.add_paragraph()

# ── Q1 ────────────────────────────────────────────────────────────────────────
doc.add_heading('Question i – What is a Data Breach Response Plan and Why is it Needed?', level=1)

doc.add_heading('Definition', level=2)
doc.add_paragraph(
    'A Data Breach Response Plan (DBRP) is a documented framework that sets out the roles, '
    'responsibilities, and step-by-step actions an organisation will take when a data breach '
    'occurs or is suspected. It covers the entire lifecycle of a breach — from initial detection '
    'and containment through to assessment, notification, and post-incident review '
    '(OAIC, Part 2, 2025).'
)

doc.add_heading('Why You Need It', level=2)
reasons = [
    ('Meet legal obligations', 'Under the Privacy Act 1988 (Cth) and the NDB scheme, Australian '
     'entities must take reasonable steps to protect personal information and notify affected '
     'individuals of eligible breaches. A DBRP demonstrates those reasonable steps.'),
    ('Limit harm and costs', 'A fast, coordinated response reduces the likelihood of serious '
     'harm to individuals (e.g. identity theft, financial loss) and minimises financial and '
     'reputational damage to the organisation.'),
    ('Preserve public trust', 'Transparency and timely notification build consumer confidence '
     'and show that the organisation handles personal information responsibly.'),
    ('Enable rapid action', 'Without a pre-planned response, confusion and delay amplify the '
     'impact. A rehearsed plan ensures staff know exactly what to do and who to contact '
     'immediately.'),
]
for heading, body in reasons:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(heading + ': ')
    run.bold = True
    p.add_run(body)

doc.add_paragraph(
    'In the context of the incidents above, organisations such as the University of Sydney '
    'and BECKS Jewellery that had a DBRP in place were better positioned to contain the '
    'breach quickly, notify victims, and fulfil their regulatory obligations.'
)
doc.add_paragraph()

# ── Q2 ────────────────────────────────────────────────────────────────────────
doc.add_heading('Question ii – What Information Should the Plan Cover?', level=1)
doc.add_paragraph(
    'Based on OAIC guidance (Part 2, updated February 2025), a comprehensive DBRP should include:'
)

plan_items = [
    ('1. Definition of a Data Breach',
     'Clear explanation of what constitutes a data breach and how staff can recognise one '
     '(e.g. unauthorised access, accidental disclosure, ransomware).'),
    ('2. Containment, Assessment and Management Strategy',
     'Step-by-step actions to contain the breach (e.g. isolate affected systems), assess its '
     'scope (data types and volume affected), and manage ongoing risks.'),
    ('3. Roles and Responsibilities',
     'Identify the response team — team leader, project manager, privacy officer, ICT/forensics, '
     'legal, HR, media/comms — with clear escalation paths and backup contacts.'),
    ('4. Communications Strategy',
     'Specify who notifies affected individuals, when (mandatory timelines under NDB scheme), '
     'how (email, phone, public notice), and criteria for contacting external bodies such as '
     'the OAIC, Australian Cyber Security Centre (ACSC), and law enforcement.'),
    ('5. Escalation Procedures',
     'Define thresholds for escalating a breach to the response team — e.g. number of affected '
     'individuals, risk of serious harm, or systemic failure indicators.'),
    ('6. Record-Keeping Policy',
     'Document all breaches and suspected breaches, actions taken, and outcomes to support '
     'compliance and future reviews.'),
    ('7. Post-Breach Review',
     'After resolution, assess what went wrong, evaluate response effectiveness, and update '
     'data-handling practices and the plan itself.'),
    ('8. Integration with Other Plans',
     'Link to the disaster recovery plan, cyber security incident response plan, and any '
     'insurance policy requirements for data breaches.'),
    ('9. Regular Testing',
     'Conduct tabletop exercises (e.g. simulated ransomware attack) to ensure staff '
     'understand their roles and the plan remains current.'),
]

for title, body in plan_items:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(title + ': ')
    run.bold = True
    p.add_run(body)

doc.add_paragraph()

# ── Q3 ────────────────────────────────────────────────────────────────────────
doc.add_heading('Question iii – Practical, High-Impact Cybersecurity Risk Reduction Tips', level=1)
doc.add_paragraph(
    'The following tips are tailored to the Australian context and directly informed by '
    'the incident types described above.'
)

doc.add_heading('For Individuals', level=2)
individual_tips = [
    ('Use Multi-Factor Authentication (MFA)',
     'Enable MFA on all accounts — especially email, banking and government services (myGov). '
     'This prevents account takeover even if passwords are stolen.'),
    ('Use strong, unique passwords',
     'Use a password manager (e.g. Bitwarden, 1Password) to generate and store unique '
     'passwords. Reused passwords amplify breach damage across services.'),
    ('Monitor for breaches',
     'Register with services like Have I Been Pwned (haveibeenpwned.com) to receive alerts '
     'if your email appears in a data breach.'),
    ('Be phishing-aware',
     'Verify unexpected emails, SMS, or calls claiming to be from banks, telcos (e.g. Dodo) '
     'or government agencies before clicking links or providing information.'),
    ('Keep devices updated',
     'Apply operating system and application updates promptly — most attacks exploit known '
     'vulnerabilities with available patches.'),
    ('Back up important data',
     'Maintain offline or cloud backups of important files. Ransomware (as seen with BECKS) '
     'cannot encrypt data it cannot reach.'),
]
for title, body in individual_tips:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(title + ': ')
    run.bold = True
    p.add_run(body)

doc.add_heading('For Businesses', level=2)
business_tips = [
    ('Develop and test a Data Breach Response Plan',
     'As detailed above — all Australian businesses holding personal information should have '
     'a documented, tested DBRP aligned with the Privacy Act and NDB scheme.'),
    ('Apply the Essential Eight',
     'Follow the ACSC\'s Essential Eight mitigation strategies: patch applications, patch '
     'operating systems, restrict administrative privileges, enable MFA, application control, '
     'configure Microsoft Office macros, user application hardening, and regular backups.'),
    ('Conduct regular risk assessments',
     'Identify and prioritise assets, threats and vulnerabilities — particularly in the supply '
     'chain (as demonstrated by the Defence contractor breaches).'),
    ('Segment networks and restrict access',
     'Apply least-privilege access controls and network segmentation to contain breaches '
     'and prevent lateral movement by attackers.'),
    ('Train staff regularly',
     'Human error is a leading cause of breaches. Run phishing simulations and awareness '
     'training at least annually.'),
    ('Engage with the ACSC',
     'Report incidents to the Australian Cyber Security Centre (cyber.gov.au) and leverage '
     'free resources, alerts and threat intelligence available to Australian organisations.'),
    ('Review third-party and supply chain risk',
     'Audit the security practices of vendors and contractors — the Defence supply chain '
     'breaches show that attackers target the weakest link in the chain.'),
    ('Implement ransomware-specific controls',
     'Maintain tested offline backups, disable unnecessary remote access, and deploy endpoint '
     'detection and response (EDR) tools to detect ransomware early '
     '(relevant to the BECKS Jewellery incident).'),
]
for title, body in business_tips:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(title + ': ')
    run.bold = True
    p.add_run(body)

doc.add_paragraph()

# ── References ────────────────────────────────────────────────────────────────
doc.add_heading('References', level=1)
refs = [
    'Office of the Australian Information Commissioner (OAIC) (2025). Part 2: Preparing a data '
    'breach response plan. https://www.oaic.gov.au/privacy/guidance-and-advice/data-breach-'
    'preparation-and-response/part-2-preparing-a-data-breach-response-plan',
    'Australian Cyber Security Centre (ACSC). Essential Eight Explained. https://www.cyber.gov.au',
    'Privacy Act 1988 (Cth) — Notifiable Data Breaches (NDB) scheme, Part IIIC.',
]
for ref in refs:
    doc.add_paragraph(ref, style='List Bullet')

doc.save('/workspace/lab 7.docx')
print("lab 7.docx created successfully")
