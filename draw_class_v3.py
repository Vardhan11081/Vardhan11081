"""
FreshBite Salads – Class Diagram  (v3)
Clean orthogonal arrows with no crossing; edge-anchored routing for
long-distance relationships.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

W, H = 28, 22
fig, ax = plt.subplots(figsize=(W, H))
ax.set_xlim(0, W); ax.set_ylim(0, H)
ax.axis('off')
fig.patch.set_facecolor('white'); ax.set_facecolor('white')

HDR  = '#c8d8f0'
BOX  = 'white'
BORD = '#222'
TXT  = '#111'
ARR  = '#333'
ROW_H = 0.265
PAD   = 0.11
NH    = 0.44
CW    = 4.80

# ═══════════════════════════════════════════════════════════════════════════
# UML class box – returns (x0, bot_y, top_y, cx)
# ═══════════════════════════════════════════════════════════════════════════
def uml(ax, cx, top_y, name, attrs, methods):
    ah = len(attrs)  * ROW_H + 2*PAD
    mh = len(methods)* ROW_H + 2*PAD
    total = NH + ah + mh
    x0    = cx - CW/2
    bot   = top_y - total

    # shadow
    ax.add_patch(FancyBboxPatch((x0+0.07, bot-0.07), CW, total,
        boxstyle='square,pad=0', lw=0, fc='#bbb', zorder=2))
    # box
    ax.add_patch(FancyBboxPatch((x0, bot), CW, total,
        boxstyle='square,pad=0', lw=1.6, ec=BORD, fc=BOX, zorder=3))
    # header fill
    ax.add_patch(mpatches.Rectangle((x0, top_y-NH), CW, NH,
        fc=HDR, ec='none', zorder=4))
    div1 = top_y - NH
    div2 = div1 - ah
    ax.plot([x0, x0+CW], [div1, div1], color=BORD, lw=1.4, zorder=5)
    ax.plot([x0, x0+CW], [div2, div2], color=BORD, lw=1.4, zorder=5)

    ax.text(cx, top_y-NH/2, name,
        ha='center', va='center', fontsize=9.5, fontweight='bold',
        color='#0a2040', zorder=6)
    for i, a in enumerate(attrs):
        ax.text(x0+0.14, div1-PAD-(i+.5)*ROW_H, a,
            ha='left', va='center', fontsize=7.2,
            family='monospace', color=TXT, zorder=6)
    for i, m in enumerate(methods):
        ax.text(x0+0.14, div2-PAD-(i+.5)*ROW_H, m,
            ha='left', va='center', fontsize=7.2,
            family='monospace', color=TXT, zorder=6)
    return bot, top_y, cx   # (bot_y, top_y, cx)

# ═══════════════════════════════════════════════════════════════════════════
# Arrow helpers
# ═══════════════════════════════════════════════════════════════════════════
def lbl(ax, x, y, text):
    ax.text(x, y, text, ha='center', va='center', fontsize=7.8,
        style='italic', color='#222',
        bbox=dict(boxstyle='round,pad=0.14', fc='white', ec='none', alpha=0.92))

def mult(ax, x, y, text):
    ax.text(x, y, text, ha='center', va='center', fontsize=8.5,
        fontweight='bold', color='#111')

def parrow(ax, pts, label='', lseg=None, loff=(0, 0.22),
           m1=None, m1pt=None, m2=None, m2pt=None,
           style='->', lw=1.3, dash=False):
    ls = '--' if dash else '-'
    for i in range(len(pts)-2):
        ax.plot([pts[i][0], pts[i+1][0]], [pts[i][1], pts[i+1][1]],
            color=ARR, lw=lw, ls=ls,
            solid_capstyle='round', solid_joinstyle='round', zorder=5)
    ax.annotate('', xy=pts[-1], xytext=pts[-2],
        arrowprops=dict(arrowstyle=style, color=ARR, lw=lw,
                        linestyle=ls))
    if label:
        si = lseg if lseg is not None else max(0, len(pts)//2 - 1)
        mx = (pts[si][0]+pts[si+1][0])/2 + loff[0]
        my = (pts[si][1]+pts[si+1][1])/2 + loff[1]
        lbl(ax, mx, my, label)
    if m1 and m1pt: mult(ax, *m1pt, m1)
    if m2 and m2pt: mult(ax, *m2pt, m2)

# ═══════════════════════════════════════════════════════════════════════════
# TITLE
# ═══════════════════════════════════════════════════════════════════════════
ax.text(14, 21.75, '6.2  Class Diagram',
    ha='center', fontsize=14, fontweight='bold', color='#0a2040')

# ═══════════════════════════════════════════════════════════════════════════
# ROW 1  (top = 21.40)
# ═══════════════════════════════════════════════════════════════════════════
T1 = 21.30

user_cx  = 4.0
ub, ut, _ = uml(ax, user_cx, T1, "User",
    ["-  userId: int",
     "-  username: String",
     "-  firstName: String",
     "-  lastName: String",
     "-  dateOfBirth: Date",
     "-  email: String",
     "-  password: String",
     "-  tax: double",
     "-  accountStatus: String",
     "-  failedLoginAttempts: int",
     "-  lastActivityDate: Date"],
    ["+  register(): void",
     "+  login(): void",
     "+  logout(): void",
     "+  verifyEmail(code: String): boolean",
     "+  reactivateAccount(): void",
     "+  updateProfile(): void"])

sal_cx = 12.30
sb, st, _ = uml(ax, sal_cx, T1, "Salad",
    ["-  saladId: int",
     "-  name: String",
     "-  ingredients: String",
     "-  description: String",
     "-  allergenWarnings: String",
     "-  nutritionalInfo: String",
     "-  price: double",
     "-  portionSize: String"],
    ["+  getDetails(): void",
     "+  updatePrice(price: double): void",
     "+  getPrice(): double"])

cus_cx = 20.60
csb, cst, _ = uml(ax, cus_cx, T1, "CustomSalad",
    ["-  customIngredients: List<String>"],
    ["+  addIngredient(ingredient: String): void",
     "+  removeIngredient(ingredient: String): void",
     "+  calculatePrice(): double"])

# ═══════════════════════════════════════════════════════════════════════════
# ROW 2  (top = min(row1 bots) - 1.0)
# ═══════════════════════════════════════════════════════════════════════════
T2 = min(ub, sb, csb) - 0.90

cart_cx = 7.20
cb, ct, _ = uml(ax, cart_cx, T2, "ShoppingCart",
    ["-  cartId: int",
     "-  sessionId: String",
     "-  createdDate: Date"],
    ["+  addItem(item: CartItem): void",
     "+  removeItem(itemId): void",
     "+  updateQuantity(itemId, qty: int): void",
     "+  getTotal(): double",
     "+  clearCart(): void"])

ci_cx = 14.80
cib, cit, _ = uml(ax, ci_cx, T2, "CartItem",
    ["-  cartItemId: int",
     "-  quantity: int",
     "-  portionSize: String",
     "-  subtotal: double"],
    ["+  calculateSubtotal(): double",
     "+  updateQuantity(qty: int): void"])

ver_cx = 22.00
vb, vt, _ = uml(ax, ver_cx, T2, "Verification",
    ["-  verificationId: int",
     "-  verificationCode: String",
     "-  isVerified: boolean",
     "-  expiryDate: Date"],
    ["+  generateCode(): String",
     "+  sendVerificationEmail(): void",
     "+  verifyCode(code: String): boolean"])

# ═══════════════════════════════════════════════════════════════════════════
# ROW 3  (top = min(row2 bots) - 1.0)
# ═══════════════════════════════════════════════════════════════════════════
T3 = min(cb, cib, vb) - 0.90

ord_cx = 4.0
ob, ot, _ = uml(ax, ord_cx, T3, "Order",
    ["-  orderId: int",
     "-  orderDate: Date",
     "-  total: double",
     "-  tax: double",
     "-  deliveryCharge: double",
     "-  orderStatus: String"],
    ["+  createOrder(): void",
     "+  updateStatus(status: String): void",
     "+  calculateTotal(): double",
     "+  getOrderDetails(): String"])

pay_cx = 11.00
pb, pt, _ = uml(ax, pay_cx, T3, "Payment",
    ["-  paymentId: int",
     "-  amount: double",
     "-  paymentMethod: String",
     "-  paymentStatus: String",
     "-  transactionDate: Date"],
    ["+  processPayment(): boolean",
     "+  verifyPayment(): boolean",
     "+  getReceipt(): String"])

adr_cx = 18.00
ab, at_, _ = uml(ax, adr_cx, T3, "Address",
    ["-  addressId: int",
     "-  street: String",
     "-  city: String",
     "-  state: String",
     "-  postcode: String",
     "-  country: String",
     "-  addressType: String"],
    ["+  addAddress(): void",
     "+  validateAddress(): void",
     "+  deleteAddress(): void"])

rwd_cx = 25.00
rb, rt, _ = uml(ax, rwd_cx, T3, "RewardPoints",
    ["-  points: int",
     "-  totalPoints: int",
     "-  isEligibleForFree: boolean"],
    ["+  addPoints(points: int): void",
     "+  redeemPoints(): void",
     "+  checkEligibility(): boolean"])

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# All routed with horizontal+vertical segments (no diagonals)
# ═══════════════════════════════════════════════════════════════════════════

# ── 1. CustomSalad --|> Salad  (inheritance – open triangle) ─────────────────
# Child right edge → horizontal → Salad right edge (same row)
parrow(ax,
    [(cus_cx - CW/2,  (T1+csb)/2),
     (sal_cx + CW/2,  (T1+sb)/2)],
    style='-|>', lw=1.6,
    m1='',     m2='',
    label='')
# Label above
lbl(ax, (cus_cx - CW/2 + sal_cx + CW/2)/2,
        (T1+csb)/2 + 0.28, '«extends»')

# ── 2. User --places (1:0..*)→ ShoppingCart ──────────────────────────────────
# User bottom → down → ShoppingCart top  (both in left column area)
parrow(ax,
    [(user_cx, ub),
     (user_cx, T2 + (T2-cb)/2 + 0.30),   # midpoint between rows
     (cart_cx, T2 + (T2-cb)/2 + 0.30),
     (cart_cx, T2)],
    label='places', lseg=1,
    m1='1',  m1pt=(user_cx-0.45, ub-0.28),
    m2='0..*', m2pt=(cart_cx+0.55, T2+0.28))

# ── 3. User --requires (1:1)→ Verification  ──────────────────────────────────
# User right → horizontal → Verification left  (route via top of row2 gap)
VIA_Y3 = T2 + 0.40   # just above row2 top
parrow(ax,
    [(user_cx + CW/2, (ut+ub)/2),
     (ver_cx - CW/2,  (vt+vb)/2)],
    label='requires', lseg=0, loff=(0, 0.24),
    m1='1',    m1pt=(user_cx+CW/2+0.32, (ut+ub)/2+0.24),
    m2='1',    m2pt=(ver_cx-CW/2-0.28,  (vt+vb)/2+0.24))

# ── 4. User --earns (1:1)→ RewardPoints ──────────────────────────────────────
# Route: User right → right margin → down → RewardPoints top
RX = user_cx + CW/2   # start at User right
parrow(ax,
    [(user_cx + CW/2,  ub - (ub-ob)*0.40),   # midway down User right edge
     (27.20,           ub - (ub-ob)*0.40),    # far-right margin
     (27.20,           T3 + 0.22),
     (rwd_cx + CW/2,   T3 + 0.22),
     (rwd_cx + CW/2,   T3)],
    label='earns', lseg=1,
    m1='1',    m1pt=(27.20-0.38, ub-(ub-ob)*0.40+0.24),
    m2='1',    m2pt=(rwd_cx+CW/2-0.30, T3+0.46))

# ── 5. User --has (1:0..*)→ Address ──────────────────────────────────────────
# Route via left margin: User left → down → Address top-left
LX = 0.40  # left margin
parrow(ax,
    [(user_cx - CW/2,  ub - (ub-ob)*0.50),
     (LX,              ub - (ub-ob)*0.50),
     (LX,              T3 + 0.22),
     (adr_cx - CW/2,   T3 + 0.22),
     (adr_cx - CW/2,   T3)],
    label='has', lseg=1,
    m1='1',    m1pt=(LX+0.32, ub-(ub-ob)*0.50+0.24),
    m2='0..*', m2pt=(adr_cx-CW/2+0.40, T3+0.46))

# ── 6. ShoppingCart --contains (1:0..*)→ CartItem  ───────────────────────────
# Horizontal, same row
parrow(ax,
    [(cart_cx + CW/2, (ct+cb)/2),
     (ci_cx  - CW/2, (cit+cib)/2)],
    label='contains', lseg=0, loff=(0, 0.24),
    m1='1',    m1pt=(cart_cx+CW/2+0.30, (ct+cb)/2+0.24),
    m2='0..*', m2pt=(ci_cx -CW/2-0.35,  (cit+cib)/2+0.24))

# ── 7. CartItem --references (0..*:1)→ Salad  ────────────────────────────────
# CartItem top → up → Salad bottom  (both roughly same x column)
parrow(ax,
    [(ci_cx, cit),
     (ci_cx, T1 + 0.30),
     (sal_cx, T1 + 0.30),
     (sal_cx, sb)],
    label='references', lseg=1, loff=(0, 0.22),
    m1='0..*', m1pt=(ci_cx+0.52, cit+0.30),
    m2='1',    m2pt=(sal_cx+0.28, sb-0.28))

# ── 8. ShoppingCart --includes (1:1..*)→ Order  ──────────────────────────────
# Cart bottom → down → Order top  (similar x)
parrow(ax,
    [(cart_cx, cb),
     (cart_cx, T3 + 0.22),
     (ord_cx,  T3 + 0.22),
     (ord_cx,  T3)],
    label='includes', lseg=1, loff=(0.3, 0.22),
    m1='1',    m1pt=(cart_cx+0.42, cb-0.28),
    m2='1..*', m2pt=(ord_cx+0.52,  T3+0.48))

# ── 9. Order --paid by (1:1)→ Payment  ───────────────────────────────────────
# Horizontal, same row
parrow(ax,
    [(ord_cx + CW/2, (ot+ob)/2),
     (pay_cx - CW/2, (pt+pb)/2)],
    label='paid by', lseg=0, loff=(0, 0.24),
    m1='1', m1pt=(ord_cx+CW/2+0.28, (ot+ob)/2+0.24),
    m2='1', m2pt=(pay_cx-CW/2-0.25, (pt+pb)/2+0.24))

# ── 10. Order --delivered to (1:1)→ Address  ──────────────────────────────────
# Route under the boxes: Order bottom → down → right → Address bottom
BOT_Y = min(ob, pb, ab) - 0.50
parrow(ax,
    [(ord_cx,  ob),
     (ord_cx,  BOT_Y),
     (adr_cx,  BOT_Y),
     (adr_cx,  ab)],
    label='delivered to', lseg=1, loff=(0, -0.28),
    m1='1', m1pt=(ord_cx+0.30, ob-0.28),
    m2='1', m2pt=(adr_cx+0.28, ab-0.28))

# ═══════════════════════════════════════════════════════════════════════════
plt.tight_layout()
plt.savefig('/workspace/output/class_v3.png', dpi=180,
    bbox_inches='tight', facecolor='white')
plt.close()
print("Class v3 done.")
