from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("../docs/fpdf2-logo.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Title", border=1, align="C")
        # Performing a line break:
        self.ln(50)


def main():
    name = input("Name: ")

    pdf = FPDF(unit="mm", format="A4")
    pdf.add_page()
    pdf.set_margins(0, 10, 0)

    pdf.image('shirtificate.png', x=1, y=60)
    pdf.set_font("helvetica", "B", 40)
    pdf.cell(0, 40, text="CS50 Shirtificate", align="C")
    # current_x = FPDF.get_x(pdf)
    # print(current_x)
    # current_y = FPDF.get_y(pdf)
    # print(current_y)

    pdf.set_xy(0, 90)
    # current_x = FPDF.get_x(pdf)
    # print(current_x)
    # current_y = FPDF.get_y(pdf)
    # print(current_y)

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 40)
    pdf.cell(0, 100, text=f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
