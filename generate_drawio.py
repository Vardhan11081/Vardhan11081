"""
Generate draw.io (.drawio) XML files for:
  1. FreshBite Salads – Level 1 DFD
  2. FreshBite Salads – Class Diagram

Both files can be opened and edited in draw.io (app.diagrams.net).
"""
import xml.etree.ElementTree as ET

# ── XML builder helpers ───────────────────────────────────────────────────────
class DiagramBuilder:
    def __init__(self, page_w=1654, page_h=1169, title='Diagram'):
        self.eid = 2          # next cell id
        self.title = title
        self.page_w = page_w
        self.page_h = page_h
        self.model = ET.Element('mxGraphModel', {
            'dx': '1422', 'dy': '762', 'grid': '1', 'gridSize': '10',
            'guides': '1', 'tooltips': '1', 'connect': '1', 'arrows': '1',
            'fold': '1', 'page': '1', 'pageScale': '1',
            'pageWidth': str(page_w), 'pageHeight': str(page_h),
            'math': '0', 'shadow': '1'
        })
        self.root = ET.SubElement(self.model, 'root')
        ET.SubElement(self.root, 'mxCell', id='0')
        ET.SubElement(self.root, 'mxCell', id='1', parent='0')

    def _id(self):
        i = self.eid
        self.eid += 1
        return str(i)

    def vertex(self, label, style, x, y, w, h, parent='1', extra=None):
        cid = self._id()
        attrs = {'id': cid, 'value': label, 'style': style,
                 'vertex': '1', 'parent': parent}
        if extra:
            attrs.update(extra)
        c = ET.SubElement(self.root, 'mxCell', attrs)
        ET.SubElement(c, 'mxGeometry',
                      x=str(int(x)), y=str(int(y)),
                      width=str(int(w)), height=str(int(h)), **{'as': 'geometry'})
        return cid

    def edge(self, label, style, src, tgt, pts=None, parent='1'):
        cid = self._id()
        c = ET.SubElement(self.root, 'mxCell', {
            'id': cid, 'value': label, 'style': style,
            'edge': '1', 'source': str(src), 'target': str(tgt),
            'parent': parent
        })
        geo = ET.SubElement(c, 'mxGeometry', relative='1', **{'as': 'geometry'})
        if pts:
            arr = ET.SubElement(geo, 'Array', **{'as': 'points'})
            for px, py in pts:
                ET.SubElement(arr, 'mxPoint', x=str(int(px)), y=str(int(py)))
        return cid

    def to_xml(self):
        self._indent(self.model)
        return ('<?xml version="1.0" encoding="UTF-8"?>\n' +
                ET.tostring(self.model, encoding='unicode'))

    def _indent(self, elem, level=0):
        pad = '\n' + '  ' * level
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = pad + '  '
            if not elem.tail or not elem.tail.strip():
                elem.tail = pad
            for child in elem:
                self._indent(child, level + 1)
            if not child.tail or not child.tail.strip():
                child.tail = pad
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = pad


# ══════════════════════════════════════════════════════════════════════════════
#  DFD
# ══════════════════════════════════════════════════════════════════════════════
def build_dfd():
    S  = 58   # scale: units → pixels
    DH = 17   # diagram height in units

    def px(x): return x * S
    def py(y): return (DH - y) * S  # flip y (draw.io y=0 is top)

    # bounding box helpers
    def circle_bbox(cx, cy, r):
        return px(cx - r), py(cy + r), px(2*r), px(2*r)

    def rect_bbox(x1, y, w, h):
        return px(x1), py(y + h), px(w), py_h(h)

    def py_h(h): return h * S    # just scale height (no flip)

    d = DiagramBuilder(page_w=1540, page_h=1100, title='FreshBite DFD')

    # ── Styles ────────────────────────────────────────────────────────────────
    PROC = ('ellipse;whiteSpace=wrap;html=1;'
            'fillColor=#0a3055;strokeColor=#4a7aab;strokeWidth=2;'
            'fontColor=#ffffff;fontSize=10;fontStyle=1;')
    EXT  = ('rounded=0;whiteSpace=wrap;html=1;'
            'fillColor=#2e6b3e;strokeColor=#ffffff;strokeWidth=3;'
            'fontColor=#ffffff;fontSize=10;fontStyle=1;double=1;')
    DS   = ('rounded=0;whiteSpace=wrap;html=1;'
            'fillColor=#fff2cc;strokeColor=#d6b656;strokeWidth=2;'
            'fontSize=9;fontStyle=1;')
    BG   = ('rounded=0;whiteSpace=wrap;html=1;'
            'fillColor=#a8d8ea;strokeColor=none;fontSize=0;')
    ARR  = ('edgeStyle=orthogonalEdgeStyle;rounded=0;'
            'orthogonalLoop=1;jettySize=auto;html=1;fontSize=8;'
            'exitPerimeter=0;entryPerimeter=0;')
    ARR_OPEN = ARR + 'endArrow=open;endSize=10;'

    # Background
    d.vertex('', BG, 0, 0, px(24), py(0))

    # ── Process circles ───────────────────────────────────────────────────────
    PR = 1.18
    x, y, w, h = circle_bbox(5.5, 13.5, PR)
    P1 = d.vertex('1.0\nBrowse\nMenu', PROC, x, y, w, h)

    x, y, w, h = circle_bbox(14.5, 13.5, PR)
    P2 = d.vertex('2.0\nManage User\nAccount', PROC, x, y, w, h)

    x, y, w, h = circle_bbox(5.5, 9.0, PR)
    P3 = d.vertex('3.0\nManage\nShopping Cart', PROC, x, y, w, h)

    x, y, w, h = circle_bbox(12.5, 9.0, PR)
    P4 = d.vertex('4.0\nProcess\nCheckout', PROC, x, y, w, h)

    x, y, w, h = circle_bbox(6.5, 4.5, PR)
    P5 = d.vertex('5.0\nManage\nOrders', PROC, x, y, w, h)

    x, y, w, h = circle_bbox(14.5, 3.5, PR)
    P6 = d.vertex('6.0\nManage\nReward Points', PROC, x, y, w, h)

    # ── External entities ─────────────────────────────────────────────────────
    Cust = d.vertex('Customer', EXT,
                    px(1.5-1.2), py(9.0+1.1), px(2.4), py_h(2.2))
    ETop = d.vertex('Email\nService', EXT,
                    px(22.5-1.1), py(14.0+0.775), px(2.2), py_h(1.55))
    PGW  = d.vertex('Payment\nGateway', EXT,
                    px(22.5-1.1), py(9.0+0.9), px(2.2), py_h(1.8))
    EBot = d.vertex('Email\nService', EXT,
                    px(22.5-1.1), py(3.5+0.775), px(2.2), py_h(1.55))

    # ── Data stores ───────────────────────────────────────────────────────────
    DSH = 0.66
    D1x = 5.5 + PR + 0.25
    D1w = 14.5 - PR - 0.25 - D1x
    D1 = d.vertex('D1    Salad Database', DS,
                  px(D1x), py(13.5 + DSH/2), px(D1w), py_h(DSH))

    D2x = 14.5 + PR + 0.30
    D2 = d.vertex('D2    User Account Database', DS,
                  px(D2x), py(13.5 + 0.30 + DSH), px(4.8), py_h(DSH))

    D3x, D3y = 5.5 - 0.30, 7.0
    D3 = d.vertex('D3    Shopping Cart', DS,
                  px(D3x), py(D3y + DSH), px(4.5), py_h(DSH))

    D4x = 6.5 + PR + 0.30
    D4 = d.vertex('D4    Order Database', DS,
                  px(D4x), py(4.5 + DSH/2), px(4.7), py_h(DSH))

    D5x, D5y = 12.5 - 0.30, 9.0 - PR - 1.30
    D5 = d.vertex('D5    Address Database', DS,
                  px(D5x), py(D5y + DSH), px(4.5), py_h(DSH))

    # ── Arrows ────────────────────────────────────────────────────────────────
    # Customer → P1 via left margin
    d.edge('Browse Request', ARR_OPEN, Cust, P1,
           pts=[(px(3.0), py(9.5)), (px(3.0), py(13.65))])

    # P1 → Customer via left margin
    d.edge('Salad Details\n(name, ingredients,\nnutrition, allergens)',
           ARR_OPEN, P1, Cust,
           pts=[(px(2.6), py(13.35)), (px(2.6), py(9.8))])

    # Customer → P2 via top margin y=15.6
    d.edge('Registration Details /\nLogin Credentials',
           ARR_OPEN, Cust, P2,
           pts=[(px(1.2), py(15.6)), (px(14.2), py(15.6))])

    # P2 → Customer via top margin y=16.2
    d.edge('Account Confirmation /\nLogin Status',
           ARR_OPEN, P2, Cust,
           pts=[(px(14.8), py(16.2)), (px(0.9), py(16.2))])

    # Customer ↔ P3 horizontal
    d.edge('Add/Remove/\nUpdate Items', ARR_OPEN, Cust, P3)
    d.edge('Updated Cart\nContents', ARR_OPEN, P3, Cust)

    # P1 ↔ D1
    d.edge('Salad Info', ARR_OPEN, P1, D1)
    d.edge('', ARR_OPEN, D1, P1)

    # P2 ↔ D2
    d.edge('Store/Update\nUser Info', ARR_OPEN, P2, D2)
    d.edge('User Details /\nAccount Status', ARR_OPEN, D2, P2)

    # P2 ↔ Email top
    d.edge('Verification Email', ARR_OPEN, P2, ETop)
    d.edge('Verification Code\nResponse', ARR_OPEN, ETop, P2)

    # P2 → P4 via waypoint below P2 then across
    d.edge('User Authentication\nStatus', ARR_OPEN, P2, P4,
           pts=[(px(14.2), py(12.0)), (px(12.8), py(12.0))])

    # P3 ↔ D3 vertical
    d.edge('Store Cart Items', ARR_OPEN, P3, D3)
    d.edge('Cart Data', ARR_OPEN, D3, P3)

    # P3 → P4 horizontal
    d.edge('Delivery Address /\nPayment Details', ARR_OPEN, P3, P4)

    # P4 ↔ Payment Gateway
    d.edge('Payment Request', ARR_OPEN, P4, PGW)
    d.edge('Payment Confirmation /\nRejection', ARR_OPEN, PGW, P4)

    # P4 ↔ D5
    d.edge('Store Address', ARR_OPEN, P4, D5)
    d.edge('Saved Addresses', ARR_OPEN, D5, P4)

    # P4 → P5 via bend
    d.edge('Confirmed Payment /\nOrder Details', ARR_OPEN, P4, P5,
           pts=[(px(12.1), py(6.0)), (px(6.9), py(6.0))])

    # P5 ↔ D4
    d.edge('Store Order', ARR_OPEN, P5, D4)
    d.edge('Order Status', ARR_OPEN, D4, P5)

    # P5 → Email bot
    d.edge('Order Confirmation\nEmail', ARR_OPEN, P5, EBot)

    # P5 → Customer via left-bottom margin
    d.edge('Order Status Updates', ARR_OPEN, P5, Cust,
           pts=[(px(2.0), py(4.3)), (px(2.0), py(7.9))])

    # P5 → P6
    d.edge('Completed\nOrder Info', ARR_OPEN, P5, P6)

    # P6 → Email bot
    d.edge('Update Reward\nPoints', ARR_OPEN, P6, EBot)

    # P6 → Customer via bottom margin y=1.5
    d.edge('Points Balance /\nFree Salad Eligibility', ARR_OPEN, P6, Cust,
           pts=[(px(14.0), py(1.5)), (px(1.8), py(1.5))])

    # Title text
    d.vertex('<b>FreshBite Salads – Level 1 Data Flow Diagram</b>',
             'text;html=1;strokeColor=none;fillColor=none;'
             'align=center;verticalAlign=middle;whiteSpace=wrap;'
             'rounded=0;fontSize=14;fontStyle=1;fontColor=#0a2040;',
             px(4), py(16.95), px(16), py_h(0.5))

    return d


# ══════════════════════════════════════════════════════════════════════════════
#  CLASS DIAGRAM
# ══════════════════════════════════════════════════════════════════════════════
def build_class():
    """
    Uses draw.io swimlane cells for each UML class box.
    Row heights are computed from attribute/method counts.
    """
    d = DiagramBuilder(page_w=1400, page_h=1100, title='FreshBite Class Diagram')

    CW   = 245    # class box width
    LH   = 17     # line height (pixels) per attribute/method
    PAD  = 6      # top+bottom padding inside each section
    NH   = 25     # name header height
    HGAP = 55     # horizontal gap between classes in same row
    VGAP = 70     # vertical gap between rows

    HDR_STYLE = ('swimlane;fontStyle=1;align=center;startSize={nh};'
                 'fillColor=#c8d8f0;strokeColor=#222222;strokeWidth=1.6;'
                 'fontSize=10;fontColor=#0a2040;')
    TXT_STYLE = ('text;strokeColor=none;fillColor=none;align=left;'
                 'verticalAlign=top;spacingLeft=6;overflow=hidden;'
                 'rotatable=0;fontSize=9;fontFamily=Courier New;')
    DIV_STYLE = 'line;fillColor=none;strokeColor=#222222;strokeWidth=1.2;'
    INH_ARR  = ('edgeStyle=orthogonalEdgeStyle;rounded=0;'
                'orthogonalLoop=1;jettySize=auto;html=1;'
                'endArrow=block;endFill=0;startArrow=none;'
                'strokeWidth=1.6;fontSize=9;fontStyle=2;')
    ASC_ARR  = ('edgeStyle=orthogonalEdgeStyle;rounded=0;'
                'orthogonalLoop=1;jettySize=auto;html=1;'
                'endArrow=open;endSize=10;startArrow=none;'
                'strokeWidth=1.4;fontSize=9;fontStyle=2;')

    def class_box(name, attrs, methods, x, y):
        ah = len(attrs)  * LH + PAD
        mh = len(methods)* LH + PAD
        total = NH + ah + 2 + mh
        hs = HDR_STYLE.format(nh=NH)
        cid = d.vertex(name, hs, x, y, CW, total)
        # attributes text
        a_text = '\n'.join(attrs)
        d.vertex(a_text, TXT_STYLE, 0, NH, CW, ah, parent=cid)
        # divider
        d.vertex('', DIV_STYLE, 0, NH + ah, CW, 2, parent=cid)
        # methods text
        m_text = '\n'.join(methods)
        d.vertex(m_text, TXT_STYLE, 0, NH + ah + 2, CW, mh, parent=cid)
        return cid, total

    # ── Row 1 ──────────────────────────────────────────────────────────────────
    R1Y = 60

    user_id, user_h = class_box('User',
        ['-  userId: int', '-  username: String', '-  firstName: String',
         '-  lastName: String', '-  dateOfBirth: Date', '-  email: String',
         '-  password: String', '-  tax: double', '-  accountStatus: String',
         '-  failedLoginAttempts: int', '-  lastActivityDate: Date'],
        ['+  register(): void', '+  login(): void', '+  logout(): void',
         '+  verifyEmail(code: String): boolean',
         '+  reactivateAccount(): void', '+  updateProfile(): void'],
        30, R1Y)

    sal_x = 30 + CW + HGAP
    sal_id, sal_h = class_box('Salad',
        ['-  saladId: int', '-  name: String', '-  ingredients: String',
         '-  description: String', '-  allergenWarnings: String',
         '-  nutritionalInfo: String', '-  price: double',
         '-  portionSize: String'],
        ['+  getDetails(): void', '+  updatePrice(price: double): void',
         '+  getPrice(): double'],
        sal_x, R1Y)

    cus_x = sal_x + CW + HGAP
    cus_id, cus_h = class_box('CustomSalad',
        ['-  customIngredients: List\u003cString\u003e'],
        ['+  addIngredient(ingredient: String): void',
         '+  removeIngredient(ingredient: String): void',
         '+  calculatePrice(): double'],
        cus_x, R1Y)

    max_r1 = max(user_h, sal_h, cus_h)

    # ── Row 2 ──────────────────────────────────────────────────────────────────
    R2Y = R1Y + max_r1 + VGAP

    cart_x = 30 + CW//2
    cart_id, cart_h = class_box('ShoppingCart',
        ['-  cartId: int', '-  sessionId: String', '-  createdDate: Date'],
        ['+  addItem(item: CartItem): void', '+  removeItem(itemId): void',
         '+  updateQuantity(itemId, qty: int): void',
         '+  getTotal(): double', '+  clearCart(): void'],
        cart_x, R2Y)

    ci_x = cart_x + CW + HGAP
    ci_id, ci_h = class_box('CartItem',
        ['-  cartItemId: int', '-  quantity: int',
         '-  portionSize: String', '-  subtotal: double'],
        ['+  calculateSubtotal(): double',
         '+  updateQuantity(qty: int): void'],
        ci_x, R2Y)

    ver_x = ci_x + CW + HGAP
    ver_id, ver_h = class_box('Verification',
        ['-  verificationId: int', '-  verificationCode: String',
         '-  isVerified: boolean', '-  expiryDate: Date'],
        ['+  generateCode(): String',
         '+  sendVerificationEmail(): void',
         '+  verifyCode(code: String): boolean'],
        ver_x, R2Y)

    max_r2 = max(cart_h, ci_h, ver_h)

    # ── Row 3 ──────────────────────────────────────────────────────────────────
    R3Y = R2Y + max_r2 + VGAP

    ord_id, ord_h = class_box('Order',
        ['-  orderId: int', '-  orderDate: Date', '-  total: double',
         '-  tax: double', '-  deliveryCharge: double',
         '-  orderStatus: String'],
        ['+  createOrder(): void', '+  updateStatus(status: String): void',
         '+  calculateTotal(): double', '+  getOrderDetails(): String'],
        30, R3Y)

    pay_x = 30 + CW + HGAP
    pay_id, pay_h = class_box('Payment',
        ['-  paymentId: int', '-  amount: double',
         '-  paymentMethod: String', '-  paymentStatus: String',
         '-  transactionDate: Date'],
        ['+  processPayment(): boolean', '+  verifyPayment(): boolean',
         '+  getReceipt(): String'],
        pay_x, R3Y)

    adr_x = pay_x + CW + HGAP
    adr_id, adr_h = class_box('Address',
        ['-  addressId: int', '-  street: String', '-  city: String',
         '-  state: String', '-  postcode: String',
         '-  country: String', '-  addressType: String'],
        ['+  addAddress(): void', '+  validateAddress(): void',
         '+  deleteAddress(): void'],
        adr_x, R3Y)

    rwd_x = adr_x + CW + HGAP
    rwd_id, rwd_h = class_box('RewardPoints',
        ['-  points: int', '-  totalPoints: int',
         '-  isEligibleForFree: boolean'],
        ['+  addPoints(points: int): void',
         '+  redeemPoints(): void', '+  checkEligibility(): boolean'],
        rwd_x, R3Y)

    # ── Relationships ──────────────────────────────────────────────────────────
    # 1. CustomSalad --|> Salad  (inheritance)
    d.edge('', INH_ARR, cus_id, sal_id)

    # 2. User --places 1:0..* → ShoppingCart
    d.edge('places\n1      0..*', ASC_ARR, user_id, cart_id,
           pts=[(30 + CW//2, R2Y - 10)])

    # 3. User --requires 1:1 → Verification  (route right)
    d.edge('requires\n1          1', ASC_ARR, user_id, ver_id,
           pts=[(30 + CW + 5, R1Y + user_h//2),
                (ver_x + CW//2, R1Y + user_h//2)])

    # 4. User --earns 1:1 → RewardPoints  (right margin route)
    RX = rwd_x + CW + 20   # right margin x
    r1_mid_y = R1Y + user_h // 2
    r3_mid_y = R3Y + rwd_h // 2
    d.edge('earns\n1      1', ASC_ARR, user_id, rwd_id,
           pts=[(RX, r1_mid_y), (RX, r3_mid_y)])

    # 5. User --has 1:0..* → Address  (left margin route)
    LX = 10   # left margin x
    r3_adr_mid_y = R3Y + adr_h // 2
    d.edge('has\n1   0..*', ASC_ARR, user_id, adr_id,
           pts=[(LX, r1_mid_y), (LX, r3_adr_mid_y)])

    # 6. ShoppingCart --contains 1:0..* → CartItem  (horizontal)
    d.edge('contains\n1       0..*', ASC_ARR, cart_id, ci_id)

    # 7. CartItem --references 0..*:1 → Salad  (up from CartItem to Salad)
    ci_mid_x = ci_x + CW // 2
    sal_mid_x = sal_x + CW // 2
    d.edge('references\n0..*        1', ASC_ARR, ci_id, sal_id,
           pts=[(ci_mid_x, R1Y + sal_h + 20),
                (sal_mid_x, R1Y + sal_h + 20)])

    # 8. ShoppingCart --includes 1:1..* → Order  (down)
    d.edge('includes\n1      1..*', ASC_ARR, cart_id, ord_id,
           pts=[(cart_x + CW//2, R3Y - 10)])

    # 9. Order --paid by 1:1 → Payment  (horizontal)
    d.edge('paid by\n1         1', ASC_ARR, ord_id, pay_id)

    # 10. Order --delivered to 1:1 → Address  (via bottom)
    BOT_Y = R3Y + max(ord_h, pay_h, adr_h) + 30
    d.edge('delivered to\n1             1', ASC_ARR, ord_id, adr_id,
           pts=[(30 + CW//2, BOT_Y), (adr_x + CW//2, BOT_Y)])

    # Title
    d.vertex('<b>6.2  Class Diagram – FreshBite Salads</b>',
             'text;html=1;strokeColor=none;fillColor=none;align=center;'
             'verticalAlign=middle;whiteSpace=wrap;rounded=0;'
             'fontSize=14;fontStyle=1;fontColor=#0a2040;',
             30, 10, rwd_x + CW - 30, 40)

    return d


# ── Write files ───────────────────────────────────────────────────────────────
dfd_d = build_dfd()
with open('/workspace/output/FreshBite_DFD.drawio', 'w', encoding='utf-8') as f:
    f.write(dfd_d.to_xml())
print("DFD .drawio saved.")

cls_d = build_class()
with open('/workspace/output/FreshBite_ClassDiagram.drawio', 'w', encoding='utf-8') as f:
    f.write(cls_d.to_xml())
print("Class diagram .drawio saved.")
