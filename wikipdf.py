from fpdf import FPDF
import sys


def pdfCreate(title, steps, url):
    pdf = FPDF()
    pdf.add_font('arial','','arial.ttf',uni=True)
    pdf.add_page()
    pdf.set_font("arial", size=12)
    pdf.cell(10, 10, txt=title, ln=2, align="C")

    print(url)    
    x=0
    stepCount = len(steps)
    while x<stepCount-1:
        pdf.set_font("arial", size=18)
        pdf.cell(10, 10, txt=str(x+1)+". "+steps[x]["step"], ln=2, align="L")
        #print(steps[x]["pic"])
        pdf.set_font("arial", size=12)
        pdf.cell(10, 10, txt=steps[x]["detailed"], ln=2, align="L")
        x+=1

    pdf.output("simple_demo.pdf")