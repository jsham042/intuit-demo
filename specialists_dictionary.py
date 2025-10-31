"""
Intuit Customer Service Specialist Dictionary
This dictionary contains detailed descriptions of specialists to help route customer inquiries
using vector search for optimal matching.
"""

SPECIALISTS = [
    # Tax Specialists - Individual
    {
        "id": "TAX-001",
        "name": "Individual Tax Return Specialist",
        "description": "Helps individuals with filing federal and state income tax returns, W-2 forms, 1099 forms, standard deductions, and personal tax credits. Assists with TurboTax software for individual filers."
    },
    {
        "id": "TAX-002",
        "name": "Self-Employment Tax Specialist",
        "description": "Assists self-employed individuals, freelancers, and gig workers with Schedule C, quarterly estimated taxes, self-employment tax calculations, and business expense deductions."
    },
    {
        "id": "TAX-003",
        "name": "Investment Income Tax Specialist",
        "description": "Handles capital gains and losses, dividend income, stock sales, cryptocurrency taxation, Form 1099-B, wash sales, and investment-related tax reporting."
    },
    {
        "id": "TAX-004",
        "name": "Rental Property Tax Specialist",
        "description": "Specializes in rental property income, Schedule E, depreciation, rental expenses, vacation rental taxation, and real estate tax issues."
    },
    {
        "id": "TAX-005",
        "name": "Retirement Income Tax Specialist",
        "description": "Assists with IRA distributions, 401(k) withdrawals, Required Minimum Distributions (RMD), Social Security taxation, pension income, and retirement account tax planning."
    },
    {
        "id": "TAX-006",
        "name": "Tax Deduction Specialist",
        "description": "Helps maximize deductions including itemized deductions, medical expenses, charitable contributions, mortgage interest, state and local taxes (SALT), and educational expenses."
    },
    {
        "id": "TAX-007",
        "name": "Tax Credit Specialist",
        "description": "Specializes in tax credits including Child Tax Credit, Earned Income Tax Credit (EITC), education credits (American Opportunity, Lifetime Learning), energy credits, and dependent care credits."
    },
    {
        "id": "TAX-008",
        "name": "State Tax Specialist",
        "description": "Handles state-specific tax returns, multi-state filing, state tax credits and deductions, and state tax residency issues."
    },
    {
        "id": "TAX-009",
        "name": "Amended Return Specialist",
        "description": "Assists with filing amended tax returns (Form 1040-X), correcting errors on filed returns, and claiming missed deductions or credits."
    },
    {
        "id": "TAX-010",
        "name": "Foreign Income Tax Specialist",
        "description": "Helps with foreign income reporting, FBAR filings, Foreign Tax Credit, FATCA compliance, and expatriate tax issues."
    },
    
    # Tax Specialists - Business
    {
        "id": "TAX-011",
        "name": "Small Business Tax Specialist",
        "description": "Assists small business owners with business tax returns, Form 1120, 1120-S, 1065, business deductions, and tax planning strategies for businesses."
    },
    {
        "id": "TAX-012",
        "name": "S-Corporation Tax Specialist",
        "description": "Specializes in S-Corp elections, Form 1120-S, K-1 distributions, reasonable compensation issues, and S-Corporation tax compliance."
    },
    {
        "id": "TAX-013",
        "name": "Partnership Tax Specialist",
        "description": "Handles partnership tax returns (Form 1065), partner basis calculations, guaranteed payments, and partnership tax allocations."
    },
    {
        "id": "TAX-014",
        "name": "C-Corporation Tax Specialist",
        "description": "Manages C-Corp tax returns (Form 1120), corporate tax rates, dividend distributions, and corporate tax planning."
    },
    {
        "id": "TAX-015",
        "name": "LLC Tax Specialist",
        "description": "Assists with LLC tax elections, single-member LLC taxation, multi-member LLC taxation, and state LLC tax requirements."
    },
    {
        "id": "TAX-016",
        "name": "Payroll Tax Specialist",
        "description": "Handles payroll tax compliance, Form 941, 940, W-2 and W-3 filing, employment taxes, and payroll tax deposits."
    },
    {
        "id": "TAX-017",
        "name": "Sales Tax Specialist",
        "description": "Specializes in sales tax collection, nexus determination, multi-state sales tax compliance, sales tax exemptions, and sales tax reporting."
    },
    {
        "id": "TAX-018",
        "name": "Excise Tax Specialist",
        "description": "Handles federal and state excise taxes, fuel taxes, environmental taxes, and industry-specific excise tax compliance."
    },
    {
        "id": "TAX-019",
        "name": "Business Expense Specialist",
        "description": "Assists with categorizing and maximizing business expense deductions, Section 179 deductions, bonus depreciation, and business asset depreciation."
    },
    {
        "id": "TAX-020",
        "name": "Tax Extension Specialist",
        "description": "Helps file tax extensions (Form 4868, 7004), estimate taxes due with extensions, and manage extension deadlines."
    },
    
    # Tax Specialists - Specialized
    {
        "id": "TAX-021",
        "name": "Estate Tax Specialist",
        "description": "Handles estate tax returns (Form 706), estate tax planning, inheritance tax issues, and estate valuation."
    },
    {
        "id": "TAX-022",
        "name": "Gift Tax Specialist",
        "description": "Assists with gift tax returns (Form 709), annual exclusion gifts, lifetime exemptions, and gift tax planning."
    },
    {
        "id": "TAX-023",
        "name": "Trust Tax Specialist",
        "description": "Specializes in trust tax returns (Form 1041), grantor trusts, complex trusts, simple trusts, and trust income distributions."
    },
    {
        "id": "TAX-024",
        "name": "Non-Profit Tax Specialist",
        "description": "Handles Form 990, 990-EZ, 990-N, tax-exempt organization compliance, and charitable organization tax issues."
    },
    {
        "id": "TAX-025",
        "name": "IRS Notice Response Specialist",
        "description": "Assists with responding to IRS notices, CP2000 notices, audit notices, collection notices, and IRS correspondence."
    },
    {
        "id": "TAX-026",
        "name": "Tax Audit Defense Specialist",
        "description": "Helps with IRS audit preparation, audit representation, providing documentation, and navigating the audit process."
    },
    {
        "id": "TAX-027",
        "name": "Offer in Compromise Specialist",
        "description": "Assists with submitting Offers in Compromise, negotiating tax debt settlements, and evaluating OIC eligibility."
    },
    {
        "id": "TAX-028",
        "name": "Installment Agreement Specialist",
        "description": "Helps set up IRS payment plans, installment agreements, and managing tax debt payment arrangements."
    },
    {
        "id": "TAX-029",
        "name": "Tax Penalty Abatement Specialist",
        "description": "Assists with requesting penalty relief, first-time penalty abatement, reasonable cause claims, and reducing tax penalties."
    },
    {
        "id": "TAX-030",
        "name": "Identity Theft Tax Specialist",
        "description": "Helps victims of tax-related identity theft, filing Form 14039, obtaining IP PINs, and resolving fraudulent returns."
    },
    
    # QuickBooks Specialists - General
    {
        "id": "QB-001",
        "name": "QuickBooks Online Setup Specialist",
        "description": "Assists with initial QuickBooks Online setup, company file creation, chart of accounts setup, and initial configuration."
    },
    {
        "id": "QB-002",
        "name": "QuickBooks Desktop Specialist",
        "description": "Helps with QuickBooks Desktop (Pro, Premier, Enterprise), desktop software installation, company file management, and desktop-specific features."
    },
    {
        "id": "QB-003",
        "name": "QuickBooks Migration Specialist",
        "description": "Assists with migrating from QuickBooks Desktop to Online, converting company files, and data transition planning."
    },
    {
        "id": "QB-004",
        "name": "Chart of Accounts Specialist",
        "description": "Helps design and organize chart of accounts, account structure, account types, and account customization in QuickBooks."
    },
    {
        "id": "QB-005",
        "name": "QuickBooks Reconciliation Specialist",
        "description": "Assists with bank reconciliation, credit card reconciliation, finding reconciliation discrepancies, and fixing reconciliation errors."
    },
    {
        "id": "QB-006",
        "name": "QuickBooks Reporting Specialist",
        "description": "Helps generate and customize financial reports, profit and loss statements, balance sheets, cash flow reports, and custom report creation."
    },
    {
        "id": "QB-007",
        "name": "QuickBooks Banking Specialist",
        "description": "Assists with bank feeds, connecting bank accounts, categorizing transactions, and managing bank connections in QuickBooks."
    },
    {
        "id": "QB-008",
        "name": "QuickBooks Multi-Currency Specialist",
        "description": "Handles multi-currency transactions, foreign exchange, currency conversions, and international business accounting in QuickBooks."
    },
    {
        "id": "QB-009",
        "name": "QuickBooks Integration Specialist",
        "description": "Assists with third-party app integrations, API connections, data syncing with other platforms, and QuickBooks ecosystem apps."
    },
    {
        "id": "QB-010",
        "name": "QuickBooks Performance Specialist",
        "description": "Helps optimize QuickBooks performance, troubleshoot slow software, reduce file size, and improve system speed."
    },
    
    # QuickBooks Specialists - Features
    {
        "id": "QB-011",
        "name": "QuickBooks Invoicing Specialist",
        "description": "Assists with creating invoices, customizing invoice templates, recurring invoices, online invoice payments, and invoice tracking."
    },
    {
        "id": "QB-012",
        "name": "QuickBooks Accounts Receivable Specialist",
        "description": "Helps manage customer payments, track outstanding invoices, aging reports, customer credits, and receivables management."
    },
    {
        "id": "QB-013",
        "name": "QuickBooks Accounts Payable Specialist",
        "description": "Assists with vendor bills, bill payments, 1099 contractor management, vendor credits, and payables tracking."
    },
    {
        "id": "QB-014",
        "name": "QuickBooks Expense Tracking Specialist",
        "description": "Helps categorize expenses, track business spending, receipt capture, expense reports, and expense management."
    },
    {
        "id": "QB-015",
        "name": "QuickBooks Inventory Specialist",
        "description": "Assists with inventory tracking, stock levels, COGS calculations, inventory valuation, and inventory management features."
    },
    {
        "id": "QB-016",
        "name": "QuickBooks Job Costing Specialist",
        "description": "Helps with project-based accounting, job costing, tracking project profitability, and project management in QuickBooks."
    },
    {
        "id": "QB-017",
        "name": "QuickBooks Time Tracking Specialist",
        "description": "Assists with employee time tracking, billable hours, timesheet management, and time-based invoicing."
    },
    {
        "id": "QB-018",
        "name": "QuickBooks Estimates Specialist",
        "description": "Helps create and manage estimates, quotes, proposals, converting estimates to invoices, and estimate tracking."
    },
    {
        "id": "QB-019",
        "name": "QuickBooks Purchase Orders Specialist",
        "description": "Assists with creating purchase orders, PO approval workflows, receiving inventory, and purchase order tracking."
    },
    {
        "id": "QB-020",
        "name": "QuickBooks Sales Tax Specialist",
        "description": "Helps configure sales tax settings, automated sales tax calculations, sales tax reporting, and multi-jurisdiction sales tax."
    },
    
    # QuickBooks Specialists - Industry Specific
    {
        "id": "QB-021",
        "name": "QuickBooks Contractor Specialist",
        "description": "Assists contractors with job costing, progress invoicing, retention tracking, and construction-specific accounting in QuickBooks."
    },
    {
        "id": "QB-022",
        "name": "QuickBooks Retail Specialist",
        "description": "Helps retail businesses with point of sale integration, inventory management, retail sales tracking, and multi-location retail."
    },
    {
        "id": "QB-023",
        "name": "QuickBooks E-commerce Specialist",
        "description": "Assists online sellers with e-commerce platform integration (Shopify, Amazon, etc.), online sales tracking, and marketplace accounting."
    },
    {
        "id": "QB-024",
        "name": "QuickBooks Real Estate Specialist",
        "description": "Helps real estate professionals with property tracking, rental income, security deposits, and real estate-specific accounting."
    },
    {
        "id": "QB-025",
        "name": "QuickBooks Restaurant Specialist",
        "description": "Assists restaurants with menu costing, food inventory, POS integration, tip tracking, and restaurant accounting."
    },
    {
        "id": "QB-026",
        "name": "QuickBooks Professional Services Specialist",
        "description": "Helps consultants, lawyers, accountants with billable hours, client retainers, trust accounting, and professional services billing."
    },
    {
        "id": "QB-027",
        "name": "QuickBooks Non-Profit Specialist",
        "description": "Assists non-profit organizations with fund accounting, donor tracking, grant management, and non-profit financial reporting."
    },
    {
        "id": "QB-028",
        "name": "QuickBooks Manufacturing Specialist",
        "description": "Helps manufacturers with bill of materials, assembly tracking, work in progress, and manufacturing accounting."
    },
    {
        "id": "QB-029",
        "name": "QuickBooks Healthcare Specialist",
        "description": "Assists medical practices with patient billing, insurance claims, healthcare-specific accounting, and HIPAA compliance considerations."
    },
    {
        "id": "QB-030",
        "name": "QuickBooks Property Management Specialist",
        "description": "Helps property managers with multiple properties, tenant rent tracking, maintenance expenses, and property accounting."
    },
    
    # Payroll Specialists
    {
        "id": "PAY-001",
        "name": "Payroll Setup Specialist",
        "description": "Assists with initial payroll setup, employee onboarding, tax withholding setup, and payroll configuration in QuickBooks or Intuit Payroll."
    },
    {
        "id": "PAY-002",
        "name": "Payroll Processing Specialist",
        "description": "Helps with running payroll, processing paychecks, direct deposits, pay stubs, and regular payroll operations."
    },
    {
        "id": "PAY-003",
        "name": "Payroll Tax Filing Specialist",
        "description": "Assists with payroll tax deposits, quarterly filings (Form 941), annual filings (Form 940), and payroll tax compliance."
    },
    {
        "id": "PAY-004",
        "name": "W-2 and 1099 Specialist",
        "description": "Helps with year-end W-2 preparation, 1099-NEC for contractors, W-3 filing, and year-end payroll tax forms."
    },
    {
        "id": "PAY-005",
        "name": "Employee Benefits Specialist",
        "description": "Assists with setting up health insurance deductions, 401(k) contributions, HSA, FSA, and other employee benefit deductions."
    },
    {
        "id": "PAY-006",
        "name": "Multi-State Payroll Specialist",
        "description": "Helps businesses with employees in multiple states, state payroll tax withholding, and multi-state payroll compliance."
    },
    {
        "id": "PAY-007",
        "name": "Garnishment Specialist",
        "description": "Assists with wage garnishments, child support orders, tax levies, and other involuntary payroll deductions."
    },
    {
        "id": "PAY-008",
        "name": "Payroll Correction Specialist",
        "description": "Helps fix payroll errors, void paychecks, process payroll adjustments, and correct payroll mistakes."
    },
    {
        "id": "PAY-009",
        "name": "Contractor Payment Specialist",
        "description": "Assists with paying independent contractors, 1099 reporting, contractor classification, and non-employee compensation."
    },
    {
        "id": "PAY-010",
        "name": "Time and Attendance Specialist",
        "description": "Helps with time tracking integration, overtime calculations, PTO tracking, and time-based payroll."
    },
    
    # Accounting & Bookkeeping Specialists
    {
        "id": "ACCT-001",
        "name": "General Bookkeeping Specialist",
        "description": "Assists with daily bookkeeping tasks, recording transactions, maintaining ledgers, and basic accounting operations."
    },
    {
        "id": "ACCT-002",
        "name": "Financial Statement Specialist",
        "description": "Helps prepare and interpret financial statements including balance sheets, income statements, and cash flow statements."
    },
    {
        "id": "ACCT-003",
        "name": "Accounts Reconciliation Specialist",
        "description": "Assists with reconciling all types of accounts, finding discrepancies, and ensuring accurate account balances."
    },
    {
        "id": "ACCT-004",
        "name": "Month-End Close Specialist",
        "description": "Helps with month-end closing procedures, adjusting entries, accruals, and period-end accounting tasks."
    },
    {
        "id": "ACCT-005",
        "name": "Year-End Close Specialist",
        "description": "Assists with year-end closing, annual adjustments, preparing for tax season, and fiscal year-end procedures."
    },
    {
        "id": "ACCT-006",
        "name": "Cash Flow Management Specialist",
        "description": "Helps with cash flow forecasting, managing working capital, cash flow analysis, and liquidity management."
    },
    {
        "id": "ACCT-007",
        "name": "Budget Planning Specialist",
        "description": "Assists with creating budgets, budget vs actual analysis, financial planning, and budget management."
    },
    {
        "id": "ACCT-008",
        "name": "Fixed Asset Specialist",
        "description": "Helps track fixed assets, calculate depreciation, manage asset disposals, and maintain asset registers."
    },
    {
        "id": "ACCT-009",
        "name": "Journal Entry Specialist",
        "description": "Assists with recording journal entries, adjusting entries, correcting entries, and general ledger maintenance."
    },
    {
        "id": "ACCT-010",
        "name": "Audit Preparation Specialist",
        "description": "Helps prepare for financial audits, organize documentation, respond to auditor requests, and audit readiness."
    },
    
    # Technical Support Specialists
    {
        "id": "TECH-001",
        "name": "Software Installation Specialist",
        "description": "Assists with installing Intuit software products, system requirements, download issues, and installation troubleshooting."
    },
    {
        "id": "TECH-002",
        "name": "Login and Password Specialist",
        "description": "Helps with account login issues, password resets, two-factor authentication, and account access problems."
    },
    {
        "id": "TECH-003",
        "name": "Data Backup and Restore Specialist",
        "description": "Assists with backing up company files, restoring from backups, data recovery, and backup best practices."
    },
    {
        "id": "TECH-004",
        "name": "Software Update Specialist",
        "description": "Helps with updating Intuit software, managing updates, troubleshooting update errors, and version upgrades."
    },
    {
        "id": "TECH-005",
        "name": "Error Message Specialist",
        "description": "Assists with diagnosing and resolving software error messages, crashes, and technical error codes."
    },
    {
        "id": "TECH-006",
        "name": "Network Connectivity Specialist",
        "description": "Helps with network connection issues, multi-user access, firewall configuration, and connectivity troubleshooting."
    },
    {
        "id": "TECH-007",
        "name": "Data Import/Export Specialist",
        "description": "Assists with importing data from other software, exporting data, CSV files, and data migration."
    },
    {
        "id": "TECH-008",
        "name": "User Permissions Specialist",
        "description": "Helps set up user roles, manage access permissions, add/remove users, and configure user security settings."
    },
    {
        "id": "TECH-009",
        "name": "Mobile App Specialist",
        "description": "Assists with Intuit mobile apps (iOS and Android), mobile features, syncing issues, and mobile troubleshooting."
    },
    {
        "id": "TECH-010",
        "name": "Printer Setup Specialist",
        "description": "Helps with setting up printers, configuring check printing, form printing, and resolving printing issues."
    },
    
    # Subscription & Billing Specialists
    {
        "id": "SUB-001",
        "name": "Subscription Management Specialist",
        "description": "Assists with managing Intuit subscriptions, plan changes, subscription renewals, and service tier upgrades/downgrades."
    },
    {
        "id": "SUB-002",
        "name": "Billing and Payment Specialist",
        "description": "Helps with billing questions, payment method updates, invoice inquiries, and payment processing issues."
    },
    {
        "id": "SUB-003",
        "name": "Refund and Cancellation Specialist",
        "description": "Assists with subscription cancellations, refund requests, service termination, and account closure."
    },
    {
        "id": "SUB-004",
        "name": "License Management Specialist",
        "description": "Helps with software license activation, multi-user licenses, license transfers, and license key issues."
    },
    {
        "id": "SUB-005",
        "name": "Pricing and Plans Specialist",
        "description": "Assists with understanding pricing tiers, comparing plans, choosing the right subscription, and cost optimization."
    },
    
    # Specialized Product Specialists
    {
        "id": "PROD-001",
        "name": "TurboTax Live Specialist",
        "description": "Assists with TurboTax Live services, connecting with tax experts, live tax advice, and expert review features."
    },
    {
        "id": "PROD-002",
        "name": "QuickBooks Live Specialist",
        "description": "Helps with QuickBooks Live Bookkeeping services, connecting with bookkeepers, and live bookkeeping support."
    },
    {
        "id": "PROD-003",
        "name": "Mint Specialist",
        "description": "Assists with Mint personal finance app, budget tracking, bill reminders, credit score monitoring, and financial goals."
    },
    {
        "id": "PROD-004",
        "name": "Credit Karma Specialist",
        "description": "Helps with Credit Karma services, credit monitoring, credit score questions, and financial product recommendations."
    },
    {
        "id": "PROD-005",
        "name": "Mailchimp Specialist",
        "description": "Assists with Mailchimp email marketing, campaign creation, audience management, and marketing automation."
    },
    {
        "id": "PROD-006",
        "name": "QuickBooks Payments Specialist",
        "description": "Helps with accepting payments, payment processing, merchant services, and QuickBooks payment integration."
    },
    {
        "id": "PROD-007",
        "name": "QuickBooks Capital Specialist",
        "description": "Assists with QuickBooks Capital loans, financing options, loan applications, and business funding."
    },
    {
        "id": "PROD-008",
        "name": "QuickBooks Workforce Specialist",
        "description": "Helps employees access pay stubs, W-2s, and payroll information through QuickBooks Workforce portal."
    },
    {
        "id": "PROD-009",
        "name": "TurboTax Mobile Specialist",
        "description": "Assists with TurboTax mobile app, filing taxes on mobile devices, photo upload features, and mobile-specific issues."
    },
    {
        "id": "PROD-010",
        "name": "ProConnect Tax Specialist",
        "description": "Helps tax professionals with ProConnect Tax software, professional tax preparation, and practice management."
    },
    
    # Compliance & Regulatory Specialists
    {
        "id": "COMP-001",
        "name": "GDPR Compliance Specialist",
        "description": "Assists with GDPR compliance in Intuit products, data privacy, EU regulations, and data protection requirements."
    },
    {
        "id": "COMP-002",
        "name": "Data Security Specialist",
        "description": "Helps with data security features, encryption, secure data handling, and security best practices in Intuit products."
    },
    {
        "id": "COMP-003",
        "name": "SOX Compliance Specialist",
        "description": "Assists with Sarbanes-Oxley compliance, internal controls, audit trails, and compliance reporting features."
    },
    {
        "id": "COMP-004",
        "name": "PCI Compliance Specialist",
        "description": "Helps with payment card industry compliance, secure payment processing, and PCI DSS requirements."
    },
    {
        "id": "COMP-005",
        "name": "Accessibility Specialist",
        "description": "Assists with accessibility features in Intuit products, ADA compliance, screen reader compatibility, and accessible design."
    },
    
    # Advanced Features Specialists
    {
        "id": "ADV-001",
        "name": "API Integration Specialist",
        "description": "Assists developers with Intuit API integration, OAuth, API documentation, and custom integrations."
    },
    {
        "id": "ADV-002",
        "name": "Custom Reports Specialist",
        "description": "Helps create advanced custom reports, report formulas, filtered reports, and complex reporting requirements."
    },
    {
        "id": "ADV-003",
        "name": "Workflow Automation Specialist",
        "description": "Assists with automating workflows, creating automated rules, recurring transactions, and process automation."
    },
    {
        "id": "ADV-004",
        "name": "Multi-Company Management Specialist",
        "description": "Helps manage multiple company files, switch between companies, consolidated reporting, and multi-entity accounting."
    },
    {
        "id": "ADV-005",
        "name": "Advanced Inventory Specialist",
        "description": "Assists with advanced inventory features including FIFO/LIFO, lot tracking, serial numbers, and complex inventory scenarios."
    },
    {
        "id": "ADV-006",
        "name": "Class and Location Tracking Specialist",
        "description": "Helps set up and use class tracking, location tracking, department accounting, and segment reporting."
    },
    {
        "id": "ADV-007",
        "name": "Project Profitability Specialist",
        "description": "Assists with tracking project profitability, job costing analysis, project-based reporting, and margin analysis."
    },
    {
        "id": "ADV-008",
        "name": "Advanced Payroll Features Specialist",
        "description": "Helps with advanced payroll features including certified payroll, union reporting, prevailing wage, and complex payroll scenarios."
    },
    {
        "id": "ADV-009",
        "name": "Consolidated Financial Reporting Specialist",
        "description": "Assists with consolidated financial statements, intercompany eliminations, and multi-entity reporting."
    },
    {
        "id": "ADV-010",
        "name": "Budget vs Actual Analysis Specialist",
        "description": "Helps with budget creation, variance analysis, budget reporting, and financial performance analysis."
    },
    
    # Customer Success & Training Specialists
    {
        "id": "CS-001",
        "name": "New User Onboarding Specialist",
        "description": "Assists new users with getting started, initial setup, basic training, and product orientation."
    },
    {
        "id": "CS-002",
        "name": "Best Practices Specialist",
        "description": "Helps implement best practices, optimize workflows, improve efficiency, and maximize product value."
    },
    {
        "id": "CS-003",
        "name": "Training and Certification Specialist",
        "description": "Assists with product training, certification programs, educational resources, and learning paths."
    },
    {
        "id": "CS-004",
        "name": "Account Migration Specialist",
        "description": "Helps migrate from competitor products to Intuit products, data conversion, and transition planning."
    },
    {
        "id": "CS-005",
        "name": "ProAdvisor Support Specialist",
        "description": "Assists accounting professionals with ProAdvisor program, client management, and professional features."
    },
]


def get_specialist_by_id(specialist_id):
    """
    Retrieve a specialist by their ID.
    
    Args:
        specialist_id (str): The specialist ID (e.g., 'TAX-001')
    
    Returns:
        dict: The specialist dictionary or None if not found
    """
    for specialist in SPECIALISTS:
        if specialist['id'] == specialist_id:
            return specialist
    return None


def get_specialists_by_category(category_prefix):
    """
    Get all specialists in a specific category.
    
    Args:
        category_prefix (str): The category prefix (e.g., 'TAX', 'QB', 'PAY')
    
    Returns:
        list: List of specialists in that category
    """
    return [s for s in SPECIALISTS if s['id'].startswith(category_prefix)]


def get_all_specialist_descriptions():
    """
    Get all specialist descriptions as a list of tuples (id, description).
    Useful for creating embeddings for vector search.
    
    Returns:
        list: List of tuples containing (id, name, description)
    """
    return [(s['id'], s['name'], s['description']) for s in SPECIALISTS]


def get_specialist_count():
    """
    Get the total number of specialists in the dictionary.
    
    Returns:
        int: Total count of specialists
    """
    return len(SPECIALISTS)


def get_categories():
    """
    Get all unique specialist categories.
    
    Returns:
        list: List of category prefixes
    """
    categories = set()
    for specialist in SPECIALISTS:
        category = specialist['id'].split('-')[0]
        categories.add(category)
    return sorted(list(categories))


if __name__ == "__main__":
    # Example usage
    print(f"Total specialists: {get_specialist_count()}")
    print(f"\nCategories: {', '.join(get_categories())}")
    
    print("\nSample specialists:")
    for i, specialist in enumerate(SPECIALISTS[:5]):
        print(f"\n{i+1}. {specialist['name']} ({specialist['id']})")
        print(f"   {specialist['description']}")

