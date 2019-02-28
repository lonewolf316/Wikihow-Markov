from fpdf import FPDF

def pdfCreate(title, steps, url):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("times", size=12)
    pdf.cell(200, 10, txt=title, ln=1, align="C")

    print(url)    
    x=0
    stepCount = len(steps)
    while x<stepCount-1:
        pdf.set_font("times", size=18)
        pdf.cell(200, 10, txt=str(x)+"."+"\n"+steps[x]["step"], ln=1, align="C")
        #print(steps[x]["pic"])
        pdf.set_font("times", size=12)
        pdf.cell(200, 10, txt=steps[x]["detailed"], ln=1, align="C")
        x+=1

    pdf.output("simple_demo.pdf")