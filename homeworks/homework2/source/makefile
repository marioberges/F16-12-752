ASSIGNMENT = assignment
SOLUTION = solution
RUBRIC = rubric
QUIZ = quiz
LATEX = pdflatex
penultimateword = $(wordlist $(words $1),$(words $1), x $1)

all: $(ASSIGNMENT) $(SOLUTION) $(RUBRIC) $(QUIZ)

$(ASSIGNMENT): 
	$(LATEX) $(ASSIGNMENT).tex
	@mv $(ASSIGNMENT).pdf ../12-752_$(call penultimateword,$(subst /, ,$(CURDIR))).pdf
	
$(SOLUTION):	
	$(LATEX) $(SOLUTION).tex
	@mv $(SOLUTION).pdf ../12-752_$(call penultimateword,$(subst /, ,$(CURDIR)))_Solution.pdf

$(RUBRIC):
	$(LATEX) $(RUBRIC).tex
	@mv $(RUBRIC).pdf ../12-752_$(call penultimateword,$(subst /, ,$(CURDIR)))_Rubric.pdf

$(QUIZ):
	$(LATEX) $(QUIZ).tex
	@mv $(QUIZ).pdf ../12-752_$(call penultimateword,$(subst /, ,$(CURDIR)))_Quiz.pdf

clean:
	-rm -f *.aux *.log *.pdf  *.out *~
