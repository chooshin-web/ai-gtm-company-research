from datetime import datetime
import os

# Sample company database
companies = {
    "OpenAI": {
        "industry": "Artificial Intelligence",
        "website": "https://openai.com",
        "pain_points": [
            "Scaling enterprise adoption",
            "Managing AI infrastructure",
            "Developer engagement"
        ]
    },

    "HubSpot": {
        "industry": "CRM Software",
        "website": "https://hubspot.com",
        "pain_points": [
            "Customer retention",
            "Sales pipeline optimization",
            "Marketing automation"
        ]
    },

    "Stripe": {
        "industry": "Financial Technology",
        "website": "https://stripe.com",
        "pain_points": [
            "Global payment compliance",
            "Merchant onboarding",
            "Fraud prevention"
        ]
    }
}

# Ask the user for a company
company_name = input("Enter a company name (OpenAI, HubSpot, Stripe): ").strip().lower()

# Find the matching company regardless of capitalization
company = None
real_company_name = None

for name in companies:
    if name.lower() == company_name:
        company = companies[name]
        real_company_name = name
        break

if company is None:
    print("\n❌ Company not found in the sample database.")
    exit()

# Create report
report = f"""
=========================================
AI GTM COMPANY RESEARCH REPORT
=========================================

Generated:
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Company:
{real_company_name}

Industry:
{company['industry']}

Website:
{company['website']}

Key Business Pain Points:
"""

for pain in company["pain_points"]:
    report += f"- {pain}\n"

report += """

Recommended Outreach Strategy:
- Personalize the first email.
- Mention a recent company achievement.
- Explain how your solution saves time or money.
- End with a clear call-to-action.

=========================================
End of Report
=========================================
"""

# Display report
print(report)

# Save report
os.makedirs("outputs", exist_ok=True)

filename = f"outputs/{real_company_name.lower()}_report.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write(report)

print(f"\n✅ Report successfully saved as: {filename}")