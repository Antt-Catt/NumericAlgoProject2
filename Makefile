all: rapport clean

rapport:
	pdflatex -interaction batchmode rapport.tex
	pdflatex -interaction batchmode rapport.tex

vrapport:
	pdflatex rapport.tex
	pdflatex rapport.tex

clean:
	rm -rf *.log *.aux *.toc
	rm -f chapters/*.aux

cleanall: clean
	rm -f *.pdf
