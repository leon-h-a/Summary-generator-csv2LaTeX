from csv2latex.coverter import Converter

# todo: run script by drag & dropping the .csv file on .py script

# Set LaTeX doc type
# Set how headers are recognised and in what cell i.e. A$3 (Excel)
# Optional: Set font, font size, color, bold/italic etc...

conv = Converter(
    latex_doc_type="journal"
)
