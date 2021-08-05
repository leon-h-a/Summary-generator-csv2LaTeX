from csv2latex.coverter import Converter

output_filepath = "C:\\some\\path"

# Set LaTeX doc type
tex_type = "journal"

# The script can automatically add .tex file alias to the .bash_aliases.
# In that case, the <output_filepath> is the same path that the alias will be linked to
# If you do not want to use this feature, set "alias" to None.
bash_aliases = {
    "alias": None
}

conv = Converter(
    latex_doc_type="tex_type",
    bash_aliases=bash_aliases,
    latex_author="Leon"
)
