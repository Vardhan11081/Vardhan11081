import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(figsize=(22, 16))
ax.set_xlim(0, 22)
ax.set_ylim(0, 16)
ax.axis('off')
BG = '#a8d8ea'
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

PROC_COL  = '#0a3055'   # dark navy blue for process circles
EXT_COL   = '#2e6b3e'   # dark green for external entities
DS_ORG    = '#d4831a'   # orange left strip
DS_BG     = '#f8f8f8'   # white body
BORDER    = '#444444'
ARR       = '#111111'
WHITE     = 'white'

# ─── drawing helpers ─────────────────────────────────────────────────────────

def process(ax, cx, cy, r, num, *lines):
    c = plt.Circle((cx, cy), r, facecolor=PROC_COL,
                   edgecolor='#4a7aab', linewidth=1.5, zorder=4)
    ax.add_patch(c)
    ax.plot([cx - r*0.78, cx + r*0.78], [cy + r*0.30, cy + r*0.30],
            color=WHITE, lw=0.8, alpha=0.55, zorder=5)
    ax.text(cx, cy + r*0.63, num, ha='center', va='center',
            fontsize=9, fontweight='bold', color=WHITE, zorder=6)
    n = len(lines)
    for i, ln in enumerate(lines):
        yy = cy - r*0.05 - (i - (n-1)/2) * r*0.38
        ax.text(cx, yy, ln, ha='center', va='center',
                fontsize=8, fontweight='bold', color=WHITE, zorder=6)

def ext_entity(ax, cx, cy, w, h, *lines):
    for off, lw in [(0, 2.2), (0.13, 1.5)]:
        ax.add_patch(FancyBboxPatch(
            (cx - w/2 + off, cy - h/2 + off),
            w - 2*off, h - 2*off,
            boxstyle="square,pad=0",
            linewidth=lw, edgecolor=WHITE, facecolor=EXT_COL, zorder=4))
    n = len(lines)
    for i, ln in enumerate(lines):
        yy = cy + (n-1)*0.20 - i*0.40
        ax.text(cx, yy, ln, ha='center', va='center',
                fontsize=9, fontweight='bold', color=WHITE, zorder=6)

def datastore(ax, x1, y, w, h, dsid, name):
    ow = 0.85
    ax.add_patch(mpatches.Rectangle((x1, y), w, h,
                                    fc=DS_BG, ec=BORDER, lw=1.5, zorder=4))
    ax.add_patch(mpatches.Rectangle((x1, y), ow, h,
                                    fc=DS_ORG, ec='none', zorder=5))
    ax.plot([x1+ow, x1+ow], [y, y+h], color=BORDER, lw=1.5, zorder=6)
    ax.text(x1+ow/2, y+h/2, dsid, ha='center', va='center',
            fontsize=8, fontweight='bold', color=WHITE, zorder=7)
    ax.text(x1+ow+(w-ow)/2, y+h/2, name, ha='center', va='center',
            fontsize=8.5, zorder=7)

def arrow(ax, x1, y1, x2, y2, label='', fs=7.2, color=ARR, rad=0):
    cs = f'arc3,rad={rad}' if rad != 0 else 'arc3,rad=0'
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.25,
                                connectionstyle=cs))
    if label:
        mx = (x1+x2)/2 + abs(y2-y1)*rad*0.5
        my = (y1+y2)/2
        ax.text(mx, my, label, ha='center', va='center', fontsize=fs,
                color='#111', multialignment='center',
                bbox=dict(boxstyle='round,pad=0.14', fc=WHITE, ec='none', alpha=0.88))

# ─── Title ────────────────────────────────────────────────────────────────────
ax.text(11, 15.65, 'FreshBite Salads – Level 1 Data Flow Diagram',
        ha='center', va='center', fontsize=13.5, fontweight='bold',
        color='#0a2040')

# ─── External Entities ────────────────────────────────────────────────────────
ext_entity(ax,  1.60,  9.50, 2.35, 2.10, 'Customer')
ext_entity(ax, 20.45, 14.20, 2.30, 1.50, 'Email', 'Service')
ext_entity(ax, 20.45,  9.20, 2.30, 1.80, 'Payment', 'Gateway')
ext_entity(ax, 20.45,  3.80, 2.30, 1.50, 'Email', 'Service')

# ─── Processes ────────────────────────────────────────────────────────────────
PR = 1.18
process(ax,  5.50, 13.50, PR, '1.0', 'Browse', 'Menu')
process(ax, 13.50, 13.50, PR, '2.0', 'Manage User', 'Account')
process(ax,  5.50,  9.00, PR, '3.0', 'Manage', 'Shopping', 'Cart')
process(ax, 11.50,  9.00, PR, '4.0', 'Process', 'Checkout')
process(ax,  8.00,  4.50, PR, '5.0', 'Manage', 'Orders')
process(ax, 14.50,  3.00, PR, '6.0', 'Manage Reward', 'Points')

# ─── Data Stores ──────────────────────────────────────────────────────────────
DSW, DSH = 4.30, 0.68
datastore(ax,  8.20, 13.10, DSW,      DSH, 'D1', 'Salad Database')
datastore(ax, 15.90, 11.90, DSW+0.5,  DSH, 'D2', 'User Account Database')
datastore(ax,  7.00,  7.00, DSW,      DSH, 'D3', 'Shopping Cart')
datastore(ax, 10.20,  4.55, DSW,      DSH, 'D4', 'Order Database')
datastore(ax, 13.70,  8.20, DSW,      DSH, 'D5', 'Address Database')

# ─── Arrows ───────────────────────────────────────────────────────────────────

# Customer → P1  Browse Request
arrow(ax, 2.78, 10.30, 4.35, 13.10, 'Browse Request')

# P1 → Customer  Salad Details
arrow(ax, 4.35, 12.85, 2.78,  9.80,
      'Salad Details\n(name, ingredients,\nnutrition, allergens)')

# Customer → P2  Registration / Login
arrow(ax, 2.78, 10.10, 12.35, 13.30,
      'Registration Details /\nLogin Credentials')

# P2 → Customer  Account Confirmation
arrow(ax, 12.35, 13.10, 2.78,  9.70,
      'Account Confirmation /\nLogin Status', rad=-0.15)

# Customer → P3  Add/Remove/Update Items
arrow(ax, 2.78,  9.30, 4.35,  9.30, 'Add/Remove/Update Items')

# P3 → Customer  Updated Cart Contents
arrow(ax, 4.35,  9.00, 2.78,  9.05, 'Updated Cart Contents')

# P3 → Customer  Salad Price / Portion Info
arrow(ax, 4.35,  8.75, 2.78,  8.75, 'Salad Price /\nPortion Info')

# P1 ↔ D1
arrow(ax, 6.68, 13.50, 8.20, 13.45, 'Salad Info')

# P2 → D2
arrow(ax, 14.50, 13.80, 16.65, 12.60, 'Store/Update\nUser Info')

# D2 → P2
arrow(ax, 16.65, 12.40, 14.50, 13.30, 'User Details /\nAccount Status')

# P2 → Email Service top
arrow(ax, 14.55, 13.55, 19.30, 14.20, 'Verification Email')

# Email Service top → P2
arrow(ax, 19.30, 14.00, 14.55, 13.35, 'Verification Code\nResponse')

# P2 → P4  User Auth Status
arrow(ax, 13.00, 12.32, 11.50, 10.18, 'User Authentication\nStatus')

# P3 → D3  Store Cart Items
arrow(ax, 6.20,  8.30, 7.80,  7.35, 'Store Cart Items')

# D3 → P3  Cart Data
arrow(ax, 7.80,  7.10, 6.20,  8.10, 'Cart Data')

# P3 → P4
arrow(ax, 6.68,  9.00, 10.32, 9.00, 'Delivery Address /\nPayment Details')

# P4 → Payment Gateway
arrow(ax, 12.55,  9.40, 19.30,  9.40, 'Payment Request')

# Payment Gateway → P4
arrow(ax, 19.30,  9.05, 12.55,  8.75, 'Payment Confirmation /\nRejection')

# P4 → D5
arrow(ax, 12.60,  8.55, 13.70,  8.55, 'Store Address')

# D5 → P4
arrow(ax, 13.70,  8.30, 12.60,  8.30, 'Saved Addresses')

# P4 → P5
arrow(ax, 10.80,  7.85,  8.80,  5.65, 'Confirmed Payment /\nOrder Details')

# P5 → D4
arrow(ax,  9.15,  4.75, 10.20,  4.88, 'Store Order')

# D4 → P5
arrow(ax, 10.20,  4.60,  9.15,  4.40, 'Order Status')

# P5 → Customer  Order Status Updates
arrow(ax,  6.85,  3.75,  2.78,  8.65, 'Order Status\nUpdates')

# P5 → Email bottom  Order Confirmation
arrow(ax,  9.10,  3.90, 19.30,  3.80, 'Order Confirmation Email')

# P5 → P6
arrow(ax,  9.15,  4.25, 13.30,  3.20, 'Completed Order Info')

# P6 → Customer  Points Balance
arrow(ax, 13.35,  2.30,  2.78,  8.50, 'Points Balance /\nFree Salad Eligibility')

# P6 → Email bottom  Update Reward Points
arrow(ax, 15.60,  3.00, 19.30,  3.50, 'Update Reward\nPoints')

# ─── Legend ───────────────────────────────────────────────────────────────────
lx, ly = 0.25, 0.15
ax.add_patch(FancyBboxPatch((lx, ly), 7.5, 1.50,
             boxstyle="square,pad=0", lw=1, ec='#888', fc='#d8eef8', zorder=3))
ax.text(lx+3.75, ly+1.30, 'Legend', ha='center', fontsize=8.5,
        fontweight='bold', zorder=4)
# ext entity swatch
ext_entity(ax, lx+1.0, ly+0.70, 1.3, 0.52, 'External\nEntity')
ax.text(lx+1.0, ly+0.25, 'External Entity', ha='center', fontsize=7.5, zorder=5)

# process swatch
c = plt.Circle((lx+3.2, ly+0.72), 0.32, facecolor=PROC_COL,
               edgecolor='#4a7aab', lw=1.2, zorder=4)
ax.add_patch(c)
ax.text(lx+3.2, ly+0.72, 'P#', ha='center', va='center',
        fontsize=7.5, fontweight='bold', color=WHITE, zorder=5)
ax.text(lx+3.2, ly+0.25, 'Process', ha='center', fontsize=7.5, zorder=5)

# datastore swatch
datastore(ax, lx+4.5, ly+0.47, 2.7, 0.50, 'D#', 'Data Store')
ax.text(lx+5.85, ly+0.25, 'Data Store', ha='center', fontsize=7.5, zorder=5)

plt.tight_layout()
plt.savefig('/workspace/output/dfd_level1_v2.png', dpi=180,
            bbox_inches='tight', facecolor=BG)
plt.close()
print("DFD v2 saved.")
