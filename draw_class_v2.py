import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(26, 20))
ax.set_xlim(0, 26)
ax.set_ylim(0, 20)
ax.axis('off')
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

W         = 4.70     # class box width
ROW_H     = 0.26     # per-attribute row height
PAD       = 0.12     # vertical padding inside compartment
NAME_H    = 0.44     # name section height
HEADER_BG = '#c8d8f0'
BOX_BG    = 'white'
BORDER    = '#222222'
ASSOC_COL = '#333333'
TEXT_COL  = '#111111'


# ─── UML class box ────────────────────────────────────────────────────────────
def uml_class(ax, cx, top_y, name, attrs, methods, italic=False):
    attr_h  = len(attrs)  * ROW_H + 2*PAD
    meth_h  = len(methods)* ROW_H + 2*PAD
    total_h = NAME_H + attr_h + meth_h
    x0      = cx - W/2
    bot_y   = top_y - total_h

    # box shadow
    ax.add_patch(FancyBboxPatch((x0+0.06, bot_y-0.06), W, total_h,
                                boxstyle="square,pad=0",
                                lw=0, fc='#cccccc', zorder=2))
    # outer box
    ax.add_patch(FancyBboxPatch((x0, bot_y), W, total_h,
                                boxstyle="square,pad=0",
                                lw=1.6, ec=BORDER, fc=BOX_BG, zorder=3))
    # name background
    ax.add_patch(mpatches.Rectangle((x0, top_y-NAME_H), W, NAME_H,
                                    fc=HEADER_BG, ec='none', zorder=4))
    div1 = top_y - NAME_H
    div2 = div1  - attr_h
    ax.plot([x0, x0+W], [div1, div1], color=BORDER, lw=1.4, zorder=5)
    ax.plot([x0, x0+W], [div2, div2], color=BORDER, lw=1.4, zorder=5)

    sty = 'italic' if italic else 'normal'
    ax.text(cx, top_y - NAME_H/2, name,
            ha='center', va='center', fontsize=9.5,
            fontweight='bold', style=sty, color='#0a2040', zorder=6)

    for i, a in enumerate(attrs):
        ay = div1 - PAD - (i+0.5)*ROW_H
        ax.text(x0+0.15, ay, a, ha='left', va='center',
                fontsize=7.3, family='monospace', color=TEXT_COL, zorder=6)

    for i, m in enumerate(methods):
        my = div2 - PAD - (i+0.5)*ROW_H
        ax.text(x0+0.15, my, m, ha='left', va='center',
                fontsize=7.3, family='monospace', color=TEXT_COL, zorder=6)
    return bot_y


# ─── relationship helpers ─────────────────────────────────────────────────────
def line(ax, x1, y1, x2, y2, label='', m1='', m2='',
         arrowstyle='->', lw=1.3, dash=False):
    ls = '--' if dash else '-'
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=arrowstyle, color=ASSOC_COL,
                                lw=lw, linestyle=ls))
    mx, my = (x1+x2)/2, (y1+y2)/2
    if label:
        ax.text(mx, my, label, ha='center', va='center', fontsize=8,
                color='#333', style='italic',
                bbox=dict(boxstyle='round,pad=0.12',
                          fc='white', ec='none', alpha=0.9))
    off = 0.18
    if m1:
        ax.text(x1+(x2-x1)*0.10, y1+(y2-y1)*0.10+off, m1,
                ha='center', va='center', fontsize=8.5, color='#111',
                fontweight='bold')
    if m2:
        ax.text(x2-(x2-x1)*0.10, y2-(y2-y1)*0.10+off, m2,
                ha='center', va='center', fontsize=8.5, color='#111',
                fontweight='bold')


def inherit(ax, cx_child, bot_child, cx_parent, bot_parent):
    """Open triangle from child bottom to parent bottom (pointing up)."""
    line(ax, cx_child, bot_child, cx_parent, bot_parent,
         arrowstyle='-|>', lw=1.5)


# ─── Title ────────────────────────────────────────────────────────────────────
ax.text(13, 19.80, '6.2  Class Diagram',
        ha='center', va='center', fontsize=14, fontweight='bold',
        color='#0a2040')

# ═══════════════════════════════════════════════════════════════════════════════
# ROW 1   (top_y = 19.3)
# ═══════════════════════════════════════════════════════════════════════════════
TOP1 = 19.20

user_cx = 3.80
user_bot = uml_class(ax, user_cx, TOP1, "User",
    attrs=[
        "-  userId: int",
        "-  username: String",
        "-  firstName: String",
        "-  lastName: String",
        "-  dateOfBirth: Date",
        "-  email: String",
        "-  password: String",
        "-  tax: double",
        "-  accountStatus: String",
        "-  failedLoginAttempts: int",
        "-  lastActivityDate: Date",
    ],
    methods=[
        "+  register(): void",
        "+  login(): void",
        "+  logout(): void",
        "+  verifyEmail(code: String): boolean",
        "+  reactivateAccount(): void",
        "+  updateProfile(): void",
    ])

salad_cx = 11.80
salad_bot = uml_class(ax, salad_cx, TOP1, "Salad",
    attrs=[
        "-  saladId: int",
        "-  name: String",
        "-  ingredients: String",
        "-  description: String",
        "-  allergenWarnings: String",
        "-  nutritionalInfo: String",
        "-  price: double",
        "-  portionSize: String",
    ],
    methods=[
        "+  getDetails(): void",
        "+  updatePrice(price: double): void",
        "+  getPrice(): double",
    ])

custom_cx = 20.00
custom_bot = uml_class(ax, custom_cx, TOP1, "CustomSalad",
    attrs=[
        "-  customIngredients: List<String>",
    ],
    methods=[
        "+  addIngredient(ingredient: String): void",
        "+  removeIngredient(ingredient: String): void",
        "+  calculatePrice(): double",
    ])

# ═══════════════════════════════════════════════════════════════════════════════
# ROW 2   (top_y based on min of row-1 bottoms minus gap)
# ═══════════════════════════════════════════════════════════════════════════════
TOP2 = min(user_bot, salad_bot, custom_bot) - 0.70

cart_cx = 7.00
cart_bot = uml_class(ax, cart_cx, TOP2, "ShoppingCart",
    attrs=[
        "-  cartId: int",
        "-  sessionId: String",
        "-  createdDate: Date",
    ],
    methods=[
        "+  addItem(item: CartItem): void",
        "+  removeItem(itemId): void",
        "+  updateQuantity(itemId, qty: int): void",
        "+  getTotal(): double",
        "+  clearCart(): void",
    ])

cartitem_cx = 14.50
cartitem_bot = uml_class(ax, cartitem_cx, TOP2, "CartItem",
    attrs=[
        "-  cartItemId: int",
        "-  quantity: int",
        "-  portionSize: String",
        "-  subtotal: double",
    ],
    methods=[
        "+  calculateSubtotal(): double",
        "+  updateQuantity(qty: int): void",
    ])

verif_cx = 21.50
verif_bot = uml_class(ax, verif_cx, TOP2, "Verification",
    attrs=[
        "-  verificationId: int",
        "-  verificationCode: String",
        "-  isVerified: boolean",
        "-  expiryDate: Date",
    ],
    methods=[
        "+  generateCode(): String",
        "+  sendVerificationEmail(): void",
        "+  verifyCode(code: String): boolean",
    ])

# ═══════════════════════════════════════════════════════════════════════════════
# ROW 3   (top_y based on min of row-2 bottoms minus gap)
# ═══════════════════════════════════════════════════════════════════════════════
TOP3 = min(cart_bot, cartitem_bot, verif_bot) - 0.80

order_cx = 3.80
order_bot = uml_class(ax, order_cx, TOP3, "Order",
    attrs=[
        "-  orderId: int",
        "-  orderDate: Date",
        "-  total: double",
        "-  tax: double",
        "-  deliveryCharge: double",
        "-  orderStatus: String",
    ],
    methods=[
        "+  createOrder(): void",
        "+  updateStatus(status: String): void",
        "+  calculateTotal(): double",
        "+  getOrderDetails(): String",
    ])

payment_cx = 10.50
payment_bot = uml_class(ax, payment_cx, TOP3, "Payment",
    attrs=[
        "-  paymentId: int",
        "-  amount: double",
        "-  paymentMethod: String",
        "-  paymentStatus: String",
        "-  transactionDate: Date",
    ],
    methods=[
        "+  processPayment(): boolean",
        "+  verifyPayment(): boolean",
        "+  getReceipt(): String",
    ])

address_cx = 17.20
address_bot = uml_class(ax, address_cx, TOP3, "Address",
    attrs=[
        "-  addressId: int",
        "-  street: String",
        "-  city: String",
        "-  state: String",
        "-  postcode: String",
        "-  country: String",
        "-  addressType: String",
    ],
    methods=[
        "+  addAddress(): void",
        "+  validateAddress(): void",
        "+  deleteAddress(): void",
    ])

reward_cx = 23.40
reward_bot = uml_class(ax, reward_cx, TOP3, "RewardPoints",
    attrs=[
        "-  points: int",
        "-  totalPoints: int",
        "-  isEligibleForFree: boolean",
    ],
    methods=[
        "+  addPoints(points: int): void",
        "+  redeemPoints(): void",
        "+  checkEligibility(): boolean",
    ])

# ═══════════════════════════════════════════════════════════════════════════════
# Relationships
# ═══════════════════════════════════════════════════════════════════════════════

# CustomSalad ──|> Salad  (open hollow arrow = inheritance)
line(ax, custom_cx - W/2, (TOP1 + custom_bot)/2,
        salad_cx  + W/2, (TOP1 + salad_bot)/2,
     arrowstyle='-|>', lw=1.5)

# User --places (1:0..*)-> ShoppingCart
line(ax, user_cx, user_bot,
        cart_cx, TOP2,
     label='places', m1='1', m2='0..*')

# User --has (1:0..*)-> Address
line(ax, user_cx + W/2, (TOP1 + user_bot)/2,
        address_cx - W/2, (TOP3 + address_bot)/2,
     label='has', m1='1', m2='0..*')

# User --earns (1:1)-> RewardPoints
line(ax, user_cx + W/2, user_bot + (TOP1-user_bot)*0.35,
        reward_cx - W/2, (TOP3 + reward_bot)/2,
     label='earns', m1='1', m2='1')

# User --requires (1:1)-> Verification
line(ax, user_cx + W/2, user_bot + (TOP1-user_bot)*0.55,
        verif_cx - W/2, (TOP2 + verif_bot)/2,
     label='requires', m1='1', m2='1')

# ShoppingCart --contains (1:0..*)-> CartItem
line(ax, cart_cx + W/2, (TOP2 + cart_bot)/2,
        cartitem_cx - W/2, (TOP2 + cartitem_bot)/2,
     label='contains', m1='1', m2='0..*')

# CartItem --references (0..*:1)-> Salad
line(ax, cartitem_cx, cartitem_bot,
        salad_cx, salad_bot,
     label='references', m1='0..*', m2='1')

# ShoppingCart --includes (1:1..*)-> Order
line(ax, cart_cx, cart_bot,
        order_cx, TOP3,
     label='includes', m1='1', m2='1..*')

# Order --paid by (1:1)-> Payment
line(ax, order_cx + W/2, (TOP3 + order_bot)/2,
        payment_cx - W/2, (TOP3 + payment_bot)/2,
     label='paid by', m1='1', m2='1')

# Order --delivered to (1:1)-> Address
line(ax, order_cx + W/2, (TOP3 + order_bot)/2 - 0.3,
        address_cx - W/2, (TOP3 + address_bot)/2 - 0.3,
     label='delivered to', m1='1', m2='1')

plt.tight_layout()
plt.savefig('/workspace/output/class_diagram_v2.png', dpi=180,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Class diagram v2 saved.")
