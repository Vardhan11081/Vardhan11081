import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from matplotlib.patches import FancyArrowPatch
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

# ═══════════════════════════════════════════════════════════════
# DIAGRAM 1 – Change Request Management Process (flowchart)
# ═══════════════════════════════════════════════════════════════
def make_change_process():
    fig, ax = plt.subplots(figsize=(10, 13))
    fig.patch.set_facecolor('#f0f4f8')
    ax.set_xlim(0, 10); ax.set_ylim(0, 13); ax.axis('off')
    ax.set_title('Change Request Management Process', fontsize=12,
                 fontweight='bold', pad=8)

    def process_box(ax, x, y, w, h, text, fc='#dbeafe', ec='#1a4a7a', fs=8.5):
        ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
                                   boxstyle='round,pad=0.12', lw=1.8,
                                   edgecolor=ec, facecolor=fc, zorder=5))
        ax.text(x, y, text, ha='center', va='center', fontsize=fs,
                fontweight='bold', color=ec, zorder=6, multialignment='center')

    def diamond(ax, x, y, w, h, text, fc='#fef9c3', ec='#854d0e'):
        pts = [[x, y+h/2],[x+w/2, y],[x, y-h/2],[x-w/2, y]]
        poly = plt.Polygon(pts, closed=True, facecolor=fc, edgecolor=ec, lw=1.8, zorder=5)
        ax.add_patch(poly)
        ax.text(x, y, text, ha='center', va='center', fontsize=7.8,
                fontweight='bold', color=ec, zorder=6, multialignment='center')

    def arr(ax, x1, y1, x2, y2, lbl='', side='right'):
        ax.annotate('', xy=(x2,y2), xytext=(x1,y1),
                    arrowprops=dict(arrowstyle='->', color='#475569', lw=1.4), zorder=4)
        if lbl:
            ox = 0.15 if side=='right' else -0.15
            ax.text((x1+x2)/2+ox, (y1+y2)/2, lbl, ha='center', va='center',
                    fontsize=7.5, color='#475569', style='italic')

    # ── Normal flow (centre column) ──────────────────────────
    steps = [
        (5.0, 12.2, '#dcfce7', '#166534', 'START:\nChange Request Submitted\n(by user, analyst, or manager)'),
        (5.0, 10.8, '#dbeafe', '#1a4a7a', 'Step 1: Log Change Request\n(CR Form – assign CR ID, date, priority)'),
        (5.0,  9.4, '#dbeafe', '#1a4a7a', 'Step 2: Initial Assessment\n(IT Manager reviews feasibility & impact)'),
        (5.0,  7.6, '#fef9c3', '#854d0e', 'Decision:\nEmergency\nChange?'),   # diamond
        (5.0,  5.8, '#dbeafe', '#1a4a7a', 'Step 3: Impact & Cost Analysis\n(Effort, risk, schedule, resources)'),
        (5.0,  4.5, '#fef9c3', '#854d0e', 'Decision:\nApproved by\nChange Board?'),  # diamond
        (5.0,  3.1, '#dbeafe', '#1a4a7a', 'Step 4: Schedule & Assign\n(Developer, timeline, version)'),
        (5.0,  2.0, '#dbeafe', '#1a4a7a', 'Step 5: Implement & Test\n(Code, unit test, regression test)'),
        (5.0,  0.9, '#dcfce7', '#166534', 'Step 6: Deploy, Document & Close\n(Release notes, CR closed)'),
    ]

    for i, (x, y, fc, ec, text) in enumerate(steps):
        if 'Decision' in text:
            diamond(ax, x, y, 3.2, 1.1, text.replace('Decision:\n',''), fc=fc, ec=ec)
        else:
            process_box(ax, x, y, 4.5, 0.75, text, fc, ec)

    # Down arrows (normal flow)
    for ya, yb in [(11.85,11.15),(11.15,9.78),(9.03,8.17),(7.18,6.15),
                   (6.15,4.82),(4.17,3.47),(3.47,2.37),(2.37,1.26)]:
        # skip diamond positions
        arr(ax, 5.0, ya, 5.0, yb)

    # Emergency branch (right side)
    ax.annotate('', xy=(8.5, 7.6), xytext=(6.6, 7.6),
                arrowprops=dict(arrowstyle='->', color='#991b1b', lw=1.6), zorder=4)
    ax.text(7.55, 7.8, 'YES\n(Emergency)', ha='center', fontsize=7.5,
            color='#991b1b', fontweight='bold')
    process_box(ax, 8.8, 7.6, 2.6, 1.1,
                'CONTINGENCY:\nEmergency Change\nFast-Track Approval\n(Senior Mgr + IT Head)',
                '#fee2e2', '#991b1b', 7.5)
    arr(ax, 8.8, 7.05, 8.8, 5.8)
    arr(ax, 8.8, 5.8, 7.25, 5.8)

    # NO (reject) branch
    ax.annotate('', xy=(1.5, 4.5), xytext=(3.4, 4.5),
                arrowprops=dict(arrowstyle='->', color='#6b21a8', lw=1.4), zorder=4)
    ax.text(2.45, 4.75, 'NO', ha='center', fontsize=7.5,
            color='#6b21a8', fontweight='bold')
    process_box(ax, 1.2, 4.5, 2.0, 0.65, 'Reject &\nNotify User',
                '#f3e8ff', '#6b21a8', 7.5)

    # Labels
    ax.text(5.0, 8.17, 'NO (Standard)', ha='center', fontsize=7.5,
            color='#475569', style='italic')

    plt.tight_layout()
    path = '/workspace/lab11_change_process.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Change process saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# DIAGRAM 2 – Four Types of System Maintenance
# ═══════════════════════════════════════════════════════════════
def make_maintenance_types():
    fig, ax = plt.subplots(figsize=(13, 6))
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_xlim(0, 13); ax.set_ylim(0, 6); ax.axis('off')
    ax.set_title('Four Types of System Maintenance', fontsize=12,
                 fontweight='bold', pad=8)

    types = [
        (1.6,  3.0, '#dbeafe', '#1a4a7a', 'CORRECTIVE\nMAINTENANCE',
         'Fixing defects and\nerrors discovered\nafter deployment',
         '• Fix login bug\n  crashing Firefox\n• Correct invoice\n  calculation error'),
        (4.8,  3.0, '#dcfce7', '#166634', 'ADAPTIVE\nMAINTENANCE',
         'Modifying system\nto adapt to new\nenvironments/laws',
         '• Upgrade for new\n  OS/browser version\n• Update for new\n  tax legislation'),
        (8.0,  3.0, '#fef9c3', '#854d0e', 'PERFECTIVE\nMAINTENANCE',
         'Improving existing\nfunctions for better\nperformance/usability',
         '• Optimise slow\n  database queries\n• Redesign UI\n  for better UX'),
        (11.2, 3.0, '#f3e8ff', '#6b21a8', 'PREVENTIVE\nMAINTENANCE',
         'Proactive work to\nprevent future\nfailures/problems',
         '• Refactor legacy\n  spaghetti code\n• Add monitoring\n  & alert systems'),
    ]

    for x, y, fc, ec, title, desc, examples in types:
        ax.add_patch(FancyBboxPatch((x-1.45, y-2.2), 2.9, 4.4,
                                   boxstyle='round,pad=0.12', lw=1.8,
                                   edgecolor=ec, facecolor=fc, zorder=5))
        ax.text(x, y+1.85, title, ha='center', va='center', fontsize=9.5,
                fontweight='bold', color=ec, zorder=6, multialignment='center')
        ax.text(x, y+0.65, desc, ha='center', va='center', fontsize=8,
                color='#374151', zorder=6, multialignment='center')
        ax.plot([x-1.35, x+1.35], [y+0.1, y+0.1], color=ec, lw=1, ls='--')
        ax.text(x, y-0.85, examples, ha='center', va='center', fontsize=7.5,
                color='#334155', zorder=6, multialignment='center')

    # % distribution note
    dist = [(1.6,'~20%'),(4.8,'~25%'),(8.0,'~50%'),(11.2,'~5%')]
    for x, pct in dist:
        ax.text(x, 0.3, pct, ha='center', fontsize=9, fontweight='bold', color='#334155')
    ax.text(6.5, 0.05, 'Typical industry distribution of maintenance effort',
            ha='center', fontsize=8, color='#6b7280', style='italic')

    plt.tight_layout()
    path = '/workspace/lab11_maintenance.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Maintenance types saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# DIAGRAM 3 – Risk Management Framework
# ═══════════════════════════════════════════════════════════════
def make_risk_framework():
    fig, ax = plt.subplots(figsize=(13, 6))
    fig.patch.set_facecolor('#f0f4f8')
    ax.set_xlim(0, 13); ax.set_ylim(0, 6); ax.axis('off')
    ax.set_title('Risk Management Framework – Identification, Assessment, Control',
                 fontsize=12, fontweight='bold', pad=8)

    phases = [
        (2.0, 3.0, '#dbeafe', '#1a4a7a', 'RISK\nIDENTIFICATION',
         'Brainstorming, SWOT,\nchecklist review,\nexpert interviews,\nhistorical data',
         'Outputs:\nRisk register\n(list of threats)'),
        (5.5, 3.0, '#fef9c3', '#854d0e', 'RISK\nASSESSMENT',
         'Estimate Likelihood\n(High/Med/Low)\nEstimate Impact\n(High/Med/Low)\nPriority = L × I',
         'Outputs:\nRisk matrix\nPriority ranking'),
        (9.0, 3.0, '#dcfce7', '#166534', 'RISK\nCONTROL',
         'Avoid · Mitigate\nTransfer · Accept\nImplement controls\nMonitor & review',
         'Outputs:\nRisk response\nplan + monitoring'),
    ]

    for x, y, fc, ec, title, methods, outputs in phases:
        ax.add_patch(FancyBboxPatch((x-1.65, y-2.2), 3.3, 4.4,
                                   boxstyle='round,pad=0.12', lw=1.8,
                                   edgecolor=ec, facecolor=fc, zorder=5))
        ax.text(x, y+1.8, title, ha='center', va='center', fontsize=9.5,
                fontweight='bold', color=ec, zorder=6, multialignment='center')
        ax.text(x, y+0.5, methods, ha='center', va='center', fontsize=8,
                color='#374151', zorder=6, multialignment='center')
        ax.plot([x-1.55, x+1.55], [y-0.2, y-0.2], color=ec, lw=1, ls='--')
        ax.text(x, y-1.1, outputs, ha='center', va='center', fontsize=8,
                color='#374151', fontweight='bold', zorder=6, multialignment='center')

    # Arrows
    for x1, x2 in [(3.65, 3.85), (7.15, 7.35)]:
        ax.annotate('', xy=(x2, 3.0), xytext=(x1, 3.0),
                    arrowprops=dict(arrowstyle='->', color='#64748b', lw=2), zorder=4)

    # Feedback loop
    ax.annotate('', xy=(2.0, 0.5), xytext=(9.0, 0.5),
                arrowprops=dict(arrowstyle='->', color='#6b21a8', lw=1.4,
                                connectionstyle='arc3,rad=-0.3'), zorder=3)
    ax.text(5.5, 0.18, 'Continuous monitoring & review cycle',
            ha='center', fontsize=8, color='#6b21a8', style='italic')

    # Risk matrix mini
    ax.add_patch(FancyBboxPatch((11.3, 1.5), 1.5, 1.5,
                               boxstyle='round,pad=0.05', lw=1.2,
                               edgecolor='#854d0e', facecolor='#fef9c3'))
    ax.text(12.05, 2.75, 'Risk Matrix', ha='center', fontsize=7.5,
            fontweight='bold', color='#854d0e')
    cells = [('#fee2e2','H×H'),('#fef9c3','H×M'),('#dcfce7','H×L'),
             ('#fef9c3','M×H'),('#fef9c3','M×M'),('#dcfce7','M×L'),
             ('#dcfce7','L×H'),('#dcfce7','L×M'),('#dcfce7','L×L')]
    for idx,(fc,lbl) in enumerate(cells):
        row, col = divmod(idx, 3)
        cx = 11.35 + col*0.5 + 0.25
        cy = 2.5 - row*0.35
        ax.add_patch(FancyBboxPatch((cx-0.22, cy-0.15), 0.44, 0.3,
                                   boxstyle='square,pad=0', facecolor=fc,
                                   edgecolor='#aaa', lw=0.5, zorder=6))
        ax.text(cx, cy, lbl, ha='center', va='center', fontsize=5.5, zorder=7)

    plt.tight_layout()
    path = '/workspace/lab11_risk.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Risk framework saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# Build diagrams
# ═══════════════════════════════════════════════════════════════
cr_path   = make_change_process()
maint_path = make_maintenance_types()
risk_path  = make_risk_framework()


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

def form_row(doc, label, field='line', choices=None, size=10):
    p = doc.add_paragraph()
    r = p.add_run(f'{label}  '); r.bold = True; r.font.size = Pt(size)
    if field == 'line':
        p.add_run('_' * 52).font.size = Pt(size)
    elif field == 'choices' and choices:
        p.add_run('  ' + '    '.join([f'☐ {c}' for c in choices])).font.size = Pt(size)
    elif field == 'scale':
        p.add_run('  ☐ Low    ☐ Medium    ☐ High    ☐ Critical').font.size = Pt(size)
    elif field == 'yn':
        p.add_run('  ☐ Yes    ☐ No').font.size = Pt(size)
    elif field == 'multi':
        p.add_run('\n' + '_'*62 + '\n' + '_'*62).font.size = Pt(size)
    return p

# ── Title ───────────────────────────────────────────────────
t = doc.add_heading('BN314 – System Architecture', 0)
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
s = doc.add_heading('Lecture 11: Managing System Support and Security – Laboratory Activity', 1)
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)

# ══════════════════════════════════════════════════════════
# GROUP ACTIVITY
# ══════════════════════════════════════════════════════════
H(doc, 'PART A – Group Activity', level=1)
SP(doc)

# ── GA1 ─────────────────────────────────────────────────
H(doc, 'Group Activity 1: Change Request Management Process and Form')

B(doc, 'The flowchart below illustrates the standard change request process, '
       'including an emergency/contingency path for critical changes:')
doc.add_picture(cr_path, width=Inches(4.5))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)

B(doc, 'Process Summary:')
steps_cr = [
    ('Submit',     'User, analyst, or manager submits a Change Request (CR) using the standard form.'),
    ('Log',        'IT team logs the CR in the change management system, assigns a unique CR ID, date, and initial priority.'),
    ('Assess',     'IT Manager performs an initial feasibility check. If the change is an emergency, fast-track contingency approval is invoked immediately.'),
    ('Impact Analysis', 'For non-emergency changes: cost, effort, risk, and schedule impact are analysed and documented.'),
    ('Change Board Review', 'Change Advisory Board (CAB) or IT Manager approves or rejects. Rejected CRs are logged and the requester is notified.'),
    ('Schedule & Assign', 'Approved CRs are scheduled into a release, assigned to a developer, and linked to a version in the VCS.'),
    ('Implement & Test', 'Developer implements the change; unit, regression, and UAT are performed.'),
    ('Deploy & Close', 'Change is deployed to production, release notes are updated, and the CR is formally closed.'),
    ('Contingency Plan', 'For emergency changes: a Senior Manager and IT Head provide immediate verbal/email approval. The change is implemented on an emergency basis, fully documented within 24 hours, and reviewed at the next CAB meeting.'),
]
tbl(doc, steps_cr, ['Step', 'Description'])
SP(doc)

doc.add_heading('CHANGE REQUEST FORM', level=3).alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)
form_row(doc, 'CR ID (auto-assigned):')
form_row(doc, 'Date Submitted:')
form_row(doc, 'Requested By (Name / Dept):')
form_row(doc, 'System / Module Affected:')
form_row(doc, 'Change Type:', 'choices',
         ['Corrective', 'Adaptive', 'Perfective', 'Preventive', 'Emergency'])
form_row(doc, 'Priority:', 'scale')
form_row(doc, 'Description of Change Requested:', 'multi')
form_row(doc, 'Business Justification:', 'multi')
form_row(doc, 'Impact on Other Systems / Users:', 'multi')
form_row(doc, 'Estimated Effort (hours):')
form_row(doc, 'Proposed Implementation Date:')
form_row(doc, 'Test Plan / Rollback Plan:', 'multi')
form_row(doc, 'Approved By (Change Board):')
form_row(doc, 'Approval Date:')
form_row(doc, 'Assigned Developer:')
form_row(doc, 'Actual Completion Date:')
form_row(doc, 'Post-Implementation Notes:', 'multi')
SP(doc)

# ── GA2 ─────────────────────────────────────────────────
H(doc, 'Group Activity 2: Version Control Software – Research Memo')
SP(doc)
doc.add_heading('MEMORANDUM', level=3)
B(doc, 'TO:      IT Management Team\n'
       'FROM:    Systems Analysis Group\n'
       'DATE:    May 2026\n'
       'RE:      Version Control Software Evaluation – Git / GitHub')
SP(doc)
BB(doc, 'Product Evaluated: ', 'Git (open-source VCS) with GitHub (cloud-hosted repository platform)')
BB(doc, 'Vendor: ', 'Git – open source (linus Torvalds, 2005); GitHub – Microsoft (github.com)')
BB(doc, 'Cost: ', 'Git: free and open source. GitHub: Free tier (unlimited public/private repos for individuals); '
         'GitHub Teams: USD $4/user/month; GitHub Enterprise: USD $21/user/month.')
SP(doc)
B(doc, 'Key Features:')
tbl(doc, [
    ('Distributed Version Control',
     'Every developer has a full local copy of the repository history, enabling offline work and fast operations without a central server.'),
    ('Branching and Merging',
     'Lightweight branches allow developers to work on features, hotfixes, or experiments in isolation. Merge and pull request workflows enforce code review before integration.'),
    ('Pull Requests & Code Review',
     'GitHub pull requests enable peer review, automated checks, and discussion before code is merged into the main branch — critical for quality control.'),
    ('CI/CD Integration',
     'GitHub Actions enables automated build, test, and deployment pipelines triggered on every commit or pull request, supporting DevOps workflows.'),
    ('Issue & Project Tracking',
     'Built-in issue tracker, project boards, and milestone tracking link code changes directly to bug reports and feature requests.'),
    ('Security Scanning',
     'Dependabot automatically identifies vulnerable dependencies; code scanning detects security issues in code before deployment.'),
    ('Audit Trail',
     'Complete, tamper-evident history of every commit, merge, and deployment — essential for compliance and incident investigation.'),
    ('Access Control',
     'Fine-grained repository and branch permissions; integration with enterprise SSO/SAML for organisational access management.'),
], ['Feature', 'Description'])
SP(doc)
B(doc, 'Findings: Git with GitHub is the industry standard for version control, used by '
       'over 100 million developers worldwide. Its branching model, pull request workflow, '
       'and CI/CD integration make it suitable for teams of any size. The free tier is '
       'sufficient for educational and small commercial projects. For enterprise use, '
       'the security scanning, audit logging, and SAML SSO features justify the subscription cost.')
SP(doc)

# ── GA3 ─────────────────────────────────────────────────
H(doc, 'Group Activity 3: Recent Security Breach – Documentation and Prevention')
BB(doc, 'Incident: ', 'MOVEit Transfer Mass Data Breach (2023)')
BB(doc, 'Disclosed: ', 'May–June 2023')
BB(doc, 'Threat Actor: ', 'CL0P Ransomware Group')
BB(doc, 'Affected organisations: ',
   'Over 2,700 organisations worldwide including government agencies (US Department of Energy, '
   'UK payroll provider Zellis), universities, airlines, and financial institutions. '
   'Estimated 93+ million individuals affected.')
SP(doc)
BB(doc, 'What happened: ',
   'CL0P exploited a critical SQL injection zero-day vulnerability (CVE-2023-34362) in '
   'Progress Software\'s MOVEit Transfer file-transfer application. The vulnerability '
   'allowed unauthenticated attackers to submit crafted SQL queries, escalate privileges, '
   'and exfiltrate data from the connected databases. Attackers moved laterally to '
   'extract sensitive customer and employee data including names, Social Security '
   'numbers, payroll data, and health records before the vulnerability was publicly known.')
SP(doc)
B(doc, 'How the attack could have been avoided:')
tbl(doc, [
    ('Timely patching & vulnerability management',
     'Progress Software released a patch on May 31, 2023. Organisations with automated patch management and short patch-deployment SLAs (< 24–48 hours for critical vulnerabilities) would have had less exposure time.'),
    ('Input validation & parameterised queries',
     'The root cause was a SQL injection flaw. Mandatory use of parameterised queries / prepared statements in all database-interacting code would have made the vulnerability impossible to exploit.'),
    ('Network segmentation',
     'MOVEit servers with unrestricted outbound internet access allowed data exfiltration. Strict egress filtering and network segmentation would have limited or prevented data exfiltration even after initial compromise.'),
    ('Web Application Firewall (WAF)',
     'A properly configured WAF with SQL injection detection rules could have blocked or alerted on the malicious SQL payloads before they reached the database.'),
    ('Principle of least privilege',
     'The application\'s database account had excessive privileges. Using least-privilege database accounts limits the scope of data accessible through a SQL injection attack.'),
    ('Continuous vulnerability scanning',
     'Regular automated scanning of internet-facing applications (DAST/SAST tools) would have detected the SQL injection vulnerability internally before attackers exploited it.'),
    ('Zero-trust architecture',
     'Treating file-transfer servers as untrusted segments, requiring continuous authentication and restricting lateral movement, would have contained the blast radius of the breach.'),
], ['Prevention Measure', 'Explanation'])
SP(doc)

# ══════════════════════════════════════════════════════════
# WRITTEN QUESTIONS
# ══════════════════════════════════════════════════════════
H(doc, 'PART B – Written Questions', level=1)
SP(doc)

# ── WQ1 ─────────────────────────────────────────────────
H(doc, 'Written Question 1: Four Types of System Maintenance')
doc.add_picture(maint_path, width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)
tbl(doc, [
    ('Corrective',
     'Diagnosing and fixing defects, bugs, and errors discovered after the system has been deployed. Reactive — triggered by failure reports.',
     '1. A payroll module calculates overtime incorrectly for part-time staff — fix is applied.\n'
     '2. A login screen crashes on Mozilla Firefox v115 — browser compatibility bug is patched.'),
    ('Adaptive',
     'Modifying the system to accommodate changes in its operating environment — new hardware, OS updates, regulatory changes, or third-party API changes.',
     '1. System is updated to comply with updated GST reporting requirements under new tax legislation.\n'
     '2. Application is migrated from Python 3.8 to Python 3.12 following end-of-life announcement.'),
    ('Perfective',
     'Enhancing or improving existing features to improve performance, usability, or functionality — not fixing bugs, but making good things better. The most common type (~50% of effort).',
     '1. Slow database queries in the student search function are optimised, reducing response time from 4 sec to 0.3 sec.\n'
     '2. The reporting module UI is redesigned with a more intuitive dashboard after user feedback.'),
    ('Preventive',
     'Proactively modifying the system to prevent future failures — refactoring brittle code, improving documentation, adding monitoring, or addressing technical debt before it causes problems.',
     '1. Legacy spaghetti code in the invoicing module is refactored into clean, testable components to prevent future maintenance failures.\n'
     '2. Automated health-check monitoring and alerting is added to detect memory leaks before they cause outages.'),
], ['Type', 'Description', 'Two Examples'])
SP(doc)

# ── WQ2 ─────────────────────────────────────────────────
H(doc, 'Written Question 2: Should Newly Hired Analysts Be Assigned to Maintenance Projects?')
BB(doc, 'Position: No — with qualifications. ',
   'Newly hired systems analysts should generally NOT be assigned to maintenance '
   'projects as their primary role, for the following reasons:')
SP(doc)
B(doc, 'Arguments against assigning new analysts to maintenance:')
BU(doc, 'Lack of system knowledge: maintenance requires deep understanding of the existing codebase, data structures, and business rules. New analysts lack this context and would spend most of their time reading legacy documentation rather than adding value.')
BU(doc, 'Poor learning environment: maintenance is often reactive, ad-hoc, and isolated — it does not expose new analysts to the full SDLC (requirements gathering, design, testing, deployment), limiting their professional development.')
BU(doc, 'Risk to system stability: without sufficient context, a new analyst making maintenance changes is more likely to introduce new defects or unintended side effects in production systems.')
BU(doc, 'Motivation and retention: maintenance work (especially corrective) is often repetitive and can be frustrating. Assigning new hires primarily to maintenance can lead to low morale and early attrition.')
SP(doc)
B(doc, 'When it can be appropriate:')
BU(doc, 'Structured mentoring: if paired with a senior analyst who provides context, code review, and oversight, maintenance can be an effective way for new analysts to learn a system incrementally.')
BU(doc, 'Simple, well-documented fixes: new analysts can handle low-risk, well-defined corrective maintenance tickets under supervision to build confidence and system familiarity.')
BU(doc, 'Recommended approach: rotate new analysts through maintenance for a defined onboarding period (e.g., 4–6 weeks with mentoring), then transition them to new development projects.')
SP(doc)

# ── WQ3 ─────────────────────────────────────────────────
H(doc, 'Written Question 3: What-If Analysis and Spreadsheet in Capacity Planning')
BB(doc, 'What-if analysis: ',
   'A decision-support technique that explores the impact of changing one or more '
   'input variables on system outputs. It answers "What would happen to system '
   'performance, cost, or capacity if [condition] changes?" It allows managers to '
   'model scenarios and evaluate options before committing to infrastructure changes.')
SP(doc)
B(doc, 'How a spreadsheet supports capacity planning:')
BU(doc, 'Variable modelling: a spreadsheet model captures current capacity metrics (users, transactions/hour, storage GB, response time) as input variables. Changing a variable instantly recalculates all dependent outputs.')
BU(doc, 'Growth scenarios: by adjusting "expected user growth rate" (e.g., +20% per quarter), the spreadsheet projects future load, identifies when current infrastructure will be exceeded, and estimates upgrade costs.')
BU(doc, 'Example: a model with columns [Month, Active Users, Transactions/Day, DB Size (GB), Server CPU %, Estimated Response Time (ms)] using growth formulas allows an IT manager to ask: "If users grow 30% next quarter, when will response time exceed our 2-second SLA?" and plan server upgrades accordingly.')
BU(doc, 'Cost modelling: what-if scenarios can compare the cost of on-premise hardware upgrades vs cloud auto-scaling to find the most cost-effective capacity strategy.')
SP(doc)

# ── WQ4 ─────────────────────────────────────────────────
H(doc, 'Written Question 4: Release Methodology and Version Control Importance')
BB(doc, 'Release methodology: ',
   'A structured process and set of policies governing how software changes are '
   'packaged, tested, approved, and deployed to production. It defines the release '
   'schedule (continuous/weekly/monthly), versioning scheme (semantic versioning: '
   'MAJOR.MINOR.PATCH), testing gates, rollback procedures, and change communication '
   'to stakeholders. Common approaches include:')
BU(doc, 'Continuous Delivery (CD): every validated commit is automatically deployable to production.')
BU(doc, 'Sprint-based releases: releases aligned to agile sprint cycles (e.g., every 2 weeks).')
BU(doc, 'Scheduled major releases: large, infrequent releases with fixed dates (e.g., quarterly).')
SP(doc)
B(doc, 'Why version control is important:')
tbl(doc, [
    ('Traceability',   'Every change is linked to who made it, when, and why — essential for audits and defect root-cause analysis.'),
    ('Rollback',       'If a release introduces a critical bug, the team can revert to the previous stable version in minutes.'),
    ('Parallel development', 'Multiple developers and teams work concurrently on separate branches without conflicts.'),
    ('Release integrity', 'A specific version tag guarantees that exactly the right code is deployed to production — no more, no less.'),
    ('Compliance',     'Regulated industries (finance, healthcare) require complete audit trails of system changes. VCS provides this automatically.'),
    ('Disaster recovery', 'If production systems are compromised or destroyed, the VCS repository is the source of truth for rebuilding.'),
], ['Reason', 'Explanation'])
SP(doc)

# ── WQ5 ─────────────────────────────────────────────────
H(doc, 'Written Question 5: Response Time, Bandwidth, Throughput, and Turnaround Time')
tbl(doc, [
    ('Response Time',
     'The elapsed time from when a user submits a request (e.g., clicks a button) to when the system displays the first output. Measures user-perceived interactive performance.',
     'A student searches for a course; response time = time from pressing Search to when results appear on screen. Target: < 2 seconds.'),
    ('Bandwidth',
     'The maximum data transfer capacity of a network connection, measured in bits per second (Mbps, Gbps). Defines the upper limit of how much data can flow per unit time.',
     'A 1 Gbps office network can transfer a maximum of 1,000 Mb of data per second between systems.'),
    ('Throughput',
     'The actual amount of work or data successfully processed by a system per unit of time. Throughput is the real-world achieved rate, which is always less than or equal to bandwidth.',
     'A web server processes 850 requests/second under peak load even though its network bandwidth supports 2,000 requests/second — throughput is constrained by CPU, not bandwidth.'),
    ('Turnaround Time',
     'The total elapsed time from when a job or batch task is submitted to when its complete output is available. Used for batch processing rather than interactive queries.',
     'A nightly payroll batch job submitted at 11:00 PM and completed at 1:00 AM has a turnaround time of 2 hours.'),
], ['Term', 'Definition', 'Example'])
SP(doc)
B(doc, 'Relationship: Bandwidth sets the upper bound for throughput. Throughput measures '
       'actual system capacity. Response time and turnaround time measure the user\'s '
       'experience of that capacity — both are degraded when throughput approaches '
       'bandwidth limits or when server processing bottlenecks reduce effective throughput.')
SP(doc)

# ── WQ6 ─────────────────────────────────────────────────
H(doc, 'Written Question 6: Risk Management – Identification, Assessment, and Control')
doc.add_picture(risk_path, width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)
BB(doc, 'Risk Management: ',
   'A systematic process of identifying, analysing, and responding to threats that '
   'could adversely affect an information system\'s security, availability, integrity, '
   'or achievement of business objectives.')
SP(doc)
BB(doc, '1. Risk Identification: ',
   'The process of discovering and documenting all potential threats to the system. '
   'Methods include: brainstorming sessions, SWOT analysis, threat modelling (STRIDE), '
   'review of historical incidents and near-misses, vulnerability scanning, and expert '
   'interviews. Output: a risk register listing all identified risks with their potential '
   'causes and consequences.')
SP(doc)
BB(doc, '2. Risk Assessment: ',
   'Evaluating each identified risk on two dimensions: '
   'Likelihood (how probable is it that this risk will occur? — High/Medium/Low) and '
   'Impact (how severe would the consequences be? — High/Medium/Low). '
   'Priority = Likelihood × Impact. A risk matrix visualises which risks require '
   'immediate attention (High × High) vs those that can be monitored (Low × Low).')
SP(doc)
BB(doc, '3. Risk Control: ',
   'Deciding how to respond to each prioritised risk:')
BU(doc, 'Avoid – eliminate the activity or condition that creates the risk (e.g., stop storing unnecessary sensitive data).')
BU(doc, 'Mitigate – reduce the likelihood or impact through controls (e.g., add encryption, MFA, backup systems).')
BU(doc, 'Transfer – shift the financial risk to a third party (e.g., cyber insurance, outsourcing to a certified provider).')
BU(doc, 'Accept – acknowledge low-priority risks and monitor them without active intervention.')
B(doc, 'Risk management is a continuous cycle — risks are re-assessed as the system, environment, and threat landscape evolve.')
SP(doc)

# ── WQ7 ─────────────────────────────────────────────────
H(doc, 'Written Question 7: Technical Obsolescence – Example and Threat to Information Systems')
BB(doc, 'Definition: ',
   'Technical obsolescence occurs when hardware, software, or technology components '
   'become outdated, unsupported, or incompatible with current systems — making '
   'them a liability rather than an asset to the information system.')
SP(doc)
BB(doc, 'Example – Windows Server 2003 / Internet Explorer: ',
   'Many organisations continued running mission-critical applications on Windows Server 2003 '
   'long after Microsoft ended mainstream support in 2010 and extended support in 2015. '
   'Similarly, Internet Explorer 11 (retired June 2022) was still in active use at many '
   'enterprises. Both products stopped receiving security patches, meaning every newly '
   'discovered vulnerability was permanently unpatched.')
SP(doc)
B(doc, 'How technical obsolescence threatens an information system:')
tbl(doc, [
    ('Security vulnerability',
     'Unpatched, end-of-life software accumulates known, public vulnerabilities with no available fix. Attackers specifically target obsolete systems — the WannaCry ransomware attack (2017) primarily exploited unpatched Windows XP and Server 2003 systems, causing USD $4 billion in damages globally.'),
    ('Incompatibility',
     'Modern browsers, APIs, operating systems, and security protocols (TLS 1.3) drop support for old standards. Obsolete components cannot integrate with modern systems, forcing costly workarounds or isolating the organisation from new services.'),
    ('Vendor support loss',
     'No patches, no bug fixes, no technical support. When failures occur, the organisation has no recourse — no hotline, no updates, no community support.'),
    ('Compliance failure',
     'Regulatory frameworks (PCI-DSS, GDPR, ISO 27001, HIPAA) require use of supported, patched software. Running end-of-life software can directly violate compliance requirements and expose the organisation to fines and audits.'),
    ('Talent scarcity',
     'IT staff skilled in obsolete technologies (e.g., COBOL mainframes, Windows NT) are increasingly rare and expensive, making maintenance and support progressively harder.'),
], ['Threat', 'Explanation'])
SP(doc)
B(doc, 'Mitigation: organisations should maintain a technology roadmap with end-of-life dates '
       'for all components, begin migration planning 12–18 months before EOL, and enforce '
       'a policy of not deploying components without a supported maintenance lifecycle.')

doc.save('/workspace/lab11.docx')
print('lab11.docx created successfully.')
