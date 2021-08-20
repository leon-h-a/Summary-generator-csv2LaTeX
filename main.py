from csv2latex.coverter import Converter
from pathlib import Path

input_folder = ""
output_folder = Path("")

# If the alias name is left as None, the bash alias will not be created
bash_aliases_path = ""
alias_name = ""

bash_aliases = {
    "alias_path": bash_aliases_path,
    "alias": None
}

conv = Converter(
    input_folder=input_folder,
    output_folder=output_folder,
    bash_aliases=bash_aliases,
    latex_author="Author"
)
