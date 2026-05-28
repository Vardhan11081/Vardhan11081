import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

# ═══════════════════════════════════════════════════════════════
# DIAGRAM 1 – Use Case Diagram  (Online Course Registration)
# ═══════════════════════════════════════════════════════════════
def make_use_case_diagram():
    fig, ax = plt.subplots(figsize=(13, 8))
    fig.patch.set_facecolor('#f0f4f8')
    ax.set_xlim(0, 13); ax.set_ylim(0, 8); ax.axis('off')
    ax.set_title('Use Case Diagram – Online Course Registration System',
                 fontsize=12, fontweight='bold', pad=8)

    # System boundary
    ax.add_patch(FancyBboxPatch((2.8, 0.4), 7.8, 7.1,
                                boxstyle='round,pad=0.15', linewidth=2,
                                edgecolor='#1a4a7a', facecolor='#eef4fb'))
    ax.text(6.7, 7.25, 'Online Course Registration System',
            ha='center', fontsize=10, fontweight='bold', color='#1a4a7a')

    # ── Actor helper ──────────────────────────────────────────
    def actor(ax, x, y, label):
        ax.add_patch(plt.Circle((x, y+0.55), 0.25, color='#334155', zorder=5))
        ax.plot([x,x],[y+0.30, y-0.25], color='#334155', lw=2, zorder=5)
        ax.plot([x-0.38,x+0.38],[y+0.08,y+0.08], color='#334155', lw=2, zorder=5)
        ax.plot([x,x-0.32],[y-0.25,y-0.75], color='#334155', lw=2, zorder=5)
        ax.plot([x,x+0.32],[y-0.25,y-0.75], color='#334155', lw=2, zorder=5)
        ax.text(x, y-0.95, label, ha='center', fontsize=8.5,
                fontweight='bold', color='#1e3a5f')

    # ── Use case ellipse ──────────────────────────────────────
    def uc(ax, x, y, label, w=2.1, h=0.58):
        ax.add_patch(mpatches.Ellipse((x,y), w, h, lw=1.5,
                                      edgecolor='#1a4a7a', facecolor='#dbeafe', zorder=5))
        ax.text(x, y, label, ha='center', va='center',
                fontsize=8, zorder=6, multialignment='center')

    # ── Association line ─────────────────────────────────────
    def assoc(ax, x1, y1, x2, y2):
        ax.plot([x1,x2],[y1,y2], color='#475569', lw=1.2, zorder=3)

    def dashed(ax, x1, y1, x2, y2, label=''):
        ax.annotate('', xy=(x2,y2), xytext=(x1,y1),
                    arrowprops=dict(arrowstyle='->', color='#6b7280',
                                   lw=1.1, linestyle='dashed'), zorder=3)
        if label:
            ax.text((x1+x2)/2+0.1,(y1+y2)/2+0.15, label,
                    fontsize=7.5, color='#6b7280', style='italic')

    # Actors
    actor(ax, 1.2, 5.5, 'Student')
    actor(ax, 1.2, 2.2, 'Lecturer')
    actor(ax, 11.8, 5.5, 'Admin\nStaff')
    actor(ax, 11.8, 2.2, 'Payment\nGateway')

    # Use cases
    ucs = [
        (6.7, 6.6, 'Register for\nCourse'),
        (4.5, 5.4, 'Browse Course\nCatalogue'),
        (6.7, 5.4, 'View Timetable'),
        (8.9, 5.4, 'Pay Course\nFees'),
        (4.5, 3.8, 'Submit\nAssignment'),
        (6.7, 3.8, 'View Grades'),
        (8.9, 3.8, 'Generate\nEnrolment Report'),
        (4.5, 2.4, 'Upload Course\nMaterials'),
        (8.9, 2.4, 'Manage Student\nRecords'),
        (6.7, 1.1, 'Send\nNotification'),
    ]
    for x, y, lbl in ucs:
        uc(ax, x, y, lbl)

    # Student associations
    for ux, uy in [(6.7,6.6),(4.5,5.4),(6.7,5.4),(8.9,5.4),(4.5,3.8),(6.7,3.8)]:
        assoc(ax, 1.6, 5.5, ux-1.05, uy)

    # Lecturer associations
    for ux, uy in [(4.5,2.4),(6.7,3.8),(4.5,3.8)]:
        assoc(ax, 1.6, 2.2, ux-1.05, uy)

    # Admin associations
    for ux, uy in [(8.9,3.8),(8.9,2.4),(6.7,6.6)]:
        assoc(ax, 11.4, 5.5, ux+1.05, uy)

    # Payment Gateway
    assoc(ax, 11.4, 2.2, 8.9+1.05, 5.4)

    # Include / extend relationships
    dashed(ax, 6.7, 6.31, 6.7, 5.69, '«include»')
    dashed(ax, 8.55, 5.4, 8.9-1.05, 5.4, '«include»')
    dashed(ax, 6.7, 3.51, 6.7, 1.39, '«extend»')

    plt.tight_layout()
    path = '/workspace/lab6_use_case_diagram.png'
    plt.savefig(path, dpi=150, bbox_inches='tight',
                facecolor=fig.get_facecolor())
    plt.close()
    print(f'Use case diagram saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# DIAGRAM 2 – System Sequence Diagram (SSD) for "Register for Course"
# ═══════════════════════════════════════════════════════════════
def make_ssd():
    fig, ax = plt.subplots(figsize=(12, 9))
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_xlim(0, 12); ax.set_ylim(0, 9); ax.axis('off')
    ax.set_title('System Sequence Diagram (SSD) – Register for Course',
                 fontsize=12, fontweight='bold', pad=8)

    # Lifeline headers
    headers = [(2.0, 'Student\n(Actor)'), (6.0, ':Registration\nSystem'), (10.0, ':Payment\nGateway')]
    head_colors = ['#c8e6c9', '#dbeafe', '#fef9c3']
    head_edges  = ['#2e7d32', '#1a4a7a', '#854d0e']
    for (x, lbl), fc, ec in zip(headers, head_colors, head_edges):
        ax.add_patch(FancyBboxPatch((x-1.0, 8.3), 2.0, 0.6,
                                   boxstyle='round,pad=0.1', lw=1.6,
                                   edgecolor=ec, facecolor=fc, zorder=5))
        ax.text(x, 8.6, lbl, ha='center', va='center',
                fontsize=8.5, fontweight='bold', zorder=6, multialignment='center')

    # Lifelines (dashed vertical)
    for x in [2.0, 6.0, 10.0]:
        ax.plot([x,x],[8.3, 0.5], color='#94a3b8', lw=1.2,
                linestyle='dashed', zorder=2)

    # Activation boxes
    def actbox(ax, x, y_top, y_bot, fc='#bfdbfe', ec='#1a4a7a'):
        ax.add_patch(FancyBboxPatch((x-0.18, y_bot), 0.36, y_top-y_bot,
                                   boxstyle='square,pad=0',
                                   facecolor=fc, edgecolor=ec, lw=1.2, zorder=4))

    actbox(ax, 2.0, 8.3, 0.8, '#bbf7d0', '#166534')
    actbox(ax, 6.0, 7.8, 1.2, '#bfdbfe', '#1a4a7a')
    actbox(ax, 10.0, 4.5, 3.0, '#fef08a', '#854d0e')

    # Messages
    msgs = [
        # (x1, x2, y, label, direction, style)
        (2.18,  5.82, 7.8, 'browseCourses()', 'right', 'solid'),
        (5.82,  2.18, 7.2, 'courseList', 'left', 'dashed'),
        (2.18,  5.82, 6.6, 'selectCourse(courseID)', 'right', 'solid'),
        (5.82,  2.18, 6.0, 'courseDetails', 'left', 'dashed'),
        (2.18,  5.82, 5.4, 'registerStudent(studentID,\ncourseID)', 'right', 'solid'),
        (5.82,  2.18, 4.8, 'registrationConfirmation', 'left', 'dashed'),
        (6.18,  9.82, 4.3, 'processPayment(amount)', 'right', 'solid'),
        (9.82,  6.18, 3.7, 'paymentStatus: SUCCESS', 'left', 'dashed'),
        (5.82,  2.18, 3.1, 'receiptAndEnrolmentID', 'left', 'dashed'),
    ]

    for x1, x2, y, lbl, direction, style in msgs:
        lw = 1.5
        ls = 'dashed' if style == 'dashed' else 'solid'
        color = '#64748b' if style == 'dashed' else '#1e3a5f'
        ax.annotate('', xy=(x2,y), xytext=(x1,y),
                    arrowprops=dict(arrowstyle='->', color=color,
                                   lw=lw, linestyle=ls), zorder=5)
        off = 0.14
        ax.text((x1+x2)/2, y+off, lbl, ha='center', va='bottom',
                fontsize=8, color=color,
                style='italic' if style=='dashed' else 'normal', zorder=6)

    # Fragment / loop box
    ax.add_patch(FancyBboxPatch((1.0, 4.9), 9.5, 1.0,
                               boxstyle='square,pad=0', lw=1.4,
                               edgecolor='#7c3aed', facecolor='none',
                               linestyle='dashed', zorder=3))
    ax.add_patch(FancyBboxPatch((1.0, 5.75), 0.8, 0.3,
                               boxstyle='square,pad=0', lw=0,
                               facecolor='#7c3aed', zorder=4))
    ax.text(1.4, 5.9, 'opt', ha='center', va='center',
            fontsize=8, color='white', fontweight='bold', zorder=5)
    ax.text(2.5, 5.78, '[if course has waitlist]',
            fontsize=7.5, color='#7c3aed', style='italic', zorder=5)

    # Legend
    legend = [
        mpatches.Patch(facecolor='white', edgecolor='#1e3a5f', lw=1.5,
                       label='Solid arrow = synchronous message'),
        mpatches.Patch(facecolor='white', edgecolor='#64748b', lw=1.5,
                       linestyle='dashed', label='Dashed arrow = return message'),
        mpatches.Patch(facecolor='none', edgecolor='#7c3aed', lw=1.4,
                       linestyle='dashed', label='opt = optional combined fragment'),
    ]
    ax.legend(handles=legend, loc='lower right', fontsize=8, framealpha=0.95)

    plt.tight_layout()
    path = '/workspace/lab6_ssd.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'SSD saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# Build diagrams
# ═══════════════════════════════════════════════════════════════
uc_path  = make_use_case_diagram()
ssd_path = make_ssd()


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

def BN(doc, text, size=11):
    p = doc.add_paragraph(text, style='List Number')
    p.style.font.size = Pt(size)
    return p

def BB(doc, bold_part, rest, size=11):
    p = doc.add_paragraph()
    r = p.add_run(bold_part); r.bold = True; r.font.size = Pt(size)
    p.add_run(rest).font.size = Pt(size)
    return p

def SP(doc): doc.add_paragraph()

def table2(doc, rows_data, col_headers, col_widths_in=None):
    t = doc.add_table(rows=len(rows_data)+1, cols=len(col_headers))
    t.style = 'Table Grid'
    for i, h in enumerate(col_headers):
        c = t.rows[0].cells[i]; c.text = h
        for run in c.paragraphs[0].runs: run.bold = True; run.font.size = Pt(9.5)
    for ri, row in enumerate(rows_data, 1):
        for ci, val in enumerate(row):
            c = t.rows[ri].cells[ci]; c.text = val
            for run in c.paragraphs[0].runs: run.font.size = Pt(9.5)
    return t

# ── Title ────────────────────────────────────────────────────
t = doc.add_heading('BN314 – System Architecture', 0)
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
s = doc.add_heading('Lecture 6: Object Modelling – Laboratory Activity', 1)
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)

# ════════════════════════════════════════════════════════════
# Q1
# ════════════════════════════════════════════════════════════
H(doc, 'Question 1: Object-Oriented Analysis (OOA)')
B(doc, 'Object-oriented analysis (OOA) is a requirements-gathering and system-modelling '
       'technique that views a system as a collection of interacting objects — each '
       'combining data (attributes) and behaviour (methods). OOA identifies the classes, '
       'relationships, and interactions needed to satisfy business requirements before '
       'design and coding begin.')
SP(doc)
B(doc, 'Advantages of OOA:')
BU(doc, 'Modularity – the system is divided into self-contained objects that can be designed, tested, and maintained independently.')
BU(doc, 'Reusability – classes and objects developed for one project can be reused in others, reducing development time and cost.')
BU(doc, 'Maintainability – encapsulation hides internal complexity, so changes to one object do not cascade through the entire system.')
BU(doc, 'Scalability – new functionality can be added by creating new subclasses or extending existing ones without modifying proven code.')
BU(doc, 'Natural mapping – objects correspond directly to real-world entities (Student, Course, Invoice), making models intuitive for stakeholders.')
BU(doc, 'Consistency across SDLC – the same object model used in analysis flows through design and into code, reducing translation errors.')
SP(doc)

# ════════════════════════════════════════════════════════════
# Q2
# ════════════════════════════════════════════════════════════
H(doc, 'Question 2: Object, Attribute, and Method – Definitions and Examples')
BB(doc, 'Object: ', 'A real-world entity or concept that has identity, state (data), and behaviour (operations). Objects are instances of a class.')
BB(doc, 'Attribute: ', 'A data value or characteristic that describes the state of an object. Stored as a variable within the object.')
BB(doc, 'Method: ', 'An operation or function defined within a class that describes the behaviour an object can perform or the services it provides.')
SP(doc)
table2(doc, [
    ('Object',    'Student (s1)', 'Course (c1)', 'Invoice (inv1)'),
    ('Attribute', 'studentID = "S00123"\nfirstName = "Alice"\nenrolmentDate = 15/03/2026',
                  'courseCode = "BN314"\ncourseName = "Sys Architecture"\ncreditPoints = 12',
                  'invoiceID = "INV-0042"\namount = 3500.00\ndueDate = 01/06/2026'),
    ('Method',    'enrol(courseID)\nviewGrades()\nupdateProfile()',
                  'getEnrolledStudents()\naddLecturer(lecturerID)\ngetTimetable()',
                  'generateInvoice()\napplyDiscount(rate)\nmarkAsPaid()'),
], ['Component', 'Example 1 – Student', 'Example 2 – Course', 'Example 3 – Invoice'])
SP(doc)

# ════════════════════════════════════════════════════════════
# Q3
# ════════════════════════════════════════════════════════════
H(doc, 'Question 3: Encapsulation')
B(doc, 'Encapsulation is the OO principle of bundling an object\'s data (attributes) and '
       'the methods that operate on that data together within a single unit (the class), '
       'and restricting direct external access to internal data by exposing only a '
       'controlled public interface.')
SP(doc)
B(doc, 'How it is used in OOA:')
BU(doc, 'Data hiding: attributes are declared private; external code can only read or modify them through public getter/setter methods (e.g., getBalance(), setEmail()). This prevents accidental or unauthorised data corruption.')
BU(doc, 'Interface definition: during analysis, the analyst identifies which methods are public (accessible by other objects) and which are private (internal implementation details). This defines the object\'s "contract" with the rest of the system.')
BU(doc, 'Change isolation: if the internal implementation of an object changes (e.g., how a fee is calculated), objects that use it are unaffected as long as the public interface remains the same. This greatly reduces maintenance cost.')
BU(doc, 'Example: A BankAccount object encapsulates balance (private attribute). External objects cannot modify balance directly; they must call deposit(amount) or withdraw(amount), which contain validation logic internally.')
SP(doc)

# ════════════════════════════════════════════════════════════
# Q4
# ════════════════════════════════════════════════════════════
H(doc, 'Question 4: Polymorphism – Definition and Examples')
B(doc, 'Polymorphism (Greek: "many forms") is the OO principle that allows objects of '
       'different classes to respond to the same message (method call) in different, '
       'class-specific ways. A single interface can represent different underlying forms.')
SP(doc)
table2(doc, [
    ('1. Method Overriding\n(Runtime polymorphism)',
     'A superclass defines calculateFee(). Subclasses FullTimeStudent and PartTimeStudent each override it with different logic. Calling calculateFee() on any student object automatically uses the correct version.',
     'Same method name → different behaviour per subclass'),
    ('2. Method Overloading\n(Compile-time polymorphism)',
     'A class defines sendNotification(email) and sendNotification(email, sms). The system calls the right version based on the arguments provided.',
     'Same method name, different parameter signatures'),
    ('3. Interface polymorphism',
     'Classes PDFReport, ExcelReport, and HTMLReport all implement a Printable interface with a print() method. Code that calls print() works for any type without knowing the concrete class.',
     'Single interface → many implementations'),
], ['Example', 'Description', 'Key Point'])
SP(doc)

# ════════════════════════════════════════════════════════════
# Q5
# ════════════════════════════════════════════════════════════
H(doc, 'Question 5: Class, Subclass, and Superclass – Definitions and Examples')
BB(doc, 'Class: ', 'A blueprint or template that defines the common attributes and methods shared by all objects of that type. No memory is allocated for data until an object (instance) is created from the class.')
BB(doc, 'Superclass (Parent class): ', 'A generalised class whose attributes and methods are inherited by one or more subclasses. It contains common, shared characteristics.')
BB(doc, 'Subclass (Child class): ', 'A specialised class that inherits all attributes and methods from its superclass and may add its own additional attributes, methods, or override inherited ones.')
SP(doc)
table2(doc, [
    ('Class',      'Person',    'Vehicle',     'Account'),
    ('Superclass', 'Person\n(parent of Student & Lecturer)',
                   'Vehicle\n(parent of Car & Truck)',
                   'Account\n(parent of SavingsAccount & LoanAccount)'),
    ('Subclass',   'Student (inherits name, DOB from Person; adds studentID, enrolments)\nLecturer (inherits from Person; adds staffID, courses)',
                   'Car (inherits from Vehicle; adds numDoors, fuelType)\nTruck (inherits from Vehicle; adds payloadCapacity)',
                   'SavingsAccount (inherits from Account; adds interestRate)\nLoanAccount (inherits from Account; adds repaymentSchedule)'),
], ['Component', 'Example 1', 'Example 2', 'Example 3'])
SP(doc)

# ════════════════════════════════════════════════════════════
# Q6
# ════════════════════════════════════════════════════════════
H(doc, 'Question 6: Actor – Definition and Examples')
B(doc, 'An actor is any person, organisation, system, or external entity that interacts '
       'with the system being modelled — either by providing input to it or by receiving '
       'output from it. Actors exist outside the system boundary and are represented in '
       'use case diagrams as stick figures (for human actors) or rectangles (for system actors).')
SP(doc)
table2(doc, [
    ('Student',          'Human actor',  'Browses courses, registers for subjects, submits assignments, views grades.'),
    ('Admin Staff',      'Human actor',  'Manages student records, generates reports, configures course offerings.'),
    ('Payment Gateway',  'System actor', 'External system that processes credit card or online payments and returns a transaction status.'),
], ['Actor', 'Type', 'Interaction with System'])
SP(doc)

# ════════════════════════════════════════════════════════════
# Q7
# ════════════════════════════════════════════════════════════
H(doc, 'Question 7: Use Case Diagram vs Use Case Description')
BB(doc, 'Use Case Diagram: ',
   'A UML diagram that visually shows the system boundary, actors, use cases (functional goals), '
   'and the relationships between them (association, include, extend, generalisation). '
   'It provides a high-level overview of what the system does and who interacts with it.')
BB(doc, 'Use Case (Description): ',
   'A detailed textual or tabular specification of a single use case that describes the '
   'sequence of steps (main flow, alternative flows, exception flows) that occur when an '
   'actor achieves a specific goal using the system.')
SP(doc)
B(doc, 'Key difference: the diagram shows scope and relationships at a glance; '
       'the description provides the step-by-step logic of a single interaction.')
SP(doc)
B(doc, 'Sample Use Case Diagram – Online Course Registration System:')
doc.add_picture(uc_path, width=Inches(6.2))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)

B(doc, 'Sample Use Case Description – "Register for Course":')
SP(doc)
uc_desc = doc.add_table(rows=11, cols=2)
uc_desc.style = 'Table Grid'
uc_rows = [
    ('Use Case Name',        'Register for Course'),
    ('Actor(s)',             'Student (primary); Payment Gateway (secondary)'),
    ('Precondition',         'Student is authenticated. Course catalogue is available. Course has open enrolment places.'),
    ('Trigger',              'Student selects "Register" from the course catalogue.'),
    ('Main Flow',
     '1. Student browses the course catalogue.\n'
     '2. Student selects a desired course.\n'
     '3. System displays course details and available places.\n'
     '4. Student confirms registration.\n'
     '5. System records the enrolment and calculates fees.\n'
     '6. System redirects to payment; Payment Gateway processes fee.\n'
     '7. System issues an enrolment confirmation and receipt.'),
    ('Alternative Flow',     'Step 3a: If no places available, system offers waitlist option.'),
    ('Exception Flow',       'Step 6a: If payment fails, enrolment is not confirmed; student is notified.'),
    ('Postcondition',        'Student is enrolled; fee is paid; confirmation is sent by email.'),
    ('Frequency',            'Multiple times per enrolment period.'),
    ('Priority',             'High – core system function.'),
    ('Notes',                'System must enforce prerequisite checks before confirming registration.'),
]
for i, (field, val) in enumerate(uc_rows):
    r = uc_desc.rows[i].cells
    r[0].text = field; r[1].text = val
    for run in r[0].paragraphs[0].runs: run.bold = True; run.font.size = Pt(9.5)
    for run in r[1].paragraphs[0].runs: run.font.size = Pt(9.5)
SP(doc)

# ════════════════════════════════════════════════════════════
# Q8
# ════════════════════════════════════════════════════════════
H(doc, 'Question 8: Black Box Concept in OOA')
BB(doc, 'Black box: ',
   'A system or object whose internal workings are hidden from the outside. Only the '
   'inputs it accepts and the outputs it produces are visible; the internal implementation '
   'is invisible and irrelevant to the user of that object.')
SP(doc)
B(doc, 'Why it is important in OOA:')
BU(doc, 'Abstraction and simplicity: users of an object only need to know what it does (its interface), not how it does it. This reduces cognitive complexity for analysts and developers.')
BU(doc, 'Encapsulation enabler: the black-box view is the practical result of encapsulation — private attributes and internal methods are truly "inside the box".')
BU(doc, 'Independent development: because objects are treated as black boxes, different teams can develop, test, and update objects independently without breaking the rest of the system.')
BU(doc, 'Reusability: a black-box object can be plugged into new systems without understanding its internals — just its interface (e.g., a PaymentGateway object used across many applications).')
BU(doc, 'Use case alignment: each use case describes the system as a black box from the actor\'s perspective — inputs go in, outputs come out; internal processes are not described.')
SP(doc)

# ════════════════════════════════════════════════════════════
# Q9
# ════════════════════════════════════════════════════════════
H(doc, 'Question 9: Precondition vs Postcondition in a Use Case')
table2(doc, [
    ('Definition',
     'A condition that must be TRUE before the use case can begin. It describes the required state of the system and actors prior to execution.',
     'A condition that is guaranteed to be TRUE after the use case has successfully completed. It describes the new state of the system.'),
    ('Purpose',
     'Sets the valid starting context; prevents the use case from running in an inappropriate state.',
     'Defines the expected outcome; used to verify that the use case achieved its goal (test assertion).'),
    ('Example\n(Register for Course)',
     '• Student is logged in.\n• Course catalogue is loaded.\n• Course has available places.',
     '• Student is enrolled in the course.\n• Fee payment is recorded.\n• Confirmation email is sent.'),
    ('Who defines it',
     'Analyst specifies the required system state before the interaction starts.',
     'Analyst specifies the guaranteed system state after successful execution.'),
], ['Aspect', 'Precondition', 'Postcondition'])
SP(doc)

# ════════════════════════════════════════════════════════════
# Q10
# ════════════════════════════════════════════════════════════
H(doc, 'Question 10: System Sequence Diagram (SSD) – Purpose and Symbols')
BB(doc, 'Purpose: ',
   'A System Sequence Diagram (SSD) is a UML diagram that depicts the sequence of '
   'messages and interactions between one or more actors and the system (treated as a '
   'black box) for a specific use case scenario. It shows what messages are sent, in '
   'what order, and the system\'s responses — without revealing internal system logic.')
SP(doc)
B(doc, 'SSDs are used to:')
BU(doc, 'Identify the system operations (inputs the system must handle) for each use case.')
BU(doc, 'Define the system\'s public interface — the starting point for designing system operation contracts.')
BU(doc, 'Bridge the gap between use case descriptions and interaction/design-level diagrams.')
SP(doc)
B(doc, 'Symbols used in an SSD:')
table2(doc, [
    ('Lifeline',           'Vertical dashed line beneath an actor or system box; represents the existence of a participant over time.'),
    ('Actor Box',          'Rectangle at the top of a lifeline representing a human actor or external system.'),
    ('System Box',         'Rectangle labelled with the system name (treated as a black box); sits at the top of the system lifeline.'),
    ('Activation Box',     'Narrow rectangle on a lifeline; shows the period during which a participant is active/processing.'),
    ('Synchronous Message','Solid horizontal arrow with a filled arrowhead; represents a call/request sent from actor to system.'),
    ('Return Message',     'Dashed horizontal arrow; represents the system\'s response back to the caller.'),
    ('Combined Fragment',  'Rectangular frame with a label in the top-left corner; shows conditional (opt), loop, or alternative (alt) flows.'),
    ('Sequence Number',    'Numbers on messages (optional) indicate the order of interaction.'),
], ['Symbol', 'Description'])
SP(doc)

B(doc, 'Sample SSD – "Register for Course" use case:')
doc.add_picture(ssd_path, width=Inches(6.2))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)

# ════════════════════════════════════════════════════════════
# Q11
# ════════════════════════════════════════════════════════════
H(doc, 'Question 11: Steps to Develop an SSD')
steps = [
    ('Identify the use case',
     'Select a specific use case scenario to model (e.g., the main success flow of "Register for Course").'),
    ('Identify actors',
     'Determine which actors (human users or external systems) interact with the system in this use case.'),
    ('Place lifelines',
     'Draw vertical dashed lifelines for each actor and for the system (as a single black-box object). '
     'Label each with a rectangle at the top.'),
    ('Identify system messages (inputs)',
     'Working through the use case description step by step, identify every input the actor sends to the '
     'system (e.g., browseCourses(), selectCourse(id), registerStudent(sid, cid)). Each becomes a solid arrow.'),
    ('Add return messages',
     'For each system message, add a dashed return arrow showing the data or confirmation the system sends back.'),
    ('Add activation boxes',
     'Draw activation rectangles on lifelines to show when each participant is active.'),
    ('Add combined fragments',
     'Use opt, alt, or loop fragments to show conditional or repeating interactions identified in the use case flows.'),
    ('Sequence and label messages',
     'Ensure messages appear in chronological top-to-bottom order. Label each with a meaningful operation name '
     'and parameters. Optionally add sequence numbers.'),
    ('Review and validate',
     'Check the SSD against the use case description. Verify that every step in the use case is represented '
     'and that all system inputs and return values are correctly captured.'),
]
for i, (title, desc) in enumerate(steps, 1):
    BB(doc, f'Step {i} – {title}: ', desc)
SP(doc)

# ════════════════════════════════════════════════════════════
# Q12
# ════════════════════════════════════════════════════════════
H(doc, 'Question 12: Business Process Modelling (BPM) and Its Role in Business Process Management')
BB(doc, 'Definition: ',
   'Business Process Modelling (BPM) is the activity of creating visual or formal representations '
   '(models) of an organisation\'s business workflows — showing tasks, decision points, participants, '
   'data flows, and events — using standardised notations such as BPMN (Business Process Model and '
   'Notation), UML Activity Diagrams, or swimlane flowcharts.')
SP(doc)
B(doc, 'Why BPM is a critical component of successful business process management:')
BU(doc,
   'Visibility and shared understanding: BPM models make complex, implicit workflows explicit and '
   'visible to all stakeholders — managers, analysts, IT teams, and front-line staff — creating '
   'a shared language and reducing misunderstandings.')
BU(doc,
   'Process improvement and optimisation: By mapping the "as-is" process, organisations can '
   'identify bottlenecks, redundancies, unnecessary handoffs, and delays. The "to-be" model then '
   'guides targeted improvement initiatives.')
BU(doc,
   'IT alignment: BPM models define exactly what the information system must support, ensuring '
   'that software requirements (captured in use cases, DFDs, SSDs) accurately reflect real '
   'business operations and goals.')
BU(doc,
   'Compliance and governance: Documented process models serve as evidence for regulatory audits, '
   'ISO certification, and internal governance reviews, demonstrating that the organisation '
   'operates its processes in a controlled, consistent manner.')
BU(doc,
   'Change management: When organisations undergo restructuring or system upgrades, BPM models '
   'show exactly what will change, helping to train staff, manage resistance, and measure '
   'the impact of changes.')
BU(doc,
   'Automation enablement: A precise BPM model is a prerequisite for process automation using '
   'BPM platforms (e.g., IBM BPM, Appian, Camunda). Processes cannot be automated reliably '
   'without first being accurately modelled.')
BU(doc,
   'Performance measurement: BPM models define process boundaries and handoff points that '
   'can be instrumented with KPIs (e.g., cycle time, error rate, throughput), enabling '
   'continuous performance monitoring and data-driven improvement.')
SP(doc)

doc.save('/workspace/lab6.docx')
print('lab6.docx created successfully.')
