from pylatex import Document, Section, Command, NoEscape, NewPage, HugeText, NewLine


def create_latex_doc():
    return Document('basic')


def create_titlepage(doc, title, author):
    doc.preamble.append(HugeText(Command('title', title)))
    doc.preamble.append(Command('author', author))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))
    doc.append(NewPage())


def insert_h1(doc, textblock):
    with doc.create(Section(textblock.text, numbering=False)):
        doc.append(' ')


def insert_paragraph(doc, textblock):
    doc.append("(" + textblock.page + ") - ")
    doc.append(textblock.text)
    doc.append(NewLine())
    doc.append(NewLine())


def generate_tex_file(doc, path):
    doc.generate_tex(path)
