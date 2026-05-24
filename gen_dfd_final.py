"""
Level-1 DFD – FreshBite Salads
Style matching the uploaded document:
  • White background
  • External entities: pale-green fill, dark-green border
  • Processes: pale-blue fill, mid-blue border, circle
  • Data stores: pale-orange fill, dark-orange border, open-ended rect
  • Data flows: solid black arrows with italic black labels
  • Mostly straight / orthogonal routing
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

W, H = 28, 18
fig, ax = plt.subplots(figsize=(W, H))
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis('off')
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# ── palette ──────────────────────────────────────────────────
C_PROC_F  = '#D6E4F7'   # pale blue fill
C_PROC_E  = '#2E75B6'   # blue border
C_ENT_F   = '#E2EFDA'   # pale green fill
C_ENT_E   = '#375623'   # dark green border
C_DS_F    = '#FEF0D9'   # pale orange fill
C_DS_E    = '#C55A11'   # dark orange border
C_ARROW   = '#000000'
C_LABEL   = '#111111'

# ── helpers ──────────────────────────────────────────────────
def process(ax, cx, cy, num, label, r=1.0):
    c = plt.Circle((cx,cy), r, fc=C_PROC_F, ec=C_PROC_E, lw=1.8, zorder=4)
    ax.add_patch(c)
    # divider line
    ax.plot([cx-r*0.75, cx+r*0.75], [cy+0.15, cy+0.15],
            color=C_PROC_E, lw=1.0, zorder=5)
    ax.text(cx, cy+0.52, num, ha='center', va='center',
            fontsize=9.5, fontweight='bold', color=C_PROC_E, zorder=6)
    # wrap label
    words = label.split()
    mid = len(words)//2
    line1 = ' '.join(words[:mid]); line2 = ' '.join(words[mid:])
    ax.text(cx, cy-0.22, line1+'\n'+line2 if line2 else line1,
            ha='center', va='top', fontsize=8.2, color='#1a1a1a',
            fontweight='bold', zorder=6, linespacing=1.25)

def entity(ax, x, y, w, h, label):
    r = FancyBboxPatch((x,y), w, h, boxstyle='square,pad=0.05',
                        lw=2.0, ec=C_ENT_E, fc=C_ENT_F, zorder=4)
    ax.add_patch(r)
    ax.text(x+w/2, y+h/2, label, ha='center', va='center',
            fontsize=9, fontweight='bold', color=C_ENT_E, zorder=5)

def datastore(ax, x, y, w, h, ds_id, label):
    # Background
    bg = FancyBboxPatch((x+0.02, y+0.02), w-0.02, h-0.04,
                         boxstyle='square,pad=0', lw=0, fc=C_DS_F, zorder=3)
    ax.add_patch(bg)
    # Open-ended (left closed, right open)
    ax.plot([x, x],     [y, y+h], color=C_DS_E, lw=2.2, zorder=5)
    ax.plot([x, x+w],   [y+h, y+h], color=C_DS_E, lw=1.8, zorder=5)
    ax.plot([x, x+w],   [y, y],     color=C_DS_E, lw=1.8, zorder=5)
    # divider after ID
    ax.plot([x+1.0, x+1.0], [y, y+h], color=C_DS_E, lw=1.2, zorder=5)
    ax.text(x+0.5, y+h/2, ds_id, ha='center', va='center',
            fontsize=8.5, fontweight='bold', color=C_DS_E, zorder=6)
    ax.text(x+1.1+((w-1.0)/2), y+h/2, label, ha='center', va='center',
            fontsize=8.5, color='#2b1200', zorder=6)

def flow(ax, pts, label='', label_offset=(0, 0.15), ha='center'):
    """
    pts: list of (x,y) waypoints – draws connected line segments with arrowhead at end.
    """
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    # draw all but the last segment as plain lines
    for i in range(len(pts)-2):
        ax.plot([xs[i], xs[i+1]], [ys[i], ys[i+1]],
                color=C_ARROW, lw=1.15, zorder=3)
    # last segment with arrowhead
    ax.annotate('', xy=(xs[-1], ys[-1]), xytext=(xs[-2], ys[-2]),
                arrowprops=dict(arrowstyle='->', color=C_ARROW, lw=1.15), zorder=3)
    # label at midpoint of whole path
    if label:
        mx = xs[len(xs)//2] + label_offset[0]
        my = ys[len(ys)//2] + label_offset[1]
        ax.text(mx, my, label, ha=ha, va='bottom',
                fontsize=6.8, color=C_LABEL, style='italic', zorder=7,
                bbox=dict(boxstyle='round,pad=0.12', fc='white', ec='none', alpha=0.85))

# ═════════════════════════════════════════════════════════════
#  TITLE
# ═════════════════════════════════════════════════════════════
ax.text(W/2, H-0.38,
        'First-Level Data Flow Diagram (Level-1 DFD) – FreshBite Salads Online Ordering System',
        ha='center', fontsize=12.5, fontweight='bold', color='#0D2B55', zorder=6)

# ═════════════════════════════════════════════════════════════
#  EXTERNAL ENTITIES
# ═════════════════════════════════════════════════════════════
# Customer appears on the left (same entity, different flow sources)
entity(ax, 0.2, 13.8, 2.5, 0.85, 'Customer')    # for Browse
entity(ax, 0.2, 10.5, 2.5, 0.85, 'Customer')    # for User Acct
entity(ax, 0.2,  7.2, 2.5, 0.85, 'Customer')    # for Cart
entity(ax, 0.2,  2.3, 2.5, 0.85, 'Customer')    # for status/rewards

# Right-side entities
entity(ax, 24.0, 13.5, 3.7, 0.85, 'Email Service')
entity(ax, 24.0,  9.5, 3.7, 0.85, 'Payment Gateway')
entity(ax, 24.0,  4.5, 3.7, 0.85, 'Email Service')

# ═════════════════════════════════════════════════════════════
#  PROCESSES
# ═════════════════════════════════════════════════════════════
P1  = (5.8, 14.2)   # Browse Menu
P2  = (15.0, 14.2)  # Manage User Account
P3  = (5.8, 8.5)    # Manage Shopping Cart
P4  = (14.0, 8.5)   # Process Checkout
P5  = (20.5, 8.5)   # Manage Orders
P6  = (14.0, 3.2)   # Manage Reward Points

process(ax, *P1, '1.0', 'Browse Menu')
process(ax, *P2, '2.0', 'Manage User Account')
process(ax, *P3, '3.0', 'Manage Shopping Cart')
process(ax, *P4, '4.0', 'Process Checkout')
process(ax, *P5, '5.0', 'Manage Orders')
process(ax, *P6, '6.0', 'Manage Reward Points')

# ═════════════════════════════════════════════════════════════
#  DATA STORES
# ═════════════════════════════════════════════════════════════
# D1 Salad Database – between P1 and P2 at top
D1 = (9.0, 15.5); ds_w = 4.6; ds_h = 0.62
datastore(ax, D1[0], D1[1], ds_w, ds_h, 'D1', 'Salad Database')

# D2 User Account DB – below P2 / above P4
D2 = (9.0, 12.0)
datastore(ax, D2[0], D2[1], 5.0, ds_h, 'D2', 'User Account Database')

# D3 Shopping Cart – right of P3
D3 = (8.4, 9.8)
datastore(ax, D3[0], D3[1], 4.0, ds_h, 'D3', 'Shopping Cart')

# D5 Address Database – above P4
D5 = (11.0, 11.0)
datastore(ax, D5[0], D5[1], 4.5, ds_h, 'D5', 'Address Database')

# D4 Order Database – right of P5
D4 = (17.8, 10.5)
datastore(ax, D4[0], D4[1], 4.4, ds_h, 'D4', 'Order Database')

# ═════════════════════════════════════════════════════════════
#  DATA FLOWS
# ═════════════════════════════════════════════════════════════
R = 1.0   # process radius

# ── P1 Browse Menu ──────────────────────────────────────────
# Customer → P1
flow(ax, [(2.7, 14.22), (4.8, 14.22)], 'Browse Request')
# D1 → P1
flow(ax, [(D1[0], D1[1]), (5.1, D1[1]), (5.1, 15.2)], 'Salad Info',
     label_offset=(0.3, 0.08))
# P1 → Customer
flow(ax, [(4.8, 14.0), (2.7, 14.0)], 'Salad Details',
     label_offset=(0, -0.22), ha='center')

# ── P2 Manage User Account ──────────────────────────────────
# Customer → P2 (horizontal via bend)
flow(ax, [(2.7, 10.92), (2.7, 14.5), (14.0, 14.5)],
     'Registration Details / Login Credentials', label_offset=(0, 0.12))
# P2 → D2
flow(ax, [(14.7, 13.25), (14.7, 12.62)], 'Store/Update User Info',
     label_offset=(0.15, 0.08))
# D2 → P2
flow(ax, [(13.3, 12.62), (13.3, 13.25)], 'User Details / Account Status',
     label_offset=(-0.2, 0.08), ha='right')
# P2 → Email Service
flow(ax, [(16.0, 14.22), (24.0, 14.22)], 'Verification Email')
# P2 → Customer
flow(ax, [(14.3, 13.2), (14.3, 11.35), (2.7, 11.35)],
     'Account Confirmation / Login Status', label_offset=(0, 0.12))

# ── P3 Manage Shopping Cart ─────────────────────────────────
# Customer → P3
flow(ax, [(2.7, 7.62), (4.8, 7.62)], 'Add/Remove/Update Items',
     label_offset=(0, -0.22))
# D1 → P3 (vertical)
flow(ax, [(11.3, 15.5), (11.3, 9.8), (8.4, 9.8), (8.4, 9.5)],
     'Salad Price & Portion Info', label_offset=(0.35, 0.08))
# P3 ↔ D3
flow(ax, [(6.0, 9.5), (6.0, 9.8), (8.4, 9.8)], 'Store Cart Items',
     label_offset=(0, 0.12))
flow(ax, [(8.4, 9.95), (6.8, 9.95), (6.8, 9.5)], 'Cart Data',
     label_offset=(0, 0.12))
# P3 → Customer
flow(ax, [(4.8, 8.2), (2.7, 8.2)], 'Updated Cart Contents',
     label_offset=(0, -0.22))
# P3 → P4
flow(ax, [(6.8, 8.5), (13.0, 8.5)], 'Cart Items for Checkout')

# ── P4 Process Checkout ─────────────────────────────────────
# Customer → P4
flow(ax, [(2.7, 7.5), (2.7, 7.8), (7.0, 7.8), (7.0, 7.2), (13.0, 7.2)],
     'Delivery Address / Payment Details', label_offset=(0, -0.2))
# D2 → P4 (auth)
flow(ax, [(13.3, 12.0), (13.3, 9.5)], 'User Authentication Status',
     label_offset=(-0.2, 0.12), ha='right')
# D5 ↔ P4
flow(ax, [(14.0, 11.0), (14.0, 9.5)], 'Saved Addresses',
     label_offset=(0.15, 0.1))
flow(ax, [(14.6, 9.5), (14.6, 11.0)], 'Store Address',
     label_offset=(0.15, 0.1))
# P4 → Payment Gateway
flow(ax, [(15.0, 8.5), (24.0, 9.92)], 'Payment Request',
     label_offset=(0, 0.12))
flow(ax, [(24.0, 9.7), (15.0, 8.2)], 'Payment Confirmation / Rejection',
     label_offset=(0, -0.22))
# P4 → P5
flow(ax, [(15.0, 8.5), (19.5, 8.5)], 'Confirmed Payment & Order Details')

# ── P5 Manage Orders ────────────────────────────────────────
# P5 ↔ D4
flow(ax, [(20.5, 9.5), (20.5, 10.5), (22.2, 10.5)], 'Store Order',
     label_offset=(0, 0.12))
flow(ax, [(22.2, 10.72), (20.9, 10.72), (20.9, 9.5)], 'Order Status',
     label_offset=(0, 0.12))
# P5 → Email Service
flow(ax, [(21.5, 8.5), (27.7, 8.5), (27.7, 4.92), (27.7, 4.92)],
     '', label_offset=(0,0))
flow(ax, [(21.5, 8.2), (21.5, 5.8), (24.0, 5.0)],
     'Order Confirmation Email', label_offset=(0.2, 0.12))
# P5 → Customer (order status updates)
flow(ax, [(20.5, 7.5), (20.5, 2.72), (2.7, 2.72)],
     'Order Status Updates', label_offset=(0, 0.12))
# P5 → P6
flow(ax, [(20.5, 7.5), (20.5, 4.2), (15.0, 4.2), (15.0, 4.2)],
     'Completed Order Info', label_offset=(0, 0.12))

# ── P6 Manage Reward Points ─────────────────────────────────
# D2 → P6
flow(ax, [(9.0, 12.0), (8.0, 12.0), (8.0, 3.2), (13.0, 3.2)],
     'Current Points Balance', label_offset=(0.3, 0.12))
# P6 → D2
flow(ax, [(13.2, 4.2), (13.2, 12.0), (9.0, 12.0)],
     'Update Reward Points', label_offset=(-0.3, 0.12), ha='right')
# P6 → Customer
flow(ax, [(13.0, 2.8), (2.7, 2.8)],
     'Points Balance / Free Salad Eligibility', label_offset=(0, -0.22))

# ═════════════════════════════════════════════════════════════
#  LEGEND
# ═════════════════════════════════════════════════════════════
lx, ly = 0.3, 0.1
# Process
ax.add_patch(plt.Circle((lx+0.3, ly+0.32), 0.28, fc=C_PROC_F, ec=C_PROC_E, lw=1.5, zorder=4))
ax.text(lx+0.7, ly+0.32, '= Process', va='center', fontsize=8, color='#111')
# Entity
ax.add_patch(FancyBboxPatch((lx+1.8, ly+0.1), 0.8, 0.44,
             boxstyle='square,pad=0.03', lw=1.8, ec=C_ENT_E, fc=C_ENT_F, zorder=4))
ax.text(lx+2.2, ly+0.32, 'Ent', ha='center', va='center', fontsize=8, color=C_ENT_E, fontweight='bold')
ax.text(lx+2.72, ly+0.32, '= External Entity', va='center', fontsize=8, color='#111')

# Data store
ds_lx = lx + 5.0
ax.plot([ds_lx, ds_lx], [ly+0.08, ly+0.56], color=C_DS_E, lw=2.2, zorder=4)
ax.plot([ds_lx, ds_lx+1.2], [ly+0.56, ly+0.56], color=C_DS_E, lw=1.8, zorder=4)
ax.plot([ds_lx, ds_lx+1.2], [ly+0.08, ly+0.08], color=C_DS_E, lw=1.8, zorder=4)
ax.add_patch(FancyBboxPatch((ds_lx+0.02, ly+0.09), 1.18, 0.46,
             boxstyle='square,pad=0', lw=0, fc=C_DS_F, zorder=3))
ax.text(ds_lx+0.6, ly+0.32, 'Dx', ha='center', va='center', fontsize=7.5,
        color=C_DS_E, fontweight='bold')
ax.text(ds_lx+1.35, ly+0.32, '= Data Store', va='center', fontsize=8, color='#111')

# Arrow
ax.annotate('', xy=(lx+8.5, ly+0.32), xytext=(lx+7.6, ly+0.32),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.2))
ax.text(lx+8.65, ly+0.32, '= Data Flow', va='center', fontsize=8, color='#111')

plt.tight_layout(pad=0.4)
plt.savefig('/workspace/dfd_final.png', dpi=150, bbox_inches='tight', facecolor='white')
print("DFD final saved.")
