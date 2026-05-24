import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import matplotlib.lines as mlines

fig, ax = plt.subplots(figsize=(24, 18))
ax.set_xlim(0, 24)
ax.set_ylim(0, 18)
ax.axis('off')
ax.set_facecolor('#FAFAFA')
fig.patch.set_facecolor('#FAFAFA')

ax.text(12, 17.6, "FreshBite Salads – UML Class Diagram",
        ha='center', va='center', fontsize=15, fontweight='bold', color='#1a1a2e')

# ─────────────────────────────────────────
# Helper: draw a UML class box
# ─────────────────────────────────────────
def draw_class(ax, x, y, name, attrs, methods, width=3.8, header_color='#2C5F8A'):
    """
    Draws a UML class box.
    x,y = bottom-left corner
    Returns (x, y, width, total_height)
    """
    line_h = 0.28
    header_h = 0.45
    attrs_h = max(len(attrs), 1) * line_h + 0.15
    methods_h = max(len(methods), 1) * line_h + 0.15
    total_h = header_h + attrs_h + methods_h

    # Header background
    hdr = FancyBboxPatch((x, y + total_h - header_h), width, header_h,
                         boxstyle="square,pad=0", linewidth=1.5,
                         edgecolor='#1a3a5c', facecolor=header_color, zorder=3)
    ax.add_patch(hdr)
    # Attr section
    attr_box = FancyBboxPatch((x, y + methods_h), width, attrs_h,
                              boxstyle="square,pad=0", linewidth=1.5,
                              edgecolor='#1a3a5c', facecolor='#EBF5FB', zorder=3)
    ax.add_patch(attr_box)
    # Methods section
    meth_box = FancyBboxPatch((x, y), width, methods_h,
                              boxstyle="square,pad=0", linewidth=1.5,
                              edgecolor='#1a3a5c', facecolor='#F0FFF0', zorder=3)
    ax.add_patch(meth_box)

    # Class name
    ax.text(x + width/2, y + total_h - header_h/2, f'«class»\n{name}',
            ha='center', va='center', fontsize=8.5, fontweight='bold',
            color='white', zorder=5)

    # Attributes
    for i, a in enumerate(attrs):
        ax.text(x + 0.1, y + methods_h + attrs_h - 0.12 - i*line_h, a,
                ha='left', va='top', fontsize=6.8, color='#1a3a5c',
                fontfamily='monospace', zorder=5)

    # Methods
    for i, m in enumerate(methods):
        ax.text(x + 0.1, y + methods_h - 0.12 - i*line_h, m,
                ha='left', va='top', fontsize=6.8, color='#1a3a5c',
                fontfamily='monospace', zorder=5)

    return x, y, width, total_h

def assoc(ax, x1, y1, x2, y2, label='', mult1='', mult2='',
          style='->', color='#333', lw=1.2, dashed=False):
    """Draw association/inheritance arrow with labels."""
    ls = '--' if dashed else '-'
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                                linestyle=ls), zorder=2)
    mx, my = (x1+x2)/2, (y1+y2)/2
    if label:
        ax.text(mx + 0.05, my + 0.1, label, ha='center', va='bottom',
                fontsize=6.5, color='#444', style='italic', zorder=6,
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.85, pad=0.5))
    if mult1:
        ax.text(x1 + (x2-x1)*0.12, y1 + (y2-y1)*0.12, mult1,
                ha='center', fontsize=7, color='#880E4F', fontweight='bold', zorder=6)
    if mult2:
        ax.text(x1 + (x2-x1)*0.88, y1 + (y2-y1)*0.88, mult2,
                ha='center', fontsize=7, color='#880E4F', fontweight='bold', zorder=6)

# ─────────────────────────────────────────
# Define & place each class
# ─────────────────────────────────────────

# 1. User  (top-left)
user_attrs = [
    "-userId: String",
    "-username: String",
    "-firstName: String",
    "-lastName: String",
    "-dateOfBirth: Date",
    "-email: String",
    "-password: String",
    "-accountStatus: String",
    "-rewardPoints: int",
    "-loginAttempts: int",
]
user_methods = [
    "+register(): void",
    "+login(): boolean",
    "+logout(): void",
    "+updateProfile(): void",
    "+reactivateAccount(): boolean",
]
draw_class(ax, 0.3, 11.5, "User", user_attrs, user_methods, width=3.8)

# 2. Address (below User)
addr_attrs = [
    "-addressId: String",
    "-street: String",
    "-city: String",
    "-state: String",
    "-postCode: String",
    "-country: String",
    "-isDefault: boolean",
]
addr_methods = [
    "+addAddress(): void",
    "+updateAddress(): void",
    "+deleteAddress(): void",
]
draw_class(ax, 0.3, 5.8, "Address", addr_attrs, addr_methods, width=3.8)

# 3. Salad (top-center)
salad_attrs = [
    "-saladId: String",
    "-name: String",
    "-description: String",
    "-ingredients: List<String>",
    "-nutritionalInfo: String",
    "-allergenWarnings: String",
    "-price: double",
    "-portionSizes: List<String>",
]
salad_methods = [
    "+getDetails(): String",
    "+getPrice(size: String): double",
    "+getSizes(): List<String>",
]
draw_class(ax, 5.0, 12.0, "Salad", salad_attrs, salad_methods, width=3.8)

# 4. CustomSalad – extends Salad  (right of Salad)
csalad_attrs = [
    "-customIngredients: List<String>",
    "-customName: String",
]
csalad_methods = [
    "+createCustomSalad(): void",
    "+addIngredient(i: String): void",
    "+removeIngredient(i: String): void",
]
draw_class(ax, 9.5, 12.0, "CustomSalad", csalad_attrs, csalad_methods, width=3.8)

# 5. ShoppingCart (center)
cart_attrs = [
    "-cartId: String",
    "-sessionId: String",
    "-createdAt: DateTime",
    "-status: String",
]
cart_methods = [
    "+addItem(item: CartItem): void",
    "+removeItem(itemId: String): void",
    "+updateQuantity(id,qty): void",
    "+getTotal(): double",
    "+clearCart(): void",
]
draw_class(ax, 5.0, 7.2, "ShoppingCart", cart_attrs, cart_methods, width=3.8)

# 6. CartItem  (below ShoppingCart)
cartitem_attrs = [
    "-itemId: String",
    "-quantity: int",
    "-portionSize: String",
    "-unitPrice: double",
]
cartitem_methods = [
    "+calculateSubtotal(): double",
    "+updateQuantity(q: int): void",
]
draw_class(ax, 5.0, 3.0, "CartItem", cartitem_attrs, cartitem_methods, width=3.8)

# 7. Order (right side)
order_attrs = [
    "-orderId: String",
    "-totalCost: double",
    "-tax: double",
    "-deliveryCharge: double",
    "-status: String",
    "-createdAt: DateTime",
]
order_methods = [
    "+placeOrder(): void",
    "+updateStatus(s: String): void",
    "+cancelOrder(): void",
    "+getOrderDetails(): String",
]
draw_class(ax, 14.0, 10.5, "Order", order_attrs, order_methods, width=3.8)

# 8. Payment (bottom-right)
payment_attrs = [
    "-paymentId: String",
    "-amount: double",
    "-method: String",
    "-status: String",
    "-transactionId: String",
    "-paidAt: DateTime",
]
payment_methods = [
    "+processPayment(): boolean",
    "+verifyPayment(): boolean",
    "+refund(): void",
]
draw_class(ax, 14.0, 5.5, "Payment", payment_attrs, payment_methods, width=3.8)

# 9. RewardPoints (bottom-center)
rp_attrs = [
    "-pointsId: String",
    "-totalPoints: int",
    "-redeemedPoints: int",
    "-lastUpdated: DateTime",
]
rp_methods = [
    "+earnPoints(n: int): void",
    "+redeemPoints(): boolean",
    "+getBalance(): int",
]
draw_class(ax, 9.5, 5.5, "RewardPoints", rp_attrs, rp_methods, width=3.8)

# 10. Notification (top-right)
notif_attrs = [
    "-notifId: String",
    "-type: String",
    "-message: String",
    "-sentAt: DateTime",
]
notif_methods = [
    "+sendEmail(): void",
    "+sendVerificationCode(): void",
]
draw_class(ax, 19.0, 12.5, "Notification", notif_attrs, notif_methods, width=4.7)

# ─────────────────────────────────────────
# Associations
# ─────────────────────────────────────────
# User -> Address  (1 to many)
assoc(ax, 2.2, 11.5, 2.2, 9.2, label='has', mult1='1', mult2='0..*')
# User -> ShoppingCart (1 to 1 per session)
assoc(ax, 4.1, 13.5, 5.0, 9.5, label='owns', mult1='1', mult2='1')
# User -> RewardPoints (1 to 1)
assoc(ax, 3.5, 11.5, 11.5, 8.3, label='earns', mult1='1', mult2='1')
# User -> Order (1 to many)
assoc(ax, 4.1, 12.5, 14.0, 13.5, label='places', mult1='1', mult2='0..*')
# ShoppingCart -> CartItem (1 to many)
assoc(ax, 6.9, 7.2, 6.9, 5.8, label='contains', mult1='1', mult2='1..*')
# CartItem -> Salad (many to 1)
assoc(ax, 6.9, 3.0, 6.9, 13.7, label='refers to', mult1='0..*', mult2='1')
# CustomSalad --|> Salad (inheritance – hollow triangle)
assoc(ax, 9.5, 14.0, 8.8, 14.0, style='-|>', color='#1a3a5c', lw=1.8)
# Order -> Payment (1 to 1)
assoc(ax, 15.9, 10.5, 15.9, 9.1, label='paid via', mult1='1', mult2='1')
# Order -> CartItem (1 to many)
assoc(ax, 14.0, 12.5, 8.8, 4.8, label='includes', mult1='1', mult2='1..*')
# Order -> Address (delivery address)
assoc(ax, 14.0, 11.5, 4.1, 7.8, label='delivered to', mult1='1', mult2='1')
# User -> Notification
assoc(ax, 4.1, 14.5, 19.0, 14.5, label='receives', mult1='1', mult2='0..*')
# Order -> Notification
assoc(ax, 17.9, 10.5, 21.35, 12.5, label='triggers', mult1='1', mult2='0..*')

# ─────────────────────────────────────────
# Legend
# ─────────────────────────────────────────
ax.text(0.3, 1.2, "Legend:", fontsize=8, fontweight='bold', color='#1a1a2e')
# Inheritance
ax.annotate('', xy=(1.8, 0.8), xytext=(0.6, 0.8),
            arrowprops=dict(arrowstyle='-|>', color='#1a3a5c', lw=1.8))
ax.text(1.9, 0.8, "Inheritance", va='center', fontsize=7.5)
# Association
ax.annotate('', xy=(4.7, 0.8), xytext=(3.4, 0.8),
            arrowprops=dict(arrowstyle='->', color='#333', lw=1.2))
ax.text(4.8, 0.8, "Association", va='center', fontsize=7.5)
# Multiplicity
ax.text(6.5, 0.8, "Multiplicity shown near arrow ends (e.g. 1, 0..*, 1..*)",
        va='center', fontsize=7.5, color='#880E4F')
# Visibility
ax.text(0.3, 0.45, "+ public   - private   # protected",
        fontsize=7.5, fontfamily='monospace', color='#333')

plt.tight_layout(pad=0.5)
plt.savefig('/workspace/class_diagram.png', dpi=150, bbox_inches='tight',
            facecolor='#FAFAFA')
print("Class diagram saved.")
