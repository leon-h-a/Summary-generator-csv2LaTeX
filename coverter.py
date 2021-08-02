from utils.csv import *
from utils.latex import *


class Converter:
    def __init__(self,
                 latex_type,
                 font,
                 font_size: int,
                 heading_size: int):

        self.latex_type = latex_type
        self.font = font
        self.font_size = font_size
        self.heading_size = heading_size

        raise NotImplemented

    def run(self):
        self.load_csv()
        self.create_LaTeX_doc()
        self.populate_LaTeX_doc()

    def load_csv(self):
        # Use from utils.csv
        raise NotImplemented

    def create_LaTeX_doc(self):
        # Use from utils.latex
        raise NotImplemented

    def populate_LaTeX_doc(self):
        # Use from utils.latex
        raise NotImplemented
