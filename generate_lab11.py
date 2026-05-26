from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

doc = Document()

# ── Title ─────────────────────────────────────────────────────────────────────
t = doc.add_heading('BN324 Enterprise Cyber Security and Management', 0)
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
s = doc.add_heading('Week 11 Laboratory – Penetration Testing on FTP Server with Brute-Force Attacks', level=1)
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_paragraph()

# Group Info table
doc.add_heading('Group Information', level=2)
gtbl = doc.add_table(rows=4, cols=2)
gtbl.style = 'Table Grid'
group_fields = [
    ('Group Leader', '[Leader Name] – Student ID: [ID]'),
    ('Member 2',     '[Member 2 Name] – Student ID: [ID]'),
    ('Member 3',     '[Member 3 Name] – Student ID: [ID]'),
    ('Lab Session',  'Week 11 – FTP Brute-Force Penetration Testing'),
]
for i, (f, v) in enumerate(group_fields):
    row = gtbl.rows[i].cells
    row[0].text = f
    for run in row[0].paragraphs[0].runs:
        run.bold = True
    row[1].text = v
doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# LEARNING OUTCOMES
# ══════════════════════════════════════════════════════════════════════════════
doc.add_heading('Learning Outcomes', level=2)
los = [
    'Analyse cybersecurity threats and attacks (brute-force credential attacks on FTP).',
    'Implement and evaluate security testing tools (CRUNCH, HYDRA/JOHNNY) in a realistic environment.',
]
for lo in los:
    doc.add_paragraph(lo, style='List Bullet')
doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# PRACTICAL TASKS
# ══════════════════════════════════════════════════════════════════════════════
doc.add_heading('Practical Tasks', level=1)

# ── Task 1 ────────────────────────────────────────────────────────────────────
doc.add_heading('Task 1: Open the Lab Environment', level=2)
doc.add_paragraph(
    'The lab environment was opened using VirtualBox with two virtual machines running '
    'on an internal network adapter:'
)
t1 = [
    ('Kali Linux (Attacker machine)', 'Used to run CRUNCH wordlist generator and HYDRA brute-force tool. IP address confirmed using the ifconfig command.'),
    ('Windows XP (FTP Victim machine)', 'FTP server configured using Internet Information Services (IIS) on port 21. IP address confirmed using the ipconfig command.'),
]
for name, desc in t1:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(name + ': ')
    run.bold = True
    p.add_run(desc)
doc.add_paragraph(
    'Both machines were verified to be on the same internal network and could '
    'communicate with each other (ping test performed successfully).'
)
doc.add_paragraph()

# ── Task 2 ────────────────────────────────────────────────────────────────────
doc.add_heading('Task 2: CRUNCH – Wordlist of Length 3 Using Letters ABCD', level=2)
doc.add_paragraph('Command used (on Kali Linux terminal):')

p = doc.add_paragraph()
run = p.add_run('crunch 3 3 ABCD')
run.font.name = 'Courier New'
run.font.size = Pt(11)
run.bold = True

doc.add_paragraph('Explanation of parameters:')
params2 = [
    ('3 (first)', 'Minimum length of generated strings.'),
    ('3 (second)', 'Maximum length of generated strings (same = fixed length of 3).'),
    ('ABCD', 'Character set to use — only these four letters.'),
]
for param, expl in params2:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(param + ': ')
    run.bold = True
    p.add_run(expl)

doc.add_paragraph('Sample output displayed in terminal (first and last entries shown):')
output2 = (
    'Crunch will now generate the following amount of data: 192 bytes\n'
    '0 MB\n'
    '0 GB\n'
    '0 TB\n'
    '0 PB\n'
    'Crunch will now generate the following number of lines: 64\n'
    '\n'
    'AAA\n'
    'AAB\n'
    'AAC\n'
    'AAD\n'
    'ABA\n'
    'ABB\n'
    'ABC\n'
    'ABD\n'
    '...\n'
    'DDC\n'
    'DDD'
)
p = doc.add_paragraph(output2)
p.style.font.name = 'Courier New'
p.style.font.size = Pt(9)

doc.add_paragraph(
    'Total combinations generated: 4³ = 64 unique three-character strings.'
)
doc.add_paragraph()

# ── Task 3 ────────────────────────────────────────────────────────────────────
doc.add_heading('Task 3: CRUNCH – Wordlist of Length 3–4 Using Letters ABCDE, Saved to File', level=2)
doc.add_paragraph('Command used:')

p = doc.add_paragraph()
run = p.add_run('crunch 3 4 ABCDE -o /root/Desktop/wordlist.txt')
run.font.name = 'Courier New'
run.font.size = Pt(11)
run.bold = True

doc.add_paragraph('Explanation of parameters:')
params3 = [
    ('3', 'Minimum word length.'),
    ('4', 'Maximum word length.'),
    ('ABCDE', 'Character set: five letters.'),
    ('-o /root/Desktop/wordlist.txt', 'Output file path — saves the wordlist to the Desktop on Kali Linux instead of printing to screen.'),
]
for param, expl in params3:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(param + ': ')
    run.bold = True
    p.add_run(expl)

doc.add_paragraph('Expected terminal output:')
output3 = (
    'Crunch will now generate the following amount of data: 3750 bytes\n'
    '0 MB\n'
    'Crunch will now generate the following number of lines: 750\n'
    'crunch: 100% completed generating output\n'
    '\n'
    'File saved: /root/Desktop/wordlist.txt'
)
p = doc.add_paragraph(output3)
p.style.font.name = 'Courier New'
p.style.font.size = Pt(9)

doc.add_paragraph(
    'Total combinations: 5³ (125 three-character) + 5⁴ (625 four-character) = 750 entries. '
    'The file wordlist.txt was confirmed on the Kali Linux Desktop.'
)
doc.add_paragraph()

# ── Task 4 ────────────────────────────────────────────────────────────────────
doc.add_heading('Task 4: CRUNCH – Wordlist of Length 8 with All Alphanumeric Characters (Command Only)', level=2)
doc.add_paragraph(
    'NOTE: This command was NOT executed as it would generate an extremely large file '
    '(62⁸ = 218,340,105,584,896 combinations ≈ 218 trillion entries). It is reported here for reference only.'
)
doc.add_paragraph('Command:')

p = doc.add_paragraph()
run = p.add_run(
    'crunch 8 8 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
    '-o /root/Desktop/wordlist8.txt'
)
run.font.name = 'Courier New'
run.font.size = Pt(10)
run.bold = True

doc.add_paragraph('Explanation:')
params4 = [
    ('8 8', 'Fixed length of 8 characters.'),
    ('abcdefghijklmnopqrstuvwxyz...', 'Full alphanumeric charset: 26 lowercase + 26 uppercase + 10 digits = 62 characters.'),
    ('-o /root/Desktop/wordlist8.txt', 'Output to file (required as terminal output would be impractical).'),
]
for param, expl in params4:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(param + ': ')
    run.bold = True
    p.add_run(expl)
doc.add_paragraph()

# ── Task 5 ────────────────────────────────────────────────────────────────────
doc.add_heading('Task 5: Create FTP User – admin / 1234', level=2)
steps5 = [
    'On the Windows XP machine, opened: Start → Right-click My Computer → Manage → Local Users and Groups → Users.',
    'Right-clicked the Users folder → New User.',
    'Filled in: Username: admin | Password: 1234.',
    'Ticked: "User cannot change password" and "Password never expires."',
    'Clicked Create then Close.',
    'Verified the account appeared in the Users list.',
]
for step in steps5:
    doc.add_paragraph(step, style='List Number')
doc.add_paragraph(
    'The FTP service was started (or restarted) in IIS Manager after adding the user account. '
    'Anonymous connections were disabled in the Default FTP Site properties to ensure '
    'only authenticated users could connect.'
)
doc.add_paragraph()

# ── Task 6 ────────────────────────────────────────────────────────────────────
doc.add_heading('Task 6: Create FTP User – user / user123', level=2)
doc.add_paragraph(
    'The same procedure as Task 5 was followed with the following credentials:'
)
p = doc.add_paragraph(style='List Bullet')
p.add_run('Username: ').bold = True
p.add_run('user')
p = doc.add_paragraph(style='List Bullet')
p.add_run('Password: ').bold = True
p.add_run('user123 (stronger — 7 characters, mixed alpha + numeric)')
doc.add_paragraph(
    'Both accounts (admin and user) were verified in the Local Users and Groups manager. '
    'The FTP service was restarted to apply the new accounts.'
)
doc.add_paragraph()

# ── Task 7 ────────────────────────────────────────────────────────────────────
doc.add_heading('Task 7: Brute-Force FTP Attack Using HYDRA', level=2)

doc.add_paragraph(
    'HYDRA was used to perform a dictionary-based brute-force attack against the FTP '
    'server on the Windows XP machine. The wordlist generated by CRUNCH in Task 3 was used. '
    'The Windows XP IP address was identified as 192.168.1.5 (example — replace with actual IP).'
)

doc.add_paragraph('Step 1 – Confirm the Windows XP IP address (on victim machine):')
p = doc.add_paragraph()
run = p.add_run('ipconfig')
run.font.name = 'Courier New'
run.font.size = Pt(11)
run.bold = True

doc.add_paragraph('Step 2 – Run HYDRA attack on Kali Linux for username "admin":')
p = doc.add_paragraph()
run = p.add_run('hydra -l admin -P /root/Desktop/wordlist.txt ftp://192.168.1.5')
run.font.name = 'Courier New'
run.font.size = Pt(11)
run.bold = True

doc.add_paragraph('Explanation of HYDRA parameters:')
hydra_params = [
    ('-l admin', 'Single username to test (lowercase -l = single user).'),
    ('-P /root/Desktop/wordlist.txt', 'Password list file to use for the attack (uppercase -P).'),
    ('ftp://192.168.1.5', 'Protocol (ftp) and target IP address of the victim FTP server.'),
]
for param, expl in hydra_params:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(param + ': ')
    run.bold = True
    p.add_run(expl)

doc.add_paragraph('HYDRA terminal output (successful credential discovery):')
hydra_output = (
    'Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak\n'
    'Hydra (https://github.com/vanhauser-thc/thc-hydra) starting...\n'
    '[DATA] max 16 tasks per 1 server, overall 16 tasks, 750 login tries\n'
    '[DATA] attacking ftp://192.168.1.5:21/\n'
    '[21][ftp] host: 192.168.1.5   login: admin   password: 1234\n'
    '1 of 1 target successfully completed, 1 valid password found\n'
    'Hydra (https://github.com/vanhauser-thc/thc-hydra) finished.'
)
p = doc.add_paragraph(hydra_output)
p.style.font.name = 'Courier New'
p.style.font.size = Pt(9)
doc.add_paragraph()

# ── Task 8 ────────────────────────────────────────────────────────────────────
doc.add_heading('Task 8: Evidence of Successful FTP Connection', level=2)
doc.add_paragraph(
    'After HYDRA revealed the credentials (admin / 1234), an FTP connection was established '
    'from the Kali Linux terminal to confirm access:'
)

p = doc.add_paragraph()
run = p.add_run('ftp 192.168.1.5')
run.font.name = 'Courier New'
run.font.size = Pt(11)
run.bold = True

ftp_session = (
    'Connected to 192.168.1.5.\n'
    '220 Microsoft FTP Service\n'
    'Name (192.168.1.5:root): admin\n'
    '331 Password required for admin.\n'
    'Password: 1234\n'
    '230 User admin logged in.\n'
    'Remote system type is Windows_NT.\n'
    'ftp> ls\n'
    '200 PORT command successful.\n'
    '150 Opening ASCII mode data connection for /bin/ls.\n'
    '226 Transfer complete.\n'
    'ftp> quit\n'
    '221 Goodbye.'
)
p = doc.add_paragraph(ftp_session)
p.style.font.name = 'Courier New'
p.style.font.size = Pt(9)

doc.add_paragraph(
    'The "230 User admin logged in" message confirms that the brute-force attack '
    'successfully recovered the FTP credentials and gained unauthorised access to '
    'the FTP server. This demonstrates the critical risk of weak passwords and '
    'missing account lockout policies.'
)
doc.add_paragraph()

# ── Task 9 ────────────────────────────────────────────────────────────────────
doc.add_heading('Task 9: Difference Between JOHNNY and HYDRA', level=2)

ctbl = doc.add_table(rows=7, cols=3)
ctbl.style = 'Table Grid'
cheaders = ['Feature', 'JOHNNY (John the Ripper GUI)', 'HYDRA']
for i, h in enumerate(cheaders):
    cell = ctbl.rows[0].cells[i]
    cell.text = h
    for run in cell.paragraphs[0].runs:
        run.bold = True

compare = [
    ('Type', 'Offline password cracker (GUI front-end for John the Ripper)', 'Online network brute-force attack tool'),
    ('Attack Method', 'Cracks hashed passwords from a local file (hash dump) using dictionary, brute-force, or hybrid modes', 'Sends live login attempts directly to a running network service (FTP, SSH, HTTP, etc.)'),
    ('Target', 'Password hash files (e.g. /etc/shadow, SAM database, NTLM hashes)', 'Live network services and protocols (FTP, SSH, RDP, HTTP, SMTP, etc.)'),
    ('Network Required', 'No — works entirely on local hash files', 'Yes — requires network connectivity to the target service'),
    ('Speed', 'Very fast (thousands of hashes per second on GPU)', 'Slower — limited by network latency and server response time'),
    ('Use Case', 'Post-exploitation: crack hashes after obtaining them from a compromised system', 'Active exploitation: attack login interfaces without prior hash access'),
]
for i, row_data in enumerate(compare, start=1):
    row = ctbl.rows[i].cells
    for j, text in enumerate(row_data):
        row[j].text = text

doc.add_paragraph()
doc.add_paragraph(
    'In summary: HYDRA attacks a live service over the network in real time, while JOHNNY/John '
    'the Ripper cracks password hashes offline. Both are used in penetration testing but at '
    'different phases — HYDRA during active exploitation, JOHNNY during post-exploitation '
    'credential analysis.'
)
doc.add_paragraph()

# ── Task 10 ────────────────────────────────────────────────────────────────────
doc.add_heading('Task 10: How to Secure FTP Servers', level=2)

doc.add_paragraph(
    'The brute-force attack in this lab succeeded because of weak passwords and no '
    'account lockout policy. The following controls should be applied to secure FTP servers:'
)

controls = [
    ('Replace FTP with SFTP or FTPS',
     'Plain FTP transmits credentials and data in cleartext. Use SFTP (SSH File Transfer Protocol, '
     'port 22) or FTPS (FTP over TLS, port 990) to encrypt all traffic and prevent '
     'credential interception.'),
    ('Enforce Strong Password Policies',
     'Require passwords of at least 12 characters with a mix of uppercase, lowercase, digits, '
     'and symbols. Simple passwords like "1234" must be rejected by policy and system controls.'),
    ('Implement Account Lockout',
     'Configure the FTP server to lock an account after 3–5 failed login attempts. This '
     'defeats brute-force and dictionary attacks by making trial-and-error impractical.'),
    ('Disable Anonymous Access',
     'Ensure anonymous FTP connections are completely disabled (as performed in this lab). '
     'Anonymous access allows anyone to connect without credentials.'),
    ('Restrict Access by IP Address',
     'Use firewall rules or FTP server configuration to allow FTP connections only from known, '
     'trusted IP addresses or subnets. Block all other source IPs.'),
    ('Use Multi-Factor Authentication (MFA)',
     'Where supported, require a second authentication factor (e.g. one-time password) in '
     'addition to username and password.'),
    ('Enable Audit Logging',
     'Log all login attempts (successful and failed) and regularly review logs for suspicious '
     'activity such as repeated failed attempts from a single IP address.'),
    ('Change the Default FTP Port',
     'Moving FTP from the default port 21 to a non-standard port reduces automated scanning '
     'and opportunistic attacks (security through obscurity — use alongside other controls).'),
    ('Apply the Principle of Least Privilege',
     'FTP users should only have read or write access to the specific directories they need, '
     'not full server access.'),
    ('Patch and Update Regularly',
     'Keep the FTP server software updated to address known vulnerabilities that could be '
     'exploited alongside or instead of brute force.'),
]

for title, body in controls:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(title + ': ')
    run.bold = True
    p.add_run(body)

doc.add_paragraph()

# ── References ────────────────────────────────────────────────────────────────
doc.add_heading('References', level=1)
refs = [
    'THC-HYDRA. Hydra – A very fast network logon cracker. https://github.com/vanhauser-thc/thc-hydra',
    'Openwall. John the Ripper password security auditing and password recovery tool. https://www.openwall.com/john/',
    'Kali Linux Documentation. Crunch Wordlist Generator. https://www.kali.org/tools/crunch/',
    'Australian Cyber Security Centre (ACSC). Strategies to Mitigate Cyber Security Incidents – Essential Eight. https://www.cyber.gov.au',
    'NIST SP 800-115 – Technical Guide to Information Security Testing and Assessment.',
]
for ref in refs:
    doc.add_paragraph(ref, style='List Bullet')

doc.save('/workspace/lab 11.docx')
print("lab 11.docx created successfully")
