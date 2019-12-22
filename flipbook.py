from fpdf import FPDF

title = 'I hope I get this job'
     
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.set_draw_color(204, 242, 255)
        self.set_fill_color(204, 242, 255)
        self.set_text_color(220, 50, 50)
        self.set_line_width(1)
        self.cell(0, 9, title, 0, 1, 'C', 1)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        self.set_font('Arial', '', 12)
        self.set_fill_color(204, 255, 238)
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, name):
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        self.set_font('Times', '', 12)
        self.multi_cell(0, 5, txt)

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)

    def flip_the_book(self, num, title, x, y, scale, no_of_pages):
        for i in range(no_of_pages):
                self.add_page()
                self.chapter_title(num, title)
                self.image('artwork1.jpg', 30, 60, 150)
                
    def flip_the_book_scale_up(self, num, title, x, y, from_scale, to_scale):
        for i in range(from_scale, to_scale+1, 10):
                self.add_page()
                self.chapter_title(num, title)
                self.image('artwork1.jpg', 30, 60, i)
                
    def flip_the_book_scale_down(self, num, title, x, y, from_scale, to_scale):
        for i in range(from_scale, to_scale+1, -10):
                self.add_page()
                self.chapter_title(num, title)
                self.image('artwork1.jpg', 30, 60, i)
        

pdf = PDF()
pdf.set_title(title)
pdf.set_author('Rushali Mohbe')
pdf.print_chapter(1, 'My school life', 'school.txt')
pdf.print_chapter(2, 'My college life', 'college.txt')
pdf.flip_the_book(3,'Static Flip Book', 30, 60, 150, 1)
pdf.flip_the_book_scale_up(4,'Scale up Flip Book', 30, 60, 100, 150)
pdf.flip_the_book_scale_down(5,'Scale down Flip Book', 30, 60, 150, 100)
pdf.output('RobotsUnite.pdf', 'F')
