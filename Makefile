all: rapport clean

rapport:
	pdflatex -interaction batchmode report/rapport.tex
	pdflatex -interaction batchmode report/rapport.tex

vrapport:
	pdflatex report/rapport.tex
	pdflatex report/rapport.tex

clean:
	rm -rf *.log *.aux *.toc
	rm -f chapters/*.aux

cleanall: clean
	rm -f *.pdf
