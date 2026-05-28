import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

# ═══════════════════════════════════════════════════════════════
# DIAGRAM 1 – Design Activities flow
# ═══════════════════════════════════════════════════════════════
def make_design_activities():
    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor('#f0f4f8')
    ax.set_xlim(0, 14); ax.set_ylim(0, 7); ax.axis('off')
    ax.set_title('Systems Design Activities – Overview', fontsize=12,
                 fontweight='bold', pad=8)

    activities = [
        (1.1,  3.5, '#1a4a7a', '#dbeafe', '1\nEnvironment\nDesign',     'Hardware, network,\ninfrastructure'),
        (3.3,  3.5, '#166534', '#dcfce7', '2\nUser Interface\nDesign',   'Screens, forms,\nreports, menus'),
        (5.5,  3.5, '#854d0e', '#fef9c3', '3\nData Design',              'Database schema,\ntables, keys'),
        (7.7,  3.5, '#6b21a8', '#f3e8ff', '4\nProcess Design',           'Modules, programs,\nalgorithms'),
        (9.9,  3.5, '#9a3412', '#ffedd5', '5\nSecurity &\nControls',     'Auth, access,\nencryption, audit'),
        (12.1, 3.5, '#0f766e', '#ccfbf1', '6\nArchitecture\nDesign',     'Application\narchitecture, tiers'),
    ]

    for x, y, ec, fc, label, sub in activities:
        ax.add_patch(FancyBboxPatch((x-0.95, y-1.1), 1.9, 2.2,
                                   boxstyle='round,pad=0.15', lw=1.8,
                                   edgecolor=ec, facecolor=fc, zorder=5))
        ax.text(x, y+0.6, label, ha='center', va='center', fontsize=8,
                fontweight='bold', color=ec, zorder=6, multialignment='center')
        ax.text(x, y-0.5, sub, ha='center', va='center', fontsize=7.2,
                color='#334155', zorder=6, multialignment='center')

    # Arrows between boxes
    for x in [2.05, 4.25, 6.45, 8.65, 10.85]:
        ax.annotate('', xy=(x+0.2, 3.5), xytext=(x, 3.5),
                    arrowprops=dict(arrowstyle='->', color='#475569', lw=1.5), zorder=4)

    # Inputs banner
    ax.add_patch(FancyBboxPatch((0.1, 5.4), 5.5, 0.85,
                               boxstyle='round,pad=0.1', lw=1.4,
                               edgecolor='#1a4a7a', facecolor='#e0f2fe'))
    ax.text(2.85, 5.83, 'INPUTS: System Requirements Spec · Use Cases · DFDs · ERDs · Feasibility Study',
            ha='center', va='center', fontsize=8, color='#0c4a6e')

    # Outputs banner
    ax.add_patch(FancyBboxPatch((8.4, 5.4), 5.5, 0.85,
                               boxstyle='round,pad=0.1', lw=1.4,
                               edgecolor='#166534', facecolor='#dcfce7'))
    ax.text(11.15, 5.83, 'OUTPUTS: Design Spec · Database Schema · UI Prototypes · Architecture Docs',
            ha='center', va='center', fontsize=8, color='#14532d')

    # Arrow input → activity 1
    ax.annotate('', xy=(1.1, 4.6), xytext=(2.85, 5.4),
                arrowprops=dict(arrowstyle='->', color='#1a4a7a', lw=1.3), zorder=4)
    # Arrow activity 6 → outputs
    ax.annotate('', xy=(11.15, 5.4), xytext=(12.1, 4.6),
                arrowprops=dict(arrowstyle='->', color='#166534', lw=1.3), zorder=4)

    # Bottom note
    ax.text(7, 0.55, 'Security & Controls design affects ALL other design elements',
            ha='center', fontsize=8.5, style='italic', color='#9a3412',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffedd5',
                      edgecolor='#9a3412', lw=1.2))

    plt.tight_layout()
    path = '/workspace/lab7_design_activities.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Design activities diagram saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# DIAGRAM 2 – Fraud Triangle
# ═══════════════════════════════════════════════════════════════
def make_fraud_triangle():
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.axis('off')
    ax.set_title('The Fraud Triangle', fontsize=13, fontweight='bold', pad=8)

    # Triangle vertices
    vtop  = (5.0, 6.3)
    vbl   = (1.0, 1.1)
    vbr   = (9.0, 1.1)

    triangle = plt.Polygon([vtop, vbl, vbr], closed=True,
                           facecolor='#fee2e2', edgecolor='#991b1b',
                           linewidth=2.5, zorder=3)
    ax.add_patch(triangle)

    # Vertex labels – boxes
    def vtx_box(ax, x, y, title, desc, fc, ec, ha_align, va_align):
        ax.add_patch(FancyBboxPatch((x-1.55 if ha_align=='right' else x-1.55 if ha_align=='center' else x+0.05,
                                     y-0.55 if va_align=='top' else y+0.05),
                                   3.0, 1.1, boxstyle='round,pad=0.12',
                                   facecolor=fc, edgecolor=ec, lw=1.6, zorder=6))
        bx = x-0.05 if ha_align=='right' else x+1.55 if ha_align=='left' else x
        ax.text(bx, y+(0.2 if va_align=='top' else 0.7), title,
                ha='center', va='center', fontsize=9, fontweight='bold', color=ec, zorder=7)
        ax.text(bx, y+(-0.2 if va_align=='top' else 0.3), desc,
                ha='center', va='center', fontsize=7.8, color='#374151', zorder=7,
                multialignment='center')

    # Top – Opportunity
    ax.add_patch(FancyBboxPatch((3.25, 6.45), 3.5, 1.0,
                               boxstyle='round,pad=0.12', facecolor='#fef9c3',
                               edgecolor='#854d0e', lw=1.8, zorder=6))
    ax.text(5.0, 7.15, 'OPPORTUNITY', ha='center', va='center',
            fontsize=9.5, fontweight='bold', color='#854d0e', zorder=7)
    ax.text(5.0, 6.82, 'Weak controls, system vulnerabilities\nDesigner has MOST control here',
            ha='center', va='center', fontsize=7.8, color='#374151', zorder=7,
            multialignment='center')

    # Bottom-left – Pressure
    ax.add_patch(FancyBboxPatch((-1.3, -0.1), 3.5, 1.0,
                               boxstyle='round,pad=0.12', facecolor='#dbeafe',
                               edgecolor='#1a4a7a', lw=1.8, zorder=6))
    ax.text(0.45, 0.6, 'PRESSURE / INCENTIVE', ha='center', va='center',
            fontsize=9.5, fontweight='bold', color='#1a4a7a', zorder=7)
    ax.text(0.45, 0.2, 'Financial stress, personal problems\nHard to control by designer',
            ha='center', va='center', fontsize=7.8, color='#374151', zorder=7,
            multialignment='center')

    # Bottom-right – Rationalisation
    ax.add_patch(FancyBboxPatch((7.8, -0.1), 3.5, 1.0,
                               boxstyle='round,pad=0.12', facecolor='#dcfce7',
                               edgecolor='#166534', lw=1.8, zorder=6))
    ax.text(9.55, 0.6, 'RATIONALISATION', ha='center', va='center',
            fontsize=9.5, fontweight='bold', color='#166534', zorder=7)
    ax.text(9.55, 0.2, '"Everyone does it", moral justification\nHard to control by designer',
            ha='center', va='center', fontsize=7.8, color='#374151', zorder=7,
            multialignment='center')

    # Centre note
    ax.text(5.0, 3.4, 'FRAUD occurs when\nall three elements\nare present',
            ha='center', va='center', fontsize=9.5, fontweight='bold',
            color='#991b1b', zorder=7, multialignment='center',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                      edgecolor='#991b1b', lw=1.5))

    plt.tight_layout()
    path = '/workspace/lab7_fraud_triangle.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Fraud triangle saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# DIAGRAM 3 – Symmetric (Single-Key) Encryption
# ═══════════════════════════════════════════════════════════════
def make_encryption():
    fig, ax = plt.subplots(figsize=(13, 5))
    fig.patch.set_facecolor('#f0f4f8')
    ax.set_xlim(0, 13); ax.set_ylim(0, 5); ax.axis('off')
    ax.set_title('Single-Key (Symmetric) Encryption Process', fontsize=12,
                 fontweight='bold', pad=8)

    def box(ax, x, y, w, h, text, fc, ec, fs=9):
        ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
                                   boxstyle='round,pad=0.15', lw=1.8,
                                   edgecolor=ec, facecolor=fc, zorder=5))
        ax.text(x, y, text, ha='center', va='center', fontsize=fs,
                fontweight='bold', zorder=6, multialignment='center', color=ec)

    def arr(ax, x1, y1, x2, y2, lbl='', loy=0.22):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='#334155', lw=2), zorder=4)
        if lbl:
            ax.text((x1+x2)/2, (y1+y2)/2+loy, lbl, ha='center', va='bottom',
                    fontsize=8, color='#334155', style='italic')

    # Sender side
    box(ax, 1.1, 2.5, 1.7, 1.0, 'Plaintext\nMessage', '#dcfce7', '#166534')
    arr(ax, 1.95, 2.5, 2.9, 2.5, '')
    box(ax, 3.5, 2.5, 1.6, 1.0, 'Encryption\nAlgorithm', '#dbeafe', '#1a4a7a')

    # Shared key (top)
    box(ax, 6.5, 4.3, 2.2, 0.7, '[KEY]  Shared Secret Key', '#fef9c3', '#854d0e', fs=8.5)
    arr(ax, 5.0, 3.9, 4.1, 3.0, 'encrypt with key', loy=0.15)
    arr(ax, 8.0, 3.9, 8.9, 3.0, 'decrypt with key', loy=0.15)

    # Ciphertext (middle)
    arr(ax, 4.3, 2.5, 5.6, 2.5, '')
    box(ax, 6.5, 2.5, 2.0, 1.0, 'Ciphertext\n(Encrypted)', '#f3e8ff', '#6b21a8')
    ax.annotate('', xy=(7.85, 2.5), xytext=(8.8, 2.5),
                arrowprops=dict(arrowstyle='<-', color='#334155', lw=2), zorder=4)

    # Receiver side
    box(ax, 9.4, 2.5, 1.6, 1.0, 'Decryption\nAlgorithm', '#dbeafe', '#1a4a7a')
    arr(ax, 10.2, 2.5, 11.1, 2.5, '')
    box(ax, 11.9, 2.5, 1.7, 1.0, 'Plaintext\nMessage', '#dcfce7', '#166534')

    # Labels
    ax.text(2.6, 1.2, 'SENDER', ha='center', fontsize=9, fontweight='bold',
            color='#1a4a7a',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#dbeafe',
                      edgecolor='#1a4a7a', lw=1))
    ax.text(10.4, 1.2, 'RECEIVER', ha='center', fontsize=9, fontweight='bold',
            color='#1a4a7a',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#dbeafe',
                      edgecolor='#1a4a7a', lw=1))
    ax.text(6.5, 1.2, 'Transmitted over\nunsecured channel',
            ha='center', fontsize=8, color='#991b1b', style='italic',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#fee2e2',
                      edgecolor='#991b1b', lw=1))

    # Key exchange problem note
    ax.text(6.5, 0.4, '⚠  Key Distribution Problem: both parties must share the same secret key securely BEFORE communication',
            ha='center', fontsize=8, color='#9a3412', style='italic')

    plt.tight_layout()
    path = '/workspace/lab7_encryption.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Encryption diagram saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# Build diagrams
# ═══════════════════════════════════════════════════════════════
da_path  = make_design_activities()
ft_path  = make_fraud_triangle()
enc_path = make_encryption()


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

def tbl(doc, rows_data, headers):
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

# ── Title ────────────────────────────────────────────────────
t = doc.add_heading('BN314 – System Architecture', 0)
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
s = doc.add_heading('Lecture 7: Systems Design – Laboratory Activity', 1)
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)

# ════════════════════════════════════════════════════════════
# Q1
# ════════════════════════════════════════════════════════════
H(doc, 'Question 1: Systems Analysis vs Systems Design')
tbl(doc, [
    ('Objective',
     'Understand and document WHAT the system must do — gather and model business requirements, current processes, and user needs.',
     'Determine HOW the system will be built — translate requirements into a detailed blueprint for construction.'),
    ('Focus',
     'Problem domain: existing processes, data flows, user requirements, and system constraints.',
     'Solution domain: hardware, software, databases, user interfaces, security, and architecture.'),
    ('Question answered',
     '"What does the system need to do?"',
     '"How will we build it?"'),
    ('Deliverables',
     'Requirements specification, DFDs, use cases, ERDs, feasibility study.',
     'Design specification, database schema, UI prototypes, architecture diagrams, security plan.'),
], ['Aspect', 'Systems Analysis', 'Systems Design'])
SP(doc)

# ════════════════════════════════════════════════════════════
# Q2
# ════════════════════════════════════════════════════════════
H(doc, 'Question 2: Inputs and Outputs of Systems Design')
B(doc, 'Inputs:')
BU(doc, 'System requirements specification (from systems analysis)')
BU(doc, 'Use case descriptions and use case diagrams')
BU(doc, 'Data Flow Diagrams (DFDs) and Entity-Relationship Diagrams (ERDs)')
BU(doc, 'Feasibility study and project constraints (budget, timeline, technology)')
BU(doc, 'Business rules and regulatory/compliance requirements')
BU(doc, 'Existing infrastructure inventory (hardware, software, network)')
SP(doc)
B(doc, 'Outputs:')
BU(doc, 'Systems design specification document')
BU(doc, 'Database design (schema, table structures, normalisation plan)')
BU(doc, 'User interface prototypes and screen layouts')
BU(doc, 'Application/program design (modules, algorithms, pseudocode)')
BU(doc, 'Network and hardware architecture plan')
BU(doc, 'Security and controls design')
BU(doc, 'Test plan and acceptance criteria')
SP(doc)

# ════════════════════════════════════════════════════════════
# Q3
# ════════════════════════════════════════════════════════════
H(doc, 'Question 3: Design Activities – List and Description')
B(doc, 'The diagram below shows the six design activities and their relationships:')
doc.add_picture(da_path, width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)
tbl(doc, [
    ('1. Environment Design',
     'Defines the physical and technical environment: hardware, servers, network topology, cloud vs on-premise, operating systems, and infrastructure needed to run the system.'),
    ('2. User Interface (UI) Design',
     'Designs screens, forms, menus, reports, and navigation flows. Focuses on usability, accessibility, and how users interact with the system.'),
    ('3. Data Design',
     'Translates the logical data model (ERD) into a physical database design — tables, columns, data types, keys, indexes, and storage optimisation.'),
    ('4. Process Design',
     'Defines application programs, modules, algorithms, and program logic (pseudocode, flowcharts, structured English) that implement the system\'s functions.'),
    ('5. Security & Controls Design',
     'Designs authentication, authorisation, access controls, encryption, audit trails, integrity controls, and fraud prevention mechanisms.'),
    ('6. Architecture Design',
     'Defines how components are organised into tiers (presentation, business logic, data), selects architectural patterns (MVC, microservices), and ensures scalability and maintainability.'),
], ['Activity', 'Description'])
SP(doc)

# ════════════════════════════════════════════════════════════
# Q4
# ════════════════════════════════════════════════════════════
H(doc, 'Question 4: Why Is the Environment "Described" While Other Elements Are "Designed"?')
B(doc,
  'The environment is described rather than designed because it largely consists of '
  'external, pre-existing infrastructure constraints — hardware vendors, network '
  'configurations, cloud platforms, and operating systems — over which the system '
  'designer has limited control. The designer does not create these components from '
  'scratch; they document what environment exists or will be procured, and specify '
  'the technical requirements the system must operate within.')
SP(doc)
B(doc,
  'In contrast, elements like the user interface, database, and application programs '
  'are genuinely designed from scratch by the project team. The analyst has full creative '
  'control over screen layouts, table structures, module logic, and security mechanisms — '
  'these are built, not just described. The environment description sets the boundary '
  'conditions within which design decisions for all other elements must fit.')
SP(doc)

# ════════════════════════════════════════════════════════════
# Q5
# ════════════════════════════════════════════════════════════
H(doc, 'Question 5: Models Developed During Each Design Activity')
tbl(doc, [
    ('Environment Design',    'Network topology diagrams, hardware configuration diagrams, deployment diagrams (UML), infrastructure specification sheets.'),
    ('UI Design',             'Wireframes, mockups, screen navigation diagrams, storyboards, prototype screens, report layouts.'),
    ('Data Design',           'Physical data model (PDM), database schema, table/column definitions, data dictionary updates, normalisation worksheets.'),
    ('Process Design',        'Structure charts, program flowcharts, pseudocode / structured English, module hierarchy diagrams, sequence diagrams.'),
    ('Security & Controls',   'Access control matrix, threat models, audit log specifications, encryption key management plans, integrity control tables.'),
    ('Architecture Design',   'Component diagrams (UML), package diagrams, tier/layer architecture diagrams, deployment diagrams.'),
], ['Design Activity', 'Models / Deliverables Produced'])
SP(doc)

# ════════════════════════════════════════════════════════════
# Q6
# ════════════════════════════════════════════════════════════
H(doc, 'Question 6: Key Elements of the Environment Description')
tbl(doc, [
    ('Hardware',        'Servers (web, application, database), client devices, printers, barcode scanners, and other peripheral devices.'),
    ('Network',         'Network topology (LAN, WAN, cloud), bandwidth requirements, protocols (TCP/IP, HTTPS), firewall and DMZ configuration.'),
    ('Software Platform','Operating system, web server, application server, DBMS (e.g., PostgreSQL, Oracle), middleware, and third-party APIs.'),
    ('Cloud/Hosting',   'Decision between on-premise, cloud (AWS, Azure, GCP), hybrid; availability zones, storage tiers, and SLAs.'),
    ('Development Tools','IDE, version control (Git), CI/CD pipelines, testing frameworks, and deployment tools.'),
    ('Regulatory/Compliance Environment', 'Data residency requirements, privacy laws (GDPR, Privacy Act), industry standards (PCI-DSS, ISO 27001) that constrain the environment.'),
], ['Element', 'Description'])
SP(doc)

# ════════════════════════════════════════════════════════════
# Q7
# ════════════════════════════════════════════════════════════
H(doc, 'Question 7: Three Examples of Application Components')
BB(doc, '1. Presentation Layer Component – ',
   'The web or mobile front end that handles all user interaction (e.g., a React.js web '
   'application presenting enrolment forms, dashboards, and reports to students and staff).')
BB(doc, '2. Business Logic Layer Component – ',
   'A middleware module that implements business rules (e.g., a fee calculation engine that '
   'determines tuition fees based on enrolment type, course credits, and discount eligibility).')
BB(doc, '3. Data Access Layer Component – ',
   'A database interface module (e.g., an ORM or repository class) that handles all read/write '
   'operations to the database, abstracting SQL queries from the business logic layer.')
SP(doc)
B(doc, 'Additional examples: authentication service, email notification module, reporting engine, '
       'payment processing API wrapper, batch job scheduler.')
SP(doc)

# ════════════════════════════════════════════════════════════
# Q8
# ════════════════════════════════════════════════════════════
H(doc, 'Question 8: Security and Controls – Impact on Other Design Elements')
B(doc,
  'Security and controls design is cross-cutting — it directly impacts every other '
  'design element:')
tbl(doc, [
    ('User Interface',     'Login screens, CAPTCHA, session timeout messages, role-based menu visibility, and masked input fields (password fields) must all be built into the UI.'),
    ('Data Design',        'Encryption of sensitive columns (e.g., passwords stored as hashed values), audit timestamp fields, and access logs require additional table columns and structures.'),
    ('Process Design',     'Every module must include input validation, authorisation checks, and error handling to prevent injection attacks, buffer overflows, and unauthorised operations.'),
    ('Environment Design', 'Firewalls, intrusion detection systems, TLS certificates, and VPNs must be specified in the infrastructure configuration.'),
    ('Architecture Design','Security zones (DMZ, internal network), single sign-on (SSO) integration, and zero-trust architecture decisions shape the overall system architecture.'),
], ['Affected Element', 'Security Impact'])
SP(doc)

# ════════════════════════════════════════════════════════════
# Q9
# ════════════════════════════════════════════════════════════
H(doc, 'Question 9: Integrity Controls vs Security Controls')
tbl(doc, [
    ('Definition',
     'Mechanisms that ensure data entered into the system is accurate, complete, consistent, and valid.',
     'Mechanisms that protect the system and its data from unauthorised access, modification, disclosure, or destruction.'),
    ('Primary goal',
     'Data quality and correctness.',
     'Confidentiality, integrity (in the security sense), and availability (CIA triad).'),
    ('Examples',
     'Required field validation, range checks, referential integrity (foreign keys), format checks.',
     'Password authentication, role-based access control, encryption, audit logs.'),
    ('Who they protect against',
     'Accidental errors by legitimate users (typos, wrong values, missing data).',
     'Malicious actors, unauthorised insiders, external attackers.'),
], ['Aspect', 'Integrity Controls', 'Security Controls'])
SP(doc)
BB(doc, 'Why no separate design activity? ',
   'Both integrity and security controls are deeply embedded in the design of the '
   'user interface (forms, validation messages), data layer (constraints, keys), '
   'and processes (validation logic, authorisation checks). Designing them as a '
   'separate, isolated activity would lead to fragmented, inconsistent implementations. '
   'Instead, they are addressed as a unified activity that cross-cuts all other design '
   'elements, ensuring controls are integrated — not bolted on — at every level.')
SP(doc)

# ════════════════════════════════════════════════════════════
# Q10
# ════════════════════════════════════════════════════════════
H(doc, 'Question 10: Four Types of Integrity Controls for Input Forms')
tbl(doc, [
    ('1. Existence / Required Field Check',
     'Ensures that mandatory fields are not left blank before the form is submitted.',
     '"Student ID is required." Error shown if the field is empty on submit.',
     'Most frequently seen — virtually every online form enforces required fields.'),
    ('2. Range / Limit Check',
     'Validates that a numeric or date value falls within an acceptable range.',
     '"Age must be between 16 and 100." Date of birth cannot be in the future.',
     'Very common in financial and booking systems.'),
    ('3. Format / Pattern Check',
     'Verifies that data matches a required format or pattern (e.g., email, phone, postcode).',
     '"Email address must be in the format name@domain.com."',
     'Common in registration and payment forms.'),
    ('4. Consistency / Cross-Field Check',
     'Ensures that values in two or more related fields are logically consistent with each other.',
     '"End date cannot be earlier than start date." Confirm password must match password.',
     'Common in booking, scheduling, and account creation forms.'),
], ['Control Type', 'Description', 'Example', 'Frequency'])
SP(doc)
B(doc,
  'Why they are important: Without integrity controls, inaccurate data enters the database, '
  'leading to incorrect reports, failed transactions, poor decisions, and costly data cleansing '
  'exercises. They are the first line of defence for data quality.')
SP(doc)

# ════════════════════════════════════════════════════════════
# Q11
# ════════════════════════════════════════════════════════════
H(doc, 'Question 11: Two Primary Objectives of Security Controls')
BB(doc, '1. Prevent unauthorised access: ',
   'Ensure that only authenticated and authorised users can access the system, '
   'its data, and its functions. This includes protecting against external attackers, '
   'unauthorised insiders, and misuse of legitimate credentials (authentication, '
   'access control lists, role-based authorisation, encryption).')
BB(doc, '2. Protect data confidentiality, integrity, and availability (CIA triad): ',
   'Ensure that sensitive data is not disclosed to unauthorised parties (confidentiality), '
   'that data is not altered without authorisation (integrity), and that the system '
   'remains available to authorised users when needed (availability).')
SP(doc)

# ════════════════════════════════════════════════════════════
# Q12
# ════════════════════════════════════════════════════════════
H(doc, 'Question 12: The Fraud Triangle')
B(doc, 'The fraud triangle, developed by criminologist Donald Cressey, states that fraud '
       'occurs when three conditions are simultaneously present:')
SP(doc)
tbl(doc, [
    ('Pressure /\nIncentive',
     'A motivating force — typically financial (debt, greed, gambling) or personal (coercion) — that drives a person to consider committing fraud.',
     'An employee facing financial hardship is tempted to manipulate expense claims.',
     'Low — system designers cannot control personal circumstances or motivations.'),
    ('Opportunity',
     'A weakness in the system, process, or controls that makes fraud possible — a gap that can be exploited without detection.',
     'Lack of audit trails, no separation of duties, no access controls on financial data.',
     'HIGH — system designers directly control this element through security controls, audit logs, access restrictions, and integrity checks.'),
    ('Rationalisation',
     'The fraudster\'s internal justification — convincing themselves the act is acceptable ("I\'ll pay it back", "the company owes me").',
     '"I\'ve been underpaid for years, so taking this is fair."',
     'Low — system designers cannot influence personal ethics or moral reasoning.'),
], ['Element', 'Definition', 'Example', 'Designer Control'])
SP(doc)
B(doc,
  'Greatest control: Opportunity. System designers exercise the greatest control over '
  'opportunity by implementing strong access controls, mandatory audit trails, separation '
  'of duties, dual-approval workflows, and integrity/security controls that eliminate or '
  'minimise exploitable gaps in the system.')
doc.add_picture(ft_path, width=Inches(5.5))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)

# ════════════════════════════════════════════════════════════
# Q13
# ════════════════════════════════════════════════════════════
H(doc, 'Question 13: Authentication, Access Control Lists, and Authorisation')
BB(doc, 'Authentication: ',
   'The process of verifying that a user, system, or device is who or what it claims to be. '
   'It answers the question "Who are you?" Methods include: passwords, PINs, biometrics '
   '(fingerprint, facial recognition), smart cards, and multi-factor authentication (MFA) '
   '— combining two or more of something you know, have, and are.')
SP(doc)
BB(doc, 'Access Control List (ACL): ',
   'A table or list attached to a resource (file, database table, network port, API endpoint) '
   'that specifies which users or roles are permitted to perform which operations (read, write, '
   'execute, delete) on that resource. ACLs are the mechanism that enforces authorisation at '
   'the resource level. Example: a database ACL might grant role "Lecturer" SELECT access '
   'on the Grades table but deny INSERT/UPDATE/DELETE.')
SP(doc)
BB(doc, 'Authorisation: ',
   'The process of determining what actions an authenticated user is permitted to perform. '
   'It answers the question "What are you allowed to do?" After authentication confirms '
   'identity, authorisation checks the user\'s role and permissions against the ACL before '
   'granting access. Example: an authenticated Student can view their own grades but cannot '
   'view another student\'s grades or modify any grade records.')
SP(doc)

# ════════════════════════════════════════════════════════════
# Q14
# ════════════════════════════════════════════════════════════
H(doc, 'Question 14: Single-Key (Symmetric) Encryption')
B(doc,
  'In symmetric encryption, the same secret key is used by both the sender to encrypt '
  'plaintext into ciphertext and by the receiver to decrypt the ciphertext back into '
  'plaintext. Both parties must possess an identical copy of the shared key before '
  'secure communication can begin. Common symmetric algorithms include AES (Advanced '
  'Encryption Standard), DES, and 3DES.')
SP(doc)
doc.add_picture(enc_path, width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)
B(doc, 'How it works (step by step):')
BU(doc, 'Step 1 – Key sharing: sender and receiver agree on and securely exchange a shared secret key (this is the critical challenge).')
BU(doc, 'Step 2 – Encryption: the sender applies an encryption algorithm (e.g., AES-256) to the plaintext using the key, producing ciphertext.')
BU(doc, 'Step 3 – Transmission: the ciphertext is sent over the network; even if intercepted, it is unreadable without the key.')
BU(doc, 'Step 4 – Decryption: the receiver applies the same algorithm with the same key to reverse the ciphertext back to plaintext.')
SP(doc)
tbl(doc, [
    ('Speed',            'Significantly faster than asymmetric encryption; suitable for encrypting large volumes of data (files, database records, network streams).'),
    ('Simplicity',       'Straightforward algorithm; well-understood and widely implemented in hardware and software.'),
    ('Low overhead',     'Requires less computational power than asymmetric methods; used for bulk data encryption in protocols like TLS (for data transfer after the handshake).'),
    ('Strong security',  'AES-256 is effectively unbreakable with current technology when properly implemented.'),
], ['Strength', 'Explanation'])
SP(doc)
tbl(doc, [
    ('Key distribution problem',  'Both parties must share the same key securely before communication begins. Transmitting the key over an insecure channel risks interception — creating a "chicken and egg" problem.'),
    ('Key management complexity', 'In a system with n users, n(n-1)/2 unique keys are needed for all pairs to communicate privately. Managing thousands of keys is operationally challenging.'),
    ('No non-repudiation',        'Because both parties have the same key, it is impossible to prove which party sent a particular message — either could have encrypted it.'),
    ('Key compromise risk',       'If the shared key is stolen or leaked, all past and future communications encrypted with that key are compromised.'),
], ['Weakness', 'Explanation'])
SP(doc)

doc.save('/workspace/lab7.docx')
print('lab7.docx created successfully.')
