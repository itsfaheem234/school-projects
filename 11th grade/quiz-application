import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz - Class 11 CS")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")
  # Quiz data - Class 11 CS NCERT based questions
        self.questions = [
            {
                "question": "What is Python?",
                "options": ["A snake", "A high-level programming language", "A database", "An operating system"],
                "answer": 1
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["function", "def", "define", "func"],
                "answer": 1
            },
            {
                "question": "What is the output of: print(type([]))?",
                "options": ["<class 'tuple'>", "<class 'list'>", "<class 'dict'>", "<class 'set'>"],
                "answer": 1
            },
            {
                "question": "Which of the following is a mutable data type?",
                "options": ["Tuple", "String", "List", "Integer"],
                "answer": 2
            },
            {
                "question": "What does the len() function do?",
                "options": ["Returns length of object", "Converts to integer", "Creates a list", "None of these"],
                "answer": 0
            },
            {
                "question": "Which operator is used for exponentiation in Python?",
                "options": ["^", "**", "//", "%"],
                "answer": 1
            },
            {
                "question": "What is the correct way to create a dictionary?",
                "options": ["d = []", "d = ()", "d = {}", "d = <>"],
                "answer": 2
            },
            {
                "question": "Which loop is used when number of iterations is unknown?",
                "options": ["for loop", "while loop", "do-while loop", "infinite loop"],
                "answer": 1
            },
            {
                "question": "What is the output of: print(10 // 3)?",
                "options": ["3.33", "3", "4", "3.0"],
                "answer": 1
            },
            {
                "question": "Which keyword is used to handle exceptions in Python?",
                "options": ["catch", "try", "except", "Both B and C"],
                "answer": 3
            },
            {
                "question": "What is the correct syntax for a single line comment?",
                "options": ["// comment", "# comment", "/* comment */", "-- comment"],
                "answer": 1
            },
            {
                "question": "Which function is used to get input from user?",
                "options": ["input()", "get()", "read()", "scanf()"],
                "answer": 0
            },
            {
                "question": "What is the index of the first element in a Python list?",
                "options": ["1", "0", "-1", "Depends on list"],
                "answer": 1
            },
            {
                "question": "Which method is used to add an element at the end of a list?",
                "options": ["add()", "append()", "insert()", "push()"],
                "answer": 1
            },
            {
                "question": "What is the output of: print('Hello'[1])?",
                "options": ["H", "e", "l", "Error"],
                "answer": 1
            }
        ]
        
        # Shuffle questions for randomness
        random.shuffle(self.questions)
        
        # Select 10 questions
        self.questions = self.questions[:10]
        
        # Quiz state
        self.current_question = 0
        self.score = 0
        self.selected_answer = tk.IntVar()
        self.time_left = 300  # 5 minutes (300 seconds)
        self.timer_running = False
        
        # Show welcome screen
        self.show_welcome_screen()
    
    def show_welcome_screen(self):
        self.clear_screen()
        
        frame = tk.Frame(self.root, bg="#1e1e2e")
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        title = tk.Label(frame, text="🐍 Python Quiz", font=("Arial", 36, "bold"), 
                        bg="#1e1e2e", fg="#89dceb")
        title.pack(pady=20)
        
        subtitle = tk.Label(frame, text="Class 11 Computer Science", 
                           font=("Arial", 18), bg="#1e1e2e", fg="#cdd6f4")
        subtitle.pack(pady=10)
        
        info = tk.Label(frame, text="📝 10 Questions | ⏱️ 5 Minutes | 🎯 10 Points", 
                       font=("Arial", 14), bg="#1e1e2e", fg="#f5e0dc")
        info.pack(pady=20)
        
        start_btn = tk.Button(frame, text="Start Quiz", font=("Arial", 16, "bold"),
                             bg="#89b4fa", fg="#1e1e2e", padx=40, pady=15,
                             cursor="hand2", command=self.show_instructions)
        start_btn.pack(pady=20)
    
    def show_instructions(self):
        self.clear_screen()
        
        frame = tk.Frame(self.root, bg="#1e1e2e")
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        title = tk.Label(frame, text="📋 Instructions", font=("Arial", 28, "bold"),
                        bg="#1e1e2e", fg="#f9e2af")
        title.pack(pady=20)
        
        instructions = [
            "• Answer all 10 multiple choice questions",
            "• Each correct answer gives you 1 point",
            "• You have 5 minutes to complete the quiz",
            "• Select one option and click Next",
            "• You cannot go back to previous questions",
            "• Timer starts when you begin the quiz"
        ]
        
        for inst in instructions:
            label = tk.Label(frame, text=inst, font=("Arial", 13),
                           bg="#1e1e2e", fg="#cdd6f4", anchor="w")
            label.pack(pady=5, padx=20)
        
        begin_btn = tk.Button(frame, text="Begin Quiz", font=("Arial", 16, "bold"),
                             bg="#a6e3a1", fg="#1e1e2e", padx=40, pady=15,
                             cursor="hand2", command=self.start_quiz)
        begin_btn.pack(pady=30)
    
    def start_quiz(self):
        self.timer_running = True
        self.show_question()
        self.update_timer()
    
    def show_question(self):
        self.clear_screen()
        self.selected_answer.set(-1)
        
        # Header with timer
        header = tk.Frame(self.root, bg="#313244", height=80)
        header.pack(fill="x")
        
        q_num = tk.Label(header, text=f"Question {self.current_question + 1}/10",
                        font=("Arial", 16, "bold"), bg="#313244", fg="#cdd6f4")
        q_num.pack(side="left", padx=30, pady=20)
        
        self.timer_label = tk.Label(header, text="⏱️ 05:00", 
                                    font=("Arial", 18, "bold"),
                                    bg="#313244", fg="#f38ba8")
        self.timer_label.pack(side="right", padx=30, pady=20)
        
        # Progress bar
        progress = ttk.Progressbar(self.root, length=800, mode='determinate',
                                  value=(self.current_question / 10) * 100)
        progress.pack()
        
        # Question area
        q_frame = tk.Frame(self.root, bg="#1e1e2e")
        q_frame.pack(pady=40, padx=40, fill="both", expand=True)
        
        question_text = self.questions[self.current_question]["question"]
        q_label = tk.Label(q_frame, text=question_text, 
                          font=("Arial", 18, "bold"), bg="#1e1e2e", 
                          fg="#cdd6f4", wraplength=700, justify="left")
        q_label.pack(pady=30)
        
        # Options
        options = self.questions[self.current_question]["options"]
        
        for i, option in enumerate(options):
            rb = tk.Radiobutton(q_frame, text=option, variable=self.selected_answer,
                               value=i, font=("Arial", 14), bg="#1e1e2e",
                               fg="#cdd6f4", selectcolor="#45475a",
                               activebackground="#1e1e2e", activeforeground="#89dceb",
                               cursor="hand2", padx=20, pady=10)
            rb.pack(anchor="w", pady=8, padx=40)
        
        # Next button
        next_btn = tk.Button(self.root, text="Next →", font=("Arial", 14, "bold"),
                            bg="#89b4fa", fg="#1e1e2e", padx=30, pady=10,
                            cursor="hand2", command=self.next_question)
        next_btn.pack(pady=20)
    
    def next_question(self):
        if self.selected_answer.get() == -1:
            messagebox.showwarning("Warning", "Please select an answer!")
            return
        
        # Check answer
        correct_answer = self.questions[self.current_question]["answer"]
        if self.selected_answer.get() == correct_answer:
            self.score += 1
        
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.timer_running = False
            self.show_results()
    
    def update_timer(self):
        if self.timer_running and self.time_left > 0:
            self.time_left -= 1
            mins = self.time_left // 60
            secs = self.time_left % 60
            self.timer_label.config(text=f"⏱️ {mins:02d}:{secs:02d}")
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.timer_running = False
            messagebox.showinfo("Time's Up!", "Time has expired!")
            self.show_results()
    
    def show_results(self):
        self.clear_screen()
        
        frame = tk.Frame(self.root, bg="#1e1e2e")
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        title = tk.Label(frame, text="🎉 Quiz Complete!", font=("Arial", 32, "bold"),
                        bg="#1e1e2e", fg="#a6e3a1")
        title.pack(pady=20)
        
        percentage = (self.score / len(self.questions)) * 100
        
        score_text = tk.Label(frame, text=f"Your Score: {self.score}/{len(self.questions)}",
                             font=("Arial", 24, "bold"), bg="#1e1e2e", fg="#89dceb")
        score_text.pack(pady=15)
        
        percent_text = tk.Label(frame, text=f"Percentage: {percentage:.1f}%",
                               font=("Arial", 20), bg="#1e1e2e", fg="#cdd6f4")
        percent_text.pack(pady=10)
        
        # Grade
        if percentage >= 90:
            grade = "A+ Outstanding! 🌟"
            color = "#a6e3a1"
        elif percentage >= 75:
            grade = "A Great Job! 👏"
            color = "#89dceb"
        elif percentage >= 60:
            grade = "B Good Work! 👍"
            color = "#f9e2af"
        elif percentage >= 40:
            grade = "C Keep Practicing! 📚"
            color = "#fab387"
        else:
            grade = "D Need Improvement! 💪"
            color = "#f38ba8"
        
        grade_label = tk.Label(frame, text=grade, font=("Arial", 18, "bold"),
                              bg="#1e1e2e", fg=color)
        grade_label.pack(pady=20)
        
        # Buttons
        btn_frame = tk.Frame(frame, bg="#1e1e2e")
        btn_frame.pack(pady=20)
        
        retry_btn = tk.Button(btn_frame, text="Retry Quiz", font=("Arial", 14, "bold"),
                             bg="#89b4fa", fg="#1e1e2e", padx=20, pady=10,
                             cursor="hand2", command=self.retry_quiz)
        retry_btn.pack(side="left", padx=10)
        
        exit_btn = tk.Button(btn_frame, text="Exit", font=("Arial", 14, "bold"),
                            bg="#f38ba8", fg="#1e1e2e", padx=20, pady=10,
                            cursor="hand2", command=self.root.quit)
        exit_btn.pack(side="left", padx=10)
    
    def retry_quiz(self):
        self.current_question = 0
        self.score = 0
        self.time_left = 300
        random.shuffle(self.questions)
        self.show_welcome_screen()
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop(


