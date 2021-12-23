@default_files = ('main.tex');

# generate pdf using pdflatex
$pdf_mode = 1;

# use bibtex if .bib file exists
$bibtex_use = 1;

# use this pdflatex command line
$pdflatex = 'pdflatex -synctex=1 --interaction=nonstopmode';

# use skim as pdf viewer
$pdf_viewer = 'open -a Skim';

# remove files on clean
$clean_ext = 'symctex.gz, sympy';

# handle pythontex blocks
@generated_exts = (@generated_exts, 'synctex.gz', 'pythontex');
add_cus_dep('pytxcode', 'tex', 0, 'pythontex');
sub pythontex { return system("pythontex \"$_[0]\""); }
