from fpdf import FPDF
import sys, requests, os, time, unicodedata

def pdfCreate(title, steps, url):
    if not os.path.exists("temp"):
        os.mkdir("temp")
    pdf = FPDF(format='letter')
    pdf.add_font('DejaVuSansMono','','DejaVuSansMono.ttf',uni=True)
    
    pdf.add_page()
    effective_page_width = pdf.w - 2*pdf.l_margin
    pdf.set_font("DejaVuSansMono", size=20)
    pdf.multi_cell(0, 10, txt=title, align="C")

    print(url)    
    x=0
    stepCount = len(steps)
    while x<stepCount-1:
        time.sleep(1)
        imgurl = steps[x]["pic"]
        if imgurl != None:
            img_data = requests.get(imgurl).content
            imgfile = "temp/"+imgurl.rsplit('/', 1)[1]
            with open(imgfile, 'wb') as handler:
                handler.write(img_data)
                handler.close()
            pdf.image(imgfile, w=effective_page_width)

        pdf.set_font("DejaVuSansMono", size=18)
        pdf.multi_cell(effective_page_width, 10, txt=str(x+1)+". "+steps[x]["step"])
        pdf.ln(5)
        pdf.set_font("DejaVuSansMono", size=12)
        pdf.multi_cell(effective_page_width, 10, txt=steps[x]["detailed"])
        pdf.ln(5)
        x+=1

    pdf.output("simple_demo.pdf")