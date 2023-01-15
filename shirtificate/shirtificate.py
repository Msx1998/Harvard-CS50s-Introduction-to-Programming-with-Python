from fpdf import FPDF


class PDF:
    def __init__(self,name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("Arial",size=12)
        self._pdf.cell(0,50, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="c")
        self._pdf.image("shirtificate.png",w=self._pdf.epw)
        self._pdf.set_font_size(50)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(x=50, y=150, txt=f"{name} took CS50")

    def save(self,name):
        self._pdf.output(name)


def main():
    name = input("Enter your name:")
    pdf = PDF(name)
    pdf.save("shirtificate.pdf")


if __name__=="__main__":
    main()
