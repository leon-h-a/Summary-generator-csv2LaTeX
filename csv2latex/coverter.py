from utils import csv
from utils import latex


class Converter:
    def __init__(self,
                 latex_doc_type):
        # csv
        self.csv_filepath = None
        self.csv_filename = None
        self.csv_data = None

        # LaTeX
        self.latex_type = latex_doc_type
        self.latex_doc = None

        self.run()

    def run(self):
        self.load_csv()
        self.create_latex_doc()
        self.populate_latex_doc()
        self.generate_tex_file()

    def load_csv(self):
        self.csv_filepath = csv.get_csv_filpath()

    def create_latex_doc(self):
        self.latex_doc = latex.create_latex_doc()

    def populate_latex_doc(self):
        latex.insert_section(
            doc=self.latex_doc,
            section_title="Title",
            section_text="Text",
        )

    def generate_tex_file(self):
        raise NotImplemented
