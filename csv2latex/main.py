from csv2latex.coverter import Converter

# Set LaTeX doc type
# Set how headers are recognised and in what cell i.e. A$3
# Set font, font size, color, bold/italic etc...

conv = Converter(
    latex_type="journal",
    font="Colibri",
    font_size=12,
    heading_size=16
)

conv.run()