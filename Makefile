IMG = problem_1.pdf problem_2.pdf problem_4.pdf problem_5.pdf \
      problem_6.pdf problem_7.pdf problem_3.pdf array_job.pdf \
      database.pdf mpi.pdf webapp.pdf qr.png

all:	taskfarm_slides.pdf taskfarm_presentation.pdf

problem_1.pdf problem_2.pdf problem_4.pdf problem_5.pdf problem_6.pdf problem_7.pdf problem_3.pdf:	generate_images.py
	python3 generate_images.py

%.pdf:	%.dia
	dia -e $@ -t pdf $<

qr.png:	genqr.sh
	./genqr.sh

%.pdf:	%.tex taskfarm.tex $(IMG)
	pdflatex $<
	pdflatex $<

clean::
	rm -f taskfarm.pdf $(IMG)
