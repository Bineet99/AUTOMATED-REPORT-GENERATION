import pandas as pd
from fpdf import FPDF

df = pd.read_csv("data.csv")

total = len(df)
avg_age = df["Age"].mean()
avg_salary = df["Salary"].mean()
dept_count = df["Department"].value_counts()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Employee Report", ln=True, align='C')
pdf.ln(10)
pdf.cell(200, 10, txt=f"Total Employees: {total}", ln=True)
pdf.cell(200, 10, txt=f"Average Age: {avg_age:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Average Salary: Rs. {avg_salary:.2f}", ln=True)
pdf.ln(5)
pdf.cell(200, 10, txt="Employees per Department:", ln=True)

for dept, count in dept_count.items():
    pdf.cell(200, 10, txt=f" - {dept}: {count}", ln=True)

pdf.output("employee_report.pdf")
