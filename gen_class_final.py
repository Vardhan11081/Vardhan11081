"""
UML Class Diagram – FreshBite Salads
Style matching uploaded document:
  • White background
  • Pale-yellow class boxes, thin black border
  • 3-compartment UML layout
  • Solid black orthogonal association lines with multiplicity
  • Hollow-triangle inheritance arrow
  • User: far left | Salad & CustomSalad: top-center/right
  • ShoppingCart: center | CartItem: center-right
  • Order/Payment/Address: bottom row
  • Verification/RewardPoints: far right
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.lines as mlines

W, H = 30, 20
fig, ax = plt.subplots(figsize=(W, H))
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis('off')
fig.patch.set_facecolor('white')

ax.text(W/2, H-0.35,
        'UML Class Diagram – FreshBite Salads Online Ordering System',
        ha='center', fontsize=13.5, fontweight='bold', color='#0D2B55', zorder=8)

# ── palette ──────────────────────────────────────────────────
CLS_FILL  = '#FFFDE7'   # pale yellow
CLS_BDR   = '#333333'   # near-black border
HDR_FILL  = '#FFF9C4'   # slightly deeper yellow header
TXT_CLR   = '#111111'
SEC_LINE  = '#555555'   # divider lines between compartments
LINE_H    = 0.255       # height per attribute/method line
PAD       = 0.12

# ──────────────────────────────────────────────────────────────
def cls_box(ax, x, y, name, attrs, methods, w=4.2):
    """Bottom-left corner at (x,y). Returns cx, cy, w, h."""
    hdr_h  = 0.48
    attr_h = len(attrs)  * LINE_H + PAD*2
    mth_h  = len(methods)* LINE_H + PAD*2
    tot    = hdr_h + attr_h + mth_h

    # header
    ax.add_patch(FancyBboxPatch((x, y+mth_h+attr_h), w, hdr_h,
        boxstyle='square,pad=0', lw=1.3, ec=CLS_BDR, fc=HDR_FILL, zorder=4))
    # attr section
    ax.add_patch(FancyBboxPatch((x, y+mth_h), w, attr_h,
        boxstyle='square,pad=0', lw=1.3, ec=CLS_BDR, fc=CLS_FILL, zorder=4))
    # method section
    ax.add_patch(FancyBboxPatch((x, y), w, mth_h,
        boxstyle='square,pad=0', lw=1.3, ec=CLS_BDR, fc=CLS_FILL, zorder=4))

    # class name
    ax.text(x+w/2, y+mth_h+attr_h+hdr_h/2, name,
            ha='center', va='center', fontsize=9, fontweight='bold',
            color='#0D2B55', zorder=6)

    # attributes
    for i, a in enumerate(attrs):
        ax.text(x+0.1, y+mth_h+attr_h - PAD - i*LINE_H,
                a, ha='left', va='top', fontsize=6.8,
                color=TXT_CLR, fontfamily='monospace', zorder=6)

    # methods
    for i, m in enumerate(methods):
        ax.text(x+0.1, y+mth_h - PAD - i*LINE_H,
                m, ha='left', va='top', fontsize=6.8,
                color='#145214', fontfamily='monospace', zorder=6)

    return x+w/2, y+tot/2, w, tot

# ──────────────────────────────────────────────────────────────
def assoc(ax, x1,y1, x2,y2, label='', m1='', m2='',
          pts=None, lpad=(0, 0.13), dashed=False, inherit=False):
    """
    Draw association line with optional waypoints (pts list of (x,y)).
    If inherit=True draws hollow-triangle arrowhead.
    """
    color = '#000000'
    lw    = 1.2
    ls    = '--' if dashed else '-'

    if pts is None:
        pts = [(x1,y1),(x2,y2)]
    else:
        pts = [(x1,y1)] + list(pts) + [(x2,y2)]

    # draw all segments except last as plain lines
    for i in range(len(pts)-2):
        ax.plot([pts[i][0], pts[i+1][0]],
                [pts[i][1], pts[i+1][1]],
                color=color, lw=lw, linestyle=ls, zorder=3)

    # last segment
    if inherit:
        ax.annotate('', xy=pts[-1], xytext=pts[-2],
            arrowprops=dict(arrowstyle='-|>', color='#000', lw=1.5,
                            mutation_scale=14), zorder=3)
    else:
        ax.annotate('', xy=pts[-1], xytext=pts[-2],
            arrowprops=dict(arrowstyle='->', color=color, lw=lw), zorder=3)

    # label at mid-segment
    if label:
        mid_i = len(pts)//2
        mx = (pts[mid_i-1][0]+pts[mid_i][0])/2 + lpad[0]
        my = (pts[mid_i-1][1]+pts[mid_i][1])/2 + lpad[1]
        ax.text(mx, my, label, ha='center', va='bottom',
                fontsize=7.2, color='#333', style='italic', zorder=7,
                bbox=dict(boxstyle='round,pad=0.12', fc='white', ec='none', alpha=0.9))

    def mult_label(ax, px, py, txt, dx, dy):
        ax.text(px+dx, py+dy, txt, ha='center', va='center',
                fontsize=7.5, color='#8B0000', fontweight='bold', zorder=8)

    if m1: mult_label(ax, pts[0][0],  pts[0][1],  m1,  0.25,  0.2)
    if m2: mult_label(ax, pts[-1][0], pts[-1][1], m2, -0.25, -0.2)

# ══════════════════════════════════════════════════════════════
#  PLACE CLASSES
# ══════════════════════════════════════════════════════════════

# ── User  (far left, tall) ───────────────────────────────────
ux, uy = 0.3, 7.5
cx_u, cy_u, w_u, h_u = cls_box(ax, ux, uy, 'User',
    ['- userId: int',
     '- username: String',
     '- firstName: String',
     '- lastName: String',
     '- dateOfBirth: Date',
     '- email: String',
     '- password: String',
     '- accountStatus: String',
     '- failedLoginAttempts: int',
     '- lastActivityDate: Date'],
    ['+ register(): void',
     '+ login(): boolean',
     '+ logout(): void',
     '+ verifyEmail(code: String): boolean',
     '+ reactivateAccount(): void',
     '+ updateProfile(): void'], w=4.2)

# ── Salad  (top center) ─────────────────────────────────────
slx, sly = 7.2, 13.8
cx_sl, cy_sl, w_sl, h_sl = cls_box(ax, slx, sly, 'Salad',
    ['- saladId: int',
     '- name: String',
     '- ingredients: String',
     '- description: String',
     '- allergenWarnings: String',
     '- nutritionalInfo: String',
     '- price: double',
     '- portionSize: String'],
    ['+ getDetails(): String',
     '+ updatePrice(p: double): void',
     '+ getPrice(): double'], w=4.4)

# ── CustomSalad  (top right, below Salad) ───────────────────
csx, csy = 12.5, 14.5
cx_cs, cy_cs, w_cs, h_cs = cls_box(ax, csx, csy, 'CustomSalad',
    ['- customIngredients: List<String>'],
    ['+ addIngredient(i: String): void',
     '+ removeIngredient(i: String): void',
     '+ calculatePrice(): double'], w=4.4)

# ── ShoppingCart  (center) ──────────────────────────────────
scx, scy_cart = 7.2, 9.8
cx_sc, cy_sc, w_sc, h_sc = cls_box(ax, scx, scy_cart, 'ShoppingCart',
    ['- cartId: int',
     '- sessionId: String',
     '- createdDate: Date'],
    ['+ addItem(item: CartItem): void',
     '+ removeItem(itemId: int): void',
     '+ updateQuantity(id, qty: int): void',
     '+ getTotal(): double',
     '+ clearCart(): void'], w=4.4)

# ── CartItem  (center-right) ────────────────────────────────
cix, ciy = 12.5, 11.2
cx_ci, cy_ci, w_ci, h_ci = cls_box(ax, cix, ciy, 'CartItem',
    ['- cartItemId: int',
     '- quantity: int',
     '- portionSize: String',
     '- subtotal: double'],
    ['+ calculateSubtotal(): double',
     '+ updateQuantity(qty: int): void'], w=4.4)

# ── Order  (bottom left, below User) ────────────────────────
ox, oy = 0.3, 2.0
cx_o, cy_o, w_o, h_o = cls_box(ax, ox, oy, 'Order',
    ['- orderId: int',
     '- orderDate: Date',
     '- totalCost: double',
     '- tax: double',
     '- deliveryCharge: double',
     '- orderStatus: String'],
    ['+ createOrder(): void',
     '+ updateStatus(status: String): void',
     '+ calculateTotal(): double',
     '+ getOrderDetails(): String'], w=4.2)

# ── Payment  (bottom center) ────────────────────────────────
px, py_pay = 5.5, 2.0
cx_p, cy_p, w_p, h_p = cls_box(ax, px, py_pay, 'Payment',
    ['- paymentId: int',
     '- amount: double',
     '- paymentMethod: String',
     '- paymentStatus: String',
     '- transactionDate: Date'],
    ['+ processPayment(): boolean',
     '+ verifyPayment(): boolean',
     '+ getReceipt(): String'], w=4.4)

# ── Address  (bottom center-right) ──────────────────────────
adx, ady = 10.8, 2.0
cx_a, cy_a, w_a, h_a = cls_box(ax, adx, ady, 'Address',
    ['- addressId: int',
     '- street: String',
     '- city: String',
     '- state: String',
     '- postcode: String',
     '- country: String',
     '- addressType: String'],
    ['+ addAddress(): void',
     '+ editAddress(): void',
     '+ deleteAddress(): void'], w=4.4)

# ── Verification  (far right, middle) ───────────────────────
vx, vy = 21.0, 12.5
cx_v, cy_v, w_v, h_v = cls_box(ax, vx, vy, 'Verification',
    ['- verificationId: int',
     '- verificationCode: String',
     '- isVerified: boolean',
     '- expiryDate: Date'],
    ['+ generateCode(): String',
     '+ sendVerificationEmail(): void',
     '+ verifyCode(code: String): boolean'], w=4.6)

# ── RewardPoints  (far right, below Verification) ───────────
rpx, rpy = 21.0, 7.8
cx_rp, cy_rp, w_rp, h_rp = cls_box(ax, rpx, rpy, 'RewardPoints',
    ['- rewardId: int',
     '- totalPoints: int',
     '- isEligibleForFree: boolean'],
    ['+ addPoints(points: int): void',
     '+ redeemPoints(): void',
     '+ checkEligibility(): boolean'], w=4.6)

# ══════════════════════════════════════════════════════════════
#  ASSOCIATIONS
# ══════════════════════════════════════════════════════════════

# User → ShoppingCart  (1 → 0..*)  "has"
assoc(ax, cx_u, uy+h_u,   cx_sc, scy_cart,
      label='has', m1='1', m2='0..*',
      pts=[(cx_u, scy_cart+h_sc+0.3)])

# User → Order  (1 → 0..*)  "places"
assoc(ax, ux+w_u/2, uy, cx_o+w_o/2, oy+h_o,
      label='places', m1='1', m2='0..*')

# User → Address  (1 → 0..*)  "has"
assoc(ax, ux+w_u, cy_u, adx, cy_a,
      label='has', m1='1', m2='0..*',
      pts=[(adx-0.5, cy_u)])

# User → Verification  (1 → 1)  "requires"
assoc(ax, ux+w_u, uy+h_u*0.75, vx, cy_v,
      label='requires', m1='1', m2='1',
      pts=[(vx-0.5, uy+h_u*0.75)])

# User → RewardPoints  (1 → 1)  "earns"
assoc(ax, ux+w_u, uy+h_u*0.45, rpx, cy_rp,
      label='earns', m1='1', m2='1',
      pts=[(rpx-0.5, uy+h_u*0.45)])

# ShoppingCart → CartItem  (1 → 0..*)  "contains"
assoc(ax, scx+w_sc, cy_sc, cix, cy_ci,
      label='contains', m1='1', m2='0..*')

# CartItem → Salad  (0..* → 1)  "references"
assoc(ax, cx_ci, ciy+h_ci, cx_sl, sly,
      label='references', m1='0..*', m2='1',
      pts=[(cx_ci, sly-0.3)])

# CustomSalad --|> Salad  (inheritance)
assoc(ax, csx, cy_cs, slx+w_sl, cy_sl,
      inherit=True, label='')

# Order → CartItem  (1 → 1..*)  "includes"
assoc(ax, ox+w_o, cy_o+0.8, cix, ciy,
      label='includes', m1='1', m2='1..*',
      pts=[(cix-0.4, cy_o+0.8)])

# Order → Payment  (1 → 1)  "paid by"
assoc(ax, ox+w_o, cy_o, px, cy_p,
      label='paid by', m1='1', m2='1')

# Order → Address  (1 → 1)  "delivered to"
assoc(ax, ox+w_o/2+1.0, oy, adx+w_a/2-0.5, ady+h_a,
      label='delivered to', m1='1', m2='1',
      pts=[(adx+w_a/2-0.5, oy-0.4),(ox+w_o/2+1.0, oy-0.4)])

# ══════════════════════════════════════════════════════════════
#  LEGEND
# ══════════════════════════════════════════════════════════════
lx, ly2 = 16.5, 1.0
ax.text(lx, ly2+1.9, 'Legend:', fontsize=8.5, fontweight='bold', color='#0D2B55')

ax.annotate('', xy=(lx+1.5, ly2+1.45), xytext=(lx+0.3, ly2+1.45),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.2))
ax.text(lx+1.65, ly2+1.45, 'Association', va='center', fontsize=8)

ax.annotate('', xy=(lx+1.5, ly2+0.95), xytext=(lx+0.3, ly2+0.95),
            arrowprops=dict(arrowstyle='-|>', color='black', lw=1.5, mutation_scale=14))
ax.text(lx+1.65, ly2+0.95, 'Inheritance (generalization)', va='center', fontsize=8)

ax.text(lx, ly2+0.5,
        '1, 0..*, 1..*  — multiplicity (shown in dark red near arrowheads)',
        fontsize=8, color='#8B0000')
ax.text(lx, ly2+0.1,
        '+ public   - private   # protected   (UML visibility modifiers)',
        fontsize=8, fontfamily='monospace', color='#333')

plt.tight_layout(pad=0.4)
plt.savefig('/workspace/class_final.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Class diagram final saved.")
