ASSIGNMENT = assignment
SOLUTION = solution
RUBRIC = rubric
QUIZ = quiz
QUIZ2 = quiz_late
LATEX = pdflatex
penultimateword = $(wordlist $(words $1),$(words $1), x $1)

all: $(ASSIGNMENT) $(SOLUTION) $(RUBRIC) $(QUIZ) $(QUIZ2)

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

$(QUIZ2):
	$(LATEX) $(QUIZ2).tex
	@mv $(QUIZ2).pdf ../12-752_$(call penultimateword,$(subst /, ,$(CURDIR)))_Quiz_Late.pdf

clean:
	-rm -f *.aux *.log *.pdf  *.out *~
