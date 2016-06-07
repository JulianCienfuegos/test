import random
import sys

class LinearEquations(object):
    def __init__(self):
        pass
    def find_intercept1(self, multiple_choice=False):
        m = random.randint(1, 10)
        x1 = random.randint(4, 20)
        y1 = random.randint(2, 15)
        while y1 - m*x1 == 0:
           m = random.randint(1, 10)
           x1 = random.randint(4, 20)
           y1 = random.randint(2, 15)
        sys.stdout.write("\item The slope of a line is {}. A coordinate on the line is ({}, {}). What is the intecept of the line?\n".format(m, x1, y1))
        if multiple_choice:
            right_answer = y1 - m*x1
            val_range = (-2*right_answer, 2*right_answer)
            low = min(val_range)
            high = max(val_range)
            a1 = random.randint(low, high)
            a2 = random.randint(low, high)
            while a2 == a1:
                a2 = random.randint(low, high)
            a3 = random.randint(low, high)
            while a3 in [a1, a2, right_answer]:
                a3 = random.randint(low, high)
            answers = [a1, a2, a3, right_answer]
            random.shuffle(answers)
            sys.stdout.write("\\begin{enumerate}\n")
            for a in answers:
                sys.stdout.write("\\item {}\n".format(a))
            sys.stdout.write("\\end{enumerate}\n")
    def find_intercept2(self, multiple_choice=False):
        m = random.randint(-20, -1)
        x1 = random.randint(-1, 10)
        b = random.randint(30, 60)
        sys.stdout.write("\item The slope of a line is {}. The y intercept is {}. What is the x intercept of the line?.\n".format(m, b))

class LatexDocument(object):
    def __init__(self, introduction="This is a test"):
        sys.stdout.write("\\documentclass[fleqn]{article}\n")
        sys.stdout.write("\\usepackage[left=1in, right=1in, top=1in, bottom=1in]{geometry}\n")
        sys.stdout.write("\\usepackage{mathexam}\n")
        sys.stdout.write("\\usepackage{amsmath}\n")
        sys.stdout.write("\\ExamClass{Sample Class}\n")
        sys.stdout.write("\\ExamName{Sample Exam}\n")
        sys.stdout.write("\\ExamHead{\\today}\n")
        sys.stdout.write("\\let\ds\displaystyle\n")
        sys.stdout.write("\\begin{document}\n")
        sys.stdout.write("\\ExamInstrBox{\n")
        sys.stdout.write(introduction+"}\n")
        sys.stdout.write("\\ExamNameLine\n")
        sys.stdout.write("\\begin{enumerate}\n")
    def end_document(self):    
        sys.stdout.write("\\end{enumerate}\n")
        sys.stdout.write("\\end{document}")
if __name__=="__main__":
    le = LinearEquations()
    ld = LatexDocument("This is an exam")
    le.find_intercept1(multiple_choice=True)
    le.find_intercept1()
    le.find_intercept1()
    le.find_intercept2()
    le.find_intercept2()
    ld.end_document()
