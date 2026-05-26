from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# ── Title ─────────────────────────────────────────────────────────────────────
t = doc.add_heading('BN324 Enterprise Cyber Security and Management', 0)
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
s = doc.add_heading('Week 8 Laboratory – NIST AI RMF and Australia\'s AI Ethics Principles', level=1)
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# TASK 1
# ══════════════════════════════════════════════════════════════════════════════
doc.add_heading('Task 1 – NIST AI 100-1: AI Risk Management Framework', level=1)

# ── Q1: Common Elements of AI Governance ──────────────────────────────────────
doc.add_heading('1. Common Elements of AI Governance', level=2)

doc.add_paragraph(
    'AI Governance is the set of policies, processes, roles and controls that '
    'organisations put in place to ensure AI systems are developed and used '
    'responsibly, safely and in alignment with legal and ethical standards. '
    'The key common elements are:'
)

elements = [
    ('Policies and Standards',
     'Documented rules that define acceptable use, design constraints, and '
     'compliance requirements for AI systems (e.g. data-use policies, '
     'model-approval checklists). They translate organisational values into '
     'enforceable guidelines.'),
    ('Roles and Accountability',
     'Clear assignment of responsibility across the AI lifecycle — developers, '
     'deployers, risk officers, and executive sponsors. Accountability structures '
     'ensure that someone is answerable for every decision the AI system makes '
     'or influences.'),
    ('Risk Management',
     'Systematic identification, assessment, and mitigation of risks arising from '
     'AI systems — including bias, security vulnerabilities, privacy breaches, and '
     'unintended consequences. This maps directly to the NIST AI RMF core functions.'),
    ('Transparency and Explainability',
     'Mechanisms that allow stakeholders to understand how an AI system works, '
     'why it makes certain decisions, and what data it relies on. This supports '
     'trust and enables challenge and audit.'),
    ('Fairness and Non-Discrimination',
     'Processes to detect and reduce bias in training data, model outputs, and '
     'deployment contexts so that AI does not produce discriminatory outcomes '
     'against individuals or groups.'),
    ('Privacy and Data Protection',
     'Controls governing data collection, storage, processing and retention in '
     'compliance with applicable privacy laws (e.g. Australia\'s Privacy Act 1988). '
     'Privacy impact assessments are a common tool.'),
    ('Monitoring and Audit',
     'Ongoing performance monitoring, logging, and independent audit of AI '
     'systems to detect drift, failures, or misuse after deployment. Metrics and '
     'key performance indicators (KPIs) are defined in advance.'),
    ('Human Oversight and Contestability',
     'Ensuring a human can review, override, or shut down an AI system when '
     'needed. Affected parties must have a pathway to challenge AI-driven decisions.'),
    ('Compliance and Legal Obligations',
     'Alignment with applicable laws, standards, and regulations — such as the '
     'Privacy Act, sector-specific regulations, and voluntary frameworks like '
     'Australia\'s AI Ethics Principles or the NIST AI RMF.'),
]

for title, body in elements:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(title + ': ')
    run.bold = True
    p.add_run(body)

doc.add_paragraph()

# ── Q2: NIST AI RMF Core Principles ──────────────────────────────────────────
doc.add_heading('2. Core Principles of the NIST AI RMF (NIST AI 100-1)', level=2)

doc.add_paragraph(
    'NIST AI 100-1 (released January 2023) provides a voluntary, sector-agnostic '
    'framework to help organisations manage risks associated with AI systems throughout '
    'their lifecycle. The framework is structured around four core functions that form '
    'an iterative, non-linear cycle:'
)

rmf_functions = [
    ('GOVERN (Cross-Cutting Foundation)',
     'GOVERN is the foundational function that underpins all others. It establishes '
     'the organisational culture, policies, accountability structures, and processes '
     'needed to manage AI risk consistently. Key outcomes include: defining roles and '
     'responsibilities; setting risk tolerance; allocating resources; and embedding '
     'AI risk management into enterprise-wide governance. GOVERN is applied continuously '
     'and informs MAP, MEASURE, and MANAGE.',
     [
         'Establish AI risk policies and risk appetite.',
         'Assign accountability and authority across the AI lifecycle.',
         'Integrate AI governance with broader organisational risk management.',
         'Foster a culture of responsible AI development.',
     ]),
    ('MAP (Context and Risk Identification)',
     'The MAP function establishes context for understanding and framing the risks '
     'associated with a specific AI system before it is deployed. It requires '
     'organisations to identify who the stakeholders are, what the system\'s intended '
     'purpose is, and what failure modes or negative impacts may arise.',
     [
         'Identify AI system purpose, scope, and affected stakeholders.',
         'Catalogue potential risks (bias, privacy, safety, security).',
         'Assess the broader societal and environmental impacts.',
         'Document assumptions, limitations, and data sources.',
     ]),
    ('MEASURE (Risk Assessment and Monitoring)',
     'The MEASURE function uses quantitative, qualitative, or mixed-method tools to '
     'analyse, assess, benchmark, and monitor AI risks and their impacts. It converts '
     'the risks identified in MAP into measurable evidence that can be tracked and reported. '
     'AI systems must be tested before deployment and monitored continuously during operation.',
     [
         'Apply metrics for fairness, reliability, robustness, and explainability.',
         'Conduct red-team testing, adversarial testing, and bias audits.',
         'Benchmark performance against defined thresholds.',
         'Document and track measurement results over time.',
     ]),
    ('MANAGE (Risk Treatment and Response)',
     'The MANAGE function uses outputs from GOVERN, MAP, and MEASURE to prioritise and '
     'treat identified AI risks. It includes implementing mitigations, monitoring '
     'residual risks, and preparing incident response and recovery plans for when '
     'AI systems behave unexpectedly or cause harm.',
     [
         'Prioritise risks by likelihood, severity, and organisational risk tolerance.',
         'Apply risk treatments: accept, mitigate, transfer, or avoid.',
         'Implement safeguards, human-review checkpoints, and fail-safes.',
         'Establish response and recovery plans for AI-related incidents.',
     ]),
]

for name, desc, bullets in rmf_functions:
    doc.add_heading(name, level=3)
    doc.add_paragraph(desc)
    for b in bullets:
        doc.add_paragraph(b, style='List Bullet')

doc.add_paragraph(
    'Together, these four functions create a continuous improvement cycle: GOVERN sets '
    'the rules, MAP identifies what could go wrong, MEASURE provides evidence of how '
    'things are going, and MANAGE acts on that evidence to reduce harm and build '
    'trustworthy AI.'
)

doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# TASK 2
# ══════════════════════════════════════════════════════════════════════════════
doc.add_heading('Task 2 – Case Study Report: Australia\'s AI Ethics Principles', level=1)

doc.add_heading('Introduction', level=2)
doc.add_paragraph(
    'The Australian Government\'s Department of Industry, Science and Resources '
    'published eight Artificial Intelligence (AI) Ethics Principles to guide '
    'businesses and governments in the responsible design, development, and '
    'implementation of AI. These voluntary principles are designed to ensure AI '
    'in Australia is safe, secure, and reliable. In October 2025, the Government '
    'further evolved this guidance by publishing the Guidance for AI Adoption, '
    'which consolidates these principles into six essential practices for responsible '
    'AI governance. This report reviews the eight principles and reflects on their '
    'significance for Australian organisations.'
)

doc.add_heading('The Eight AI Ethics Principles', level=2)

principles = [
    ('1. Human, Societal and Environmental Wellbeing',
     'AI systems should benefit individuals, society, and the environment. '
     'Developers must consider not only immediate users but also broader social '
     'and ecological impacts throughout the AI lifecycle.'),
    ('2. Human-Centred Values',
     'AI systems should respect human rights, diversity, and individual autonomy. '
     'This principle aligns with existing Australian human rights obligations and '
     'ensures AI does not erode fundamental freedoms.'),
    ('3. Fairness',
     'AI systems should be inclusive and accessible and must not produce or '
     'reinforce unfair discrimination against individuals, communities, or groups — '
     'including on the basis of age, gender, ethnicity, or disability.'),
    ('4. Privacy Protection and Security',
     'AI systems must respect and uphold privacy rights and data protection laws '
     '(particularly the Privacy Act 1988) and ensure the security of data used in '
     'AI processes against unauthorised access or misuse.'),
    ('5. Reliability and Safety',
     'AI systems should reliably operate in accordance with their intended purpose '
     'and not pose unnecessary safety risks. Systems must be tested, validated, '
     'and monitored to ensure consistent and safe behaviour.'),
    ('6. Transparency and Explainability',
     'People should be able to understand when they are significantly impacted by '
     'an AI system and be informed when they are interacting with one. Organisations '
     'should be able to explain AI-driven decisions in meaningful terms.'),
    ('7. Contestability',
     'When an AI system significantly affects a person, community, group, or the '
     'environment, there must be a timely and accessible process to challenge the '
     'use or outcome of the AI system. This safeguard is critical for high-stakes '
     'decisions such as credit assessments or public-benefit allocations.'),
    ('8. Accountability',
     'People responsible for the different phases of the AI system lifecycle '
     '(design, development, deployment, and decommission) must be identifiable '
     'and accountable for the outcomes. Human oversight of AI systems must be '
     'enabled and maintained.'),
]

for title, body in principles:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(title + ': ')
    run.bold = True
    p.add_run(body)

doc.add_heading('Feedback and Reflection', level=2)
doc.add_paragraph(
    'Australia\'s AI Ethics Principles represent a pragmatic and human-centred '
    'approach to AI governance. Several aspects are particularly noteworthy:'
)

feedback = [
    ('Voluntary but meaningful',
     'While the principles are currently voluntary (not legally binding), they '
     'establish a clear normative benchmark. Organisations that adopt them signal '
     'trustworthiness to customers, regulators, and partners. The 2025 update to '
     'the Guidance for AI Adoption shows the Government is actively refining this '
     'framework in response to emerging AI risks.'),
    ('Alignment with global frameworks',
     'The principles closely align with the NIST AI RMF (particularly GOVERN and '
     'MAP functions), the OECD AI Principles, and the EU AI Act — making it easier '
     'for Australian organisations operating internationally to demonstrate compliance '
     'across multiple jurisdictions.'),
    ('Gaps and challenges',
     'As a voluntary framework, enforcement and consistency of adoption across '
     'industries remains a challenge. SMBs, in particular, may lack the resources '
     'to implement all principles comprehensively. Greater practical guidance — such '
     'as the NAIC\'s implementation toolkit — is needed to bridge the gap between '
     'principle and practice.'),
    ('Relevance to recent incidents',
     'The principles of privacy, accountability, and contestability are directly '
     'relevant to recent Australian data breach incidents (e.g. University of Sydney, '
     'Dodo/iPrimus). Had AI-driven systems contributed to those breaches, these '
     'principles would provide the ethical baseline for evaluating organisational '
     'responsibility.'),
    ('Conclusion',
     'Australia\'s AI Ethics Principles provide a solid foundation for responsible '
     'AI use. As AI adoption accelerates across education, healthcare, defence, and '
     'commerce, transitioning from voluntary principles to enforceable standards — '
     'informed by practical implementation experience — will be essential to ensuring '
     'AI genuinely benefits all Australians.'),
]

for title, body in feedback:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(title + ': ')
    run.bold = True
    p.add_run(body)

doc.add_paragraph()

# ── References ────────────────────────────────────────────────────────────────
doc.add_heading('References', level=1)
refs = [
    'NIST (2023). NIST AI 100-1: Artificial Intelligence Risk Management Framework (AI RMF 1.0). '
    'National Institute of Standards and Technology. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf',
    'Department of Industry, Science and Resources (2019, updated 2025). Australia\'s AI Ethics '
    'Principles. Australian Government. https://www.industry.gov.au/publications/australias-ai-ethics-principles',
    'NIST AI Resource Center (2026). AI RMF Core. https://airc.nist.gov/airmf-resources/airmf/5-sec-core/',
    'National Artificial Intelligence Centre (NAIC) & Gradient Institute (2023). Implementing '
    'Australia\'s AI Ethics Principles. https://www.industry.gov.au/publications/implementing-australias-ai-ethics-principles',
]
for ref in refs:
    doc.add_paragraph(ref, style='List Bullet')

doc.save('/workspace/lab 8.docx')
print("lab 8.docx created successfully")
