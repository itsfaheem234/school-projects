# python quiz application 

### quiz application with timer and analysis

A desktop-based interactive quiz application built using **Python and Tkinter**. The application tests knowledge of Python programming concepts through randomly selected multiple-choice questions, while providing a timed quiz experience, automatic scoring, and performance grading.

This project was developed as a **Class XI Computer Science project** during the 2025–2026 academic year.

---

## features

* Python programming quiz
* graphical user interface using Tkinter
* randomly shuffled questions
* 10 multiple-choice questions per attempt
* 5-minute countdown timer
* automatic score calculation
* percentage calculation
* grade-based performance evaluation
* dedicated instructions screen
* progress bar during the quiz
* input validation
* retry quiz functionality
* dark-themed interface

The question bank contains predefined Class XI Python questions covering topics such as functions, data types, operators, loops, dictionaries, lists, strings, and exception handling.

---

## application flow

```text
welcome screen
      │
      ▼
instructions
      │
      ▼
start quiz
      │
      ▼
10 randomized questions
      │
      ├── 5-minute timer
      │
      ├── answer validation
      │
      └── progress tracking
      │
      ▼
results
      │
      ├── score
      ├── percentage
      └── grade
      │
      ▼
retry / exit
```

---

## technology used

| technology    | purpose                         |
| ------------- | ------------------------------- |
| Python        | core programming language       |
| Tkinter       | graphical user interface        |
| `tkinter.ttk` | progress bar and themed widgets |
| `messagebox`  | warnings and notifications      |
| `random`      | question shuffling              |
| `time`        | timer-related functionality     |

The project uses only Python and its associated standard-library modules, so no external packages are required.

---

## quiz system

Each quiz attempt contains **10 questions** selected from the predefined question bank.

* each correct answer = **1 point**
* maximum score = **10**
* total time = **5 minutes**
* questions cannot be revisited
* the quiz automatically ends when the timer reaches zero

## The timer is implemented using Tkinter's `after()` method and displays the remaining time in `MM:SS` format.

## grading system

| percentage | grade                |
| ---------: | -------------------- |
| 90% – 100% | A+ — Outstanding     |
|  75% – 89% | A — Great Job        |
|  60% – 74% | B — Good Work        |
|  40% – 59% | C — Keep Practicing  |
|  below 40% | D — Need Improvement |

The application calculates the percentage automatically after the quiz and displays the corresponding performance grade.

---

## concepts demonstrated

### object-oriented programming

The application is structured around a `QuizApp` class, with separate methods handling different parts of the application such as:

* welcome screen
* instructions
* question display
* answer checking
* results
* retry functionality

### GUI programming

Tkinter widgets are used to create the interface, including:

* `Label`
* `Button`
* `Radiobutton`
* `Frame`
* `Progressbar`

### data structures

Questions are stored using a **list of dictionaries**, with each dictionary containing:

```python
{
    "question": "...",
    "options": [...],
    "answer": ...
}
```

### control flow

The project uses:

* `if / elif / else`
* `for` loops
* method calls
* conditional validation

### other concepts

* variables and data types
* functions and methods
* event handling
* randomization
* exception/input validation
* countdown timers
* formatted output

These concepts are documented in the original Class XI project report.

---

## requirements

### hardware

* Intel Core i3 or equivalent processor
* 2 GB RAM
* 100 MB free storage
* 1024 × 768 display
* keyboard and mouse

### software

* Python 3.7 or higher
* Windows, macOS, or Linux
* IDLE, PyCharm, VS Code, or another Python IDE

Tkinter is included with standard Python installations.

---

## how to run

### 1. clone the repository

```bash
git clone https://github.com/your-username/python-quiz.git
cd python-quiz
```

### 2. run the program

```bash
python quiz.py
```

No additional Python packages are required.

---

## project structure

```text
python-quiz/
│
├── quiz.py
├── screenshots/
│   ├── welcome.png
│   ├── instructions.png
│   ├── quiz.png
│   └── results.png
│
└── README.md
```

*Rename `quiz.py` and the screenshot files to match the actual files in your repository.*

---

## future improvements

The original project identified several possible improvements:

* expand the question bank to 50–100 questions
* introduce difficulty levels
* cover more Class XI syllabus topics
* add an SQLite database
* store user profiles and score history
* add hints and answer explanations
* introduce negative marking
* add pause/resume functionality
* allow answer review
* add multiple themes
* add keyboard shortcuts
* generate PDF performance reports
* display time-per-question statistics
* add performance graphs
* compare previous attempts

---

## project information

**project:** Quiz Application With Timer and Analysis

**subject:** Computer Science

**class:** XI-A

**academic year:** 2025–2026

**developers:** Faheem Mohammed Shabeer & Saad Ahamed Hashim

---

## references

* *Computer Science with Python – Class XI* — Sumita Arora
* *Python Programming: An Introduction to Computer Science* — John Zelle
* *Learning Python* — Mark Lutz
* Python Documentation
* Tkinter Documentation
* W3Schools Python Tutorial
* GeeksforGeeks Python Programming
* Real Python Tkinter Tutorial

---

## license

This project was developed for educational purposes as part of the Class XI Computer Science curriculum.
