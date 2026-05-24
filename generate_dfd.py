import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(20, 14))
ax.set_xlim(0, 20)
ax.set_ylim(0, 14)
ax.axis('off')
ax.set_facecolor('#F8F9FA')
fig.patch.set_facecolor('#F8F9FA')

# Title
ax.text(10, 13.5, "FreshBite Salads – First-Level Data Flow Diagram (Level-1 DFD)",
        ha='center', va='center', fontsize=14, fontweight='bold', color='#1a1a2e')

# ─────────────────────────────────────────
# Helper functions
# ─────────────────────────────────────────

def draw_process(ax, cx, cy, label, num, r=0.85, color='#4A90D9'):
    """Circle = Process"""
    circle = plt.Circle((cx, cy), r, color=color, zorder=3)
    ax.add_patch(circle)
    circle2 = plt.Circle((cx, cy), r, color='white', fill=False, lw=1.5, zorder=4)
    ax.add_patch(circle2)
    ax.text(cx, cy+0.25, num, ha='center', va='center', fontsize=9, fontweight='bold',
            color='white', zorder=5)
    ax.text(cx, cy-0.22, label, ha='center', va='center', fontsize=7.5, color='white',
            zorder=5, wrap=True)

def draw_datastore(ax, x, y, w, h, label, ds_id, color='#E8F4FD', border='#2C7BB6'):
    """Open-ended rectangle = Data Store"""
    rect = FancyBboxPatch((x, y), w, h, boxstyle="square,pad=0", 
                          linewidth=1.5, edgecolor=border, facecolor=color, zorder=3)
    ax.add_patch(rect)
    # Left vertical line only (open on right side) – classic DFD notation
    ax.plot([x, x], [y, y+h], color=border, lw=2, zorder=4)
    ax.plot([x, x+w], [y+h, y+h], color=border, lw=2, zorder=4)
    ax.plot([x, x+w], [y, y], color=border, lw=2, zorder=4)
    ax.text(x + 0.3, y + h/2, ds_id, ha='left', va='center', fontsize=8,
            fontweight='bold', color=border, zorder=5)
    ax.text(x + w/2 + 0.2, y + h/2, label, ha='center', va='center', fontsize=8,
            color='#1a1a2e', zorder=5)

def draw_entity(ax, x, y, w, h, label, color='#FFF3CD', border='#856404'):
    """Rectangle = External Entity"""
    rect = FancyBboxPatch((x, y), w, h, boxstyle="square,pad=0.05",
                          linewidth=2, edgecolor=border, facecolor=color, zorder=3)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, label, ha='center', va='center', fontsize=8.5,
            fontweight='bold', color=border, zorder=5)

def arrow(ax, x1, y1, x2, y2, label='', color='#555555', lw=1.2):
    """Labeled arrow for data flow"""
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw), zorder=2)
    mx, my = (x1+x2)/2, (y1+y2)/2
    if label:
        ax.text(mx, my + 0.12, label, ha='center', va='bottom', fontsize=6.5,
                color='#333333', style='italic', zorder=6,
                bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='none', alpha=0.8))

# ─────────────────────────────────────────
# External Entities
# ─────────────────────────────────────────
draw_entity(ax, 0.2, 10.8, 2.2, 0.9, "Customer", color='#D4EDDA', border='#155724')
draw_entity(ax, 0.2, 7.2, 2.2, 0.9, "Customer", color='#D4EDDA', border='#155724')
draw_entity(ax, 17.6, 8.5, 2.2, 0.9, "Payment\nGateway", color='#FCE4EC', border='#880E4F')
draw_entity(ax, 17.6, 5.5, 2.2, 0.9, "Email\nService", color='#E3F2FD', border='#0D47A1')
draw_entity(ax, 17.6, 2.5, 2.2, 0.9, "Delivery\nService", color='#FFF9C4', border='#F57F17')

# ─────────────────────────────────────────
# Processes
# ─────────────────────────────────────────
#  P1: User Registration & Auth   – top-left area
draw_process(ax, 4.0, 11.2, "User Reg /\nAuth", "P1", r=0.75, color='#3A6BC8')
#  P2: Browse Salads              – top-center
draw_process(ax, 8.0, 11.2, "Browse\nSalads", "P2", r=0.75, color='#3A6BC8')
#  P3: Shopping Cart Mgmt         – center-left
draw_process(ax, 4.0, 7.8, "Shopping\nCart Mgmt", "P3", r=0.75, color='#3A6BC8')
#  P4: Checkout & Order Proc.     – center
draw_process(ax, 10.0, 7.8, "Checkout &\nOrder Proc.", "P4", r=0.75, color='#3A6BC8')
#  P5: Payment Processing         – center-right
draw_process(ax, 15.5, 8.5, "Payment\nProcessing", "P5", r=0.75, color='#3A6BC8')
#  P6: Order Tracking             – bottom-center
draw_process(ax, 10.0, 4.5, "Order\nTracking", "P6", r=0.75, color='#3A6BC8')
#  P7: Reward Points Mgmt         – bottom-left
draw_process(ax, 4.0, 4.5, "Reward\nPoints Mgmt", "P7", r=0.75, color='#3A6BC8')

# ─────────────────────────────────────────
# Data Stores
# ─────────────────────────────────────────
draw_datastore(ax, 5.8, 12.4, 3.2, 0.55, "Salad Catalog", "D1")
draw_datastore(ax, 6.2, 9.8, 3.2, 0.55, "User Database", "D2")
draw_datastore(ax, 6.2, 8.85, 3.0, 0.55, "Shopping Cart", "D3")
draw_datastore(ax, 12.0, 6.6, 2.8, 0.55, "Order Database", "D4")
draw_datastore(ax, 12.0, 5.5, 3.2, 0.55, "Address Database", "D5")
draw_datastore(ax, 1.5, 3.0, 3.2, 0.55, "Reward Points DB", "D6")

# ─────────────────────────────────────────
# Data Flows
# ─────────────────────────────────────────
# Customer → P1 (registration data)
arrow(ax, 2.42, 11.25, 3.25, 11.2, "Registration Data")
# P1 → D2 (store user record)
arrow(ax, 4.75, 10.9, 6.2, 10.1, "User Record")
# D2 → P1 (retrieve user)
arrow(ax, 6.2, 9.95, 4.75, 10.75, "User Credentials")

# Customer → P2 (browse request)
arrow(ax, 2.42, 7.65, 3.25, 7.8, "Browse Request")
# D1 → P2 (salad info)
arrow(ax, 8.0, 12.4, 8.0, 11.95, "Salad Details")
# P2 → P3 (add to cart)
arrow(ax, 5.75, 11.2, 4.8, 8.55, "Selected Item")

# P3 ↔ D3
arrow(ax, 4.75, 8.1, 6.2, 9.05, "Cart Items")
arrow(ax, 6.2, 8.95, 4.75, 8.2, "Cart Contents")

# P3 → P4 (initiate checkout)
arrow(ax, 4.75, 7.8, 9.25, 7.8, "Cart Summary")

# P4 ↔ D4
arrow(ax, 10.75, 7.5, 12.0, 6.9, "Order Record")
arrow(ax, 12.0, 6.75, 10.75, 7.6, "Order Confirmed")

# P4 ↔ D5
arrow(ax, 10.75, 7.4, 12.0, 5.85, "Delivery Address")

# P4 → P5
arrow(ax, 10.75, 7.8, 14.75, 8.5, "Payment Request")
# P5 → Payment Gateway
arrow(ax, 16.25, 8.9, 17.6, 8.9, "Auth Request")
arrow(ax, 17.6, 8.7, 16.25, 8.7, "Auth Response")

# P5 → P4 (payment result)
arrow(ax, 14.75, 8.2, 10.75, 7.9, "Payment Status")

# P4 → Email Service (confirmation)
arrow(ax, 10.75, 7.65, 17.6, 5.9, "Order Confirmation")

# P4 → P7 (earn points)
arrow(ax, 4.75, 7.5, 4.0, 5.25, "Purchase Info")
# P7 ↔ D6
arrow(ax, 4.0, 3.75, 3.0, 3.28, "Points Update")
arrow(ax, 3.0, 3.1, 3.25, 4.2, "Points Balance")

# P4 → P6 (order dispatched)
arrow(ax, 10.0, 7.05, 10.0, 5.25, "Order Details")
# P6 → Customer
arrow(ax, 9.25, 4.5, 2.42, 7.7, "Status Update")
# P6 ↔ Delivery Service
arrow(ax, 10.75, 4.5, 17.6, 2.9, "Delivery Assignment")
arrow(ax, 17.6, 2.7, 10.75, 4.3, "Delivery Status")
# P6 → Email Service
arrow(ax, 10.5, 5.25, 17.6, 5.85, "Status Notification")

# ─────────────────────────────────────────
# Legend
# ─────────────────────────────────────────
lx, ly = 0.2, 0.1
ax.add_patch(plt.Circle((lx+0.25, ly+0.3), 0.2, color='#3A6BC8'))
ax.text(lx+0.55, ly+0.3, "Process", va='center', fontsize=7.5)
rect_l = FancyBboxPatch((lx+1.3, ly+0.1), 0.55, 0.38, boxstyle="square,pad=0.02",
                         linewidth=1.5, edgecolor='#155724', facecolor='#D4EDDA')
ax.add_patch(rect_l)
ax.text(lx+1.57, ly+0.29, "Entity", va='center', ha='center', fontsize=7.5)
ax.plot([lx+2.4, lx+2.4], [ly+0.1, ly+0.48], color='#2C7BB6', lw=2)
ax.plot([lx+2.4, lx+3.3], [ly+0.48, ly+0.48], color='#2C7BB6', lw=2)
ax.plot([lx+2.4, lx+3.3], [ly+0.1, ly+0.1], color='#2C7BB6', lw=2)
ax.text(lx+2.85, ly+0.29, "Data Store", va='center', ha='center', fontsize=7.5)
ax.annotate('', xy=(lx+4.6, ly+0.3), xytext=(lx+4.0, ly+0.3),
            arrowprops=dict(arrowstyle='->', color='#555', lw=1.2))
ax.text(lx+4.75, ly+0.3, "Data Flow", va='center', fontsize=7.5)

plt.tight_layout(pad=0.5)
plt.savefig('/workspace/dfd_level1.png', dpi=150, bbox_inches='tight',
            facecolor='#F8F9FA')
print("DFD saved.")
