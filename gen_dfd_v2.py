"""
Clean Level-1 DFD – FreshBite Salads
6 processes matching the preferred document's structure.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

W, H = 22, 15
fig, ax = plt.subplots(figsize=(W, H))
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis('off')
fig.patch.set_facecolor('#FFFFFF')

# ── colour palette ──────────────────────────────────────────
C_PROC   = '#1B4F8A'   # dark blue – process circle
C_ENT    = '#1E6B3E'   # dark green – external entity box
C_STORE  = '#7B3F00'   # dark brown – data store
C_FLOW   = '#444444'   # arrow / flow label
BG_ENT   = '#EAF6EE'
BG_STORE = '#FFF8F0'

# ── helpers ─────────────────────────────────────────────────
def process(ax, cx, cy, num, label, r=0.78):
    c1 = plt.Circle((cx, cy), r, color=C_PROC, zorder=4)
    c2 = plt.Circle((cx, cy), r, facecolor='none', edgecolor='white', lw=1.4, zorder=5)
    ax.add_patch(c1); ax.add_patch(c2)
    ax.text(cx, cy+0.22, num, ha='center', va='center', fontsize=9,
            fontweight='bold', color='white', zorder=6)
    ax.text(cx, cy-0.22, label, ha='center', va='center', fontsize=7.2,
            color='white', zorder=6)

def entity(ax, x, y, w, h, label):
    r = FancyBboxPatch((x,y), w, h, boxstyle='square,pad=0.04',
                        linewidth=2, edgecolor=C_ENT, facecolor=BG_ENT, zorder=4)
    ax.add_patch(r)
    ax.text(x+w/2, y+h/2, label, ha='center', va='center',
            fontsize=8, fontweight='bold', color=C_ENT, zorder=5)

def datastore(ax, x, y, w, h, ds_id, label):
    # open-ended (left side + top + bottom lines only)
    ax.plot([x, x],     [y, y+h], color=C_STORE, lw=2, zorder=4)
    ax.plot([x, x+w],   [y+h, y+h], color=C_STORE, lw=1.5, zorder=4)
    ax.plot([x, x+w],   [y, y],   color=C_STORE, lw=1.5, zorder=4)
    bg = FancyBboxPatch((x+0.01, y+0.01), w-0.01, h-0.02,
                         boxstyle='square,pad=0', linewidth=0,
                         edgecolor='none', facecolor=BG_STORE, zorder=3)
    ax.add_patch(bg)
    ax.text(x+0.28, y+h/2, ds_id, ha='left', va='center',
            fontsize=8, fontweight='bold', color=C_STORE, zorder=5)
    ax.text(x+w/2+0.15, y+h/2, label, ha='center', va='center',
            fontsize=7.8, color='#2b1200', zorder=5)

def flow(ax, x1, y1, x2, y2, label='', lpad=(0,0.12)):
    ax.annotate('', xy=(x2,y2), xytext=(x1,y1),
                arrowprops=dict(arrowstyle='->', color=C_FLOW, lw=1.1,
                                connectionstyle='arc3,rad=0.0'), zorder=3)
    if label:
        mx = (x1+x2)/2 + lpad[0]
        my = (y1+y2)/2 + lpad[1]
        ax.text(mx, my, label, ha='center', va='bottom', fontsize=6.4,
                color='#333', style='italic', zorder=7,
                bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.9))

# ── title ────────────────────────────────────────────────────
ax.text(W/2, H-0.35, 'FreshBite Salads – First-Level Data Flow Diagram (Level-1 DFD)',
        ha='center', va='center', fontsize=13, fontweight='bold', color='#1a1a2e')

# ── External Entities ────────────────────────────────────────
# Customer (left, two positions for clarity)
entity(ax, 0.15, 10.8,  2.3, 0.85, 'Customer')   # top
entity(ax, 0.15, 6.1,   2.3, 0.85, 'Customer')   # mid
entity(ax, 0.15, 2.2,   2.3, 0.85, 'Customer')   # bottom

# Payment Gateway (right)
entity(ax, 19.55, 9.0,  2.3, 0.85, 'Payment\nGateway')
# Email Service (right)
entity(ax, 19.55, 6.1,  2.3, 0.85, 'Email\nService')

# ── Processes ─────────────────────────────────────────────────
# 1.0 Browse Menu
process(ax, 5.0, 12.2, '1.0', 'Browse\nMenu')
# 2.0 Manage User Account
process(ax, 5.0, 9.0,  '2.0', 'Manage\nUser Acct')
# 3.0 Manage Shopping Cart
process(ax, 5.0, 6.5,  '3.0', 'Manage\nCart')
# 4.0 Process Checkout
process(ax, 11.0, 6.5, '4.0', 'Process\nCheckout')
# 5.0 Manage Orders
process(ax, 16.0, 6.5, '5.0', 'Manage\nOrders')
# 6.0 Manage Reward Points
process(ax, 11.0, 3.0, '6.0', 'Manage\nReward Pts')

# ── Data Stores ────────────────────────────────────────────────
# D1 Salad Database
datastore(ax, 6.8,  13.0, 4.2, 0.55, 'D1', 'Salad Database')
# D2 User Account Database
datastore(ax, 6.8,  10.2, 4.6, 0.55, 'D2', 'User Account DB')
# D3 Shopping Cart
datastore(ax, 6.8,   7.8, 3.8, 0.55, 'D3', 'Shopping Cart')
# D4 Order Database
datastore(ax, 13.8,  7.8, 3.8, 0.55, 'D4', 'Order Database')
# D5 Address Database
datastore(ax, 13.8,  4.5, 3.8, 0.55, 'D5', 'Address DB')

# ── Data Flows ─────────────────────────────────────────────────
# Customer → 1.0 Browse Menu
flow(ax, 2.45, 11.22, 4.22, 12.2, 'Browse Request')
# D1 → 1.0
flow(ax, 6.8, 13.22, 5.78, 12.65, 'Salad Info')
# 1.0 → Customer
flow(ax, 4.22, 11.9, 2.45, 11.05, 'Salad Details')

# Customer → 2.0 Manage User Account
flow(ax, 2.45, 9.42, 4.22, 9.0, 'Reg / Login Details')
# 2.0 ↔ D2
flow(ax, 5.78, 9.3, 6.8, 10.42, 'Store/Update User')
flow(ax, 6.8, 10.25, 5.78, 8.75, 'User Details')
# 2.0 → Email Service
flow(ax, 5.78, 9.42, 19.55, 6.53, 'Verification Email', lpad=(0, 0.12))
# 2.0 → Customer
flow(ax, 4.22, 8.65, 2.45, 9.1, 'Account Status')

# Customer → 3.0 Cart
flow(ax, 2.45, 6.53, 4.22, 6.5, 'Add/Remove/Update Items')
# D1 → 3.0
flow(ax, 7.5, 13.0, 5.0, 7.28, 'Price & Portion Info', lpad=(-0.5, 0.12))
# 3.0 ↔ D3
flow(ax, 5.78, 6.85, 6.8, 8.05, 'Store Cart Items')
flow(ax, 6.8, 7.88, 5.78, 6.7,  'Cart Data')
# 3.0 → Customer
flow(ax, 4.22, 6.2, 2.45, 6.27, 'Updated Cart')
# 3.0 → 4.0
flow(ax, 5.78, 6.5, 10.22, 6.5, 'Cart Items for Checkout')

# Customer → 4.0 (delivery + payment)
flow(ax, 2.45, 6.42, 10.22, 6.3, 'Delivery Address / Payment Details', lpad=(0,-0.18))
# D2 → 4.0 (auth check)
flow(ax, 9.2, 10.42, 11.0, 7.28, 'Auth Status', lpad=(0.45, 0.1))
# D5 ↔ 4.0
flow(ax, 11.0, 5.72, 13.8, 4.77, 'Store Address')
flow(ax, 13.8, 4.95, 11.0, 5.72, 'Saved Addresses', lpad=(0, 0.12))
# 4.0 → Payment Gateway
flow(ax, 11.78, 6.9, 19.55, 9.42, 'Payment Request', lpad=(0, 0.12))
flow(ax, 19.55, 9.25, 11.78, 7.05, 'Payment Confirmation', lpad=(0,-0.18))
# 4.0 → 5.0
flow(ax, 11.78, 6.5, 15.22, 6.5, 'Confirmed Order Details')

# 5.0 ↔ D4
flow(ax, 16.0, 7.28, 15.9, 8.05, 'Store Order')
flow(ax, 15.9, 7.88, 16.0, 7.28, 'Order Status', lpad=(0.55, 0.0))
# 5.0 → Email Service
flow(ax, 16.78, 6.9, 19.55, 6.53, 'Confirmation Email')
# 5.0 → Customer
flow(ax, 15.22, 6.2, 2.45, 2.62, 'Order Status Updates', lpad=(0, 0.12))
# 5.0 → 6.0
flow(ax, 13.0, 6.1, 11.78, 3.6, 'Completed Order Info', lpad=(0.5, 0.1))

# 6.0 ↔ D2
flow(ax, 10.22, 3.0, 7.5, 10.2, 'Update Reward Points', lpad=(-1.0, 0.0))
flow(ax, 7.5, 10.3, 10.22, 3.3, 'Current Points Balance', lpad=(1.0, 0.0))
# 6.0 → Customer
flow(ax, 10.22, 2.75, 2.45, 2.42, 'Points Balance / Free Salad Eligibility')

# ── Legend ────────────────────────────────────────────────────
lx, ly = 0.2, 0.1
# Process
ax.add_patch(plt.Circle((lx+0.22, ly+0.28), 0.2, color=C_PROC, zorder=4))
ax.text(lx+0.52, ly+0.28, '= Process', va='center', fontsize=7.5, color='#222')
# Entity
r_l = FancyBboxPatch((lx+1.5, ly+0.08), 0.55, 0.38, boxstyle='square,pad=0.02',
                      lw=1.8, edgecolor=C_ENT, facecolor=BG_ENT, zorder=4)
ax.add_patch(r_l)
ax.text(lx+1.77, ly+0.27, 'Entity', ha='center', va='center', fontsize=7.5, color=C_ENT)
ax.text(lx+2.2, ly+0.28, '= External Entity', va='center', fontsize=7.5, color='#222')
# Data Store
ax.plot([lx+4.3, lx+4.3], [ly+0.08, ly+0.46], color=C_STORE, lw=2)
ax.plot([lx+4.3, lx+5.2], [ly+0.46, ly+0.46], color=C_STORE, lw=1.5)
ax.plot([lx+4.3, lx+5.2], [ly+0.08, ly+0.08], color=C_STORE, lw=1.5)
ax.text(lx+4.8, ly+0.27, '= Data Store', ha='left', va='center', fontsize=7.5, color='#222')
# Flow
ax.annotate('', xy=(lx+7.3, ly+0.28), xytext=(lx+6.6, ly+0.28),
            arrowprops=dict(arrowstyle='->', color=C_FLOW, lw=1.1))
ax.text(lx+7.4, ly+0.28, '= Data Flow', va='center', fontsize=7.5, color='#222')

plt.tight_layout(pad=0.3)
plt.savefig('/workspace/dfd_v2.png', dpi=150, bbox_inches='tight', facecolor='white')
print("DFD v2 saved.")
