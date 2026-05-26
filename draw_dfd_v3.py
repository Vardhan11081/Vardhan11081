"""
FreshBite Salads – Level 1 DFD  (v3)
All arrows routed orthogonally (horizontal → vertical → horizontal).
No diagonal lines; bidirectional flows are offset to avoid overlap.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

# ── canvas ────────────────────────────────────────────────────────────────────
W, H   = 24, 17
fig, ax = plt.subplots(figsize=(W, H))
ax.set_xlim(0, W); ax.set_ylim(0, H)
ax.axis('off')
BG = '#a8d8ea'
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)

# ── colours ───────────────────────────────────────────────────────────────────
PROC   = '#0a3055'
EXT    = '#2e6b3e'
DS_O   = '#d4831a'
DS_BG  = '#f8f8f8'
BORDER = '#444'
ARR    = '#111'
WHITE  = 'white'

# ═════════════════════════════════════════════════════════════════════════════
# drawing helpers
# ═════════════════════════════════════════════════════════════════════════════

def process(ax, cx, cy, r, num, *lines):
    ax.add_patch(plt.Circle((cx, cy), r, fc=PROC, ec='#4a7aab', lw=1.5, zorder=4))
    ax.plot([cx-r*.78, cx+r*.78], [cy+r*.30, cy+r*.30],
            color=WHITE, lw=0.8, alpha=0.55, zorder=5)
    ax.text(cx, cy+r*.63, num, ha='center', va='center',
            fontsize=9, fontweight='bold', color=WHITE, zorder=6)
    n = len(lines)
    for i, ln in enumerate(lines):
        yy = cy - r*.10 - (i-(n-1)/2)*r*.40
        ax.text(cx, yy, ln, ha='center', va='center',
                fontsize=7.8, fontweight='bold', color=WHITE, zorder=6)

def ext_entity(ax, cx, cy, w, h, *lines):
    for off, lw in [(0, 2.2), (0.14, 1.4)]:
        ax.add_patch(FancyBboxPatch(
            (cx-w/2+off, cy-h/2+off), w-2*off, h-2*off,
            boxstyle='square,pad=0', lw=lw, ec=WHITE, fc=EXT, zorder=4))
    n = len(lines)
    for i, ln in enumerate(lines):
        ax.text(cx, cy+(n-1)*.22-i*.44, ln, ha='center', va='center',
                fontsize=9, fontweight='bold', color=WHITE, zorder=6)

def datastore(ax, x1, y, w, h, dsid, name):
    ow = 0.90
    ax.add_patch(mpatches.Rectangle((x1, y), w, h, fc=DS_BG, ec=BORDER, lw=1.5, zorder=4))
    ax.add_patch(mpatches.Rectangle((x1, y), ow, h, fc=DS_O, ec='none', zorder=5))
    ax.plot([x1+ow, x1+ow], [y, y+h], color=BORDER, lw=1.5, zorder=6)
    ax.text(x1+ow/2, y+h/2, dsid, ha='center', va='center',
            fontsize=8, fontweight='bold', color=WHITE, zorder=7)
    ax.text(x1+ow+(w-ow)/2, y+h/2, name, ha='center', va='center',
            fontsize=8.5, zorder=7)


def label_box(ax, x, y, text):
    ax.text(x, y, text, ha='center', va='center', fontsize=7.3,
            color='#111', multialignment='center',
            bbox=dict(boxstyle='round,pad=0.15', fc=WHITE, ec='none', alpha=0.90))


def parrow(ax, pts, label='', lseg=None, ldy=0.20):
    """
    Orthogonal polyline arrow.
    pts  – list of (x,y) waypoints; arrowhead drawn at last point.
    lseg – which segment (0-based) to place the label on (default: middle).
    ldy  – vertical offset for label.
    """
    # draw all intermediate segments
    for i in range(len(pts)-2):
        ax.plot([pts[i][0], pts[i+1][0]], [pts[i][1], pts[i+1][1]],
                '-', color=ARR, lw=1.25, solid_capstyle='round',
                solid_joinstyle='round', zorder=5)
    # final segment with arrowhead
    ax.annotate('', xy=pts[-1], xytext=pts[-2],
                arrowprops=dict(arrowstyle='->', color=ARR, lw=1.25))
    # label
    if label:
        si = lseg if lseg is not None else max(0, len(pts)//2 - 1)
        mx = (pts[si][0]+pts[si+1][0])/2
        my = (pts[si][1]+pts[si+1][1])/2 + ldy
        label_box(ax, mx, my, label)


# ═════════════════════════════════════════════════════════════════════════════
# TITLE
# ═════════════════════════════════════════════════════════════════════════════
ax.text(12, 16.6, 'FreshBite Salads – Level 1 Data Flow Diagram',
        ha='center', fontsize=14, fontweight='bold', color='#0a2040')

# ═════════════════════════════════════════════════════════════════════════════
# POSITIONS
# ═════════════════════════════════════════════════════════════════════════════
PR = 1.18   # process radius
DSH = 0.66  # data-store height

# Processes
P1 = (5.5,  13.5)   # Browse Menu
P2 = (14.5, 13.5)   # Manage User Account
P3 = (5.5,   9.0)   # Manage Shopping Cart
P4 = (12.5,  9.0)   # Process Checkout
P5 = (6.5,   4.5)   # Manage Orders
P6 = (14.5,  3.5)   # Manage Reward Points

# External entities  (cx, cy, w, h)
C_CX, C_CY = 1.5, 9.0   # Customer
E_CX, E_CY = 22.5, 14.0 # Email Service (top)
G_CX, G_CY = 22.5,  9.0 # Payment Gateway
B_CX, B_CY = 22.5,  3.5 # Email Service (bottom)
EE_W, EE_H = 2.2, 1.55

ext_entity(ax, C_CX, C_CY,  2.4, 2.2,  'Customer')
ext_entity(ax, E_CX, E_CY,  EE_W, EE_H, 'Email', 'Service')
ext_entity(ax, G_CX, G_CY,  EE_W, 1.80, 'Payment', 'Gateway')
ext_entity(ax, B_CX, B_CY,  EE_W, EE_H, 'Email', 'Service')

# Processes
process(ax, *P1, PR, '1.0', 'Browse', 'Menu')
process(ax, *P2, PR, '2.0', 'Manage User', 'Account')
process(ax, *P3, PR, '3.0', 'Manage', 'Shopping', 'Cart')
process(ax, *P4, PR, '4.0', 'Process', 'Checkout')
process(ax, *P5, PR, '5.0', 'Manage', 'Orders')
process(ax, *P6, PR, '6.0', 'Manage Reward', 'Points')

# Data stores
DSW = 4.5
# D1 – between P1 and P2, same row
D1x = P1[0]+PR+0.25
datastore(ax, D1x, P1[1]-DSH/2, P2[0]-PR-0.25-D1x, DSH, 'D1', 'Salad Database')

# D2 – right of P2
D2x = P2[0]+PR+0.30
datastore(ax, D2x, P2[1]+0.30, DSW, DSH, 'D2', 'User Account Database')

# D3 – between P3 and P4, below
D3y = 7.0
D3x = P3[0]-0.3
datastore(ax, D3x, D3y, DSW, DSH, 'D3', 'Shopping Cart')

# D4 – right of P5, same row
D4x = P5[0]+PR+0.30
datastore(ax, D4x, P5[1]-DSH/2, DSW, DSH, 'D4', 'Order Database')

# D5 – below P4 between P4 and gateway
D5y = P4[1]-PR-1.30
D5x = P4[0]-0.3
datastore(ax, D5x, D5y, DSW, DSH, 'D5', 'Address Database')

# ═════════════════════════════════════════════════════════════════════════════
# ARROWS  – all orthogonally routed
# ═════════════════════════════════════════════════════════════════════════════

# ── A: Customer ↔ P1 Browse Menu  ───────────────────────────────────────────
# Route via left margin  x=3.0
# C→P1 (Browse Request): right edge of C → up → right to P1
parrow(ax,
    [(C_CX+1.2, C_CY+0.50),
     (3.0,      C_CY+0.50),
     (3.0,      P1[1]+0.15),
     (P1[0]-PR, P1[1]+0.15)],
    'Browse Request', lseg=2)

# P1→C (Salad Details): P1 left → left → down → C right
parrow(ax,
    [(P1[0]-PR, P1[1]-0.15),
     (2.6,      P1[1]-0.15),
     (2.6,      C_CY+0.80),
     (C_CX+1.2, C_CY+0.80)],
    'Salad Details\n(name, ingredients,\nnutrition, allergens)', lseg=2, ldy=-0.35)

# ── B: Customer ↔ P2 Manage User Account  ───────────────────────────────────
# Route via TOP margin  y=15.5
# C→P2 (Registration/Login): C top → up → right → P2 top
parrow(ax,
    [(C_CX+0.3, C_CY+1.1),
     (C_CX+0.3, 15.50),
     (P2[0]-0.3,15.50),
     (P2[0]-0.3, P2[1]+PR)],
    'Registration Details /\nLogin Credentials', lseg=1)

# P2→C (Confirmation): P2 top → up → left → C top (slightly further right)
parrow(ax,
    [(P2[0]+0.3, P2[1]+PR),
     (P2[0]+0.3, 16.10),
     (C_CX-0.3,  16.10),
     (C_CX-0.3,  C_CY+1.1)],
    'Account Confirmation /\nLogin Status', lseg=1, ldy=-0.35)

# ── C: Customer ↔ P3 Shopping Cart  ─────────────────────────────────────────
# Horizontal, same y – two offset flows
# C→P3  (Add/Remove/Update Items)
parrow(ax,
    [(C_CX+1.2, C_CY+0.20),
     (P3[0]-PR, C_CY+0.20)],
    'Add/Remove/Update Items', lseg=0, ldy=0.20)

# P3→C  (Updated Cart Contents)
parrow(ax,
    [(P3[0]-PR, C_CY-0.20),
     (C_CX+1.2, C_CY-0.20)],
    'Updated Cart Contents', lseg=0, ldy=-0.25)

# ── D: P1 ↔ D1  (horizontal, same row) ──────────────────────────────────────
parrow(ax,
    [(P1[0]+PR, P1[1]+0.12),
     (D1x,      P1[1]+0.12)],
    'Salad Info', lseg=0)

parrow(ax,
    [(D1x,      P1[1]-0.12),
     (P1[0]+PR, P1[1]-0.12)],
    '', lseg=0)  # read direction (no extra label)

# ── E: P2 ↔ D2  ──────────────────────────────────────────────────────────────
# P2→D2 (Store/Update User Info)
D2_left = D2x
D2_mid_y = P2[1]+0.30+DSH/2
parrow(ax,
    [(P2[0]+PR,  P2[1]+0.20),
     (D2_left,   P2[1]+0.20),
     (D2_left,   D2_mid_y)],
    'Store/Update\nUser Info', lseg=0)

# D2→P2 (User Details / Account Status)
parrow(ax,
    [(D2_left,  D2_mid_y),
     (D2_left,  P2[1]-0.20),
     (P2[0]+PR, P2[1]-0.20)],
    'User Details /\nAccount Status', lseg=1)

# ── F: P2 → Email Service (top) ──────────────────────────────────────────────
parrow(ax,
    [(P2[0]+PR,  P2[1]+0.35),
     (E_CX-EE_W/2, P2[1]+0.35)],
    'Verification Email', lseg=0)

# Email → P2
parrow(ax,
    [(E_CX-EE_W/2, P2[1]-0.35),
     (P2[0]+PR,    P2[1]-0.35)],
    'Verification Code\nResponse', lseg=0, ldy=-0.30)

# ── G: P2 → P4  (Auth status, route: P2 bottom → down → P4 top) ─────────────
parrow(ax,
    [(P2[0]-0.3,  P2[1]-PR),
     (P2[0]-0.3,  P4[1]+PR+0.25),
     (P4[0]+0.3,  P4[1]+PR+0.25),
     (P4[0]+0.3,  P4[1]+PR)],
    'User Authentication\nStatus', lseg=1)

# ── H: P3 ↔ D3  (vertical) ───────────────────────────────────────────────────
D3_top  = D3y + DSH
D3_cx   = D3x + DSW/2

# P3→D3 (Store Cart Items)
parrow(ax,
    [(P3[0]+0.20, P3[1]-PR),
     (P3[0]+0.20, D3_top)],
    'Store Cart Items', lseg=0, ldy=0)

# D3→P3 (Cart Data)
parrow(ax,
    [(P3[0]-0.20, D3_top),
     (P3[0]-0.20, P3[1]-PR)],
    'Cart Data', lseg=0, ldy=0)

# ── I: P3 → P4  (Checkout data, horizontal same row) ────────────────────────
parrow(ax,
    [(P3[0]+PR,  P3[1]+0.20),
     (P4[0]-PR,  P4[1]+0.20)],
    'Delivery Address /\nPayment Details', lseg=0)

# ── J: P4 ↔ Payment Gateway  (horizontal) ────────────────────────────────────
parrow(ax,
    [(P4[0]+PR,   P4[1]+0.25),
     (G_CX-EE_W/2, G_CY+0.25)],
    'Payment Request', lseg=0)

parrow(ax,
    [(G_CX-EE_W/2, G_CY-0.25),
     (P4[0]+PR,    P4[1]-0.25)],
    'Payment Confirmation /\nRejection', lseg=0, ldy=-0.30)

# ── K: P4 ↔ D5  (vertical) ────────────────────────────────────────────────────
D5_top = D5y + DSH
D5_cx  = D5x + DSW/2

parrow(ax,
    [(D5cx := D5x+DSW*.60, D5_top),
     (D5cx,                  P4[1]-PR)],
    'Saved Addresses', lseg=0, ldy=0)

parrow(ax,
    [(D5x+DSW*.30, P4[1]-PR),
     (D5x+DSW*.30, D5_top)],
    'Store Address', lseg=0, ldy=0)

# ── L: P4 → P5  (Confirmed Payment → Order Details) ─────────────────────────
# Route P4 bottom → down → left → P5 top
parrow(ax,
    [(P4[0]-0.4,  P4[1]-PR),
     (P4[0]-0.4,  P5[1]+PR+0.60),
     (P5[0]+0.4,  P5[1]+PR+0.60),
     (P5[0]+0.4,  P5[1]+PR)],
    'Confirmed Payment /\nOrder Details', lseg=1)

# ── M: P5 ↔ D4  (horizontal, same row) ───────────────────────────────────────
D4_left = D4x
D4_mid_y = P5[1]

parrow(ax,
    [(P5[0]+PR,  P5[1]+0.15),
     (D4_left,   P5[1]+0.15)],
    'Store Order', lseg=0)

parrow(ax,
    [(D4_left,  P5[1]-0.15),
     (P5[0]+PR, P5[1]-0.15)],
    'Order Status', lseg=0, ldy=-0.25)

# ── N: P5 → Email (bottom) ────────────────────────────────────────────────────
parrow(ax,
    [(D4x+DSW,    P5[1]+0.15),
     (B_CX-EE_W/2, P5[1]+0.15)],
    'Order Confirmation Email', lseg=0)

# ── O: P5 → Customer  (Order Status Updates) ─────────────────────────────────
# Route via bottom-left margin
parrow(ax,
    [(P5[0]-PR,   P5[1]-0.20),
     (2.00,       P5[1]-0.20),
     (2.00,       C_CY-1.1),
     (C_CX+1.2,   C_CY-1.1)],
    'Order Status Updates', lseg=1, ldy=-0.25)

# ── P: P5 → P6 ────────────────────────────────────────────────────────────────
parrow(ax,
    [(D4x+DSW,   P5[1]-0.20),
     (P6[0]-PR,  P6[1]+0.20)],
    'Completed Order Info', lseg=0)

# ── Q: P6 → Email (bottom) ────────────────────────────────────────────────────
parrow(ax,
    [(P6[0]+PR,    P6[1]+0.20),
     (B_CX-EE_W/2, B_CY+0.20)],
    'Update Reward Points', lseg=0)

# ── R: P6 → Customer  (Points Balance) ────────────────────────────────────────
# Route: P6 bottom → down → far left → up → Customer bottom
parrow(ax,
    [(P6[0]-0.5,  P6[1]-PR),
     (P6[0]-0.5,  1.50),
     (C_CX+0.5,   1.50),
     (C_CX+0.5,   C_CY-1.1)],
    'Points Balance /\nFree Salad Eligibility', lseg=1, ldy=-0.28)

# ═════════════════════════════════════════════════════════════════════════════
# LEGEND
# ═════════════════════════════════════════════════════════════════════════════
lx, ly = 0.25, 0.15
ax.add_patch(FancyBboxPatch((lx, ly), 8.0, 1.70,
    boxstyle='square,pad=0', lw=1, ec='#888', fc='#d0e8f5', zorder=3))
ax.text(lx+4.0, ly+1.50, 'Legend', ha='center', fontsize=8.5,
        fontweight='bold', zorder=4)
ext_entity(ax, lx+1.1, ly+0.75, 1.4, 0.60, 'External\nEntity')
c = plt.Circle((lx+3.2, ly+0.75), 0.34, fc=PROC, ec='#4a7aab', lw=1.2, zorder=4)
ax.add_patch(c)
ax.text(lx+3.2, ly+0.75, 'P#', ha='center', va='center',
        fontsize=8, fontweight='bold', color=WHITE, zorder=5)
ax.text(lx+3.2, ly+0.28, 'Process', ha='center', fontsize=7.5, zorder=5)
datastore(ax, lx+4.50, ly+0.48, 3.2, 0.55, 'D#', 'Data Store')
ax.text(lx+6.1, ly+0.28, 'Data Store', ha='center', fontsize=7.5, zorder=5)

plt.tight_layout()
plt.savefig('/workspace/output/dfd_v3.png', dpi=180,
            bbox_inches='tight', facecolor=BG)
plt.close()
print("DFD v3 done.")
