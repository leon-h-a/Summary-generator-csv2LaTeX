from pylatex import Document, Section


def create_latex_doc():
    return Document('basic')


def insert_section(doc, section_title, section_text):
    with doc.create(Section(section_title)):
        doc.append(section_text)
    return doc


def create_tex_file(doc):
    raise NotImplemented
