import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# ═══════════════════════════════════════════════════════════════
# DIAGRAM 1 – Decision Table (Student Enrolment Discount Example)
# ═══════════════════════════════════════════════════════════════
def make_decision_table():
    fig, ax = plt.subplots(figsize=(13, 6))
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_xlim(0, 13); ax.set_ylim(0, 6); ax.axis('off')
    ax.set_title('Decision Table – Student Loan Application Processing\n(TechNova Training Division)',
                 fontsize=11, fontweight='bold', pad=8)

    # Column widths and row heights
    col_labels = ['Condition / Action', 'Rule 1', 'Rule 2', 'Rule 3', 'Rule 4',
                  'Rule 5', 'Rule 6', 'Rule 7', 'Rule 8']
    col_x = [0, 2.6, 4.1, 5.6, 7.1, 8.6, 9.9, 11.2, 12.5]
    col_w = [2.6, 1.5, 1.5, 1.5, 1.5, 1.3, 1.3, 1.3, 0.5]

    # Section headers
    sections = [
        (0.0, 5.5, 5.2, 0.5, '#1a4a7a', 'white', 'CONDITIONS'),
        (0.0, 3.2, 5.2, 0.5, '#b85a00', 'white', 'ACTIONS'),
    ]

    # Row data: (label, [R1..R8])
    rows = [
        # Conditions
        ('C1: GPA ≥ 3.0?',         ['Y','Y','Y','Y','N','N','N','N'], '#dbeafe'),
        ('C2: Full-time student?',  ['Y','Y','N','N','Y','Y','N','N'], '#dbeafe'),
        ('C3: Income < $30K?',      ['Y','N','Y','N','Y','N','Y','N'], '#dbeafe'),
        # Actions
        ('A1: Approve Full Loan',   ['X','-','-','-','-','-','-','-'], '#fef3c7'),
        ('A2: Approve Partial Loan',['—','X','X','-','X','-','-','-'], '#fef3c7'),
        ('A3: Request Guarantor',   ['—','—','—','X','—','X','X','-'], '#fef3c7'),
        ('A4: Reject Application',  ['—','—','—','—','—','—','—','X'], '#fef3c7'),
    ]

    row_ys = [4.85, 4.2, 3.55, 2.85, 2.2, 1.55, 0.9]
    row_h  = 0.6

    # Header row
    header_y = 5.3
    ax.add_patch(FancyBboxPatch((0, header_y), 13, 0.6,
                               boxstyle='square,pad=0',
                               facecolor='#1a4a7a', edgecolor='white', lw=0.5))
    ax.text(1.3, header_y+0.3, 'Condition / Action',
            ha='center', va='center', fontsize=8.5, color='white', fontweight='bold')
    for i, (x, lbl) in enumerate(zip(col_x[1:], col_labels[1:]), 1):
        ax.text(x + col_w[i]/2, header_y+0.3, lbl,
                ha='center', va='center', fontsize=8.5, color='white', fontweight='bold')

    # Section divider labels
    ax.add_patch(FancyBboxPatch((-0.05, 3.25), 0.15, 2.1,
                               boxstyle='square,pad=0', facecolor='#1a4a7a'))
    ax.text(-0.0, 4.3, 'C\nO\nN\nD', ha='center', va='center',
            fontsize=7, color='white', fontweight='bold', rotation=0)
    ax.add_patch(FancyBboxPatch((-0.05, 0.85), 0.15, 2.4,
                               boxstyle='square,pad=0', facecolor='#b85a00'))
    ax.text(-0.0, 2.0, 'A\nC\nT\nN', ha='center', va='center',
            fontsize=7, color='white', fontweight='bold', rotation=0)

    for ri, (label, vals, bg) in enumerate(rows):
        y = row_ys[ri]
        # Label cell
        ax.add_patch(FancyBboxPatch((0, y-row_h/2), col_x[1], row_h,
                                   boxstyle='square,pad=0', facecolor=bg,
                                   edgecolor='#aaa', lw=0.5))
        ax.text(0.1, y, label, ha='left', va='center', fontsize=8.5)
        # Value cells
        for ci, val in enumerate(vals):
            cx = col_x[ci+1]
            cw = col_w[ci+1]
            cell_bg = '#bbf7d0' if val == 'X' else ('#fee2e2' if val == '—' else bg)
            ax.add_patch(FancyBboxPatch((cx, y-row_h/2), cw, row_h,
                                       boxstyle='square,pad=0', facecolor=cell_bg,
                                       edgecolor='#aaa', lw=0.5))
            ax.text(cx + cw/2, y, val, ha='center', va='center',
                    fontsize=9, fontweight='bold',
                    color='#166534' if val=='X' else ('#991b1b' if val=='—' else '#333'))

    # Divider line between conditions and actions
    ax.plot([0, 13], [3.22, 3.22], color='#1a4a7a', lw=1.5, ls='--')

    # Legend
    legend = [
        mpatches.Patch(color='#bbf7d0', label='X = Action applies'),
        mpatches.Patch(color='#fee2e2', label='— = Action does not apply'),
        mpatches.Patch(color='#dbeafe', label='Y/N = Condition true/false'),
    ]
    ax.legend(handles=legend, loc='lower right', fontsize=7.5, framealpha=0.9)

    plt.tight_layout()
    path = '/workspace/lab5_decision_table.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Decision table saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# DIAGRAM 2 – Decision Tree (same loan application scenario)
# ═══════════════════════════════════════════════════════════════
def make_decision_tree():
    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_xlim(0, 14); ax.set_ylim(0, 8); ax.axis('off')
    ax.set_title('Decision Tree – Student Loan Application Processing\n(Same rules as decision table above)',
                 fontsize=11, fontweight='bold', pad=8)

    DEC_C = '#dbeafe'; DEC_E = '#1a4a7a'
    ACT_C = '#dcfce7'; ACT_E = '#166534'
    REJ_C = '#fee2e2'; REJ_E = '#991b1b'
    PAR_C = '#fef9c3'; PAR_E = '#854d0e'
    GUA_C = '#f3e8ff'; GUA_E = '#6b21a8'

    def diamond(ax, x, y, w, h, label, fc=DEC_C, ec=DEC_E):
        dx, dy = w/2, h/2
        pts = [[x, y+dy],[x+dx, y],[x, y-dy],[x-dx, y]]
        poly = plt.Polygon(pts, closed=True, facecolor=fc, edgecolor=ec, lw=1.6, zorder=5)
        ax.add_patch(poly)
        ax.text(x, y, label, ha='center', va='center', fontsize=8.5,
                fontweight='bold', zorder=6, multialignment='center')

    def leaf(ax, x, y, label, fc=ACT_C, ec=ACT_E):
        box = FancyBboxPatch((x-1.1, y-0.3), 2.2, 0.6,
                             boxstyle='round,pad=0.1',
                             facecolor=fc, edgecolor=ec, lw=1.4, zorder=5)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=8,
                fontweight='bold', zorder=6, multialignment='center',
                color=ec)

    def arr(ax, x1, y1, x2, y2, label='', side='left'):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='#444', lw=1.3), zorder=4)
        mx = (x1+x2)/2; my = (y1+y2)/2
        off = -0.25 if side == 'left' else 0.25
        ax.text(mx+off, my+0.12, label, ha='center', va='bottom',
                fontsize=8, color='#555', style='italic', zorder=7)

    # Root
    diamond(ax, 7, 7.2, 2.8, 1.0, 'GPA ≥ 3.0?')

    # Level 1 – YES branch (left)
    arr(ax, 5.6, 7.2, 3.5, 5.8, 'YES', 'left')
    diamond(ax, 3.5, 5.4, 2.6, 0.9, 'Full-time\nStudent?')

    # Level 1 – NO branch (right)
    arr(ax, 8.4, 7.2, 10.5, 5.8, 'NO', 'right')
    diamond(ax, 10.5, 5.4, 2.6, 0.9, 'Full-time\nStudent?')

    # Level 2 – GPA≥3 & Full-time
    arr(ax, 2.2, 5.4, 1.5, 4.0, 'YES', 'left')
    diamond(ax, 1.5, 3.6, 2.2, 0.85, 'Income\n< $30K?')

    # Level 2 – GPA≥3 & Part-time
    arr(ax, 4.8, 5.4, 5.5, 4.0, 'NO', 'right')
    diamond(ax, 5.5, 3.6, 2.2, 0.85, 'Income\n< $30K?')

    # Level 2 – GPA<3 & Full-time
    arr(ax, 9.2, 5.4, 8.5, 4.0, 'YES', 'left')
    diamond(ax, 8.5, 3.6, 2.2, 0.85, 'Income\n< $30K?')

    # Level 2 – GPA<3 & Part-time
    arr(ax, 11.8, 5.4, 12.5, 4.0, 'NO', 'right')
    diamond(ax, 12.5, 3.6, 2.2, 0.85, 'Income\n< $30K?')

    # Leaves – GPA≥3 & Full-time
    arr(ax, 0.9, 3.2, 0.9, 2.1, 'YES', 'left')
    leaf(ax, 0.9, 1.8, 'Approve\nFull Loan', ACT_C, ACT_E)
    arr(ax, 2.1, 3.2, 2.1, 2.1, 'NO', 'right')
    leaf(ax, 2.1, 1.8, 'Approve\nPartial Loan', PAR_C, PAR_E)

    # Leaves – GPA≥3 & Part-time
    arr(ax, 4.9, 3.2, 4.9, 2.1, 'YES', 'left')
    leaf(ax, 4.9, 1.8, 'Approve\nPartial Loan', PAR_C, PAR_E)
    arr(ax, 6.1, 3.2, 6.1, 2.1, 'NO', 'right')
    leaf(ax, 6.1, 1.8, 'Request\nGuarantor', GUA_C, GUA_E)

    # Leaves – GPA<3 & Full-time
    arr(ax, 7.9, 3.2, 7.9, 2.1, 'YES', 'left')
    leaf(ax, 7.9, 1.8, 'Approve\nPartial Loan', PAR_C, PAR_E)
    arr(ax, 9.1, 3.2, 9.1, 2.1, 'NO', 'right')
    leaf(ax, 9.1, 1.8, 'Request\nGuarantor', GUA_C, GUA_E)

    # Leaves – GPA<3 & Part-time
    arr(ax, 11.9, 3.2, 11.4, 2.1, 'YES', 'left')
    leaf(ax, 11.4, 1.8, 'Request\nGuarantor', GUA_C, GUA_E)
    arr(ax, 13.1, 3.2, 13.1, 2.1, 'NO', 'right')
    leaf(ax, 13.1, 1.8, 'Reject\nApplication', REJ_C, REJ_E)

    # Legend
    legend = [
        mpatches.Patch(color=DEC_C, edgecolor=DEC_E, label='Decision Node (diamond)'),
        mpatches.Patch(color=ACT_C, edgecolor=ACT_E, label='Approve Full Loan'),
        mpatches.Patch(color=PAR_C, edgecolor=PAR_E, label='Approve Partial Loan'),
        mpatches.Patch(color=GUA_C, edgecolor=GUA_E, label='Request Guarantor'),
        mpatches.Patch(color=REJ_C, edgecolor=REJ_E, label='Reject Application'),
    ]
    ax.legend(handles=legend, loc='lower left', fontsize=8, framealpha=0.92)

    plt.tight_layout()
    path = '/workspace/lab5_decision_tree.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Decision tree saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# DIAGRAM 3 – Data Dictionary structure diagram
# ═══════════════════════════════════════════════════════════════
def make_data_dict_diagram():
    fig, ax = plt.subplots(figsize=(13, 7))
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_xlim(0, 13); ax.set_ylim(0, 7); ax.axis('off')
    ax.set_title('Data Dictionary – Structure and Entry Types',
                 fontsize=12, fontweight='bold', pad=8)

    def box(ax, x, y, w, h, title, items, fc='#dbeafe', ec='#1a4a7a', tfc='#1a4a7a'):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                                   boxstyle='round,pad=0.15',
                                   facecolor=fc, edgecolor=ec, lw=1.6, zorder=4))
        ax.add_patch(FancyBboxPatch((x, y+h-0.5), w, 0.5,
                                   boxstyle='round,pad=0.05',
                                   facecolor=tfc, edgecolor=ec, lw=0, zorder=5))
        ax.text(x+w/2, y+h-0.25, title, ha='center', va='center',
                fontsize=8.5, fontweight='bold', color='white', zorder=6)
        for i, item in enumerate(items):
            ax.text(x+0.15, y+h-0.8-i*0.42, f'• {item}',
                    ha='left', va='center', fontsize=7.8, zorder=6)

    def arr(ax, x1, y1, x2, y2):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='#555', lw=1.4), zorder=3)

    # Central node
    ax.add_patch(plt.Circle((6.5, 3.5), 1.05, facecolor='#1a4a7a',
                            edgecolor='#0f2d5c', lw=2, zorder=5))
    ax.text(6.5, 3.5, 'Data\nDictionary', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white', zorder=6)

    # Entry type boxes
    boxes = [
        (0.3, 5.0, 3.0, 1.8, 'DATA ELEMENT',
         ['Name & alias', 'Description / meaning', 'Data type (text, int, date…)',
          'Length / format', 'Validation rules', 'Default & allowed values'],
         '#dbeafe', '#1a4a7a', '#1a4a7a'),
        (4.8, 5.1, 3.4, 1.7, 'DATA STRUCTURE',
         ['Name', 'Composition (elements)', 'Description / purpose',
          'Volume & frequency', 'Related processes'],
         '#dcfce7', '#166534', '#166534'),
        (9.0, 5.0, 3.7, 1.8, 'DATA STORE',
         ['Store ID & name', 'Description', 'Composition / elements',
          'Accessing processes', 'Volume of records', 'Organisation type'],
         '#fef9c3', '#854d0e', '#854d0e'),
        (0.3, 1.0, 3.2, 1.8, 'DATA FLOW',
         ['Flow name', 'Description', 'Source (process/entity)',
          'Destination', 'Data composition', 'Frequency / volume'],
         '#f3e8ff', '#6b21a8', '#6b21a8'),
        (4.8, 0.9, 3.4, 1.7, 'EXTERNAL ENTITY',
         ['Entity name', 'Description', 'Data flows in/out',
          'Notes & constraints'],
         '#fce7f3', '#9d174d', '#9d174d'),
        (9.0, 1.0, 3.7, 1.8, 'PROCESS DESCRIPTION',
         ['Process ID & name', 'Description / logic', 'Input data flows',
          'Output data flows', 'Structured English / decision table'],
         '#ffedd5', '#9a3412', '#9a3412'),
    ]

    for (x, y, w, h, title, items, fc, ec, tfc) in boxes:
        box(ax, x, y, w, h, title, items, fc, ec, tfc)

    # Arrows from central circle to boxes (approximate midpoints)
    connections = [
        (5.55, 4.4, 1.9, 6.1),    # top-left
        (6.5,  4.55, 6.5, 6.0),   # top-centre
        (7.45, 4.4, 10.5, 6.0),   # top-right
        (5.55, 2.6, 2.0, 2.6),    # bottom-left
        (6.5,  2.45, 6.5, 2.5),   # bottom-centre
        (7.45, 2.6, 10.8, 2.6),   # bottom-right
    ]
    for x1, y1, x2, y2 in connections:
        arr(ax, x1, y1, x2, y2)

    plt.tight_layout()
    path = '/workspace/lab5_data_dict.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Data dictionary diagram saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# Build diagrams
# ═══════════════════════════════════════════════════════════════
dd_path  = make_data_dict_diagram()
dt_path  = make_decision_table()
dtr_path = make_decision_tree()


# ═══════════════════════════════════════════════════════════════
# BUILD WORD DOCUMENT
# ═══════════════════════════════════════════════════════════════
doc = Document()

def heading(doc, text, level=2):
    p = doc.add_heading(text, level=level)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    return p

def body(doc, text, size=11):
    p = doc.add_paragraph(text)
    p.style.font.size = Pt(size)
    return p

def bullet(doc, text, size=11):
    p = doc.add_paragraph(text, style='List Bullet')
    p.style.font.size = Pt(size)
    return p

def nb(doc):
    doc.add_paragraph()

def bold_body(doc, label, rest, size=11):
    p = doc.add_paragraph()
    r = p.add_run(label)
    r.bold = True
    r.font.size = Pt(size)
    p.add_run(rest).font.size = Pt(size)
    return p

# ── Title ───────────────────────────────────────────────────────
t = doc.add_heading('BN314 – System Architecture', 0)
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
s = doc.add_heading('Lecture 5: Data and Process Modelling – Laboratory Activity', 1)
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
nb(doc)

# ════════════════════════════════════════════════════════════════
# Q1 – Data Dictionary
# ════════════════════════════════════════════════════════════════
heading(doc, 'Question 1: Data Dictionary – Description and Contents')

body(doc,
     'A data dictionary (also called a data repository or data encyclopaedia) is a '
     'structured, centralised reference that formally defines every piece of data used '
     'in an information system. It documents the meaning, format, origin, relationships, '
     'and usage of each data element, ensuring that every analyst, developer, and '
     'stakeholder uses consistent, unambiguous definitions throughout the project life cycle.')
nb(doc)
body(doc,
     'A data dictionary is created alongside — and directly linked to — Data Flow Diagrams '
     '(DFDs). Every data flow, data store, process, and external entity shown in a DFD '
     'has a corresponding entry in the data dictionary.')
nb(doc)

body(doc, 'Types of information contained in a data dictionary:')
nb(doc)

# Subtable of entry types
table_dd = doc.add_table(rows=7, cols=3)
table_dd.style = 'Table Grid'
hdr = table_dd.rows[0].cells
hdr[0].text = 'Entry Type'
hdr[1].text = 'What It Defines'
hdr[2].text = 'Typical Fields'
dd_rows = [
    ('Data Element\n(Field)',
     'The smallest unit of data that has meaning in the system (e.g., StudentID, CourseCode).',
     'Name, alias, description, data type, length/format, range of valid values, default value, validation rules, source'),
    ('Data Structure\n(Record)',
     'A named grouping of related data elements that together represent a real-world concept (e.g., StudentRecord).',
     'Name, description, component elements, volume, frequency, related DFD flows'),
    ('Data Flow',
     'A labelled arrow on a DFD representing data in motion between processes, entities, or stores.',
     'Flow name, description, source, destination, composition (which elements/structures it carries), frequency'),
    ('Data Store',
     'A repository where data is held at rest (e.g., Student Database, Invoice File).',
     'Store ID, name, description, composition, volume, accessing processes, organisation method (sequential, indexed…)'),
    ('External Entity',
     'A person, organisation, or system outside the scope that sends or receives data.',
     'Name, description, data flows in/out, assumptions and constraints'),
    ('Process Description\n(Mini-spec)',
     'The logic of a lowest-level (primitive) process — what it does with its input data to produce output.',
     'Process ID, name, description, input flows, output flows, processing logic (structured English / decision table / decision tree)'),
]
for i, (etype, defines, fields) in enumerate(dd_rows, 1):
    r = table_dd.rows[i].cells
    r[0].text = etype
    r[1].text = defines
    r[2].text = fields
for row in table_dd.rows:
    for cell in row.cells:
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(9.5)
nb(doc)

body(doc,
     'Example: A data element entry for "StudentID" in a university enrolment system '
     'might read: Name = StudentID | Alias = SID | Type = Integer | Length = 8 digits | '
     'Format = XXXXXXXX | Validation = Must be unique; assigned sequentially | '
     'Source = Enrolment System | Used in = Student Record, Enrolment Form, Grade Report.')
nb(doc)

body(doc, 'The diagram below illustrates the six entry types and their key fields:')
doc.add_picture(dd_path, width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
nb(doc)

body(doc, 'Why the data dictionary is important:')
bullet(doc, 'Eliminates ambiguity — everyone uses the same name and definition for each data element.')
bullet(doc, 'Supports system design — developers use it to build databases and validation rules.')
bullet(doc, 'Enables impact analysis — when a data element changes, the dictionary shows every process and flow affected.')
bullet(doc, 'Enforces data standards — ensures consistent formats, lengths, and constraints across the system.')
nb(doc)

# ════════════════════════════════════════════════════════════════
# Q2 – Decision Tables
# ════════════════════════════════════════════════════════════════
heading(doc, 'Question 2: Decision Tables – Purpose and Creation')

body(doc,
     'A decision table is a structured, matrix-style tool used to document and analyse '
     'complex business logic by showing all possible combinations of conditions and the '
     'corresponding actions that result from each combination. It is particularly useful '
     'when multiple conditions interact to produce different outcomes.')
nb(doc)

body(doc, 'Purpose of decision tables:')
bullet(doc, 'Completeness – ensure that every possible combination of conditions is accounted for, preventing gaps in business rules.')
bullet(doc, 'Clarity – present complex conditional logic in a compact, readable format that is easy to verify with stakeholders.')
bullet(doc, 'Consistency – detect conflicting or redundant rules that might exist in narrative specifications.')
bullet(doc, 'Testing foundation – each column (rule) in the table maps directly to a test case.')
bullet(doc, 'Process specification – used as mini-specs for the lowest-level processes in a DFD.')
nb(doc)

body(doc, 'How to create a decision table:')
bold_body(doc, 'Step 1 – Identify conditions: ',
          'List all conditions (questions that can be answered Yes/No or with limited values) that affect the outcome.')
bold_body(doc, 'Step 2 – Identify actions: ',
          'List all possible actions or outcomes that the system can take.')
bold_body(doc, 'Step 3 – Calculate rules: ',
          'For n binary conditions, there are 2ⁿ possible rule combinations. For 3 conditions: 2³ = 8 rules.')
bold_body(doc, 'Step 4 – Fill in condition entries: ',
          'For each rule (column), enter Y or N for each condition using a binary counting pattern.')
bold_body(doc, 'Step 5 – Fill in action entries: ',
          'For each rule, mark X (action applies) or — (action does not apply) for each action row.')
bold_body(doc, 'Step 6 – Simplify: ',
          'Combine rules that have identical actions but differ in only one condition (the differing condition becomes "–" meaning "irrelevant").')
bold_body(doc, 'Step 7 – Verify with stakeholders: ',
          'Review the completed table to confirm all rules are correct and complete.')
nb(doc)

body(doc,
     'Example: The following decision table shows loan application processing logic '
     'with 3 conditions (GPA, enrolment status, income) and 4 possible actions:')
doc.add_picture(dt_path, width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
nb(doc)

body(doc,
     'The table has 8 rules (2³ = 8) covering every combination of the three Yes/No '
     'conditions, with a clear, unambiguous action mapped to each combination.')
nb(doc)

# ════════════════════════════════════════════════════════════════
# Q3 – Decision Trees
# ════════════════════════════════════════════════════════════════
heading(doc, 'Question 3: Why Managers Prefer Decision Trees Over Decision Tables')

body(doc,
     'A decision tree is a graphical, branching diagram that shows the same conditional '
     'logic as a decision table, but presents it as a sequential left-to-right (or '
     'top-to-bottom) flow of decisions and outcomes. Each internal node is a decision '
     'point, each branch is a possible answer, and each leaf node is an action or outcome.')
nb(doc)

body(doc, 'Reasons managers prefer decision trees:')
bullet(doc,
       'Visual and intuitive: Decision trees mirror natural human reasoning — "if this, '
       'then go here; otherwise, go there." Managers can follow the logic without needing '
       'to understand how to read a matrix or count rule columns.')
bullet(doc,
       'Storytelling format: A tree tells the "story" of a decision from start to finish, '
       'making it easier to present in meetings, board briefings, and strategy discussions.')
bullet(doc,
       'Easier to explain to non-technical audiences: Stakeholders, clients, and executives '
       'with no IT background can understand a tree diagram far more readily than a decision '
       'table, which requires knowledge of how to interpret condition/action matrices.')
bullet(doc,
       'Shows sequence and priority: The order of decisions in a tree reflects the real-world '
       'sequence in which questions are asked (e.g., first check GPA, then employment status). '
       'Decision tables do not show this ordering explicitly.')
bullet(doc,
       'Highlights the path: Managers can trace a specific scenario from root to leaf, '
       'seeing exactly which path a particular case follows — useful for explaining '
       'outcomes to clients or auditors.')
bullet(doc,
       'Better for asymmetric logic: When not all conditions apply in every branch '
       '(some paths are shorter than others), a tree handles this naturally, whereas '
       'a decision table would require many "irrelevant" (–) entries.')
nb(doc)

body(doc, 'When decision tables are preferred instead:')
bullet(doc, 'When all combinations must be exhaustively documented (e.g., compliance, auditing).')
bullet(doc, 'When the number of conditions is large (a tree with 4+ conditions becomes very wide and hard to read).')
bullet(doc, 'When the goal is to detect gaps or redundancies in business rules systematically.')
nb(doc)

body(doc,
     'Decision tree for the same loan application scenario (equivalent to the table above):')
doc.add_picture(dtr_path, width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
nb(doc)
body(doc,
     'Notice that the tree makes each decision pathway immediately visible — a manager '
     'can follow any path from "GPA ≥ 3.0?" to the final outcome without scanning a matrix. '
     'Both diagrams encode identical logic; the choice depends on the audience and purpose.')
nb(doc)

# ════════════════════════════════════════════════════════════════
# Q4 – CASE Tools
# ════════════════════════════════════════════════════════════════
heading(doc, 'Question 4: Benefits and Shortcomings of CASE Tools for Process Modelling')

body(doc,
     'Computer-Aided Software Engineering (CASE) tools are software applications that '
     'automate, support, and manage the activities of the software development life cycle '
     '(SDLC), including requirements analysis, process modelling, data modelling, design, '
     'and code generation. Examples relevant to process modelling include: Visio, Lucidchart, '
     'Enterprise Architect, IBM Rational Rose, Sparx EA, draw.io, and Oracle Designer.')
nb(doc)

body(doc, 'Categories of CASE tools:')
bullet(doc, 'Upper CASE tools – support planning, analysis, and design phases (e.g., DFDs, ERDs, data dictionaries).')
bullet(doc, 'Lower CASE tools – support construction and testing (e.g., code generators, test tools).')
bullet(doc, 'Integrated CASE (I-CASE) – support the entire SDLC with a centralised repository.')
nb(doc)

body(doc, 'Benefits of CASE tools for process modelling:')
benefits = [
    ('Consistency and Standards Enforcement',
     'CASE tools enforce diagram notation rules (e.g., correct DFD symbols, balanced flows), '
     'preventing analysts from inadvertently creating syntactically incorrect models.'),
    ('Centralised Repository',
     'All models, data dictionary entries, and process specifications are stored in a single '
     'repository. Any change to a data element is automatically reflected wherever it is used, '
     'eliminating inconsistency across documents.'),
    ('Productivity and Speed',
     'Pre-built templates, drag-and-drop interfaces, and automatic diagram layout dramatically '
     'reduce the time needed to create and update process models compared to manual methods.'),
    ('Reusability',
     'Previously defined components (entities, processes, data flows) can be reused across '
     'multiple diagrams and projects, reducing redundant work.'),
    ('Documentation Automation',
     'CASE tools can automatically generate reports, data dictionaries, and technical '
     'documentation from the models, saving significant manual documentation effort.'),
    ('Collaboration Support',
     'Modern CASE tools (e.g., Lucidchart, draw.io) support real-time multi-user editing, '
     'version control, and online sharing, facilitating team-based modelling.'),
    ('Traceability',
     'Links between requirements, models, and code can be tracked, making impact analysis '
     'easier when requirements change.'),
    ('Code Generation',
     'Some I-CASE tools can generate skeleton code or database schemas directly from process '
     'and data models, bridging the gap between design and implementation.'),
]
for bname, bdesc in benefits:
    bold_body(doc, f'{bname}: ', bdesc)
nb(doc)

body(doc, 'Shortcomings of CASE tools for process modelling:')
shortcomings = [
    ('High Cost',
     'Enterprise-grade CASE tools (e.g., IBM Rational, Sparx EA) can be expensive to '
     'license, particularly for small organisations or student projects.'),
    ('Steep Learning Curve',
     'Many CASE tools have complex interfaces and require significant training before '
     'analysts can use them productively. Poorly trained users may produce worse models '
     'than they would with simpler tools.'),
    ('Over-reliance on the Tool',
     'Analysts may focus on learning the tool rather than the underlying modelling concepts, '
     'leading to technically valid but logically incorrect models.'),
    ('Rigidity',
     'Some CASE tools enforce very strict notational rules that may not fit every project '
     'context, limiting the analyst\'s flexibility.'),
    ('Integration Issues',
     'Different CASE tools used by different team members or organisations may not be '
     'interoperable, making it difficult to share or combine models.'),
    ('Not a Substitute for Thinking',
     'CASE tools automate drawing and documentation, but cannot replace human analytical '
     'reasoning. A CASE tool can produce a perfectly drawn DFD that completely misrepresents '
     'the real system if the analyst\'s understanding is flawed.'),
    ('Maintenance Overhead',
     'Large CASE repositories require ongoing maintenance. Outdated or incomplete entries '
     'can be worse than having no CASE tool, as teams may rely on incorrect information.'),
    ('Vendor Lock-in',
     'Models created in a proprietary CASE tool format may be difficult or impossible to '
     'migrate to a different tool without significant rework.'),
]
for sname, sdesc in shortcomings:
    bold_body(doc, f'{sname}: ', sdesc)
nb(doc)

body(doc, 'Summary comparison:')
table_case = doc.add_table(rows=5, cols=2)
table_case.style = 'Table Grid'
table_case.rows[0].cells[0].text = 'Benefits'
table_case.rows[0].cells[1].text = 'Shortcomings'
case_rows = [
    ('Enforces notation standards and consistency', 'High licensing cost for enterprise tools'),
    ('Central repository eliminates duplication', 'Steep learning curve; training required'),
    ('Auto-generates documentation and reports', 'Rigidity may not suit all project types'),
    ('Supports collaboration and version control', 'Tool mastery does not replace analytical skill'),
]
for i, (b, s) in enumerate(case_rows, 1):
    table_case.rows[i].cells[0].text = b
    table_case.rows[i].cells[1].text = s
for row in table_case.rows:
    for cell in row.cells:
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(9.5)
nb(doc)

body(doc,
     'Conclusion: CASE tools are most beneficial in large, long-term projects with multiple '
     'analysts and complex models where consistency, traceability, and documentation are '
     'critical. For smaller projects or early-stage analysis, lighter tools (Lucidchart, '
     'draw.io, or even whiteboards) may be more practical.')

# Save
doc.save('/workspace/lab5.docx')
print('lab5.docx created successfully.')
