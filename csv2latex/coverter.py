from csv2latex.utils import csv
from csv2latex.utils import latex
from csv2latex.utils import bash
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s:%(message)s')


class Converter:
    def __init__(self,
                 input_folder,
                 output_folder,
                 latex_author,
                 bash_aliases,
                 ):

        # csv
        self.input_folder = input_folder
        self.csv_filepath = None
        self.csv_filename = None
        self.csv_text_blocks = list()

        # LaTeX
        self.latex_doc = None
        self.latex_author = latex_author
        self.output_folder = output_folder

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
        if self.bash_aliases["alias"] is not None:
            self.add_bash_alias()

    def locate_csv(self):
        self.csv_filepath = csv.get_csv_file(self.input_folder)
        self.csv_filename = csv.get_csv_excaped_filename(self.csv_filepath)

        logging.info('FILE PATH = {}'.format(self.csv_filepath))
        logging.info('FILE NAME = {}'.format(self.csv_filename))

    def parse_csv(self):
        self.csv_text_blocks = csv.parse_csv(self.csv_filepath)

    def create_latex_doc(self):
        self.latex_doc = latex.create_latex_doc()
        logging.info('CREATED TEX DOC IN MEMORY')

    def create_latext_titlepage(self):
        latex.create_titlepage(self.latex_doc, title=self.csv_filename, author=self.latex_author)

    def populate_latex_document(self):
        for block in self.csv_text_blocks:
            if block.style == "H1":
                latex.insert_h1(self.latex_doc, block)
            else:
                latex.insert_paragraph(self.latex_doc, block)

    def generate_tex_file(self):
        if latex.tex_file_exists(self.output_folder, self.csv_filename):
            logging.warning("Tex file directory ({}) already exists. The files inside will not be overwritten.".format(self.output_folder / self.csv_filename))
        else:
            latex.generate_tex_file(self.latex_doc, self.output_folder, self.csv_filename)
            logging.info('TEX FILE GENERATED')

    def add_bash_alias(self):
        bash.add_bash_alias(self.bash_aliases["alias_path"], self.bash_aliases["alias"], self.output_folder, self.csv_filename)
        logging.info("BASH ALIAS '{}' ADDED".format(self.bash_aliases["alias"]))
