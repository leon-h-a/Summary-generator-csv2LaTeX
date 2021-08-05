from csv2latex.utils import csv
from csv2latex.utils import latex
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s:%(message)s')


class Converter:
    def __init__(self,
                 latex_doc_type,
                 bash_aliases,
                 latex_author
                 ):

        self.latex_author = latex_author

        # csv
        self.csv_filepath = None
        self.csv_filename = None
        self.csv_text_blocks = list()

        # LaTeX
        self.latex_type = latex_doc_type
        self.latex_doc = None

        # bash
        self.bash_aliases = bash_aliases

        self.run()

    def run(self):
        self.locate_csv()
        self.parse_csv()

        self.create_latex_doc()
        self.create_latext_titlepage()
        self.populate_latex_document()
        self.generate_tex_file()

        # self.add_bash_alias()

    def locate_csv(self):
        self.csv_filepath = csv.get_csv_filepath()
        self.csv_filename = csv.get_csv_filename(self.csv_filepath)

        logging.info('FILE PATH = {}'.format(self.csv_filepath))
        logging.info('FILE NAME = {}'.format(self.csv_filename))

    def parse_csv(self):
        self.csv_text_blocks = csv.parse_csv(self.csv_filepath)

    def create_latex_doc(self):
        self.latex_doc = latex.create_latex_doc()

    def create_latext_titlepage(self):
        latex.create_titlepage(self.latex_doc, title=self.csv_filename, author=self.latex_author)

    def populate_latex_document(self):
        for block in self.csv_text_blocks:
            if block.style == "H1":
                latex.insert_h1(self.latex_doc, block)
            else:
                latex.insert_paragraph(self.latex_doc, block)

    def generate_tex_file(self):
        path = "C:\\Users\\Leon.hergesic.adamov\\Desktop\\testfile"

        latex.generate_tex_file(self.latex_doc, path)
        logging.info('TEX FILE GENERATED')
