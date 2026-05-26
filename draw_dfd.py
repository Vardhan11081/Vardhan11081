import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe

fig, ax = plt.subplots(figsize=(22, 17))
ax.set_xlim(0, 22)
ax.set_ylim(0, 17)
ax.axis('off')
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# ─── helpers ────────────────────────────────────────────────────────────────

def ext_entity(ax, cx, cy, w, h, text):
    """Double-border rectangle for external entities."""
    for off, lw in [(0, 2.0), (0.18, 1.0)]:
        r = FancyBboxPatch((cx - w/2 + off, cy - h/2 + off),
                           w - 2*off, h - 2*off,
                           boxstyle="square,pad=0",
                           linewidth=lw, edgecolor='#1a252f',
                           facecolor='#d5e8d4', zorder=3)
        ax.add_patch(r)
    ax.text(cx, cy, text, ha='center', va='center',
            fontsize=9, fontweight='bold', zorder=4, wrap=True,
            multialignment='center')


def process(ax, cx, cy, r, pid, text):
    """Circle process bubble."""
    c = plt.Circle((cx, cy), r, color='#dae8fc', linewidth=1.8,
                   edgecolor='#0e4d92', zorder=3)
    ax.add_patch(c)
    # horizontal divider for PID
    ax.plot([cx - r, cx + r], [cy + r*0.35, cy + r*0.35],
            color='#0e4d92', linewidth=1.2, zorder=4)
    ax.text(cx, cy + r*0.65, pid, ha='center', va='center',
            fontsize=8, fontweight='bold', color='#0e4d92', zorder=5)
    ax.text(cx, cy - r*0.2, text, ha='center', va='center',
            fontsize=7.5, fontweight='bold', zorder=5,
            multialignment='center')


def datastore(ax, x1, y, w, h, dsid, text):
    """Open-ended data store."""
    x2 = x1 + w
    mid = x1 + 0.55
    # fill
    bg = mpatches.Rectangle((x1, y), w, h, facecolor='#fff2cc',
                             edgecolor='none', zorder=2)
    ax.add_patch(bg)
    ax.plot([x1, x2], [y + h, y + h], color='#1a252f', lw=1.8, zorder=4)
    ax.plot([x1, x2], [y,     y    ], color='#1a252f', lw=1.8, zorder=4)
    ax.plot([x1, x1], [y,     y + h], color='#1a252f', lw=1.8, zorder=4)
    ax.text(x1 + 0.28, y + h/2, dsid, ha='center', va='center',
            fontsize=7.5, fontweight='bold', zorder=5)
    ax.plot([mid, mid], [y, y + h], color='#1a252f', lw=1.2, zorder=4)
    ax.text(x1 + w/2 + 0.3, y + h/2, text, ha='center', va='center',
            fontsize=8, zorder=5)


def arrow(ax, x1, y1, x2, y2, label='', lc='#555555', fs=7):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=lc, lw=1.4))
    mx, my = (x1+x2)/2, (y1+y2)/2
    if label:
        ax.text(mx, my, label, ha='center', va='center', fontsize=fs,
                color='#333333', style='italic',
                bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.85))


def dblarrow(ax, x1, y1, x2, y2, label='', lc='#555555', fs=7):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='<->', color=lc, lw=1.4))
    mx, my = (x1+x2)/2, (y1+y2)/2
    if label:
        ax.text(mx, my, label, ha='center', va='center', fontsize=fs,
                color='#333333', style='italic',
                bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.85))


# ─── Title ───────────────────────────────────────────────────────────────────
ax.text(11, 16.5,
        "FreshBite Salads – Level 1 Data Flow Diagram",
        ha='center', va='center', fontsize=14, fontweight='bold',
        color='#1a252f')

# ─── External Entities ───────────────────────────────────────────────────────
#  Customer (top-left)
ext_entity(ax, 1.7, 13.5, 2.6, 1.2, "Customer\n(Guest /\nRegistered)")
#  Email Service (top-right)
ext_entity(ax, 20.2, 13.5, 2.6, 1.2, "Email\nService")
#  Payment Gateway (bottom-right)
ext_entity(ax, 20.2, 3.2, 2.6, 1.2, "Payment\nGateway")
#  Admin (bottom-left)
ext_entity(ax, 1.7, 3.2, 2.6, 1.2, "Admin /\nOwner")

# ─── Processes (2 rows of 3 + 1) ─────────────────────────────────────────────
PR = 1.05   # process radius

# Row 1
process(ax,  5.5, 13.5, PR, "P1", "Register &\nAuthenticate")
process(ax, 11.0, 13.5, PR, "P2", "Browse &\nManage Menu")
process(ax, 17.0, 13.5, PR, "P3", "Manage\nShopping Cart")

# Row 2
process(ax,  5.5,  9.5, PR, "P4", "Checkout &\nCalc. Total")
process(ax, 11.0,  9.5, PR, "P5", "Process\nPayment")
process(ax, 17.0,  9.5, PR, "P6", "Manage\nOrders")

# Row 3 (centre)
process(ax, 11.0,  5.8, PR, "P7", "Manage\nRewards")

# ─── Data Stores ─────────────────────────────────────────────────────────────
DS_W = 4.5
DS_H = 0.55

datastore(ax,  3.6, 7.30, DS_W, DS_H, "DS1", "User Account Store")
datastore(ax,  3.6, 6.45, DS_W, DS_H, "DS2", "Salad / Menu Store")
datastore(ax,  9.0, 7.30, DS_W, DS_H, "DS3", "Shopping Cart Store")
datastore(ax,  9.0, 6.45, DS_W, DS_H, "DS4", "Order Store")
datastore(ax, 14.4, 7.30, DS_W, DS_H, "DS5", "Payment Store")
datastore(ax, 14.4, 6.45, DS_W, DS_H, "DS6", "Reward Points Store")
datastore(ax,  9.0, 5.60, DS_W, DS_H, "DS7", "Address Store")

# ─── Arrows: Customer → Processes ────────────────────────────────────────────
arrow(ax, 3.0, 13.5, 4.45, 13.5, "Registration\nDetails")
arrow(ax, 3.0, 13.2, 9.95, 13.1, "Browse\nRequest")
arrow(ax, 3.0, 13.8, 15.95, 13.8, "Add/Remove\nItems")

# Process P1 → Customer (verification code)
arrow(ax, 5.5, 12.45, 3.0, 12.5, "Verification\nCode")
# Email Service ← P1
arrow(ax, 6.3, 13.9, 18.9, 13.9, "Send Verif.\nEmail")
# Email Service ← P6
arrow(ax, 17.9, 13.1, 18.9, 13.1, "Order Conf.\nEmail")

# Customer → P4 (checkout request)
arrow(ax, 2.5, 12.9, 4.45, 10.0, "Checkout\nRequest")
# Customer → P4 (delivery address)
arrow(ax, 2.9, 12.7, 4.3, 9.9, "Delivery\nAddress")

# P4 → P5
arrow(ax, 6.55, 9.5, 9.95, 9.5, "Payment\nDetails")
# P5 → Payment Gateway
arrow(ax, 17.9, 9.5, 18.9, 9.5, "Payment\nRequest")
arrow(ax, 18.9, 9.2, 17.9, 9.2, "Payment\nConfirmation")

# P5 → P6
arrow(ax, 12.05, 9.5, 15.95, 9.5, "Confirmed\nPayment Info")

# P6 → Customer (order status)
arrow(ax, 16.5, 8.45, 3.0, 4.2, "Order Status\nUpdate")

# Admin → P2 (menu management)
arrow(ax, 2.5, 3.7, 10.2, 8.45, "Menu\nUpdates")

# ─── Arrows: Processes ↔ Data Stores ────────────────────────────────────────
# P1 ↔ DS1
arrow(ax, 5.5, 12.45, 5.5, 7.85,  "Store / Retrieve\nUser Data")

# P2 ↔ DS2
arrow(ax, 10.2, 12.45, 5.0, 6.98, "Read Menu /\nSalad Data")
arrow(ax, 4.5, 6.45,  10.0, 9.0,  "Menu Updates")

# P3 ↔ DS3
dblarrow(ax, 15.95, 12.45, 11.0, 7.85, "Read/Write\nCart Data")

# P4 ↔ DS3
arrow(ax, 9.0, 7.58, 5.6, 9.0, "Load Cart\nData")
# P4 ↔ DS7
arrow(ax, 5.5, 8.45, 9.7, 5.88, "Save /\nRetrieve Address")

# P5 ↔ DS5
dblarrow(ax, 16.5, 8.45, 16.65, 7.85, "Store Payment\nRecord")

# P6 ↔ DS4
dblarrow(ax, 15.95, 8.45, 11.5, 7.85, "Create / Update\nOrder Record")

# P7 ↔ DS6
dblarrow(ax, 11.0, 4.75, 16.65, 6.45, "Read/Write\nPoints")

# P5 → P7 (trigger reward)
arrow(ax, 11.0, 8.45, 11.0, 6.85, "Trigger Points\nEarning")

# ─── Legend ──────────────────────────────────────────────────────────────────
lx, ly = 0.3, 0.8
ax.text(lx, ly + 0.9, "Legend:", fontsize=9, fontweight='bold')
ext_entity(ax, lx + 1.1, ly + 0.4, 1.6, 0.5, "External\nEntity")
c = plt.Circle((lx + 3.2, ly + 0.4), 0.28, color='#dae8fc',
               linewidth=1.5, edgecolor='#0e4d92', zorder=3)
ax.add_patch(c)
ax.text(lx + 3.2, ly + 0.4, "P#", ha='center', va='center', fontsize=8,
        fontweight='bold', color='#0e4d92')
ax.text(lx + 3.2, ly - 0.05, "Process", ha='center', fontsize=8)
datastore(ax, lx + 4.3, ly + 0.15, 2.8, 0.5, "DS#", "Data Store")
ax.annotate('', xy=(lx + 8.3, ly + 0.4), xytext=(lx + 7.5, ly + 0.4),
            arrowprops=dict(arrowstyle='->', color='#555555', lw=1.4))
ax.text(lx + 8.0, ly - 0.05, "Data Flow", ha='center', fontsize=8)

plt.tight_layout()
plt.savefig('/workspace/output/dfd_level1.png', dpi=180, bbox_inches='tight',
            facecolor='white')
plt.close()
print("DFD saved.")
