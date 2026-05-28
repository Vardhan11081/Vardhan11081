import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ═══════════════════════════════════════════════════════════════
# DIAGRAM 1 – Symbol Comparison (Gane & Sarson vs Yourdon)
# ═══════════════════════════════════════════════════════════════
def make_symbol_comparison():
    fig, axes = plt.subplots(2, 4, figsize=(14, 6))
    fig.patch.set_facecolor('#f8f9fa')
    fig.suptitle('DFD Notation Comparison: Gane & Sarson vs Yourdon',
                 fontsize=13, fontweight='bold', y=0.98)

    labels_gs  = ['Process\n(Rounded Rectangle)', 'Data Flow\n(Labelled Arrow)',
                  'Data Store\n(Open Rectangle)', 'External Entity\n(Rectangle)']
    labels_yo  = ['Process\n(Circle)', 'Data Flow\n(Labelled Arrow)',
                  'Data Store\n(Parallel Lines)', 'External Entity\n(Rectangle)']
    header = ['Gane & Sarson', 'Yourdon']
    colors = ['#2C6FAC', '#e8813a']

    for col, (row_lbls, clr, hdr) in enumerate(
            zip([labels_gs, labels_yo], colors, header)):
        axes[0][col*2].axis('off')
        axes[0][col*2].text(0.5, 0.5, hdr, ha='center', va='center',
                            fontsize=12, fontweight='bold', color=clr,
                            transform=axes[0][col*2].transAxes)

    # --- draw each symbol pair row by row ---
    def ax_clear(ax):
        ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')

    # ---- Gane & Sarson symbols ----
    row_axes_gs = [axes[0][0], axes[0][1], axes[1][0], axes[1][1]]
    row_axes_yo = [axes[0][2], axes[0][3], axes[1][2], axes[1][3]]

    # Process G&S – rounded rectangle with title bar
    ax = row_axes_gs[0]; ax_clear(ax)
    rect = FancyBboxPatch((1,3), 8, 4, boxstyle="round,pad=0.3",
                          linewidth=1.5, edgecolor='#1a4a7a', facecolor='#d0e4f5')
    ax.add_patch(rect)
    ax.plot([1,9],[6.5,6.5], color='#1a4a7a', linewidth=1.2)
    ax.text(5, 7.2, '1.0', ha='center', va='center', fontsize=9, fontweight='bold')
    ax.text(5, 4.8, 'Register\nStudent', ha='center', va='center', fontsize=9)
    ax.set_title('Process', fontsize=9, color=colors[0])

    # Data Flow G&S – arrow with label
    ax = row_axes_gs[1]; ax_clear(ax)
    ax.annotate('', xy=(8.5, 5), xytext=(1.5, 5),
                arrowprops=dict(arrowstyle='->', color='#1a4a7a', lw=2))
    ax.text(5, 5.7, 'Student Data', ha='center', va='bottom', fontsize=9,
            color='#1a4a7a', style='italic')
    ax.set_title('Data Flow', fontsize=9, color=colors[0])

    # Data Store G&S – open rectangle (two horizontal lines)
    ax = row_axes_gs[2]; ax_clear(ax)
    ax.plot([1,1],[3,7], color='#1a4a7a', lw=1.5)
    ax.plot([1,9],[7,7], color='#1a4a7a', lw=1.5)
    ax.plot([1,9],[3,3], color='#1a4a7a', lw=1.5)
    ax.text(2.5, 5, 'D1', ha='center', va='center', fontsize=9, fontweight='bold')
    ax.plot([3.5,3.5],[3,7], color='#1a4a7a', lw=1.2)
    ax.text(6.5, 5, 'Student DB', ha='center', va='center', fontsize=9)
    ax.set_title('Data Store', fontsize=9, color=colors[0])

    # External Entity G&S – plain rectangle
    ax = row_axes_gs[3]; ax_clear(ax)
    rect2 = mpatches.Rectangle((1.5,3), 7, 4, linewidth=1.5,
                                edgecolor='#1a4a7a', facecolor='#c8e6c9')
    ax.add_patch(rect2)
    ax.text(5, 5, 'Student', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.set_title('External Entity', fontsize=9, color=colors[0])

    # ---- Yourdon symbols ----
    # Process – circle
    ax = row_axes_yo[0]; ax_clear(ax)
    circ = plt.Circle((5,5), 3, linewidth=1.5, edgecolor='#b85a00', facecolor='#ffe0b2')
    ax.add_patch(circ)
    ax.text(5, 5, 'Register\nStudent', ha='center', va='center', fontsize=9)
    ax.set_title('Process', fontsize=9, color=colors[1])

    # Data Flow Yourdon – same arrow
    ax = row_axes_yo[1]; ax_clear(ax)
    ax.annotate('', xy=(8.5, 5), xytext=(1.5, 5),
                arrowprops=dict(arrowstyle='->', color='#b85a00', lw=2))
    ax.text(5, 5.7, 'Student Data', ha='center', va='bottom', fontsize=9,
            color='#b85a00', style='italic')
    ax.set_title('Data Flow', fontsize=9, color=colors[1])

    # Data Store Yourdon – two parallel horizontal lines (open)
    ax = row_axes_yo[2]; ax_clear(ax)
    ax.plot([1,9],[7,7], color='#b85a00', lw=2)
    ax.plot([1,9],[3,3], color='#b85a00', lw=2)
    ax.text(5, 5, 'D1  Student DB', ha='center', va='center', fontsize=9)
    ax.set_title('Data Store', fontsize=9, color=colors[1])

    # External Entity Yourdon – rectangle (same)
    ax = row_axes_yo[3]; ax_clear(ax)
    rect3 = mpatches.Rectangle((1.5,3), 7, 4, linewidth=1.5,
                                edgecolor='#b85a00', facecolor='#fff9c4')
    ax.add_patch(rect3)
    ax.text(5, 5, 'Student', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.set_title('External Entity', fontsize=9, color=colors[1])

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    path = '/workspace/lab4_symbols.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Symbol comparison saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# DIAGRAM 2 – Context DFD (Level 0) for IT Service Company
# Company: "TechNova IT Solutions"  Services: consulting,
# software dev, cloud managed services, cybersecurity, support
# ═══════════════════════════════════════════════════════════════
def make_context_dfd():
    fig, ax = plt.subplots(figsize=(13, 9))
    fig.patch.set_facecolor('#f0f4f8')
    ax.set_xlim(0, 13); ax.set_ylim(0, 9); ax.axis('off')
    ax.set_title('Context DFD (Level 0) – TechNova IT Solutions',
                 fontsize=12, fontweight='bold', pad=10)

    # ── Central process ──────────────────────────────────────────
    cx, cy, cr = 6.5, 4.5, 1.6
    circ = plt.Circle((cx, cy), cr, linewidth=2,
                      edgecolor='#1a4a7a', facecolor='#d0e4f5', zorder=5)
    ax.add_patch(circ)
    ax.text(cx, cy+0.35, '0', ha='center', va='center',
            fontsize=11, fontweight='bold', color='#1a4a7a', zorder=6)
    ax.text(cx, cy-0.3, 'TechNova\nIT Solutions', ha='center', va='center',
            fontsize=9, fontweight='bold', zorder=6)

    def draw_entity(ax, x, y, w, h, label, color='#c8e6c9'):
        rect = FancyBboxPatch((x-w/2, y-h/2), w, h,
                              boxstyle="square,pad=0.1", linewidth=1.5,
                              edgecolor='#2e7d32', facecolor=color, zorder=5)
        ax.add_patch(rect)
        ax.text(x, y, label, ha='center', va='center',
                fontsize=8.5, fontweight='bold', zorder=6, multialignment='center')

    def arrow(ax, x1, y1, x2, y2, label, label_offset=(0, 0.25), color='#1a4a7a'):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.5),
                    zorder=4)
        mx, my = (x1+x2)/2 + label_offset[0], (y1+y2)/2 + label_offset[1]
        ax.text(mx, my, label, ha='center', va='bottom',
                fontsize=7.5, color=color, style='italic', zorder=7)

    def darrow(ax, x1, y1, x2, y2, label, label_offset=(0, 0.25)):
        """Double-headed arrow"""
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='<->', color='#555', lw=1.5), zorder=4)
        mx, my = (x1+x2)/2 + label_offset[0], (y1+y2)/2 + label_offset[1]
        ax.text(mx, my, label, ha='center', va='bottom',
                fontsize=7.5, color='#444', style='italic', zorder=7)

    # ── External entities ────────────────────────────────────────
    entities = {
        'client':      (1.2,  7.5,  'Client /\nOrganisation'),
        'employee':    (1.2,  1.5,  'Employee /\nConsultant'),
        'vendor':      (11.8, 7.5,  'Technology\nVendor'),
        'regulator':   (11.8, 1.5,  'Regulatory\nBody / Tax Dept'),
        'bank':        (6.5,  0.6,  'Bank /\nPayment Gateway'),
    }
    ew, eh = 2.4, 1.0
    for key, (x, y, lbl) in entities.items():
        draw_entity(ax, x, y, ew, eh, lbl)

    # ── Data flows ───────────────────────────────────────────────
    # Client → process
    arrow(ax, 1.2+ew/2, 7.5, cx-cr*0.7, cy+cr*0.7,
          'Service Request /\nRequirements', (0.3, 0.2))
    # process → Client
    arrow(ax, cx-cr*0.8, cy+cr*0.6, 1.2+ew/2, 7.5-0.1,
          'Deliverables /\nReports / Invoice', (-0.5, 0.2))

    # Employee → process
    arrow(ax, 1.2+ew/2, 1.5, cx-cr*0.7, cy-cr*0.7,
          'Labour / Expertise /\nTimesheets', (0.3, 0.2))
    # process → Employee
    arrow(ax, cx-cr*0.8, cy-cr*0.6, 1.2+ew/2, 1.5+0.1,
          'Assignments /\nPayslips', (-0.4, 0.2))

    # Vendor → process
    arrow(ax, 11.8-ew/2, 7.5, cx+cr*0.7, cy+cr*0.7,
          'Software Licences /\nHardware', (-0.3, 0.2))
    # process → Vendor
    arrow(ax, cx+cr*0.8, cy+cr*0.6, 11.8-ew/2, 7.5-0.1,
          'Purchase Orders /\nPayment', (0.5, 0.2))

    # Regulator → process
    arrow(ax, 11.8-ew/2, 1.5, cx+cr*0.7, cy-cr*0.7,
          'Compliance\nRequirements', (-0.3, 0.25))
    # process → Regulator
    arrow(ax, cx+cr*0.8, cy-cr*0.6, 11.8-ew/2, 1.5+0.1,
          'Tax Returns /\nAudit Reports', (0.5, 0.2))

    # Bank ↔ process
    darrow(ax, cx, cy-cr, cx, 0.6+eh/2,
           'Payments / Invoices /\nBank Statements', (0.5, 0.15))

    plt.tight_layout()
    path = '/workspace/lab4_context_dfd.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Context DFD saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# DIAGRAM 3 – Level 1 DFD for TechNova IT Solutions
# ═══════════════════════════════════════════════════════════════
def make_level1_dfd():
    fig, ax = plt.subplots(figsize=(15, 11))
    fig.patch.set_facecolor('#f0f4f8')
    ax.set_xlim(0, 15); ax.set_ylim(0, 11); ax.axis('off')
    ax.set_title('Level 1 DFD – TechNova IT Solutions',
                 fontsize=13, fontweight='bold', pad=10)

    PROC_C = '#d0e4f5'; PROC_E = '#1a4a7a'
    ENT_C  = '#c8e6c9'; ENT_E  = '#2e7d32'
    DS_C   = '#fff9c4'; DS_E   = '#f57f17'

    def process(ax, x, y, r, pid, label):
        c = plt.Circle((x, y), r, linewidth=1.8,
                       edgecolor=PROC_E, facecolor=PROC_C, zorder=5)
        ax.add_patch(c)
        ax.text(x, y+0.28, pid, ha='center', va='center',
                fontsize=8, fontweight='bold', color=PROC_E, zorder=6)
        ax.text(x, y-0.22, label, ha='center', va='center',
                fontsize=7.5, zorder=6, multialignment='center')

    def entity(ax, x, y, w, h, label):
        rect = FancyBboxPatch((x-w/2, y-h/2), w, h,
                              boxstyle="square,pad=0.1", linewidth=1.5,
                              edgecolor=ENT_E, facecolor=ENT_C, zorder=5)
        ax.add_patch(rect)
        ax.text(x, y, label, ha='center', va='center',
                fontsize=8, fontweight='bold', zorder=6, multialignment='center')

    def datastore(ax, x, y, w, h, dsid, label):
        ax.plot([x-w/2, x+w/2], [y+h/2, y+h/2], color=DS_E, lw=1.8, zorder=5)
        ax.plot([x-w/2, x+w/2], [y-h/2, y-h/2], color=DS_E, lw=1.8, zorder=5)
        rect = mpatches.Rectangle((x-w/2, y-h/2), w, h, linewidth=0,
                                   facecolor=DS_C, zorder=4)
        ax.add_patch(rect)
        ax.text(x-w/2+0.35, y, dsid, ha='center', va='center',
                fontsize=8, fontweight='bold', color=DS_E, zorder=6)
        ax.plot([x-w/2+0.7, x-w/2+0.7], [y-h/2, y+h/2], color=DS_E, lw=1.2, zorder=5)
        ax.text(x+0.15, y, label, ha='center', va='center', fontsize=8, zorder=6)

    def arr(ax, x1, y1, x2, y2, lbl, lox=0, loy=0.18, col='#333'):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=col, lw=1.4), zorder=4)
        mx = (x1+x2)/2 + lox; my = (y1+y2)/2 + loy
        ax.text(mx, my, lbl, ha='center', va='bottom',
                fontsize=7, color=col, style='italic', zorder=7)

    # ── External Entities ─────────────────────────────────────
    entity(ax, 1.2,  10.2, 2.0, 0.8, 'Client')
    entity(ax, 13.8, 10.2, 2.0, 0.8, 'Technology\nVendor')
    entity(ax, 1.2,   0.7, 2.0, 0.8, 'Employee')
    entity(ax, 13.8,  0.7, 2.0, 0.8, 'Regulatory\nBody')
    entity(ax, 7.5,   0.5, 2.2, 0.7, 'Bank')

    # ── Processes ──────────────────────────────────────────────
    process(ax, 3.5, 8.8, 0.9, '1.0', 'Client\nOnboarding')
    process(ax, 7.5, 8.8, 0.9, '2.0', 'Project\nManagement')
    process(ax, 11.5, 8.8, 0.9, '3.0', 'Procurement\n& Licensing')
    process(ax, 3.5,  5.5, 0.9, '4.0', 'Service\nDelivery')
    process(ax, 7.5,  5.5, 0.9, '5.0', 'Billing &\nInvoicing')
    process(ax, 11.5, 5.5, 0.9, '6.0', 'HR &\nPayroll')
    process(ax, 5.5,  2.8, 0.9, '7.0', 'Compliance\n& Reporting')
    process(ax, 9.5,  2.8, 0.9, '8.0', 'Quality\nAssurance')

    # ── Data Stores ────────────────────────────────────────────
    datastore(ax, 3.5,  7.0, 2.8, 0.55, 'D1', 'Client Records')
    datastore(ax, 7.5,  7.0, 2.8, 0.55, 'D2', 'Project Repository')
    datastore(ax, 11.5, 7.0, 2.8, 0.55, 'D3', 'Vendor Catalogue')
    datastore(ax, 3.5,  4.0, 2.8, 0.55, 'D4', 'Service Logs')
    datastore(ax, 7.5,  4.0, 2.8, 0.55, 'D5', 'Invoice Records')
    datastore(ax, 11.5, 4.0, 2.8, 0.55, 'D6', 'Employee DB')

    # ── Data Flows ──────────────────────────────────────────────
    # Client → Onboarding
    arr(ax, 1.2, 9.8, 2.6, 9.1, 'Contract /\nRequirements', lox=0.1)
    arr(ax, 2.6, 8.5, 1.2, 9.6, 'Proposal /\nSLA', lox=-0.3, loy=-0.15)
    # Onboarding ↔ Client DB
    arr(ax, 3.5, 7.9, 3.5, 7.27, 'Client Profile', lox=0.5)
    # Onboarding → Project Mgmt
    arr(ax, 4.4, 8.8, 6.6, 8.8, 'Approved\nProject Brief')
    # Project Mgmt ↔ Project Repo
    arr(ax, 7.5, 7.9, 7.5, 7.27, 'Project Plan\n/ Updates')
    # Vendor → Procurement
    arr(ax, 12.8, 9.8, 12.4, 9.7, 'Licence /\nHW Quote', lox=-0.2)
    arr(ax, 12.3, 8.5, 12.8, 9.6, 'PO / Payment', lox=0.2, loy=-0.15)
    # Procurement ↔ Vendor DB
    arr(ax, 11.5, 7.9, 11.5, 7.27, 'Vendor Info')
    # Project Mgmt → Service Delivery
    arr(ax, 6.6, 5.5, 4.4, 5.5, 'Task\nAssignments', loy=0.2)
    # Service Delivery ↔ Service Logs
    arr(ax, 3.5, 4.6, 3.5, 4.27, 'Service Records')
    # Service Delivery → Billing
    arr(ax, 4.4, 5.5, 6.6, 5.5, 'Completed\nWork Units', loy=0.2)
    # Billing ↔ Invoice DB
    arr(ax, 7.5, 4.6, 7.5, 4.27, 'Invoice Data')
    # Billing → Client (payment request)
    arr(ax, 7.5, 7.9, 7.5, 5.5+0.9, '', loy=0.1)   # spacer handled by D2
    arr(ax, 6.6, 5.2, 1.2, 9.8, 'Invoice', lox=-0.3, loy=0.15)
    # Bank ↔ Billing
    arr(ax, 7.5, 0.85, 7.5, 4.6, 'Payment\nConfirmation', lox=0.7)
    # HR ↔ Employee DB
    arr(ax, 11.5, 4.6, 11.5, 4.27, 'Employee Data')
    # Employee → HR
    arr(ax, 1.2, 1.1, 10.6, 5.2, 'Timesheets /\nLeave Requests', lox=0.5, loy=0.2)
    arr(ax, 10.6, 5.8, 1.2, 1.3, 'Payslips /\nContracts', lox=0.2, loy=-0.15)
    # Compliance → Regulator
    arr(ax, 6.4, 2.8, 12.8, 0.9, 'Tax / Audit\nReports', lox=0.5)
    arr(ax, 12.8, 0.9, 6.4, 2.5, 'Compliance\nReqs', lox=-0.3, loy=-0.15)
    # QA ↔ Service Delivery
    arr(ax, 9.5, 3.7, 4.4, 5.2, 'QA Feedback', lox=-0.2)
    arr(ax, 4.4, 5.0, 9.5, 3.1, 'Deliverables\nfor Review', lox=0.5, loy=0.15)

    plt.tight_layout()
    path = '/workspace/lab4_level1_dfd.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Level 1 DFD saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# DIAGRAM 4 – Alternative: UML Use Case Diagram
# ═══════════════════════════════════════════════════════════════
def make_usecase():
    fig, ax = plt.subplots(figsize=(13, 8))
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_xlim(0, 13); ax.set_ylim(0, 8); ax.axis('off')
    ax.set_title('UML Use Case Diagram – TechNova IT Solutions (Alternative to DFD)',
                 fontsize=11, fontweight='bold')

    # System boundary
    sys_rect = FancyBboxPatch((2.5, 0.5), 8, 7, boxstyle="round,pad=0.2",
                              linewidth=2, edgecolor='#1a4a7a', facecolor='#eef4fb')
    ax.add_patch(sys_rect)
    ax.text(6.5, 7.2, 'TechNova IT Solutions System', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#1a4a7a')

    def actor(ax, x, y, label):
        # head
        ax.add_patch(plt.Circle((x, y+0.5), 0.22, color='#555', zorder=5))
        # body
        ax.plot([x, x], [y+0.28, y-0.3], color='#555', lw=1.5, zorder=5)
        # arms
        ax.plot([x-0.35, x+0.35], [y+0.05, y+0.05], color='#555', lw=1.5, zorder=5)
        # legs
        ax.plot([x, x-0.3], [y-0.3, y-0.75], color='#555', lw=1.5, zorder=5)
        ax.plot([x, x+0.3], [y-0.3, y-0.75], color='#555', lw=1.5, zorder=5)
        ax.text(x, y-0.95, label, ha='center', va='top', fontsize=8, fontweight='bold')

    def usecase(ax, x, y, label, w=2.0, h=0.55):
        ell = mpatches.Ellipse((x, y), w, h, linewidth=1.4,
                               edgecolor='#2C6FAC', facecolor='#d0e4f5', zorder=5)
        ax.add_patch(ell)
        ax.text(x, y, label, ha='center', va='center', fontsize=7.5,
                zorder=6, multialignment='center')

    def assoc(ax, x1, y1, x2, y2):
        ax.plot([x1, x2], [y1, y2], color='#555', lw=1.2, zorder=3)

    # Actors
    actor(ax, 0.7, 4.2, 'Client')
    actor(ax, 12.3, 5.5, 'Employee')
    actor(ax, 12.3, 2.5, 'Vendor')
    actor(ax, 0.7, 1.2, 'Regulator')

    # Use cases
    ucs = [
        (6.5, 6.4, 'Submit Service\nRequest'),
        (4.0, 5.3, 'Sign Contract\n/ SLA'),
        (6.5, 5.3, 'Manage Project\n& Tasks'),
        (9.0, 5.3, 'Procure Licences\n/ Hardware'),
        (4.0, 3.8, 'Deliver IT\nServices'),
        (6.5, 3.8, 'Generate Invoice\n/ Payment'),
        (9.0, 3.8, 'Record Employee\nTimesheet'),
        (4.0, 2.4, 'QA Review\n& Approval'),
        (6.5, 2.4, 'Process Payroll'),
        (9.0, 2.4, 'File Compliance\nReport'),
        (6.5, 1.2, 'Archive &\nAudit Logs'),
    ]
    for x, y, lbl in ucs:
        usecase(ax, x, y, lbl)

    # Associations
    # Client
    for uc_x, uc_y in [(6.5,6.4),(4.0,5.3),(6.5,5.3),(6.5,3.8),(4.0,2.4)]:
        assoc(ax, 1.1, 4.2, uc_x-1.0, uc_y)
    # Employee
    for uc_x, uc_y in [(6.5,5.3),(4.0,3.8),(9.0,3.8),(4.0,2.4),(6.5,2.4)]:
        assoc(ax, 11.9, 5.5, uc_x+1.0, uc_y)
    # Vendor
    for uc_x, uc_y in [(9.0,5.3),(6.5,3.8)]:
        assoc(ax, 11.9, 2.5, uc_x+1.0, uc_y)
    # Regulator
    for uc_x, uc_y in [(9.0,2.4),(6.5,1.2)]:
        assoc(ax, 1.1, 1.2, uc_x-1.0, uc_y)

    # Include relationships (dashed)
    for x1,y1,x2,y2 in [(6.5,6.0,6.5,5.65),(6.5,5.0,6.5,4.15)]:
        ax.annotate('', xy=(x2,y2), xytext=(x1,y1),
                    arrowprops=dict(arrowstyle='->', color='#888',
                                   lw=1.1, linestyle='dashed'), zorder=4)
        ax.text((x1+x2)/2+0.2, (y1+y2)/2, '«include»',
                fontsize=6.5, color='#666', style='italic')

    plt.tight_layout()
    path = '/workspace/lab4_usecase.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Use Case diagram saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# Build all diagrams
# ═══════════════════════════════════════════════════════════════
sym_path    = make_symbol_comparison()
ctx_path    = make_context_dfd()
lvl1_path   = make_level1_dfd()
uc_path     = make_usecase()


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

# ── Title ───────────────────────────────────────────────────────
t = doc.add_heading('BN314 – System Architecture', 0)
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
s = doc.add_heading('Lecture 4: Data and Process Modelling – Laboratory Activity', 1)
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
nb(doc)

# ════════════════════════════════════════════════════════════════
# Q1
# ════════════════════════════════════════════════════════════════
heading(doc, 'Question 1: Data and Process Modelling Concepts and Tools')
body(doc,
     'Data and process modelling are structured techniques used in systems analysis to '
     'document, visualise, and analyse how data moves through an information system and '
     'how business processes transform that data.')
nb(doc)
body(doc, 'Key Concepts:')
bullet(doc, 'Data Modelling – describes the structure, attributes, and relationships of data '
            'within a system. Tools: Entity-Relationship Diagrams (ERDs), data dictionaries, '
            'normalisation techniques.')
bullet(doc, 'Process Modelling – describes what a system does by depicting processes, '
            'data flows, data stores, and external entities. Tools: Data Flow Diagrams (DFDs), '
            'flowcharts, BPMN, UML Activity Diagrams.')
bullet(doc, 'Data Dictionary – a centralised repository that defines the meaning, structure, '
            'and usage of every data element in a system. Complements DFDs.')
bullet(doc, 'Process Specifications (Mini-specs) – detailed descriptions of the logic inside '
            'the lowest-level DFD processes, written in structured English, decision tables, '
            'or decision trees.')
nb(doc)
body(doc, 'Common Modelling Tools:')
table = doc.add_table(rows=6, cols=3)
table.style = 'Table Grid'
hdr = table.rows[0].cells
hdr[0].text = 'Tool'; hdr[1].text = 'Type'; hdr[2].text = 'Purpose'
rows_data = [
    ('Data Flow Diagram (DFD)', 'Process Model', 'Show data movement through processes and stores'),
    ('Entity-Relationship Diagram (ERD)', 'Data Model', 'Define data structures and relationships'),
    ('Flowchart', 'Process Model', 'Depict step-by-step logic and decision flows'),
    ('BPMN Diagram', 'Process Model', 'Model business workflows with standard notation'),
    ('UML Use Case / Activity Diagram', 'Behavioural Model', 'Show system behaviour and actor interactions'),
]
for i, (tool, typ, purp) in enumerate(rows_data, 1):
    row = table.rows[i].cells
    row[0].text = tool; row[1].text = typ; row[2].text = purp
for row in table.rows:
    for cell in row.cells:
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(9.5)
nb(doc)

# ════════════════════════════════════════════════════════════════
# Q2
# ════════════════════════════════════════════════════════════════
heading(doc, 'Question 2: Gane & Sarson vs Yourdon Symbols')
body(doc,
     'Two major DFD notations exist: Gane & Sarson (widely used in structured systems '
     'analysis) and Yourdon/DeMarco (popular in academic and software engineering contexts). '
     'They use different shapes but convey the same concepts.')
nb(doc)
table2 = doc.add_table(rows=5, cols=3)
table2.style = 'Table Grid'
hdr2 = table2.rows[0].cells
hdr2[0].text = 'Component'; hdr2[1].text = 'Gane & Sarson Symbol'; hdr2[2].text = 'Yourdon Symbol'
sym_rows = [
    ('Process', 'Rounded rectangle divided horizontally — top section holds the process number, bottom holds the process name.',
               'Circle (bubble) — the process name is written inside the circle.'),
    ('Data Flow', 'Named arrow — shows direction and name of data being transferred.',
                  'Named arrow — identical to Gane & Sarson; arrows are labelled with data names.'),
    ('Data Store', 'Open-ended rectangle (two horizontal lines with left vertical) — labelled with a data store ID and name.',
                   'Two parallel horizontal lines (open on both ends) — labelled with the store name.'),
    ('External Entity', 'Plain rectangle — represents a person, organisation, or system outside the scope. Name written inside.',
                        'Rectangle — identical in shape to Gane & Sarson; sometimes shown with a shadow/duplicate for emphasis.'),
]
for i, (comp, gs, yo) in enumerate(sym_rows, 1):
    r = table2.rows[i].cells
    r[0].text = comp; r[1].text = gs; r[2].text = yo
for row in table2.rows:
    for cell in row.cells:
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(9.5)
nb(doc)
body(doc, 'The diagram below shows examples of both notation systems:')
doc.add_picture(sym_path, width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
nb(doc)

# ════════════════════════════════════════════════════════════════
# Q3
# ════════════════════════════════════════════════════════════════
heading(doc, 'Question 3: Context Diagram vs Diagram 0 (Level 1 DFD)')
body(doc,
     'Both a context diagram and Diagram 0 are types of Data Flow Diagrams, but they '
     'operate at different levels of abstraction:')
nb(doc)
table3 = doc.add_table(rows=5, cols=3)
table3.style = 'Table Grid'
hdr3 = table3.rows[0].cells
hdr3[0].text = 'Aspect'; hdr3[1].text = 'Context Diagram (Level 0)'; hdr3[2].text = 'Diagram 0 (Level 1)'
diff_rows = [
    ('Scope', 'Shows the entire system as a single process', 'Breaks the system into its major sub-processes (typically 6–8)'),
    ('Processes', 'One single central process representing the whole system', 'Multiple processes, each with a unique number (1.0, 2.0, etc.)'),
    ('Data Stores', 'NOT included — data stores are internal to the system', 'Included — shows all major data stores used by the system'),
    ('Purpose', 'Define system boundary and external interfaces at the highest level', 'Show major functions of the system and how data flows between them'),
]
for i, (asp, ctx, d0) in enumerate(diff_rows, 1):
    r = table3.rows[i].cells
    r[0].text = asp; r[1].text = ctx; r[2].text = d0
for row in table3.rows:
    for cell in row.cells:
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(9.5)
nb(doc)
body(doc,
     'The symbol NOT used in a context diagram is the Data Store. '
     'Since a context diagram treats the entire system as a black box with a single '
     'process, all data stores are considered internal and are therefore hidden at this '
     'level. Only external entities, the single central process, and data flows between '
     'them appear in a context diagram.')
nb(doc)

# ════════════════════════════════════════════════════════════════
# Q4
# ════════════════════════════════════════════════════════════════
heading(doc, 'Question 4: How to Level DFDs')
body(doc,
     'Levelling (also called decomposition or exploding) is the process of breaking a '
     'higher-level DFD process into a more detailed, lower-level DFD. It allows analysts '
     'to manage complexity by moving from a broad overview to increasing detail.')
nb(doc)
body(doc, 'Levelling process:')
bullet(doc, 'Level 0 – Context Diagram: The entire system is represented as one process. '
            'External entities and the primary data flows in/out are shown.')
bullet(doc, 'Level 1 – Diagram 0: The single process from the context diagram is exploded '
            'into 6–8 major sub-processes. Data stores appear for the first time. '
            'All data flows from the context diagram must still be present (balancing rule).')
bullet(doc, 'Level 2 – Diagram 1, 2, etc.: Each sub-process from Level 1 that is too complex '
            'to describe simply is further decomposed. A process named 3.0 at Level 1 becomes '
            'processes 3.1, 3.2, 3.3 at Level 2.')
bullet(doc, 'Level 3 and beyond: Decomposition continues until every process is a functional '
            'primitive — a process simple enough to be described by a process specification '
            '(mini-spec) without further decomposition.')
nb(doc)
body(doc, 'Rules for levelling:')
bullet(doc, 'Each level must balance with the level above it (inputs and outputs match).')
bullet(doc, 'Do not show more than 6–8 processes per diagram to maintain readability.')
bullet(doc, 'Number processes consistently: Level 1 uses 1.0, 2.0…; Level 2 uses 1.1, 1.2…; Level 3 uses 1.1.1, 1.1.2…')
bullet(doc, 'Stop decomposing when a process can be fully described in a single page of structured English.')
nb(doc)

# ════════════════════════════════════════════════════════════════
# Q5
# ════════════════════════════════════════════════════════════════
heading(doc, 'Question 5: How to Balance DFDs')
body(doc,
     'Balancing ensures consistency between a DFD and its parent diagram — the data flows '
     'entering and leaving a process at one level must exactly match the data flows entering '
     'and leaving the same process\'s detailed diagram at the next level down.')
nb(doc)
body(doc, 'Rules for balancing:')
bullet(doc, 'Input/Output Match: Every data flow entering a process in the parent diagram '
            'must appear as an input to the child diagram. Every output in the parent must '
            'appear as an output in the child.')
bullet(doc, 'No Extra External Flows: A child diagram cannot introduce new external entities '
            'or data flows that do not exist in the parent diagram at that same process.')
bullet(doc, 'Data Stores: A data store used only within a single child process need not '
            'appear at the parent level (it is an internal store). However, a store shared '
            'across multiple child processes must appear at the parent level.')
bullet(doc, 'Verification Technique: List all inputs and outputs on the parent process bubble. '
            'Then verify that the child diagram has exactly the same set of net inputs and outputs. '
            'Any mismatch indicates an imbalance that must be corrected.')
bullet(doc, 'Typical imbalance errors: a data flow missing from the child, an extra data flow '
            'in the child not present in the parent, or a data store wrongly promoted to/from '
            'parent level.')
nb(doc)

# ════════════════════════════════════════════════════════════════
# Q6
# ════════════════════════════════════════════════════════════════
heading(doc, 'Question 6: IT Service Company – Context DFD and Level 1 DFD')
body(doc,
     'Company: TechNova IT Solutions\n'
     'Start-up Budget: AUD $500,000\n'
     'Services offered: IT Consulting, Custom Software Development, Cloud Managed Services, '
     'Cybersecurity Solutions, and IT Support & Helpdesk.')
nb(doc)
body(doc,
     'TechNova serves corporate clients, engages technology vendors for licences and '
     'hardware, employs consultants and developers, interacts with the bank for payments, '
     'and submits compliance reports to the regulatory/tax authority.')
nb(doc)
body(doc, 'Context DFD (Level 0):')
doc.add_picture(ctx_path, width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
nb(doc)
body(doc,
     'The context diagram shows TechNova as a single central process. The five external '
     'entities (Client, Employee/Consultant, Technology Vendor, Regulatory Body, and Bank) '
     'interact with the system via clearly labelled data flows. No data stores appear at '
     'this level.')
nb(doc)
body(doc, 'Level 1 DFD (Diagram 0):')
doc.add_picture(lvl1_path, width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
nb(doc)
body(doc, 'The Level 1 DFD decomposes TechNova into eight core processes:')
procs = [
    ('1.0 Client Onboarding', 'Captures client requirements, generates proposals, and creates client records (D1).'),
    ('2.0 Project Management', 'Plans, assigns, and tracks all project tasks stored in the Project Repository (D2).'),
    ('3.0 Procurement & Licensing', 'Manages vendor relationships, purchase orders, and vendor catalogue (D3).'),
    ('4.0 Service Delivery', 'Executes IT services; logs work in Service Logs (D4).'),
    ('5.0 Billing & Invoicing', 'Generates invoices based on delivered work; stores records in D5; interfaces with Bank.'),
    ('6.0 HR & Payroll', 'Manages employee data (D6), processes timesheets, and generates payslips.'),
    ('7.0 Compliance & Reporting', 'Produces tax returns and audit reports submitted to the Regulatory Body.'),
    ('8.0 Quality Assurance', 'Reviews deliverables from Service Delivery and provides QA feedback.'),
]
table_p = doc.add_table(rows=len(procs)+1, cols=2)
table_p.style = 'Table Grid'
table_p.rows[0].cells[0].text = 'Process'
table_p.rows[0].cells[1].text = 'Description'
for i, (proc, desc) in enumerate(procs, 1):
    table_p.rows[i].cells[0].text = proc
    table_p.rows[i].cells[1].text = desc
for row in table_p.rows:
    for cell in row.cells:
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(9.5)
nb(doc)

# ════════════════════════════════════════════════════════════════
# Q7
# ════════════════════════════════════════════════════════════════
heading(doc, 'Question 7: Alternatives to DFDs – Pros, Cons, and Comparison')
body(doc,
     'While DFDs are a powerful tool for process and data modelling, several alternatives '
     'exist, each with different strengths depending on the project context.')
nb(doc)

table4 = doc.add_table(rows=5, cols=4)
table4.style = 'Table Grid'
hdr4 = table4.rows[0].cells
for i, h in enumerate(['Alternative', 'Description', 'Pros', 'Cons']):
    hdr4[i].text = h
alts = [
    ('UML Use Case Diagram',
     'Shows actors and their interactions with system use cases within a system boundary.',
     '+ Focus on user requirements; easy for stakeholders to validate; standard notation; integrates with other UML diagrams.',
     '– Does not show data flows or data storage; no process logic; limited for data-intensive systems.'),
    ('BPMN (Business Process Model & Notation)',
     'Models end-to-end business workflows with tasks, events, gateways, and swimlanes.',
     '+ Rich notation for complex workflows; shows decision logic, roles, and parallel flows; widely supported by tools.',
     '– Can become very complex; less focused on data structure; steeper learning curve than DFDs.'),
    ('UML Activity Diagram',
     'Depicts the sequence of activities and decisions within a process; similar to flowcharts.',
     '+ Good for control flow and parallel processes; integrates with OO design; familiar syntax.',
     '– Does not explicitly model data flows or external entities; less intuitive for business users.'),
    ('Flowchart',
     'Step-by-step graphical representation of a process using standard symbols (start, decision, action, end).',
     '+ Simple and universally understood; good for algorithm and procedure documentation.',
     '– Does not show data stores or external entities; poor for complex multi-actor systems; not scalable.'),
]
for i, (alt, desc, pros, cons) in enumerate(alts, 1):
    r = table4.rows[i].cells
    r[0].text = alt; r[1].text = desc; r[2].text = pros; r[3].text = cons
for row in table4.rows:
    for cell in row.cells:
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(9)
nb(doc)
body(doc,
     'Recommended alternative: UML Use Case Diagram. For the TechNova IT Solutions scenario, '
     'a Use Case Diagram complements the DFD by showing which actors interact with which '
     'system functions, making it easier for clients and stakeholders to validate scope and '
     'requirements — something a DFD alone does not do clearly.')
nb(doc)
body(doc, 'UML Use Case Diagram for TechNova IT Solutions:')
doc.add_picture(uc_path, width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
nb(doc)

body(doc, 'DFD vs UML Use Case – Direct Comparison:')
table5 = doc.add_table(rows=7, cols=3)
table5.style = 'Table Grid'
hdr5 = table5.rows[0].cells
for i, h in enumerate(['Criterion', 'DFD', 'UML Use Case']):
    hdr5[i].text = h
comp = [
    ('Focus', 'Data movement and transformation', 'Actor-system interactions and system scope'),
    ('Shows Data Flows', 'Yes — explicitly named arrows', 'No — only relationships'),
    ('Shows Data Stores', 'Yes — named repositories', 'No'),
    ('Audience', 'Analysts and developers', 'Stakeholders, clients, and product owners'),
    ('Complexity Handling', 'Levelled hierarchy (Level 0 → 1 → 2…)', 'Include/extend relationships'),
    ('Best For', 'Detailed data and process requirements', 'High-level scope and functional requirements'),
]
for i, (crit, dfd, uc) in enumerate(comp, 1):
    r = table5.rows[i].cells
    r[0].text = crit; r[1].text = dfd; r[2].text = uc
for row in table5.rows:
    for cell in row.cells:
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(9.5)
nb(doc)
body(doc,
     'Conclusion: Neither tool is universally superior. DFDs are best for data-centric '
     'systems analysis where understanding data movement is critical. Use Case Diagrams '
     'are best for defining system scope and communicating with non-technical stakeholders. '
     'In practice, both are used together in a complete requirements specification.')

doc.save('/workspace/lab4.docx')
print('lab4.docx created successfully.')
