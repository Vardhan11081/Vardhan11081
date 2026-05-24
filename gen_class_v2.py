"""
Clean UML Class Diagram – FreshBite Salads
Grid layout:
  Row 1 (top):    [Verification] [User] [RewardPoints]
  Row 2 (middle): [ShoppingCart] [CartItem] [Salad] [CustomSalad]
  Row 3 (bottom): [Address]      [Order]    [Payment]
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe

W, H = 26, 20
fig, ax = plt.subplots(figsize=(W, H))
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis('off')
fig.patch.set_facecolor('#FFFFFF')

ax.text(W/2, H-0.32,
        'FreshBite Salads – UML Class Diagram',
        ha='center', va='center', fontsize=14, fontweight='bold', color='#0D2B55')

# ── colour constants ──────────────────────────────────────────
HDR  = '#1B4F8A'   # header fill
ATTR = '#EBF5FB'   # attribute section fill
MTH  = '#F0FFF4'   # method section fill
BDR  = '#0D2B55'   # border
MCLR = '#145214'   # method text colour
ACLR = '#1a1a2a'   # attr text colour

LINE_H = 0.265

# ──────────────────────────────────────────────────────────────
def cls(ax, x, y, name, attrs, methods, w=4.4, stereotype=None):
    """
    Draw UML class box anchored at bottom-left (x,y).
    Returns centre_x, centre_y, width, total_height.
    """
    hdr_h  = 0.52
    attr_h = max(len(attrs),  1) * LINE_H + 0.14
    mth_h  = max(len(methods),1) * LINE_H + 0.14
    tot    = hdr_h + attr_h + mth_h

    # method section (bottom)
    ax.add_patch(FancyBboxPatch((x,y), w, mth_h,
        boxstyle='square,pad=0', lw=1.4, ec=BDR, fc=MTH, zorder=3))
    # attribute section
    ax.add_patch(FancyBboxPatch((x, y+mth_h), w, attr_h,
        boxstyle='square,pad=0', lw=1.4, ec=BDR, fc=ATTR, zorder=3))
    # header
    ax.add_patch(FancyBboxPatch((x, y+mth_h+attr_h), w, hdr_h,
        boxstyle='square,pad=0', lw=1.4, ec=BDR, fc=HDR, zorder=3))

    # stereotype + name
    st = f'«{stereotype}»\n' if stereotype else ''
    ax.text(x+w/2, y+mth_h+attr_h+hdr_h/2, st+name,
            ha='center', va='center', fontsize=8.8, fontweight='bold',
            color='white', zorder=5, linespacing=1.3)

    # attributes
    for i, a in enumerate(attrs):
        ax.text(x+0.12, y+mth_h+attr_h - 0.1 - i*LINE_H,
                a, ha='left', va='top', fontsize=6.7,
                color=ACLR, fontfamily='monospace', zorder=5)

    # methods
    for i, m in enumerate(methods):
        ax.text(x+0.12, y+mth_h - 0.1 - i*LINE_H,
                m, ha='left', va='top', fontsize=6.7,
                color=MCLR, fontfamily='monospace', zorder=5)

    cx = x + w/2
    cy = y + tot/2
    return cx, cy, w, tot

# ──────────────────────────────────────────────────────────────
def arrow(ax, x1,y1, x2,y2, style='->', label='', m1='', m2='',
          color='#333', lw=1.15, rad=0.0, dashed=False,
          lpad=(0,0.12)):
    ls = (0,(5,3)) if dashed else 'solid'
    ax.annotate('', xy=(x2,y2), xytext=(x1,y1),
        arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                        linestyle=ls,
                        connectionstyle=f'arc3,rad={rad}'), zorder=2)
    if label:
        mx = (x1+x2)/2 + lpad[0]
        my = (y1+y2)/2 + lpad[1]
        ax.text(mx, my, label, ha='center', va='bottom',
                fontsize=6.6, color='#444', style='italic', zorder=7,
                bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.9))
    if m1:
        ax.text(x1+(x2-x1)*0.13, y1+(y2-y1)*0.13, m1,
                ha='center', fontsize=7.2, color='#880E4F', fontweight='bold', zorder=8)
    if m2:
        ax.text(x1+(x2-x1)*0.87, y1+(y2-y1)*0.87, m2,
                ha='center', fontsize=7.2, color='#880E4F', fontweight='bold', zorder=8)

# ══════════════════════════════════════════════════════════════
#  PLACE CLASSES
# ══════════════════════════════════════════════════════════════

# ── Row 1: Verification | User | RewardPoints ─────────────────
vx, vy = 0.3, 13.8
cx_v, cy_v, _, h_v = cls(ax, vx, vy, 'Verification',
    ['-verificationId: int',
     '-verificationCode: String',
     '-isVerified: boolean',
     '-expiryDate: Date'],
    ['+generateCode(): String',
     '+sendVerificationEmail(): void',
     '+verifyCode(code): boolean'], w=4.3)

ux, uy = 5.5, 13.0
cx_u, cy_u, _, h_u = cls(ax, ux, uy, 'User',
    ['-userId: int',
     '-username: String',
     '-firstName: String',
     '-lastName: String',
     '-dateOfBirth: Date',
     '-email: String',
     '-password: String',
     '-accountStatus: String',
     '-failedLoginAttempts: int',
     '-lastActivityDate: Date'],
    ['+register(): void',
     '+login(): boolean',
     '+logout(): void',
     '+verifyEmail(code): boolean',
     '+reactivateAccount(): void',
     '+updateProfile(): void'], w=4.5)

rx, ry = 11.0, 14.2
cx_r, cy_r, _, h_r = cls(ax, rx, ry, 'RewardPoints',
    ['-rewardId: int',
     '-totalPoints: int',
     '-isEligibleForFree: boolean'],
    ['+addPoints(pts: int): void',
     '+redeemPoints(): void',
     '+checkEligibility(): boolean'], w=4.3)

# ── Row 2: ShoppingCart | CartItem | Salad | CustomSalad ──────
scx, scy = 0.3, 7.8
cx_sc, cy_sc, _, h_sc = cls(ax, scx, scy, 'ShoppingCart',
    ['-cartId: int',
     '-sessionId: String',
     '-createdDate: Date'],
    ['+addItem(item): void',
     '+removeItem(itemId): void',
     '+updateQuantity(id,qty): void',
     '+getTotal(): double',
     '+clearCart(): void'], w=4.3)

cix, ciy = 5.5, 8.5
cx_ci, cy_ci, _, h_ci = cls(ax, cix, ciy, 'CartItem',
    ['-cartItemId: int',
     '-quantity: int',
     '-portionSize: String',
     '-subtotal: double'],
    ['+calculateSubtotal(): double',
     '+updateQuantity(qty): void'], w=4.3)

slx, sly = 10.7, 8.2
cx_sl, cy_sl, _, h_sl = cls(ax, slx, sly, 'Salad',
    ['-saladId: int',
     '-name: String',
     '-ingredients: String',
     '-description: String',
     '-allergenWarnings: String',
     '-nutritionalInfo: String',
     '-price: double',
     '-portionSize: String'],
    ['+getDetails(): String',
     '+updatePrice(p): void',
     '+getPrice(): double'], w=4.5)

csx, csy = 16.3, 10.5
cx_cs, cy_cs, _, h_cs = cls(ax, csx, csy, 'CustomSalad',
    ['-customIngredients: List<String>'],
    ['+addIngredient(i): void',
     '+removeIngredient(i): void',
     '+calculatePrice(): double'],
    w=4.4, stereotype='extends Salad')

# ── Row 3: Address | Order | Payment ─────────────────────────
ax2, ay2 = 0.3, 2.5
cx_a, cy_a, _, h_a = cls(ax, ax2, ay2, 'Address',
    ['-addressId: int',
     '-street: String',
     '-city: String',
     '-state: String',
     '-postcode: String',
     '-country: String',
     '-addressType: String'],
    ['+addAddress(): void',
     '+editAddress(): void',
     '+deleteAddress(): void'], w=4.3)

ox, oy = 5.5, 2.5
cx_o, cy_o, _, h_o = cls(ax, ox, oy, 'Order',
    ['-orderId: int',
     '-orderDate: Date',
     '-totalCost: double',
     '-tax: double',
     '-deliveryCharge: double',
     '-orderStatus: String'],
    ['+createOrder(): void',
     '+updateStatus(s): void',
     '+calculateTotal(): double',
     '+getOrderDetails(): String'], w=4.3)

px, py = 10.7, 3.2
cx_p, cy_p, _, h_p = cls(ax, px, py, 'Payment',
    ['-paymentId: int',
     '-amount: double',
     '-paymentMethod: String',
     '-paymentStatus: String',
     '-transactionDate: Date'],
    ['+processPayment(): boolean',
     '+verifyPayment(): boolean',
     '+getReceipt(): String'], w=4.3)

# ══════════════════════════════════════════════════════════════
#  ASSOCIATIONS
# ══════════════════════════════════════════════════════════════

# User (left edge) ──"requires"─→ Verification (right edge)
arrow(ax, ux, cy_u, vx+4.3, cy_u+0.3,
      label='requires', m1='1', m2='1', color='#333')

# User (right edge) ──"earns"─→ RewardPoints (left edge)
arrow(ax, ux+4.5, cy_u+0.5, rx, cy_r,
      label='earns', m1='1', m2='1', color='#333')

# User (bottom) ──"has"─→ ShoppingCart (top)
arrow(ax, cx_u-0.6, uy, cx_sc+0.5, scy+h_sc,
      label='has', m1='1', m2='0..*', color='#333')

# User (bottom) ──"places"─→ Order (top)
arrow(ax, cx_u, uy, cx_o+0.3, oy+h_o,
      label='places', m1='1', m2='0..*', color='#333', rad=-0.15)

# User (bottom-left) ──"has"─→ Address (top)
arrow(ax, ux+0.5, uy, cx_a+0.4, ay2+h_a,
      label='has', m1='1', m2='0..*', color='#333', rad=0.15)

# ShoppingCart (right) ──"contains"─→ CartItem (left)
arrow(ax, scx+4.3, cy_sc, cix, cy_ci,
      label='contains', m1='1', m2='0..*', color='#1a5276')

# CartItem (right) ──"references"─→ Salad (left)
arrow(ax, cix+4.3, cy_ci, slx, cy_sl+0.4,
      label='references', m1='0..*', m2='1', color='#1a5276')

# CustomSalad ─────|> Salad  (inheritance – hollow triangle)
arrow(ax, csx, cy_cs, slx+4.5, cy_sl+1.0,
      style='-|>', color='#0D2B55', lw=1.8, label='', m1='', m2='')

# Order (right) ──"includes"─→ CartItem (bottom)
arrow(ax, ox+4.3, cy_o+0.5, cix+2.0, ciy,
      label='includes', m1='1', m2='1..*', color='#1a5276', rad=-0.2)

# Order (right) ──"paid by"─→ Payment (left)
arrow(ax, ox+4.3, cy_o, px, cy_p,
      label='paid by', m1='1', m2='1', color='#333')

# Order (left) ──"delivered to"─→ Address (right)
arrow(ax, ox, cy_o, ax2+4.3, cy_a+0.5,
      label='delivered to', m1='1', m2='1', color='#333')

# ══════════════════════════════════════════════════════════════
#  LEGEND
# ══════════════════════════════════════════════════════════════
lx, ly = 16.2, 1.0
ax.text(lx, ly+1.55, 'Legend', fontsize=8.5, fontweight='bold', color='#0D2B55')

# Association
ax.annotate('', xy=(lx+1.4, ly+1.1), xytext=(lx+0.2, ly+1.1),
            arrowprops=dict(arrowstyle='->', color='#333', lw=1.2))
ax.text(lx+1.55, ly+1.1, 'Association', va='center', fontsize=7.5)

# Inheritance
ax.annotate('', xy=(lx+1.4, ly+0.65), xytext=(lx+0.2, ly+0.65),
            arrowprops=dict(arrowstyle='-|>', color='#0D2B55', lw=1.8))
ax.text(lx+1.55, ly+0.65, 'Inheritance (generalization)', va='center', fontsize=7.5)

# Multiplicity
ax.text(lx, ly+0.25,
        '1, 0..*, 1..* — multiplicity near arrowheads (pink)',
        fontsize=7.5, color='#880E4F')

# Visibility key
ax.text(lx, ly-0.15, '+ public   - private   # protected',
        fontsize=7.5, fontfamily='monospace', color='#333')

plt.tight_layout(pad=0.3)
plt.savefig('/workspace/class_v2.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Class diagram v2 saved.")
