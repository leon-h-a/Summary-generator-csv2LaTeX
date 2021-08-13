from pylatex import Document, Section, Command, NoEscape, NewPage, HugeText, VerticalSpace, NewLine
import os


def create_latex_doc():
    return Document('basic')


def create_titlepage(doc, title, author):
    # \usepackage[showframe, margin=1in]{geometry}
    # \setlength{\parskip}{1em}
    # \setlength{\perindent}{0ex}
    doc.preamble.append(HugeText(Command('title', title)))
    doc.preamble.append(Command('author', author))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))
    doc.append(NewPage())


def insert_h1(doc, textblock):
    with doc.create(Section(textblock.text, numbering=False)):
        doc.append(' ')


def insert_paragraph(doc, textblock, newline):
    clean_text = textblock.text.replace('\n', ' ').replace('\r', '')

    doc.append('(' + textblock.page + ') - ' + clean_text)
    if newline:
        doc.append(VerticalSpace("5mm"))
        doc.append(NewLine())


def tex_file_exists(path, filename):
    if (path / filename).exists():
        return True


def generate_tex_file(doc, path, filename):
    os.mkdir(path / filename)
    doc.generate_tex(str(path/filename/filename))
