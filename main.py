from csv2latex.coverter import Converter
from pathlib import Path

# The script creates a folder named the same as the input filename at the end of the defined path below
output_filepath = Path("C:/Users/Leon.hergesic.adamov/OneDrive/Dokumenti/knjige/skripte")

# If the alias name is left empty, the bash alias will not be created
bash_aliases_path = "C:/Users/Leon.hergesic.adamov/AppData/Local/Packages/CanonicalGroupLimited" \
                    ".UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/home "
alias_name = None

# The script can automatically add .tex file alias to the .bash_aliases.
# In that case, the <output_filepath> is the same path that the alias will be linked to
# If you do not want to use this feature, set "alias" to None.
bash_aliases = {
    "alias_path": bash_aliases_path,
    "alias": "tew"
}

conv = Converter(
    tex_path=output_filepath,
    bash_aliases=bash_aliases,
    latex_author="Leon"
)
