import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

# ═══════════════════════════════════════════════════════════════
# DIAGRAM 1 – Three-Layer vs Client/Server Architecture
# ═══════════════════════════════════════════════════════════════
def make_architecture_comparison():
    fig, axes = plt.subplots(1, 2, figsize=(14, 8))
    fig.patch.set_facecolor('#f0f4f8')
    fig.suptitle('Client/Server Architecture vs Three-Layer Architecture',
                 fontsize=12, fontweight='bold', y=0.98)

    def box(ax, x, y, w, h, text, fc, ec, fs=9):
        ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h,
                                   boxstyle='round,pad=0.12', lw=1.8,
                                   edgecolor=ec, facecolor=fc, zorder=5))
        ax.text(x, y, text, ha='center', va='center', fontsize=fs,
                fontweight='bold', zorder=6, multialignment='center', color=ec)

    def arr(ax, x1, y1, x2, y2, lbl='', color='#475569', lox=0.2):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='<->', color=color, lw=1.5), zorder=4)
        if lbl:
            ax.text((x1+x2)/2 + lox, (y1+y2)/2, lbl, ha='left', va='center',
                    fontsize=7.8, color=color, style='italic')

    # ── Left: Client/Server ──────────────────────────────────
    ax = axes[0]
    ax.set_xlim(0, 6); ax.set_ylim(0, 8); ax.axis('off')
    ax.set_title('Client / Server (Two-Tier)', fontsize=11,
                 fontweight='bold', color='#1a4a7a', pad=6)

    # Client tier
    ax.add_patch(FancyBboxPatch((0.3, 5.2), 5.4, 2.3,
                               boxstyle='round,pad=0.1', lw=1.6,
                               edgecolor='#2C6FAC', facecolor='#dbeafe', zorder=3))
    ax.text(3.0, 7.1, 'CLIENT TIER', ha='center', fontsize=9,
            fontweight='bold', color='#1a4a7a')
    box(ax, 1.5, 6.2, 2.0, 0.9, 'Presentation\nLogic', '#bfdbfe', '#1a4a7a', 8.5)
    box(ax, 4.5, 6.2, 2.0, 0.9, 'Business\nLogic', '#bfdbfe', '#1a4a7a', 8.5)
    ax.text(3.0, 5.55, 'Desktop / Laptop / Thick Client', ha='center',
            fontsize=7.5, color='#475569', style='italic')

    arr(ax, 3.0, 5.2, 3.0, 3.9, 'SQL queries /\nresults', '#475569', 0.12)

    # Server tier
    ax.add_patch(FancyBboxPatch((0.3, 1.8), 5.4, 1.9,
                               boxstyle='round,pad=0.1', lw=1.6,
                               edgecolor='#166534', facecolor='#dcfce7', zorder=3))
    ax.text(3.0, 3.45, 'SERVER TIER', ha='center', fontsize=9,
            fontweight='bold', color='#166534')
    box(ax, 3.0, 2.6, 3.5, 0.85, 'Database Server\n(Data Storage)', '#bbf7d0', '#166534', 8.5)
    ax.text(3.0, 2.05, 'Database Server', ha='center', fontsize=7.5,
            color='#475569', style='italic')

    ax.text(3.0, 1.2,
            '- Business logic lives on client (fat client)\n'
            '- Direct DB connection from client\n'
            '- Hard to scale; security risk',
            ha='center', fontsize=8, color='#991b1b',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fee2e2',
                      edgecolor='#991b1b', lw=1))

    # ── Right: Three-Layer ───────────────────────────────────
    ax = axes[1]
    ax.set_xlim(0, 6); ax.set_ylim(0, 8); ax.axis('off')
    ax.set_title('Three-Layer Architecture (Three-Tier)', fontsize=11,
                 fontweight='bold', color='#1a4a7a', pad=6)

    layers = [
        (6.5, 7.3, '#dbeafe', '#1a4a7a', 'PRESENTATION LAYER (Tier 1)',
         'Browser / Mobile App / Thin Client', 'Web browser, React app, iOS app'),
        (4.5, 5.4, '#fef9c3', '#854d0e', 'BUSINESS LOGIC LAYER (Tier 2)',
         'Application / Web Server', 'Node.js, Java EE, .NET, Python Flask'),
        (2.5, 3.5, '#dcfce7', '#166534', 'DATA LAYER (Tier 3)',
         'Database Server', 'PostgreSQL, MySQL, Oracle, MongoDB'),
    ]

    for top_y, label_y, fc, ec, title, device, example in layers:
        ax.add_patch(FancyBboxPatch((0.3, top_y - 1.6), 5.4, 1.5,
                                   boxstyle='round,pad=0.1', lw=1.8,
                                   edgecolor=ec, facecolor=fc, zorder=3))
        ax.text(3.0, top_y - 0.4, title, ha='center', fontsize=8.5,
                fontweight='bold', color=ec)
        ax.text(3.0, top_y - 0.9, device, ha='center', fontsize=7.8,
                color='#374151', style='italic')
        ax.text(3.0, top_y - 1.3, f'e.g. {example}', ha='center',
                fontsize=7.3, color='#6b7280')

    # Arrows
    arr(ax, 3.0, 5.9, 3.0, 5.1, 'HTTP requests /\nJSON responses', '#854d0e', 0.12)
    arr(ax, 3.0, 3.95, 3.0, 3.15, 'SQL queries /\nresults', '#166534', 0.12)

    ax.text(3.0, 1.6,
            '+ Business logic isolated on app server\n'
            '+ Thin client; easy to scale each tier\n'
            '+ Database never directly exposed',
            ha='center', fontsize=8, color='#166534',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#dcfce7',
                      edgecolor='#166534', lw=1))

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    path = '/workspace/lab8_architecture.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Architecture diagram saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# DIAGRAM 2 – Technology vs Application Architecture
# ═══════════════════════════════════════════════════════════════
def make_arch_overview():
    fig, ax = plt.subplots(figsize=(13, 6))
    fig.patch.set_facecolor('#f0f4f8')
    ax.set_xlim(0, 13); ax.set_ylim(0, 6); ax.axis('off')
    ax.set_title('Technology Architecture vs Application Architecture – Relationship',
                 fontsize=12, fontweight='bold', pad=8)

    # Technology Architecture box (left)
    ax.add_patch(FancyBboxPatch((0.3, 0.4), 5.5, 5.0,
                               boxstyle='round,pad=0.15', lw=2,
                               edgecolor='#1a4a7a', facecolor='#dbeafe', zorder=3))
    ax.text(3.05, 5.1, 'TECHNOLOGY ARCHITECTURE', ha='center',
            fontsize=10, fontweight='bold', color='#1a4a7a')
    ax.text(3.05, 4.65, '"The physical and infrastructure foundation"',
            ha='center', fontsize=8, color='#334155', style='italic')

    tech_items = [
        'Hardware (servers, devices, sensors)',
        'Network (LAN, WAN, cloud, CDN)',
        'Operating systems & virtualisation',
        'DBMS platforms (PostgreSQL, Oracle)',
        'Middleware & integration platforms',
        'Security infrastructure (firewalls, TLS)',
    ]
    for i, item in enumerate(tech_items):
        ax.text(0.7, 4.1 - i*0.55, f'  {item}', ha='left', va='center',
                fontsize=8.5, color='#1e3a5f')

    # Application Architecture box (right)
    ax.add_patch(FancyBboxPatch((7.2, 0.4), 5.5, 5.0,
                               boxstyle='round,pad=0.15', lw=2,
                               edgecolor='#166534', facecolor='#dcfce7', zorder=3))
    ax.text(9.95, 5.1, 'APPLICATION ARCHITECTURE', ha='center',
            fontsize=10, fontweight='bold', color='#166534')
    ax.text(9.95, 4.65, '"The logical software structure"',
            ha='center', fontsize=8, color='#374151', style='italic')

    app_items = [
        'Software tiers (presentation, logic, data)',
        'Application components & modules',
        'APIs and web services',
        'Design patterns (MVC, microservices)',
        'UI / UX structure',
        'Business rules & workflows',
    ]
    for i, item in enumerate(app_items):
        ax.text(7.5, 4.1 - i*0.55, f'  {item}', ha='left', va='center',
                fontsize=8.5, color='#14532d')

    # Interdependence arrow
    ax.annotate('', xy=(7.1, 2.9), xytext=(5.9, 2.9),
                arrowprops=dict(arrowstyle='<->', color='#7c3aed', lw=2.2), zorder=5)
    ax.text(6.5, 3.25, 'Interdependent', ha='center', fontsize=8.5,
            fontweight='bold', color='#7c3aed')
    ax.text(6.5, 2.6, 'App architecture\nmust run ON tech\narchitecture',
            ha='center', fontsize=7.5, color='#6b21a8', multialignment='center')

    plt.tight_layout()
    path = '/workspace/lab8_arch_overview.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Arch overview saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# DIAGRAM 3 – Web Protocols stack
# ═══════════════════════════════════════════════════════════════
def make_protocols():
    fig, ax = plt.subplots(figsize=(11, 6))
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_xlim(0, 11); ax.set_ylim(0, 6); ax.axis('off')
    ax.set_title('Common Web Protocols – Stack Overview', fontsize=12,
                 fontweight='bold', pad=8)

    protocols = [
        (5.5, 5.2, 10.0, 0.75, 'APPLICATION LAYER',
         'HTTP/HTTPS · REST · SOAP · FTP · SMTP · WebSocket · GraphQL',
         '#dbeafe', '#1a4a7a'),
        (5.5, 4.1, 10.0, 0.75, 'SESSION / TRANSPORT LAYER',
         'TLS/SSL (encryption) · TCP (reliable) · UDP (fast, lossy)',
         '#dcfce7', '#166534'),
        (5.5, 3.0, 10.0, 0.75, 'NETWORK LAYER',
         'IP (IPv4 / IPv6) · DNS · DHCP · ICMP',
         '#fef9c3', '#854d0e'),
        (5.5, 1.9, 10.0, 0.75, 'LINK / PHYSICAL LAYER',
         'Ethernet · Wi-Fi (802.11) · Bluetooth · Fibre · LTE/5G',
         '#f3e8ff', '#6b21a8'),
    ]

    for x, y, w, h, layer, protos, fc, ec in protocols:
        ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
                                   boxstyle='round,pad=0.1', lw=1.8,
                                   edgecolor=ec, facecolor=fc, zorder=4))
        ax.text(x, y+0.17, layer, ha='center', va='center',
                fontsize=9, fontweight='bold', color=ec, zorder=5)
        ax.text(x, y-0.18, protos, ha='center', va='center',
                fontsize=8.2, color='#374151', zorder=5)

    # Side arrows
    for y in [3.55, 2.45, 1.34]:
        ax.annotate('', xy=(5.5, y+0.2), xytext=(5.5, y),
                    arrowprops=dict(arrowstyle='->', color='#64748b', lw=1.3))

    # Labels on right
    ax.text(10.8, 5.2, 'User-facing', ha='left', va='center',
            fontsize=8, color='#1a4a7a', style='italic')
    ax.text(10.8, 1.9, 'Physical', ha='left', va='center',
            fontsize=8, color='#6b21a8', style='italic')

    # Highlight box for key web protocols
    ax.add_patch(FancyBboxPatch((0.3, 0.2), 3.2, 1.2,
                               boxstyle='round,pad=0.1', lw=1.4,
                               edgecolor='#1a4a7a', facecolor='#e0f2fe'))
    ax.text(1.9, 1.0, 'Key for web apps:', ha='center', fontsize=8.5,
            fontweight='bold', color='#1a4a7a')
    ax.text(1.9, 0.6, 'HTTPS · TLS · REST/SOAP\nDNS · TCP/IP',
            ha='center', fontsize=8, color='#0c4a6e', multialignment='center')

    plt.tight_layout()
    path = '/workspace/lab8_protocols.png'
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Protocols diagram saved: {path}')
    return path


# ═══════════════════════════════════════════════════════════════
# Build diagrams
# ═══════════════════════════════════════════════════════════════
arch_ov_path = make_arch_overview()
arch_path    = make_architecture_comparison()
proto_path   = make_protocols()


# ═══════════════════════════════════════════════════════════════
# BUILD WORD DOCUMENT
# ═══════════════════════════════════════════════════════════════
doc = Document()

def H(doc, text, level=2):
    p = doc.add_heading(text, level=level)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    return p

def B(doc, text, size=11):
    p = doc.add_paragraph(text)
    p.style.font.size = Pt(size)
    return p

def BU(doc, text, size=11):
    p = doc.add_paragraph(text, style='List Bullet')
    p.style.font.size = Pt(size)
    return p

def BB(doc, bold_part, rest, size=11):
    p = doc.add_paragraph()
    r = p.add_run(bold_part); r.bold = True; r.font.size = Pt(size)
    p.add_run(rest).font.size = Pt(size)
    return p

def SP(doc): doc.add_paragraph()

def tbl(doc, rows_data, headers):
    t = doc.add_table(rows=len(rows_data)+1, cols=len(headers))
    t.style = 'Table Grid'
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]; c.text = h
        for run in c.paragraphs[0].runs:
            run.bold = True; run.font.size = Pt(9.5)
    for ri, row in enumerate(rows_data, 1):
        for ci, val in enumerate(row):
            c = t.rows[ri].cells[ci]; c.text = val
            for run in c.paragraphs[0].runs:
                run.font.size = Pt(9.5)
    return t

# ── Title ──────────────────────────────────────────────────
t = doc.add_heading('BN314 – System Architecture', 0)
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
s = doc.add_heading('Lecture 8: Defining System Architecture – Laboratory Activity', 1)
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)

# ════════════════════════════════════════════════════════
# Q1
# ════════════════════════════════════════════════════════
H(doc, 'Question 1: Technology Architecture vs Application Architecture')
BB(doc, 'Technology Architecture: ',
   'Defines the physical and infrastructure foundation of the system — the hardware, '
   'network, operating systems, DBMS platforms, cloud services, and middleware '
   'that the system runs on. It answers "What platform and infrastructure will the system use?"')
BB(doc, 'Application Architecture: ',
   'Defines the logical structure of the software — how application components, tiers, '
   'modules, APIs, and design patterns are organised and interact. It answers '
   '"How is the software structured and how do its parts communicate?"')
SP(doc)
tbl(doc, [
    ('Focus',          'Physical/infrastructure layer — hardware, OS, network, cloud.',
                       'Logical/software layer — components, tiers, patterns, APIs.'),
    ('Designed by',    'Infrastructure and network architects.',
                       'Software/application architects and systems analysts.'),
    ('Examples',       'AWS EC2 servers, PostgreSQL on Linux, Azure VNet, TLS certificates.',
                       'MVC pattern, REST API, three-layer architecture, microservices.'),
    ('Key concern',    'Availability, scalability, performance, and physical security.',
                       'Modularity, maintainability, reusability, and business logic separation.'),
], ['Aspect', 'Technology Architecture', 'Application Architecture'])
SP(doc)
B(doc, 'Interdependence: Application architecture must be designed to run on the '
       'available technology architecture. If the tech architecture uses cloud containers '
       '(e.g., Kubernetes), the application must be designed as stateless, containerisable '
       'components. Conversely, technology choices are constrained by what the '
       'application architecture requires — a microservices architecture demands a '
       'different infrastructure than a monolith. Neither can be designed in isolation.')
doc.add_picture(arch_ov_path, width=Inches(6.2))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)

# ════════════════════════════════════════════════════════
# Q2
# ════════════════════════════════════════════════════════
H(doc, 'Question 2: Application Software vs System Software')
tbl(doc, [
    ('Definition',
     'Software that performs specific tasks for end users, directly supporting business processes or personal productivity.',
     'Software that manages and controls hardware resources, providing a platform for application software to run.'),
    ('Primary user',
     'End users (students, staff, customers).',
     'Computers/hardware and application software (not usually the end user directly).'),
    ('Purpose',
     'Solve a specific business or personal problem.',
     'Manage hardware, memory, processes, security, and provide services to other software.'),
    ('Examples',
     'Microsoft Word, Canvas LMS, Xero (accounting), Salesforce CRM, Chrome browser, TechNova client portal.',
     'Windows 11, Linux (Ubuntu), macOS, PostgreSQL DBMS, Apache web server, VMware hypervisor, Android OS.'),
    ('Dependency',
     'Depends on system software to run.',
     'Runs directly on hardware (or firmware).'),
], ['Aspect', 'Application Software', 'System Software'])
SP(doc)

# ════════════════════════════════════════════════════════
# Q3
# ════════════════════════════════════════════════════════
H(doc, 'Question 3: Native App vs Web-Based Application – Which Is More Secure?')
B(doc, 'Native (installed) apps are generally considered more secure than web-based '
       'applications, though the answer is nuanced and depends on implementation quality.')
SP(doc)
tbl(doc, [
    ('Attack surface',
     'Smaller — runs locally; not exposed to the internet by default; no browser intermediary.',
     'Larger — always internet-facing; exposed to XSS, SQL injection, CSRF, and man-in-the-middle attacks.'),
    ('Data storage',
     'Can store sensitive data locally in encrypted form without transmitting it.',
     'Data transmitted to/from server over the network; dependent on TLS for encryption.'),
    ('Code exposure',
     'Compiled binary; harder to reverse-engineer.',
     'HTML/JavaScript often visible in browser; logic exposure risk.'),
    ('Update control',
     'Updates must be installed by user; old vulnerable versions persist.',
     'Always runs latest server-side version; easier to patch centrally.'),
    ('Authentication',
     'Can use OS-level biometrics, keychain, and device-bound credentials.',
     'Relies on browser cookie/session management; CSRF and session hijacking risks.'),
], ['Security Factor', 'Native App', 'Web-Based App'])
SP(doc)
B(doc, 'Conclusion: Native apps have a smaller attack surface, but poorly coded native '
       'apps can still be highly insecure. Modern web apps with HTTPS, CSP headers, '
       'proper authentication (OAuth2/MFA), and input validation can achieve very high '
       'security. The implementation quality matters more than the type.')
SP(doc)

# ════════════════════════════════════════════════════════
# Q4
# ════════════════════════════════════════════════════════
H(doc, 'Question 4: Embedded Software on Smartphones and Its Benefits')
B(doc, 'Three types of embedded software on a typical smartphone:')
BB(doc, '1. Firmware / Bootloader: ',
   'Low-level software (e.g., Qualcomm Snapdragon firmware) burned into hardware chips '
   'that initialises the device hardware and loads the operating system at startup.')
BB(doc, '2. Baseband Processor Software: ',
   'Embedded software that manages all cellular radio communications (4G/5G, voice calls, '
   'SMS) independently of the main application processor, handling modem protocols.')
BB(doc, '3. Sensor Drivers / Hardware Abstraction Layer (HAL): ',
   'Embedded software that provides standardised interfaces to hardware components such '
   'as the GPS module, accelerometer, fingerprint sensor, camera ISP, and NFC chip.')
SP(doc)
BB(doc, 'Benefit to application software developers: ',
   'Embedded software abstracts hardware complexity through standardised APIs. '
   'An app developer calls camera.takePicture() without writing a single line of '
   'hardware-level code. This dramatically reduces development time, improves portability '
   'across device models, and allows app developers to focus entirely on business logic '
   'and user experience rather than hardware management.')
SP(doc)

# ════════════════════════════════════════════════════════
# Q5
# ════════════════════════════════════════════════════════
H(doc, 'Question 5: Role of Protocols in Modern Software and Systems')
B(doc, 'A protocol is a set of standardised rules and conventions that define how data '
       'is formatted, transmitted, received, and acknowledged between two or more systems '
       'or software components. Protocols ensure that different systems — regardless of '
       'vendor, language, or platform — can communicate reliably and consistently.')
SP(doc)
B(doc, 'Roles protocols play:')
BU(doc, 'Interoperability: protocols allow systems from different vendors and platforms '
        'to exchange data (e.g., a Python backend communicating with a JavaScript frontend via HTTP/JSON).')
BU(doc, 'Reliability: protocols like TCP define error detection, retransmission, and '
        'sequencing to ensure data arrives complete and in order.')
BU(doc, 'Security: protocols like TLS/SSL encrypt data in transit, preventing eavesdropping '
        'and tampering between client and server.')
BU(doc, 'Standardisation: agreed protocols allow developers to build on existing infrastructure '
        'without reinventing communication mechanisms.')
BU(doc, 'Integration: web service protocols (REST, SOAP, GraphQL) allow application components '
        'and third-party services to integrate across organisational and geographic boundaries.')
SP(doc)

# ════════════════════════════════════════════════════════
# Q6
# ════════════════════════════════════════════════════════
H(doc, 'Question 6: Three Commonly Used Web Protocols')
doc.add_picture(proto_path, width=Inches(6.2))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)
tbl(doc, [
    ('HTTP / HTTPS\n(HyperText Transfer\nProtocol Secure)',
     'Application layer',
     'The foundation protocol of the World Wide Web. Defines how web clients (browsers) '
     'request resources and how servers respond. HTTPS adds TLS/SSL encryption, making '
     'all communication confidential and authenticated. Every web page load, API call, '
     'and form submission uses HTTP/HTTPS.',
     'GET /students HTTP/1.1 (browser requests student list)\nHTTPS encrypts the response'),
    ('TLS / SSL\n(Transport Layer\nSecurity)',
     'Session / Transport',
     'Provides encryption, authentication, and data integrity for any TCP-based protocol. '
     'Uses digital certificates and asymmetric key exchange to establish a secure session, '
     'then switches to symmetric encryption for speed. Protects HTTPS, email (SMTPS), and '
     'database connections.',
     'TLS 1.3 handshake establishes encrypted HTTPS session between browser and bank'),
    ('REST\n(Representational\nState Transfer)',
     'Application (architectural style over HTTP)',
     'An architectural style for designing web APIs using standard HTTP methods '
     '(GET, POST, PUT, DELETE, PATCH). Resources are addressed by URLs; data is '
     'typically exchanged as JSON. REST is stateless, scalable, and the dominant '
     'pattern for modern web and mobile APIs.',
     'GET /api/courses/BN314 returns course details as JSON'),
    ('WebSocket',
     'Application layer',
     'A full-duplex, persistent communication protocol over a single TCP connection. '
     'Unlike HTTP (request-response), WebSocket allows the server to push data to the '
     'client at any time without a new request, enabling real-time features.',
     'Live chat, stock tickers, multiplayer games, real-time dashboards'),
], ['Protocol', 'Layer', 'Description', 'Example Use'])
SP(doc)

# ════════════════════════════════════════════════════════
# Q7
# ════════════════════════════════════════════════════════
H(doc, 'Question 7: Software as a Service (SaaS)')
BB(doc, 'Software as a Service (SaaS): ',
   'A cloud delivery model in which software applications are hosted by a provider '
   'and delivered to users over the internet via a browser or thin client — without '
   'installation, local hardware requirements, or manual updates. Examples: '
   'Microsoft 365, Salesforce, Canvas LMS, Xero, Google Workspace, Zoom.')
SP(doc)
tbl(doc, [
    ('Installation',  'None — accessed via browser or lightweight client.',
                      'Installed locally on each device; version management required.'),
    ('Updates',       'Automatic, centrally managed by provider; users always have latest version.',
                      'Must be installed manually or via IT deployment tools per device.'),
    ('Data storage',  'Data stored on provider\'s cloud infrastructure.',
                      'Data stored locally or on organisation\'s own servers.'),
    ('Scalability',   'Scales elastically; add/remove users via subscription.',
                      'Limited by local hardware; additional licenses and installs needed.'),
    ('Accessibility', 'Accessible from any device with internet; device-independent.',
                      'Tied to the device where installed (unless using VDI/RDS).'),
    ('Cost model',    'Subscription (per user/month); operational expenditure (OpEx).',
                      'Licence purchase + IT support; capital expenditure (CapEx).'),
    ('Customisation', 'Limited to provider-exposed configuration options.',
                      'Full control over configuration, plugins, and integration.'),
], ['Feature', 'SaaS', 'Locally Installed Application'])
SP(doc)

# ════════════════════════════════════════════════════════
# Q8
# ════════════════════════════════════════════════════════
H(doc, 'Question 8: Web Services in Modern Application Design')
BB(doc, 'Why web services are important: ',
   'Web services expose reusable, standardised functionality over the internet via '
   'protocols (REST, SOAP, GraphQL), allowing different applications — regardless of '
   'platform or language — to integrate and share capabilities. They enable:')
BU(doc, 'Modularity and reuse: common functions (payment, authentication, mapping, '
        'notifications) are consumed as services rather than built from scratch.')
BU(doc, 'System integration: organisations connect ERP, CRM, LMS, and HR systems '
        'through web service APIs without custom point-to-point integrations.')
BU(doc, 'Third-party capability: platforms like Stripe (payments), Twilio (SMS/voice), '
        'Google Maps (geolocation), and AWS Rekognition (AI) are consumed as web services.')
BU(doc, 'Microservices architecture: modern systems decompose into small, independently '
        'deployable web services, each responsible for one bounded context.')
SP(doc)
B(doc, 'Decisions a system designer must make regarding web services:')
BU(doc, 'Build vs buy: should this capability be built in-house or consumed from a third-party API?')
BU(doc, 'Protocol choice: REST vs SOAP vs GraphQL — based on payload size, tooling, and client needs.')
BU(doc, 'Authentication/authorisation: how will API access be secured (OAuth2, API keys, JWT)?')
BU(doc, 'Service level and reliability: what uptime guarantees does the provider offer? What is the fallback if the service is unavailable?')
BU(doc, 'Data residency and privacy: does using an external service comply with data sovereignty laws (GDPR, Privacy Act)?')
SP(doc)

# ════════════════════════════════════════════════════════
# Q9
# ════════════════════════════════════════════════════════
H(doc, 'Question 9: Three-Layer Architecture vs Client/Server Architecture')
doc.add_picture(arch_path, width=Inches(6.3))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
SP(doc)
tbl(doc, [
    ('Number of tiers', 'Two — client and server.', 'Three — presentation, logic, data.'),
    ('Business logic location',
     'Often on the client (fat client), or split ambiguously.',
     'Isolated on the dedicated application/logic server — never on the client.'),
    ('Client type', 'Thick/fat client with significant processing.',
                    'Thin client (browser or lightweight app); minimal processing.'),
    ('Database access',
     'Client connects directly to the database server.',
     'Client never touches the database; only the logic layer does.'),
    ('Scalability',
     'Difficult — client upgrades required; DB server becomes a bottleneck.',
     'Each tier scaled independently; horizontal scaling of app servers is easy.'),
    ('Security',
     'DB credentials often on the client; larger attack surface.',
     'Database is never directly exposed; all access mediated by logic layer.'),
    ('Similarity',
     'Both use a separation of concerns: frontend vs backend.',
     'Both separate the user interface from data storage.'),
], ['Aspect', 'Client/Server (2-Tier)', 'Three-Layer (3-Tier)'])
SP(doc)

# ════════════════════════════════════════════════════════
# Q10
# ════════════════════════════════════════════════════════
H(doc, 'Question 10: Layers of Three-Layer Architecture')
tbl(doc, [
    ('Layer 1\nPresentation Layer\n(View)',
     'Handles all user interaction — displays information, captures input, and sends requests to the logic layer. Contains no business logic or data access code.',
     'Web browser, mobile app (iOS/Android), desktop GUI.',
     'Client device: user\'s browser, smartphone, or desktop.'),
    ('Layer 2\nBusiness Logic Layer\n(Application / Controller)',
     'Implements all business rules, workflows, calculations, and decision logic. Acts as the intermediary between the presentation and data layers; validates input, applies rules, and orchestrates responses.',
     'Node.js / Express, Java Spring Boot, Python Django, .NET Core, PHP Laravel.',
     'Application server / web server in the data centre or cloud.'),
    ('Layer 3\nData Layer\n(Model / Repository)',
     'Manages persistent data storage and retrieval. Handles all CRUD operations (Create, Read, Update, Delete) and enforces data integrity at the database level.',
     'PostgreSQL, MySQL, Oracle DB, MongoDB, Redis, Microsoft SQL Server.',
     'Dedicated database server (on-premise or cloud-managed DB service like AWS RDS).'),
], ['Layer', 'Function', 'Technology Examples', 'Deployment Device'])
SP(doc)

# ════════════════════════════════════════════════════════
# Q11
# ════════════════════════════════════════════════════════
H(doc, 'Question 11: Interoperability – Why It Is Important')
BB(doc, 'Interoperability: ',
   'The ability of different systems, applications, or components — built on different '
   'platforms, by different vendors, or in different programming languages — to exchange '
   'information and work together effectively.')
SP(doc)
B(doc, 'Why it is critical in modern systems:')
BU(doc, 'No organisation operates in isolation: modern IT ecosystems involve ERP, CRM, '
        'LMS, HR, payroll, banking, and cloud services from multiple vendors. All must '
        'exchange data seamlessly.')
BU(doc, 'Legacy system integration: most organisations have existing systems that cannot '
        'be replaced. New systems must interoperate with legacy infrastructure.')
BU(doc, 'Partner and customer integration: B2B supply chains, government data exchanges, '
        'and customer-facing APIs all require standardised, interoperable interfaces.')
BU(doc, 'Platform diversity: users access systems from Windows, macOS, iOS, Android, and '
        'Linux. Web-based, interoperable applications work across all platforms.')
BU(doc, 'Avoiding vendor lock-in: systems designed with open, interoperable standards '
        '(REST, JSON, OAuth2) can switch components without complete rewrites.')
BU(doc, 'Regulatory requirements: healthcare (HL7/FHIR), finance (ISO 20022), and '
        'government (GovTech interoperability frameworks) mandate standardised data exchange.')
SP(doc)

# ════════════════════════════════════════════════════════
# Q12
# ════════════════════════════════════════════════════════
H(doc, 'Question 12: Three Common Types of Architectural Diagrams')
tbl(doc, [
    ('Network / Infrastructure\nDiagram',
     'Shows the physical and logical arrangement of hardware, servers, network devices '
     '(routers, firewalls, switches), communication links, and cloud services. Defines '
     'zones (DMZ, internal, cloud) and connectivity.',
     'Used by infrastructure architects, network engineers, and security teams to plan '
     'deployment, configure firewalls, and document the physical environment.'),
    ('UML Deployment Diagram',
     'A UML diagram that shows how software components (artifacts) are deployed onto '
     'hardware nodes (servers, devices, containers). Shows which node hosts which '
     'component and how nodes communicate.',
     'Used by solution architects and developers to plan and document how the application '
     'is distributed across physical and virtual infrastructure.'),
    ('Application / Component Diagram\n(UML Component Diagram)',
     'Shows the logical software components, their provided/required interfaces, and '
     'the dependencies between them. Does not show hardware — focuses on how software '
     'modules and services are structured and connected.',
     'Used during application architecture design to define component boundaries, APIs, '
     'and service contracts before implementation begins.'),
], ['Diagram Type', 'Description', 'Purpose / Audience'])
SP(doc)

# ════════════════════════════════════════════════════════
# Q13
# ════════════════════════════════════════════════════════
H(doc, 'Question 13: Key Questions When Describing the System Environment')
B(doc, 'When documenting the environment, a system designer should ask and answer '
       'the following questions:')
SP(doc)
env_qs = [
    ('What hardware will the system run on?',
     'Identify server specifications, client device types, storage capacity, and peripherals.'),
    ('What is the network topology and bandwidth?',
     'Define LAN/WAN/cloud connectivity, expected traffic volumes, latency requirements, and CDN needs.'),
    ('What operating system and platform is required?',
     'Specify OS versions, DBMS, web server, application server, and any required middleware.'),
    ('What is the hosting model?',
     'On-premise, cloud (IaaS/PaaS/SaaS), hybrid — and which cloud provider(s) and regions?'),
    ('What are the performance and availability requirements?',
     'Define uptime SLA (e.g., 99.9%), response time targets, disaster recovery RTO/RPO.'),
    ('What security infrastructure is in place?',
     'Identify existing firewalls, IDS/IPS, VPN, TLS certificates, and compliance requirements (ISO 27001, PCI-DSS).'),
    ('What existing systems must the new system integrate with?',
     'Identify legacy systems, third-party APIs, and data exchange formats.'),
    ('What are the constraints (budget, technology standards)?',
     'Organisation-mandated technology standards, approved vendor lists, and budget ceiling.'),
]
for q, a in env_qs:
    BB(doc, f'Q: {q} ', f'\nA: {a}')
SP(doc)

# ════════════════════════════════════════════════════════
# Q14
# ════════════════════════════════════════════════════════
H(doc, 'Question 14: How Use Cases Guide Application Component Design')
B(doc, 'Use cases and their related artefacts directly drive the identification, '
       'scoping, and design of application components in the following ways:')
SP(doc)
BU(doc,
   'Identifying components: each use case represents a distinct system function '
   '(e.g., "Register for Course", "Process Payment", "Generate Report"). Each function '
   'typically maps to one or more application components (controllers, services, handlers). '
   'The set of use cases defines the complete set of required components.')
BU(doc,
   'Defining component interfaces: a use case description lists the system messages '
   '(from the SSD) that the system must handle. Each system message becomes a method '
   'in an application component\'s public interface (e.g., registerStudent(sid, cid), '
   'processPayment(amount, card)).')
BU(doc,
   'Identifying required data: the data flows in use cases (inputs and outputs) identify '
   'what data each component must read from and write to the data layer, informing '
   'data access component design.')
BU(doc,
   'Business rule extraction: alternative flows and exception flows in use case descriptions '
   'document business rules and edge cases (e.g., "if course is full, add to waitlist") that '
   'must be implemented in the business logic layer.')
BU(doc,
   'Component collaboration: use case diagrams show which actors and use cases interact, '
   'helping designers identify how components must collaborate and what dependencies '
   'exist between them.')
BU(doc,
   'Testing foundation: each use case (main flow + alternative + exception flows) '
   'provides a ready-made set of test scenarios for the corresponding components, '
   'ensuring design decisions are traceable to verifiable requirements.')
SP(doc)

doc.save('/workspace/lab8.docx')
print('lab8.docx created successfully.')
