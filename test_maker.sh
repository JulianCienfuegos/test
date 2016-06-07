export test_file="test.tex"
export pdf="test.pdf"
python make_test.py > $test_file
pdflatex $test_file
evince $pdf
