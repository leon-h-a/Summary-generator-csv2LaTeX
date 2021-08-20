<h1 align="center"> Summary Generator csv2LaTeX</h1>

Extract highlighted text from pdf's via LaTeX.

The old option is the usual split-screen with pdf on one and Word on the other side. This option is also followed by the continous copy-paste agony and manual entry of the page the highlight was on. Not to mention other quirks...

The other option is to open you favourite pdf reader, full screen it, highlight easily as you would normaly do. When you finish, export as .csv, plug it inside this script and out you get a .tex/.pdf document with your highlight!

## Prerequisites
 - [WSL](https://docs.microsoft.com/en-us/windows/wsl/)
 - [LaTeX for WSL](https://medium.com/@Pirmin/a-minimal-latex-setup-on-windows-using-wsl2-and-neovim-51259ff94734)

## Getting started
 1. Install requirements with `pip3 install -r requirements.txt`
 2. Set input and output folder paths in main.py and place .csv file inside input folder
 3. Run script with `python3 main.py`
