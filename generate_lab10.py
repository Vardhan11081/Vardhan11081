import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ═══════════════════════════════════════════════════════════════
# DIAGRAM 1 – Testing phases (Integration → System → UAT → Production)
# ═══════════════════════════════════════════════════════════════
def make_testing_phases():
    fig, ax = plt.subplots(figsize=(14, 5))
    fig.patch.set_facecolor('#f0f4f8')
    ax.set_xlim(0, 14); ax.set_ylim(0, 5); ax.axis('off')
    ax.set_title('Software Testing Phases – From Development to Deployment',
                 fontsize=12, fontweight='bold', pad=8)

    phases = [
        (1.3,  2.5, '#dbeafe', '#1a4a7a', 'Unit\nTesting',
         'Devs test\nindividual\nmodules'),
        (3.5,  2.5, '#dcfce7', '#166534', 'Integration\nTesting',
         'Modules tested\ntogether;\ninterfaces & data\nflows verified'),
        (5.9,  2.5, '#fef9c3', '#854d0e', 'System\nTesting',
         'Full system vs\nrequirements;\nperformance,\nsecurity, load'),
        (8.3,  2.5, '#f3e8ff', '#6b21a8', 'User Acceptance\nTesting (UAT)',
         'End users\nvalidate real\nbusiness scenarios\nand sign off'),
        (10.7, 2.5, '#ffedd5', '#9a3412', 'Regression\nTesting',
         'Re-test after\nfixes to ensure\nno new defects'),
        (13.0, 2.5, '#fee2e2', '#991b1b', 'Production\nDeployment',
         'Go-live;\nmonitoring &\npost-impl review'),
    ]

    for x, y, fc, ec, title, desc in phases:
        ax.add_patch(FancyBboxPatch((x-1.0, y-1.6), 2.0, 3.2,
                                   boxstyle='round,pad=0.12', lw=1.8,
                                   edgecolor=ec, facecolor=fc, zorder=5))
        ax.text(x, y+1.1, title, ha='center', va='center', fontsize=8.5,
                fontweight='bold', color=ec, zorder=6, multialignment='center')
        ax.text(x, y-0.5, desc, ha='center', va='center', fontsize=7.3,
                color='#374151', zorder=6, multialignment='center')

    # Arrows
    for x in [2.3, 4.5, 6.9, 9.3, 11.7]:
        ax.annotate('', xy=(x+0.2, 2.5), xytext=(x, 2.5),
                    arrowprops=dict(arrowstyle='->', color='#64748b', lw=1.8), zorder=4)

    # Highlight Integration + System testing
    ax.add_patch(FancyBboxPatch((2.4, 0.25), 5.1, 0.55,
                               boxstyle='round,pad=0.05', lw=1.3,
                               edgecolor='#166534', facecolor='#dcfce7', linestyle='dashed'))
    ax.text(4.95, 0.52, 'Primarily IT / QA team responsibility',
            ha='center', fontsize=8, color='#166534', style='italic')

    ax.add_patch(FancyBboxPatch((7.2, 0.25), 2.2, 0.55,
                               boxstyle='round,pad=0.05', lw=1.3,
                               edgecolor='#6b21a8', facecolor='#f3e8ff', linestyle='dashed'))
    ax.text(8.3, 0.52, 'Users responsibility',
            ha='center', fontsize=8, color='#6b21a8', style='italic')

    plt.tight_layout()
    path = '/workspace/lab10_testing_phases.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Testing phases saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# DIAGRAM 2 – Deployment methods comparison
# ═══════════════════════════════════════════════════════════════
def make_deployment_methods():
    fig, ax = plt.subplots(figsize=(13, 5.5))
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_xlim(0, 13); ax.set_ylim(0, 5.5); ax.axis('off')
    ax.set_title('System Deployment Methods – Comparison',
                 fontsize=12, fontweight='bold', pad=8)

    methods = [
        (1.5,  3.0, '#dbeafe', '#1a4a7a', 'Direct\nCutover\n(Big Bang)',
         'Old system OFF\nNew system ON\nin one step',
         'Fast, low cost',
         'High risk – no\nfallback if fails'),
        (4.5,  3.0, '#dcfce7', '#166634', 'Parallel\nConversion',
         'Old and new\nsystems run\nsimultaneously',
         'Safe – compare\noutputs',
         'High cost –\ndouble operations'),
        (7.5,  3.0, '#fef9c3', '#854d0e', 'Phased\nConversion',
         'New system\nrolled out\nmodule by module',
         'Risk spread\nover time',
         'Complex to\nmanage'),
        (10.5, 3.0, '#f3e8ff', '#6b21a8', 'Pilot\nConversion',
         'New system\ntested at one\nlocation first',
         'Learn before\nfull rollout',
         'Delay for full\ndeployment'),
    ]

    for x, y, fc, ec, title, how, pro, con in methods:
        ax.add_patch(FancyBboxPatch((x-1.4, y-2.0), 2.8, 3.9,
                                   boxstyle='round,pad=0.12', lw=1.8,
                                   edgecolor=ec, facecolor=fc, zorder=5))
        ax.text(x, y+1.55, title, ha='center', va='center', fontsize=9,
                fontweight='bold', color=ec, zorder=6, multialignment='center')
        ax.text(x, y+0.55, how, ha='center', va='center', fontsize=7.8,
                color='#334155', zorder=6, multialignment='center')
        ax.text(x, y-0.5, f'+ {pro}', ha='center', va='center', fontsize=7.5,
                color='#166534', zorder=6, multialignment='center')
        ax.text(x, y-1.2, f'- {con}', ha='center', va='center', fontsize=7.5,
                color='#991b1b', zorder=6, multialignment='center')

    # Risk gradient bar
    ax.text(1.5, 0.18, 'HIGHEST RISK', ha='center', fontsize=7.8,
            color='#991b1b', fontweight='bold')
    ax.text(10.5, 0.18, 'LOWEST RISK', ha='center', fontsize=7.8,
            color='#166534', fontweight='bold')
    ax.annotate('', xy=(10.5, 0.08), xytext=(1.5, 0.08),
                arrowprops=dict(arrowstyle='->', color='#6b7280', lw=1.5))

    plt.tight_layout()
    path = '/workspace/lab10_deployment.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Deployment methods saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# Build diagrams
# ═══════════════════════════════════════════════════════════════
test_path   = make_testing_phases()
deploy_path = make_deployment_methods()


# ═══════════════════════════════════════════════════════════════
# BUILD WORD DOCUMENT
# ═══════════════════════════════════════════════════════════════
doc = Document()

def H(doc, text, level=2):
    p = doc.add_heading(text, level=level)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    return p

def B(doc, text, size=11):
    p = doc.add_paragraph(text)
    p.style.font.size = Pt(size)
    return p

def BU(doc, text, size=11):
    p = doc.add_paragraph(text, style='List Bullet')
    p.style.font.size = Pt(size)
    return p

def BB(doc, bold_part, rest, size=11):
    p = doc.add_paragraph()
    r = p.add_run(bold_part); r.bold = True; r.font.size = Pt(size)
    p.add_run(rest).font.size = Pt(size)
    return p

def SP(doc): doc.add_paragraph()

def tbl(doc, rows_data, headers, col_sizes=None):
    t = doc.add_table(rows=len(rows_data)+1, cols=len(headers))
    t.style = 'Table Grid'
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]; c.text = h
        for run in c.paragraphs[0].runs:
            run.bold = True; run.font.size = Pt(9.5)
    for ri, row in enumerate(rows_data, 1):
        for ci, val in enumerate(row):
            c = t.rows[ri].cells[ci]; c.text = val
            for run in c.paragraphs[0].runs:
                run.font.size = Pt(9.5)
    return t

def form_row(doc, label, field_type='line', choices=None, size=10):
    p = doc.add_paragraph()
    r = p.add_run(f'{label}  '); r.bold = True; r.font.size = Pt(size)
    if field_type == 'line':
        p.add_run('_' * 55).font.size = Pt(size)
    elif field_type == 'scale':
        p.add_run('  1  ☐    2  ☐    3  ☐    4  ☐    5  ☐').font.size = Pt(size)
    elif field_type == 'yn':
        p.add_run('  ☐ Yes    ☐ No').font.size = Pt(size)
    elif field_type == 'yn_comment':
        p.add_run('  ☐ Yes    ☐ No    Comments: ' + '_' * 32).font.size = Pt(size)
    elif field_type == 'choices' and choices:
        p.add_run('  ' + '    '.join([f'☐ {c}' for c in choices])).font.size = Pt(size)
    elif field_type == 'multiline':
        p.add_run('\n' + '_' * 65 + '\n' + '_' * 65).font.size = Pt(size)
    return p

# ── Title ───────────────────────────────────────────────────
t = doc.add_heading('BN314 – System Architecture', 0)
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
s = doc.add_heading('Lecture 10: Deploying the New System – Laboratory Activity', 1)
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)

# ══════════════════════════════════════════════════════════
# GROUP ACTIVITY SECTION
# ══════════════════════════════════════════════════════════
H(doc, 'PART A – Group Activity', level=1)
SP(doc)

# ── Group Q1 ─────────────────────────────────────────────
H(doc, 'Group Activity 1: Generic Post-Implementation Evaluation Form')
B(doc, 'The following form can be used to evaluate any information system after deployment. '
       'It assesses training quality, system usability, technical performance, and overall satisfaction.')
SP(doc)

# Form header
doc.add_heading('POST-IMPLEMENTATION EVALUATION FORM', level=3).alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_heading('Information System Evaluation – Confidential', level=4).alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)

B(doc, 'Instructions: Please complete all sections. Your responses are anonymous and will be used to improve future system deployments. Rating scale: 1 = Very Poor, 5 = Excellent.')
SP(doc)

# Section A – Respondent info
doc.add_heading('Section A – Respondent Information', level=3)
form_row(doc, 'Department / Role:')
form_row(doc, 'How long have you used this system?', 'choices',
         ['< 1 month', '1–3 months', '3–6 months', '6+ months'])
form_row(doc, 'How frequently do you use the system?', 'choices',
         ['Daily', 'Weekly', 'Monthly', 'Rarely'])
SP(doc)

# Section B – Training
doc.add_heading('Section B – Training Received', level=3)
form_row(doc, 'B1. Did you receive formal training before using the system?', 'yn')
form_row(doc, 'B2. Training format received:', 'choices',
         ['Classroom', 'Online/e-learning', 'Manual/self-study', 'On-the-job', 'None'])
form_row(doc, 'B3. Training was adequate for my role (1–5):',  'scale')
form_row(doc, 'B4. Training materials were clear and easy to understand (1–5):', 'scale')
form_row(doc, 'B5. Training duration was sufficient (1–5):', 'scale')
form_row(doc, 'B6. What was missing from the training?', 'multiline')
SP(doc)

# Section C – System Usability
doc.add_heading('Section C – System Usability and Performance', level=3)
form_row(doc, 'C1. The system is easy to navigate and use (1–5):', 'scale')
form_row(doc, 'C2. System response time meets my needs (1–5):', 'scale')
form_row(doc, 'C3. The system produces accurate and reliable outputs (1–5):', 'scale')
form_row(doc, 'C4. System availability / uptime has been acceptable (1–5):', 'scale')
form_row(doc, 'C5. The system meets my day-to-day job requirements (1–5):', 'scale')
SP(doc)

# Section D – Problems
doc.add_heading('Section D – Problems and Issues', level=3)
form_row(doc, 'D1. Have you experienced any system errors or crashes?', 'yn_comment')
form_row(doc, 'D2. Have you experienced data loss or incorrect results?', 'yn_comment')
form_row(doc, 'D3. Were problems resolved promptly by the support team?', 'yn_comment')
form_row(doc, 'D4. Describe the most significant problem you encountered:', 'multiline')
SP(doc)

# Section E – Overall
doc.add_heading('Section E – Overall Assessment', level=3)
form_row(doc, 'E1. Overall satisfaction with the system (1–5):', 'scale')
form_row(doc, 'E2. The system has improved my productivity (1–5):', 'scale')
form_row(doc, 'E3. I would recommend this system to a colleague:', 'yn')
form_row(doc, 'E4. Most important improvement needed:', 'multiline')
form_row(doc, 'E5. Any additional comments:', 'multiline')
SP(doc)
B(doc, 'Thank you for completing this evaluation. Responses will be reviewed by the project team.')
SP(doc)

# ── Group Q2 ─────────────────────────────────────────────
H(doc, 'Group Activity 2: One-Page Post-Implementation Questionnaire (10+ Questions)')
B(doc, 'The following questionnaire is designed for distribution to users following '
       'a recent information system implementation. It focuses on system effectiveness, '
       'training quality, support, and overall impact.')
SP(doc)

doc.add_heading('POST-IMPLEMENTATION USER SATISFACTION QUESTIONNAIRE', level=3).alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_heading('System Name: ________________    Date: ________________', level=4).alignment = WD_ALIGN_PARAGRAPH.CENTER
B(doc, 'Please rate each statement using the scale:  1 = Strongly Disagree  ·  2 = Disagree  '
       '·  3 = Neutral  ·  4 = Agree  ·  5 = Strongly Agree')
SP(doc)

q2_questions = [
    ('Q1',  'The new system is easy to learn and use.',                                     'scale'),
    ('Q2',  'The system performs its functions accurately and reliably.',                    'scale'),
    ('Q3',  'The system\'s response time and speed are acceptable.',                        'scale'),
    ('Q4',  'The training I received was sufficient to use the system effectively.',         'scale'),
    ('Q5',  'The training materials (manuals, guides, videos) were clear and helpful.',     'scale'),
    ('Q6',  'The new system has improved my productivity compared to the previous system.', 'scale'),
    ('Q7',  'The system meets the needs of my daily work tasks.',                           'scale'),
    ('Q8',  'The help desk / technical support team responds promptly to issues.',          'scale'),
    ('Q9',  'I feel confident and comfortable using all features I need.',                  'scale'),
    ('Q10', 'Overall, I am satisfied with the new system.',                                 'scale'),
    ('Q11', 'What is the single biggest improvement you would suggest?',                    'multiline'),
    ('Q12', 'Did you experience any critical problems during the first 30 days? If yes, describe briefly.',
            'multiline'),
]
for qn, qlbl, qtype in q2_questions:
    form_row(doc, f'{qn}. {qlbl}', qtype)
SP(doc)

# ── Group Q3 ─────────────────────────────────────────────
H(doc, 'Group Activity 3: Designing Training – Knowing the Recipient')
B(doc, 'When designing a tutorial to train a person in the use of specific software '
       'or hardware (e.g., a web browser), the following information about the '
       'recipient is essential:')
SP(doc)
tbl(doc, [
    ('Technical proficiency',
     'Beginner, intermediate, or advanced computer user.',
     'Beginners need step-by-step screenshots and plain language; advanced users need only '
     'a quick-reference guide and shortcut keys.'),
    ('Prior experience with similar tools',
     'Has the trainee used a similar browser or application before?',
     'If yes, training can focus on differences and new features. If no, foundational concepts must be covered.'),
    ('Job role and use context',
     'What tasks will the trainee perform? (e.g., browsing, form submission, web development)',
     'A student needs different training content to an IT support officer using the same browser.'),
    ('Learning style preference',
     'Visual (video), reading (manual), or hands-on (sandbox exercises)?',
     'Some learners absorb video tutorials; others prefer written step-by-step guides or interactive labs.'),
    ('Availability and time constraints',
     'How much time can the trainee dedicate? Is training self-paced or scheduled?',
     'Short attention spans or limited time require condensed, modular micro-learning units.'),
    ('Language and literacy level',
     'Is English (or the training language) the trainee\'s first language?',
     'Non-native speakers need simpler language, visual aids, and possibly translated materials.'),
    ('Accessibility needs',
     'Does the trainee have visual, motor, or cognitive accessibility requirements?',
     'Screen reader-compatible materials, larger fonts, or keyboard-only navigation may be needed.'),
], ['Information Needed', 'How It Is Obtained', 'How It Affects Training Design'])
SP(doc)

# ── Group Q4 ─────────────────────────────────────────────
H(doc, 'Group Activity 4: Internet Research – Training Example for Software/Hardware')
BB(doc, 'Product: ', 'Microsoft Azure – Cloud Platform')
BB(doc, 'Training Provider: ', 'Microsoft Learn (https://learn.microsoft.com)')
BB(doc, 'Types of training offered: ',
   'Free self-paced learning paths and modules; instructor-led courses via Microsoft '
   'and certified partners; sandbox labs with real Azure environments; certification '
   'preparation (e.g., AZ-900 Azure Fundamentals, AZ-104 Administrator Associate).')
BB(doc, 'Cost: ',
   'Microsoft Learn self-paced modules are entirely FREE. '
   'Instructor-led courses via partners range from AUD $500 to $3,500+ depending on '
   'course length and certification level. Certification exam vouchers cost AUD $165–$330.')
SP(doc)
B(doc, 'Summary of findings:')
BU(doc, 'What we liked: The free tier is comprehensive and includes hands-on lab exercises '
        'in real Azure sandboxes — learners get genuine cloud experience without paying. '
        'Content is modular and role-based (Developer, Administrator, Architect), making '
        'it easy to find relevant material. Interactive quizzes reinforce learning at each step.')
BU(doc, 'What we did not like: The breadth of content is overwhelming for new learners — '
        'navigating hundreds of learning paths without guidance is difficult. '
        'Instructor-led training is expensive and primarily aimed at corporate buyers. '
        'Some content updates lag behind rapidly changing Azure features.')
BU(doc, 'Group discussion conclusion: The Microsoft Learn model is an excellent example '
        'of blended learning — free foundational self-paced content combined with paid '
        'certification pathways. The sandbox approach is particularly effective for '
        'technical audiences who learn best by doing.')
SP(doc)

# ══════════════════════════════════════════════════════════
# WRITTEN QUESTION SECTION
# ══════════════════════════════════════════════════════════
H(doc, 'PART B – Individual Written Questions', level=1)
SP(doc)

# ── Written Q1 ───────────────────────────────────────────
H(doc, 'Written Question 1: Integration Testing vs System Testing')
B(doc, 'The diagram below shows where integration testing and system testing fit in '
       'the overall testing lifecycle:')
doc.add_picture(test_path, width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)
tbl(doc, [
    ('Scope',
     'Tests how two or more modules or components work together when combined. '
     'Focuses on interfaces, data flows, and interactions between components.',
     'Tests the complete, fully integrated system against the original requirements specification.'),
    ('Who performs it',
     'Development team / QA engineers.',
     'QA team, with oversight from the project manager.'),
    ('What is checked',
     'Correct data passing between modules, API contracts, database reads/writes across components, error handling at boundaries.',
     'Functional correctness, performance, load capacity, security, usability, reliability, and compliance with requirements.'),
    ('Timing',
     'After unit testing; as modules are progressively combined.',
     'After all integration testing is complete; before UAT.'),
    ('Test basis',
     'Interface specifications, API contracts, data flow diagrams.',
     'System requirements specification, use cases, non-functional requirements.'),
], ['Aspect', 'Integration Testing', 'System Testing'])
SP(doc)
B(doc, 'Types of tests included in system testing:')
BU(doc, 'Functional testing – verifies each function against requirements.')
BU(doc, 'Performance/load testing – measures response time and throughput under expected and peak loads.')
BU(doc, 'Stress testing – pushes the system beyond normal limits to find breaking points.')
BU(doc, 'Security testing – attempts penetration, injection attacks, and authorisation bypass.')
BU(doc, 'Usability testing – evaluates ease of use, navigation, and UI clarity.')
BU(doc, 'Recovery testing – verifies system behaviour after crashes, power failures, or data corruption.')
BU(doc, 'Compatibility testing – ensures the system works across required browsers, OS versions, and devices.')
SP(doc)

# ── Written Q2 ───────────────────────────────────────────
H(doc, 'Written Question 2: User Acceptance Testing (UAT) – Responsibility and Objectives')
BB(doc, 'Who is responsible: ',
   'UAT is the responsibility of the end users and business stakeholders — the people '
   'who will actually use the system in their daily work. This includes:')
BU(doc, 'Subject matter experts and business analysts who define and verify the real-world scenarios.')
BU(doc, 'End users from the relevant departments (e.g., student services staff, finance officers).')
BU(doc, 'Business owners and management who must formally sign off before go-live.')
BU(doc, 'Note: IT staff may support UAT by setting up test environments, but they should NOT perform the testing — independence is critical.')
SP(doc)
B(doc, 'Primary objectives of UAT:')
BU(doc, 'Validate business requirements: confirm that the system correctly implements every agreed business requirement and use case in real-world conditions.')
BU(doc, 'Identify defects missed by earlier testing: surface issues that only become apparent when real users perform real tasks in a realistic environment.')
BU(doc, 'Build user confidence: give users hands-on experience before go-live, reducing anxiety, resistance to change, and post-deployment support calls.')
BU(doc, 'Obtain formal sign-off: produce documented evidence (test results, sign-off forms) that authorised business representatives approve the system for deployment.')
BU(doc, 'Final risk gate: act as the last quality checkpoint before production deployment, preventing premature go-live.')
SP(doc)

# ── Written Q3 ───────────────────────────────────────────
H(doc, 'Written Question 3: Identifying Test Cases for UAT')
B(doc, 'The best approach to identifying UAT test cases is to derive them directly '
       'from use cases and business process scenarios:')
BU(doc, 'Use case descriptions: each use case (main flow + alternative flows + exception flows) maps directly to one or more test cases. The main flow becomes the happy-path test; alternative/exception flows become negative and boundary tests.')
BU(doc, 'Business scenarios: ask users to describe a typical day\'s work step by step. Each real workflow becomes an end-to-end test scenario that covers multiple use cases in sequence.')
BU(doc, 'Business rules: decision tables, decision trees, and documented rules from the requirements phase define conditions and expected outcomes — each rule combination is a test case.')
BU(doc, 'Previous defect logs: review defects from earlier system or integration testing; users should test scenarios around known weak areas to verify fixes.')
BU(doc, 'Data-driven testing: use realistic, production-like data sets (anonymised) including boundary values, edge cases, and known problem data formats.')
BU(doc, 'Risk-based prioritisation: focus the most test effort on high-business-impact, high-frequency functions (e.g., student enrolment, payment processing) before low-risk functions.')
SP(doc)

# ── Written Q4 ───────────────────────────────────────────
H(doc, 'Written Question 4: When Is an Error Tracking Log Most Helpful?')
B(doc, 'An error tracking log (defect log / bug tracker) is helpful during any testing '
       'phase, but is most critical during the following:')
tbl(doc, [
    ('Integration Testing',
     'Highly beneficial. Multiple modules interact for the first time — errors at interfaces '
     '(wrong data format, missing fields, incorrect API responses) must be logged with '
     'the exact module combination, input data, and error message to enable developers '
     'to reproduce and fix them.'),
    ('System Testing',
     'Essential. System testing produces a high volume of functional, performance, and '
     'security defects across many test areas. A structured log with severity, priority, '
     'test case ID, steps to reproduce, and assigned developer is critical for managing '
     'the defect backlog.'),
    ('User Acceptance Testing (UAT)',
     'Critical. Users may not describe technical issues precisely. A log helps them '
     'document the exact steps that caused a problem, the expected vs actual result, '
     'and the business impact. Provides formal evidence of outstanding issues before sign-off.'),
    ('Regression Testing',
     'Very useful. The log shows which defects were fixed; regression tests verify '
     'that the fixes did not introduce new errors. Tracking ensures no previously '
     'closed defect re-opens unnoticed.'),
    ('Performance/Stress Testing',
     'Useful for recording response time anomalies, memory leaks, and failure '
     'thresholds identified during load testing.'),
], ['Testing Phase', 'Role of Error Tracking Log'])
SP(doc)

# ── Written Q5 ───────────────────────────────────────────
H(doc, 'Written Question 5: Data Sources and Methods for Initialising a New System Database')
B(doc, 'Sources of data:')
BU(doc, 'Legacy / existing system: data exported from the old system via ETL (Extract, Transform, Load) tools or database migration scripts.')
BU(doc, 'Manual data entry: data that exists only on paper or in spreadsheets and must be keyed in by data entry staff or end users before go-live.')
BU(doc, 'External/third-party systems: data feeds from government databases (e.g., student identifiers from PRISMS), partner organisations, or purchased reference data sets.')
BU(doc, 'Archival records: scanned and OCR-processed historical records converted to digital format.')
BU(doc, 'Default / reference data: lookup tables (country codes, course codes, role types) pre-populated by the development team from standards or business rules.')
SP(doc)
B(doc, 'Tools and methods for loading initial data:')
tbl(doc, [
    ('ETL Tool\n(e.g., Talend, SSIS)',
     'Extracts data from the source, transforms it (cleans, reformats, deduplicates), and loads it into the new database. Best for large-volume migrations from legacy databases.'),
    ('CSV / Spreadsheet Import',
     'Data is prepared in CSV or Excel format and imported using database bulk-load utilities (e.g., COPY in PostgreSQL, LOAD DATA in MySQL, SQL*Loader in Oracle).'),
    ('SQL Scripts',
     'Developers write INSERT statements or stored procedures to populate reference/lookup tables and system configuration data before go-live.'),
    ('Database Migration Tools\n(e.g., Flyway, Liquibase)',
     'Version-controlled migration scripts that initialise schema and seed data in a repeatable, auditable manner across environments.'),
    ('API / Data Feed',
     'New system calls a source system API to pull and import data directly into the new database in real time or in scheduled batches.'),
    ('Manual Data Entry Forms',
     'For small volumes or paper-based records, staff use the new system\'s own entry forms to enter data directly, often with data quality checks built in.'),
], ['Tool / Method', 'Description'])
SP(doc)

# ── Written Q6 ───────────────────────────────────────────
H(doc, 'Written Question 6: User Documentation and Training – End Users vs System Operators')
tbl(doc, [
    ('Audience',
     'Employees, managers, and customers who use the system to perform their business tasks (e.g., enrol students, process invoices, generate reports).',
     'IT staff, database administrators, and technical staff responsible for running, monitoring, and maintaining the system infrastructure.'),
    ('Documentation type',
     'User manuals, quick-start guides, online help, FAQs, tutorial videos focused on business tasks (e.g., "How to register a student").',
     'System administration guides, installation manuals, API documentation, backup/recovery procedures, troubleshooting reference guides.'),
    ('Training content',
     'Covers navigation, task workflows, data entry, report generation, and role-specific functions. Avoids technical jargon.',
     'Covers system installation, configuration, performance tuning, backup/restore, security patching, log monitoring, and disaster recovery.'),
    ('Training format',
     'Classroom, e-learning, video tutorials, role-playing exercises with realistic scenarios.',
     'Technical workshops, vendor certification courses, hands-on lab sessions, and reference documentation review.'),
    ('Language / depth',
     'Non-technical plain language; step-by-step screenshots; task-oriented.',
     'Technical terminology; command-line instructions; architecture diagrams; error code references.'),
    ('Timing',
     'Training typically completed just before go-live to minimise forgetting.',
     'Training completed earlier — operators must be ready to support go-live before end users are trained.'),
], ['Aspect', 'End Users', 'System Operators'])
SP(doc)

# ── Written Q7 ───────────────────────────────────────────
H(doc, 'Written Question 7: Source Code Control System')
BB(doc, 'Definition: ',
   'A source code control system (also called a version control system or VCS) is a '
   'tool that tracks and manages all changes to source code over time. It maintains a '
   'complete history of every modification, records who made each change and when, '
   'and enables teams to work on the same codebase simultaneously without overwriting '
   'each other\'s work. Examples: Git (most widely used), Subversion (SVN), Mercurial.')
SP(doc)
B(doc, 'Key features:')
BU(doc, 'Version history: every change is saved as a commit with a description, author, and timestamp — the full history is always available.')
BU(doc, 'Branching and merging: developers work on separate branches (e.g., feature/login-fix) without affecting the main codebase, then merge changes back when complete.')
BU(doc, 'Conflict resolution: when two developers change the same file, the VCS detects conflicts and helps merge the changes safely.')
BU(doc, 'Rollback: any version of the code can be restored — essential for undoing a breaking change.')
BU(doc, 'Audit trail: provides complete accountability for every change made to the system.')
SP(doc)
B(doc, 'Why it is necessary when multiple programmers build a system:')
tbl(doc, [
    ('Prevents overwriting',
     'Without VCS, Developer A\'s work can be erased when Developer B saves their version of the same file. VCS merges changes instead.'),
    ('Enables parallel development',
     'Each developer works on a separate branch; features are developed in isolation and merged only when stable and reviewed.'),
    ('Supports code review',
     'Pull requests / merge requests allow team members to review each other\'s changes before they enter the main codebase.'),
    ('Enables CI/CD',
     'Modern DevOps pipelines (GitHub Actions, Jenkins) trigger automated builds, tests, and deployments on every commit.'),
    ('Provides traceability',
     'Bug reports can be traced to the exact commit that introduced a defect; defect fixes can be tagged to issue tracker tickets.'),
    ('Risk management',
     'If a release introduces a critical bug, the team can immediately roll back to the last known-good version in minutes.'),
], ['Reason', 'Explanation'])
SP(doc)

# Add deployment diagram
SP(doc)
H(doc, 'Reference: System Deployment Methods')
doc.add_picture(deploy_path, width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
B(doc, 'Four deployment strategies: Direct Cutover (highest risk/lowest cost) through '
       'Pilot Conversion (lowest risk/highest preparation), relevant to selecting the '
       'appropriate go-live approach for the deployment plan.')

doc.save('/workspace/lab10.docx')
print('lab10.docx created successfully.')
