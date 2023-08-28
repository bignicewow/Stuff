from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 50)
        self.cell(80)
        self.cell(30, 20, "CS50 Shirtificate", align="C")
        self.ln(20)


    def footer(self):
        pass


    def centered_text(self, text):
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "B", 25)
        self.cell(0, 200, text, new_x="LMARGIN", new_y="NEXT", align='C')
        self.set_text_color(0,0,0)


name = input("Name: ")
pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.image("shirtificate.png", x=0, y=60)
pdf.set_font("Times", size=36)
pdf.centered_text(f"{name} took CS50")
pdf.output("shirtificate.pdf")