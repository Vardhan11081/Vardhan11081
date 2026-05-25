import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(28, 24))
ax.set_xlim(0, 28)
ax.set_ylim(0, 24)
ax.axis('off')
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# ─── helper: draw a UML class box ────────────────────────────────────────────
def uml_class(ax, cx, top_y, name, attrs, methods,
              is_abstract=False, color='#dae8fc', border='#0e4d92'):
    """
    Draw a 3-compartment UML class box centred on cx, top at top_y.
    Returns bottom y of the box.
    """
    W = 5.2          # total width
    ROW_H = 0.30     # height per text row
    PAD = 0.18       # vertical padding inside each compartment
    NAME_H = 0.50    # name compartment height

    attr_h  = max(len(attrs),  1) * ROW_H + 2 * PAD
    meth_h  = max(len(methods),1) * ROW_H + 2 * PAD
    total_h = NAME_H + attr_h + meth_h

    x0 = cx - W / 2
    y0 = top_y - total_h     # box bottom

    # outer border
    rect = FancyBboxPatch((x0, y0), W, total_h,
                          boxstyle="square,pad=0",
                          linewidth=1.6, edgecolor=border,
                          facecolor=color, zorder=3)
    ax.add_patch(rect)

    # ── name compartment ──────────────────────────────────────────────────
    name_y_top = top_y
    div1 = top_y - NAME_H
    ax.plot([x0, x0+W], [div1, div1], color=border, lw=1.2, zorder=4)
    style = 'italic' if is_abstract else 'normal'
    prefix = "«abstract»\n" if is_abstract else ""
    ax.text(cx, (name_y_top + div1)/2, prefix + name,
            ha='center', va='center', fontsize=9,
            fontweight='bold', style=style, color='#0e2954',
            multialignment='center', zorder=5)

    # ── attributes compartment ────────────────────────────────────────────
    div2 = div1 - attr_h
    ax.plot([x0, x0+W], [div2, div2], color=border, lw=1.2, zorder=4)
    for i, attr in enumerate(attrs):
        ay = div1 - PAD - (i + 0.5) * ROW_H
        ax.text(x0 + 0.18, ay, attr, ha='left', va='center',
                fontsize=7.2, family='monospace', zorder=5)

    # ── methods compartment ───────────────────────────────────────────────
    for i, meth in enumerate(methods):
        my = div2 - PAD - (i + 0.5) * ROW_H
        ax.text(x0 + 0.18, my, meth, ha='left', va='center',
                fontsize=7.2, family='monospace', zorder=5)

    return y0   # bottom of box


# ─── helper: draw relationship lines ─────────────────────────────────────────
def assoc(ax, x1, y1, x2, y2, label='', mult1='', mult2='',
          style='->', color='#333333', lw=1.3, dash=None):
    ls = '--' if dash else '-'
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color,
                                lw=lw, linestyle=ls))
    mx, my = (x1+x2)/2, (y1+y2)/2
    if label:
        ax.text(mx, my, label, ha='center', va='center', fontsize=7,
                color='#333333', style='italic',
                bbox=dict(boxstyle='round,pad=0.12', fc='white',
                          ec='none', alpha=0.9))
    if mult1:
        ax.text(x1 + (x2-x1)*0.12, y1 + (y2-y1)*0.12, mult1,
                ha='center', va='center', fontsize=7.5, color='#c0392b',
                fontweight='bold')
    if mult2:
        ax.text(x2 - (x2-x1)*0.12, y2 - (y2-y1)*0.12, mult2,
                ha='center', va='center', fontsize=7.5, color='#c0392b',
                fontweight='bold')


def inherit(ax, cx1, bot1, cx2, top2):
    """Hollow-triangle inheritance arrow from child (cx1,bot1) to parent (cx2,top2)."""
    assoc(ax, cx1, bot1, cx2, top2, style='-|>', color='#0e4d92', lw=1.5)


# ─── Class definitions ────────────────────────────────────────────────────────

# ── User (abstract) – top centre ─────────────────────────────────────────────
user_cx, user_ty = 14.0, 23.5
user_by = uml_class(ax, user_cx, user_ty, "User",
    attrs=[
        "- userId       : String",
        "- username     : String",
        "- firstName    : String",
        "- lastName     : String",
        "- dateOfBirth  : Date",
        "- email        : String",
        "# password     : String",
        "# accountStatus: AccountStatus",
        "# failedLogins : int",
        "# lastLoginDate: Date",
        "# verifyCode   : String",
        "# isVerified   : boolean",
    ],
    methods=[
        "+ register()        : void",
        "+ login()           : boolean",
        "+ logout()          : void",
        "+ verifyAccount()   : boolean",
        "+ reactivateAccount(): void",
        "# hashPassword()    : String",
    ],
    is_abstract=True, color='#ffe6cc', border='#d6790d')

# ── RegisteredUser ────────────────────────────────────────────────────────────
reg_cx, reg_ty = 20.5, 18.5
reg_by = uml_class(ax, reg_cx, reg_ty, "RegisteredUser",
    attrs=[
        "- rewardPoints  : int",
        "- addresses     : List<Address>",
    ],
    methods=[
        "+ updateProfile()    : void",
        "+ manageAddresses()  : void",
        "+ viewOrderHistory() : List<Order>",
        "+ redeemPoints()     : boolean",
        "+ saveAddress()      : void",
    ],
    color='#dae8fc', border='#0e4d92')

# ── GuestUser ─────────────────────────────────────────────────────────────────
guest_cx, guest_ty = 7.5, 18.5
guest_by = uml_class(ax, guest_cx, guest_ty, "GuestUser",
    attrs=[
        "- sessionId : String",
        "- cartId    : String",
    ],
    methods=[
        "+ browseMenu()  : List<Salad>",
        "+ addToCart()   : void",
        "+ viewCart()    : ShoppingCart",
    ],
    color='#d5e8d4', border='#2e7d32')

# ── Salad ─────────────────────────────────────────────────────────────────────
salad_cx, salad_ty = 2.8, 12.5
salad_by = uml_class(ax, salad_cx, salad_ty, "Salad",
    attrs=[
        "- saladId        : String",
        "- name           : String",
        "- description    : String",
        "- ingredients    : List<String>",
        "- nutritionalInfo: String",
        "- allergenWarnings: String",
        "- portionSizes   : List<PortionSize>",
        "- price          : Map<PortionSize,Double>",
        "- isCustom       : boolean",
    ],
    methods=[
        "+ getDetails()          : String",
        "+ getPrice(size)        : double",
        "+ updatePrice(size,amt) : void",
        "+ isAvailable()         : boolean",
    ],
    color='#fff2cc', border='#d6b656')

# ── ShoppingCart ──────────────────────────────────────────────────────────────
cart_cx, cart_ty = 8.5, 12.5
cart_by = uml_class(ax, cart_cx, cart_ty, "ShoppingCart",
    attrs=[
        "- cartId    : String",
        "- sessionId : String",
        "- userId    : String",
        "- items     : List<CartItem>",
        "- createdAt : Date",
    ],
    methods=[
        "+ addItem(item)          : void",
        "+ removeItem(itemId)     : void",
        "+ updateQuantity(id,qty) : void",
        "+ calculateTotal()       : double",
        "+ clearCart()            : void",
        "+ getItemCount()         : int",
    ],
    color='#dae8fc', border='#0e4d92')

# ── CartItem ──────────────────────────────────────────────────────────────────
cartitem_cx, cartitem_ty = 8.5, 7.0
cartitem_by = uml_class(ax, cartitem_cx, cartitem_ty, "CartItem",
    attrs=[
        "- cartItemId  : String",
        "- saladId     : String",
        "- portionSize : PortionSize",
        "- quantity    : int",
        "- unitPrice   : double",
    ],
    methods=[
        "+ getSubtotal() : double",
        "+ updateQty(qty): void",
    ],
    color='#dae8fc', border='#0e4d92')

# ── Order ─────────────────────────────────────────────────────────────────────
order_cx, order_ty = 14.5, 12.5
order_by = uml_class(ax, order_cx, order_ty, "Order",
    attrs=[
        "- orderId        : String",
        "- userId         : String",
        "- orderStatus    : OrderStatus",
        "- items          : List<OrderItem>",
        "- totalAmount    : double",
        "- tax            : double",
        "- deliveryCharge : double",
        "- deliveryAddress: Address",
        "- createdAt      : Date",
        "- updatedAt      : Date",
    ],
    methods=[
        "+ createOrder()        : void",
        "+ updateStatus(status) : void",
        "+ calculateTotal()     : double",
        "+ cancelOrder()        : boolean",
        "+ getOrderSummary()    : String",
    ],
    color='#ffe6cc', border='#d6790d')

# ── OrderItem ─────────────────────────────────────────────────────────────────
orderitem_cx, orderitem_ty = 14.5, 6.2
orderitem_by = uml_class(ax, orderitem_cx, orderitem_ty, "OrderItem",
    attrs=[
        "- orderItemId : String",
        "- saladId     : String",
        "- portionSize : PortionSize",
        "- quantity    : int",
        "- unitPrice   : double",
    ],
    methods=[
        "+ getSubtotal() : double",
    ],
    color='#ffe6cc', border='#d6790d')

# ── Payment ───────────────────────────────────────────────────────────────────
payment_cx, payment_ty = 21.0, 12.5
payment_by = uml_class(ax, payment_cx, payment_ty, "Payment",
    attrs=[
        "- paymentId     : String",
        "- orderId       : String",
        "- amount        : double",
        "- paymentMethod : PaymentMethod",
        "- paymentStatus : PaymentStatus",
        "- transactionRef: String",
        "- transactionDate: Date",
    ],
    methods=[
        "+ processPayment()  : boolean",
        "+ verifyPayment()   : boolean",
        "+ refundPayment()   : boolean",
        "+ getReceipt()      : String",
    ],
    color='#e1d5e7', border='#6a1b9a')

# ── Address ───────────────────────────────────────────────────────────────────
address_cx, address_ty = 21.0, 6.5
address_by = uml_class(ax, address_cx, address_ty, "Address",
    attrs=[
        "- addressId  : String",
        "- userId     : String",
        "- street     : String",
        "- suburb     : String",
        "- city       : String",
        "- state      : String",
        "- postalCode : String",
        "- country    : String",
        "- addressType: AddressType",
    ],
    methods=[
        "+ validate()   : boolean",
        "+ toString()   : String",
        "+ update()     : void",
    ],
    color='#d5e8d4', border='#2e7d32')

# ── RewardProgram ─────────────────────────────────────────────────────────────
reward_cx, reward_ty = 7.5, 4.5
reward_by = uml_class(ax, reward_cx, reward_ty, "RewardProgram",
    attrs=[
        "- programId       : String",
        "- userId          : String",
        "- totalPoints     : int",
        "- pointsPerSalad  : int = 1",
        "- pointsThreshold : int = 15",
    ],
    methods=[
        "+ addPoints(qty)       : void",
        "+ deductPoints(pts)    : void",
        "+ checkEligibility()   : boolean",
        "+ redeemFreeSalad()    : boolean",
        "+ getPointsBalance()   : int",
    ],
    color='#f8cecc', border='#ae4132')


# ─── Relationships ─────────────────────────────────────────────────────────────

# Inheritance: GuestUser & RegisteredUser → User
inherit(ax, guest_cx, guest_ty, user_cx - 1.8, user_by)
inherit(ax, reg_cx,   reg_ty,   user_cx + 1.8, user_by)

# RegisteredUser 1 ──< * Order
assoc(ax, reg_cx - 0.5, reg_by, order_cx + 0.5, order_ty,
      label="places", mult1="1", mult2="0..*",
      style='->', color='#555555')

# RegisteredUser 1 ──< * Address
assoc(ax, reg_cx + 0.4, reg_by,
      address_cx - 0.3, address_ty,
      label="has", mult1="1", mult2="0..*",
      style='->', color='#555555')

# User (or GuestUser) 1 ── 1 ShoppingCart
assoc(ax, guest_cx - 0.2, guest_by, cart_cx - 0.8, cart_ty,
      label="owns", mult1="1", mult2="1",
      style='->', color='#555555')

# ShoppingCart 1 ──< * CartItem  (composition)
assoc(ax, cart_cx, cart_by, cartitem_cx, cartitem_ty,
      label="contains", mult1="1", mult2="0..*",
      style='->', color='#333333', lw=1.5)

# CartItem *──1 Salad
assoc(ax, cartitem_cx - 2.3, (cartitem_ty + cartitem_by)/2,
      salad_cx + 2.3, (salad_ty + salad_by)/2,
      label="references", mult1="*", mult2="1",
      style='->', color='#555555')

# Order 1 ──< * OrderItem  (composition)
assoc(ax, order_cx, order_by, orderitem_cx, orderitem_ty,
      label="contains", mult1="1", mult2="1..*",
      style='->', color='#333333', lw=1.5)

# OrderItem *──1 Salad
assoc(ax, orderitem_cx - 2.3, (orderitem_ty + orderitem_by)/2,
      salad_cx + 2.3, (salad_ty + salad_by)/2 - 0.5,
      label="references", mult1="*", mult2="1",
      style='->', color='#555555')

# Order 1 ── 1 Payment
assoc(ax, order_cx + 2.6, (order_ty + order_by)/2,
      payment_cx - 2.6, (payment_ty + payment_by)/2,
      label="paid via", mult1="1", mult2="1",
      style='->', color='#555555')

# Order 1 ── 1 Address (delivery)
assoc(ax, order_cx + 1.5, order_by,
      address_cx - 1.2, address_ty,
      label="delivers to", mult1="1", mult2="1",
      style='->', color='#555555')

# RegisteredUser 1 ── 1 RewardProgram
assoc(ax, reg_cx - 2.0, reg_by,
      reward_cx + 1.2, reward_ty,
      label="enrolled in", mult1="1", mult2="1",
      style='->', color='#555555')


# ─── Title & Legend ───────────────────────────────────────────────────────────
ax.text(14, 23.85,
        "FreshBite Salads – Class Diagram",
        ha='center', va='center', fontsize=14,
        fontweight='bold', color='#0e2954')

# Legend box
lx, ly, lw, lh = 0.2, 0.1, 5.6, 2.8
ax.add_patch(FancyBboxPatch((lx, ly), lw, lh,
             boxstyle="square,pad=0", linewidth=1,
             edgecolor='#666', facecolor='#f9f9f9', zorder=3))
ax.text(lx + lw/2, ly + lh - 0.25, "Legend",
        ha='center', va='center', fontsize=9,
        fontweight='bold', zorder=4)

entries = [
    ('#ffe6cc', '#d6790d', "«abstract» User (base class)"),
    ('#dae8fc', '#0e4d92', "Registered / Guest User & Cart"),
    ('#fff2cc', '#d6b656', "Salad / Menu"),
    ('#ffe6cc', '#d6790d', "Order & OrderItem"),
    ('#e1d5e7', '#6a1b9a', "Payment"),
    ('#d5e8d4', '#2e7d32', "Address / GuestUser"),
    ('#f8cecc', '#ae4132', "RewardProgram"),
]
for i, (fc, ec, lbl) in enumerate(entries):
    ey = ly + lh - 0.65 - i * 0.30
    ax.add_patch(FancyBboxPatch((lx + 0.2, ey - 0.12), 0.45, 0.23,
                 boxstyle="square,pad=0", lw=1, ec=ec, fc=fc, zorder=4))
    ax.text(lx + 0.85, ey, lbl, va='center', fontsize=7.5, zorder=5)

plt.tight_layout()
plt.savefig('/workspace/output/class_diagram.png', dpi=180,
            bbox_inches='tight', facecolor='white')
plt.close()
print("Class diagram saved.")
