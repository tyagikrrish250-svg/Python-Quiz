
import tkinter as tk
from tkinter import ttk, messagebox
import time
import random

# ============================================================
# Professional Python Quiz App
# Standard-library only: no external packages required.
# ============================================================

APP_BG = "#0B1220"
PANEL = "#111C2E"
PANEL_2 = "#16243A"
ACCENT = "#3776AB"
ACCENT_2 = "#FFD343"
TEXT = "#F4F7FB"
MUTED = "#AAB7C7"
SUCCESS = "#22C55E"
DANGER = "#EF4444"
WARNING = "#F59E0B"

QUESTIONS = [
# ------------------------- SET 1 -------------------------
[
("Which keyword is used to define a function in Python?", ["func", "define", "def", "function"], 2),
("Which of these is a valid Python variable name?", ["2value", "my-value", "my_value", "class"], 2),
("What is the output of print(2 + 3 * 4)?", ["20", "14", "24", "9"], 1),
("Which symbol starts a single-line comment in Python?", ["//", "#", "--", "/*"], 1),
("What is the type of 10 in Python?", ["float", "str", "int", "number"], 2),
("Which function displays output on the screen?", ["input()", "display()", "print()", "show()"], 2),
("Which function reads user input?", ["read()", "input()", "scan()", "get()"], 1),
("Which is the correct way to create a string?", ["name = 'Python'", "name = Python", "string name = 'Python'", "name := Python"], 0),
("What does len('Python') return?", ["5", "6", "7", "Error"], 1),
("Which operator performs exponentiation?", ["^", "**", "//", "%%"], 1),
("What does // do in Python?", ["Division", "Remainder", "Floor division", "Exponentiation"], 2),
("Which value represents the absence of a value?", ["None", "Null", "Empty", "Void"], 0),
("Python is primarily which type of language?", ["Compiled only", "Interpreted/high-level", "Assembly", "Machine code"], 1),
("Which extension is commonly used for Python source files?", [".pt", ".python", ".py", ".pyt"], 2),
("Which function returns the data type of an object?", ["datatype()", "type()", "kind()", "typeof()"], 1),
],
# ------------------------- SET 2 -------------------------
[
("Which data type stores True or False?", ["bool", "binary", "logical", "bit"], 0),
("What is the result of bool(0)?", ["True", "False", "0", "None"], 1),
("Which collection is ordered and mutable?", ["tuple", "list", "frozenset", "string"], 1),
("Which collection is immutable?", ["list", "set", "tuple", "dict"], 2),
("How do you create an empty list?", ["{}", "[]", "()", "list{}"], 1),
("How do you create an empty dictionary?", ["[]", "()", "{}", "dict[]"], 2),
("Which collection stores unique unordered elements?", ["list", "tuple", "set", "string"], 2),
("What does 'Python'[0] return?", ["P", "y", "n", "Python"], 0),
("What does [10, 20, 30][-1] return?", ["10", "20", "30", "-1"], 2),
("Which method adds one item to the end of a list?", ["add()", "append()", "push()", "insert_end()"], 1),
("Which method removes and returns the last list item by default?", ["delete()", "remove()", "pop()", "discard()"], 2),
("Which dictionary method safely gets a value for a key?", ["fetch()", "get()", "value()", "find()"], 1),
("What does set([1, 1, 2, 2]) contain?", ["[1,1,2,2]", "{1,2}", "{1,1,2,2}", "Error"], 1),
("Which operator checks membership?", ["in", "has", "contains", "inside"], 0),
("What is the result of len({1, 2, 3})?", ["2", "3", "4", "Error"], 1),
],
# ------------------------- SET 3 -------------------------
[
("Which keyword begins a conditional statement?", ["if", "when", "check", "condition"], 0),
("Which keyword handles an alternative condition?", ["else if", "elseif", "elif", "otherwise"], 2),
("Which loop is commonly used to iterate over a sequence?", ["repeat", "for", "foreach", "loop"], 1),
("Which keyword exits a loop immediately?", ["stop", "exit", "break", "return"], 2),
("Which keyword skips to the next loop iteration?", ["skip", "continue", "next", "pass"], 1),
("What does range(5) generate?", ["1 to 5", "0 to 5 inclusive", "0 to 4", "5 values starting at 1"], 2),
("Which statement does nothing and acts as a placeholder?", ["empty", "pass", "skip", "null"], 1),
("What is the output of 5 > 3 and 2 < 1?", ["True", "False", "2", "Error"], 1),
("What does not in do?", ["Negates a Boolean", "Checks non-membership", "Checks inequality only", "Stops a loop"], 1),
("Which operator means logical OR?", ["||", "or", "|", "OR"], 1),
("Which operator means logical AND?", ["&&", "and", "&", "AND"], 1),
("What is the result of 10 % 3?", ["1", "3", "0", "3.33"], 0),
("What does a nested loop mean?", ["A loop with no body", "A loop inside another loop", "A loop with an error", "A loop that runs once"], 1),
("Which loop is best when the number of iterations depends on a condition?", ["while", "for", "switch", "repeat"], 0),
("What happens if a while loop condition never becomes false and has no break?", ["It runs forever", "It runs once", "It causes syntax error", "It skips"], 0),
],
# ------------------------- SET 4 -------------------------
[
("What does a function's return statement do?", ["Prints output automatically", "Sends a value back to the caller", "Stops Python permanently", "Defines a variable"], 1),
("What is a parameter?", ["A value returned by a function", "A variable listed in a function definition", "A module", "An exception"], 1),
("What is an argument?", ["A value passed to a function", "A function name", "A loop counter", "A class"], 0),
("What does *args allow?", ["Only keyword arguments", "Variable-length positional arguments", "Only strings", "File arguments"], 1),
("What does **kwargs allow?", ["Variable-length keyword arguments", "Only integers", "Positional arguments only", "Classes"], 0),
("What is a lambda function?", ["An anonymous small function", "A class constructor", "A loop", "A package"], 0),
("Which keyword creates an anonymous function expression?", ["anon", "lambda", "func", "def"], 1),
("What is recursion?", ["A function calling itself", "A loop without a condition", "A module import", "A class without methods"], 0),
("What is a docstring?", ["A Python error", "Documentation string associated with code", "A file extension", "A package manager"], 1),
("What does variable scope describe?", ["Variable's data type", "Where a variable can be accessed", "Variable's size", "Its memory address only"], 1),
("Which keyword allows assignment to a global variable inside a function?", ["global", "public", "extern", "outer"], 0),
("Which keyword refers to a variable in an enclosing non-global scope?", ["outer", "nonlocal", "enclose", "parent"], 1),
("What is a default parameter value?", ["A value used when an argument is omitted", "A random value", "A required value", "A return type"], 0),
("Can a Python function return multiple values?", ["No", "Yes, typically packed into a tuple", "Only with classes", "Only with print()"], 1),
("What does callable(obj) check?", ["Whether obj is a number", "Whether obj can be called", "Whether obj is iterable", "Whether obj is a class only"], 1),
],
# ------------------------- SET 5 -------------------------
[
("Which keyword is used to define a class?", ["object", "class", "struct", "type"], 1),
("What is __init__ commonly used for?", ["Deleting an object", "Initializing an object", "Importing a module", "Printing a class"], 1),
("What does self usually refer to?", ["The current instance", "The parent class only", "The module", "The Python interpreter"], 0),
("What is inheritance?", ["A class acquiring features from another class", "Copying a file", "Calling a loop", "Creating a variable"], 0),
("What is polymorphism?", ["One interface supporting different implementations", "Multiple inheritance only", "A syntax error", "Data encryption"], 0),
("What is encapsulation?", ["Bundling data and methods with controlled access", "Running code faster", "Creating loops", "Importing packages"], 0),
("Which decorator commonly defines a static method?", ["@static", "@staticmethod", "@staticmethod", "@method"], 2),
("Which decorator commonly defines a class method?", ["@classmethod", "@class", "@classmethod()", "@class_method"], 0),
("What is method overriding?", ["Subclass providing its own implementation of a parent method", "Deleting a method", "Calling a method twice", "Making a method private"], 0),
("Which function checks whether an object is an instance of a class?", ["instance()", "isinstance()", "typecheck()", "isinstanceof()"], 1),
("What is a class attribute?", ["An attribute shared at the class level", "A local variable only", "A function argument", "An imported package"], 0),
("Which special method controls the string representation used by str(obj)?", ["__str__", "__text__", "__reprstr__", "__string__"], 0),
("Which special method is commonly used for an unambiguous developer-oriented representation?", ["__repr__", "__show__", "__debug__", "__dev__"], 0),
("Can Python support multiple inheritance?", ["No", "Yes", "Only for abstract classes", "Only for built-ins"], 1),
("What is composition in OOP?", ["Building a class using objects of other classes", "Deleting parent classes", "Using only inheritance", "Converting strings"], 0),
],
# ------------------------- SET 6 -------------------------
[
("Which statement imports a module?", ["include math", "using math", "import math", "require math"], 2),
("How do you import only sqrt from math?", ["import math.sqrt", "from math import sqrt", "include sqrt from math", "using math.sqrt"], 1),
("Which module is commonly used for generating random values?", ["random", "rand", "numbers", "choice"], 0),
("Which module provides regular expressions?", ["regex", "re", "regexp", "pattern"], 1),
("Which module is commonly used for JSON encoding/decoding?", ["json", "js", "datajson", "serialize"], 0),
("What does pip primarily manage?", ["Python packages", "Python variables", "CPU processes", "Database tables"], 0),
("What is a Python module?", ["A Python file containing reusable code", "Only a class", "A hardware component", "A database"], 0),
("What is a package?", ["A collection of related Python modules", "A single variable", "A loop", "A comment"], 0),
("Which block handles exceptions?", ["try/except", "catch/throw", "handle/error", "safe/rescue"], 0),
("Which keyword explicitly raises an exception?", ["throw", "raise", "error", "except"], 1),
("Which block executes whether or not an exception occurs?", ["always", "finally", "last", "ensure"], 1),
("Which keyword creates a custom exception class?", ["exception", "class", "errorclass", "raiseclass"], 1),
("What exception is raised by 10 / 0?", ["ValueError", "ZeroDivisionError", "ArithmeticError only", "TypeError"], 1),
("What exception can occur when converting 'abc' to int?", ["ValueError", "NameError", "KeyError", "IndexError"], 0),
("What exception occurs when a dictionary key is missing using dict[key]?", ["KeyError", "IndexError", "LookupError only", "MissingKeyError"], 0),
],
# ------------------------- SET 7 -------------------------
[
("Which function opens a file?", ["file()", "open()", "load()", "readfile()"], 1),
("Which mode opens a file for reading?", ["r", "w", "a", "x"], 0),
("Which mode opens a file for writing and can truncate it?", ["r", "w", "a", "rw"], 1),
("Which mode appends to an existing file?", ["r", "w", "a", "p"], 2),
("Why is 'with open(...) as f' recommended?", ["It automatically manages closing the file", "It makes files faster", "It encrypts the file", "It prevents all exceptions"], 0),
("Which method reads the entire file contents?", ["read()", "readall()", "all()", "contents()"], 0),
("Which method reads one line?", ["line()", "readline()", "read_one()", "nextline()"], 1),
("Which method writes text to a file?", ["write()", "put()", "send()", "append_text()"], 0),
("Which module provides path utilities and OS interaction?", ["os", "pathlib only", "system", "filesys"], 0),
("Which modern module provides object-oriented filesystem paths?", ["path", "pathlib", "fs", "ospath"], 1),
("What does CSV stand for?", ["Computer Separated Values", "Comma-Separated Values", "Common Structured Values", "Column Stored Variables"], 1),
("Which module can read and write CSV files?", ["csv", "table", "comma", "data"], 0),
("Which JSON function converts a Python object to a JSON string?", ["json.parse()", "json.dumps()", "json.loadstr()", "json.stringify()"], 1),
("Which JSON function loads JSON from a file object?", ["json.load()", "json.read()", "json.open()", "json.file()"], 0),
("What does serialization mean?", ["Converting an object into a storable/transmittable representation", "Deleting an object", "Sorting a list", "Compiling Python"], 0),
],
# ------------------------- SET 8 -------------------------
[
("What is a list comprehension?", ["A compact way to create lists", "A list debugging tool", "A list sorting algorithm", "A list class"], 0),
("What is a generator?", ["An iterator that produces values lazily", "A random number only", "A class decorator", "A file writer"], 0),
("Which keyword yields a value from a generator?", ["yield", "generate", "returning", "emit"], 0),
("What does iter(obj) return?", ["An iterator for obj when supported", "A list", "A generator always", "The first item"], 0),
("What does next(it) do?", ["Gets the next item from an iterator", "Restarts the iterator", "Sorts it", "Closes it"], 0),
("What is an iterator?", ["An object implementing iteration protocol", "Only a list", "A function with yield only", "A loop variable"], 0),
("What does enumerate() commonly provide?", ["Index-value pairs", "Sorted values", "Only indexes", "Only values"], 0),
("What does zip(a, b) commonly produce?", ["Pairs elements from iterables", "Adds lists", "Sorts both", "Duplicates elements"], 0),
("What is a decorator?", ["A callable that modifies or wraps another callable", "A comment", "A data type", "A loop"], 0),
("Which syntax applies a decorator?", ["#decorator", "@decorator", "$decorator", "&decorator"], 1),
("What does map() return in Python 3?", ["A map object/iterator", "A list always", "A dictionary", "A set"], 0),
("What does filter() do?", ["Keeps elements satisfying a condition", "Sorts elements", "Transforms every element", "Deletes the sequence"], 0),
("What is a set comprehension?", ["A compact syntax for creating sets", "A set debugger", "A set iterator only", "A tuple builder"], 0),
("What is unpacking in Python?", ["Assigning elements of an iterable to multiple variables", "Deleting elements", "Sorting", "Encrypting"], 0),
("What does * do in an assignment like a, *b = [1,2,3]?", ["Collects remaining items into b", "Multiplies b", "Deletes b", "Creates a tuple named a"], 0),
],
# ------------------------- SET 9 -------------------------
[
("What is PEP 8?", ["Python style guide", "Package manager", "Testing framework", "Python compiler"], 0),
("What does the Zen of Python begin with?", ["Code is poetry", "Beautiful is better than ugly", "Simple is always best", "Python is easy"], 1),
("Which command commonly runs a Python file from a terminal?", ["run python.py", "python file.py", "execute file.py", "py run file"], 1),
("What is a virtual environment?", ["An isolated environment for project dependencies", "A cloud server", "A Python class", "A text editor"], 0),
("Which command can create a virtual environment?", ["python -m venv .venv", "python --virtual .venv", "pip virtual .venv", "venv create python"], 0),
("What does __name__ == '__main__' usually allow?", ["Code to run when the file is executed directly", "A class to inherit", "A package to install", "A file to become JSON"], 0),
("What is unit testing?", ["Testing small units of code independently", "Testing hardware", "Testing internet speed", "Testing only the UI"], 0),
("Which standard-library module is used for unit testing?", ["unittest", "pytest", "testlib", "check"], 0),
("What is a syntax error?", ["Invalid Python grammar", "A wrong result", "A runtime exception only", "A missing package always"], 0),
("What is a runtime error?", ["An error that occurs while a program executes", "A spelling mistake only", "A comment", "A syntax feature"], 0),
("What is a logical error?", ["The program runs but produces incorrect results", "A syntax error", "An import error only", "A compiler crash"], 0),
("What is debugging?", ["Finding and fixing program defects", "Writing comments", "Installing Python", "Compressing code"], 0),
("What does assert do?", ["Checks a condition and raises AssertionError if false", "Prints a message only", "Stops every loop", "Imports a module"], 0),
("What is type hinting used for?", ["Communicating expected types", "Forcing runtime types in all cases", "Encrypting data", "Speeding every program"], 0),
("Which tool is commonly used to format Python code automatically?", ["Black", "Bash", "Pip", "Flask"], 0),
],
# ------------------------- SET 10 ------------------------
[
("What is the average time complexity of dictionary lookup by key?", ["O(n)", "O(log n)", "O(1) average", "O(n²)"], 2),
("Which built-in function returns the largest item?", ["top()", "max()", "largest()", "high()"], 1),
("Which built-in function returns the smallest item?", ["min()", "small()", "lowest()", "bottom()"], 0),
("What does sorted() return?", ["A new sorted list", "Sorts only tuples in place", "A set", "A dictionary"], 0),
("What does list.sort() return?", ["The sorted list", "None", "A tuple", "A generator"], 1),
("What is a shallow copy?", ["A copy where nested referenced objects may be shared", "A completely independent recursive copy", "No copy", "A sorted copy"], 0),
("Which module provides deepcopy()?", ["copy", "deep", "clone", "objects"], 0),
("What is duck typing?", ["Using an object's behavior rather than its explicit type", "Typing only ducks", "Static typing", "Database typing"], 0),
("What does @property allow?", ["A method to be accessed like an attribute", "A class to become immutable", "A function to become global", "A module to be imported"], 0),
("What is an abstract base class commonly used for?", ["Defining an interface/contract for subclasses", "Creating database tables", "Sorting lists", "Writing JSON"], 0),
("Which module supports abstract base classes?", ["abc", "abstract", "interface", "base"], 0),
("What does functools.lru_cache provide?", ["Memoization/caching of function results", "File caching only", "List sorting", "Database access"], 0),
("What does contextlib help create?", ["Context managers and related utilities", "GUI windows only", "Network sockets", "Dataframes"], 0),
("Which keyword can be used in a context manager's custom implementation?", ["with", "context", "manage", "using"], 0),
("Which built-in returns an immutable sequence of items?", ["tuple()", "list()", "set()", "dict()"], 0),
]
]

def flatten_questions():
    out = []
    for set_no, question_set in enumerate(QUESTIONS, start=1):
        for q_no, (question, options, answer) in enumerate(question_set, start=1):
            out.append({
                "set": set_no,
                "number": q_no,
                "question": question,
                "options": options,
                "answer": answer
            })
    return out

ALL_QUESTIONS = flatten_questions()


class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Quiz Pro")
        self.geometry("1100x760")
        self.minsize(900, 650)
        self.configure(bg=APP_BG)

        self.selected_set = None
        self.quiz_questions = []
        self.current_index = 0
        self.answers = {}
        self.time_left = 30
        self.timer_job = None
        self.welcome_phase = 0
        self.active_scroll_canvas = None

        # One global mouse-wheel handler makes scrolling work even when the
        # pointer is directly over cards, labels, or buttons inside a canvas.
        self.bind_all("<MouseWheel>", self._global_mousewheel)
        self.bind_all("<Button-4>", self._global_scroll_up)
        self.bind_all("<Button-5>", self._global_scroll_down)

        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("TScrollbar", troughcolor=PANEL, background=ACCENT, arrowcolor=TEXT)

        self.container = tk.Frame(self, bg=APP_BG)
        self.container.pack(fill="both", expand=True)

        self.show_welcome()

    def _global_mousewheel(self, event):
        canvas = self.active_scroll_canvas
        if canvas is None or not canvas.winfo_exists():
            return
        delta = getattr(event, "delta", 0)
        if delta == 0:
            return
        # Windows normally reports multiples of 120; using sign keeps the
        # behavior consistent across high-resolution touchpads and mice.
        units = -1 if delta > 0 else 1
        canvas.yview_scroll(units, "units")

    def _global_scroll_up(self, event):
        canvas = self.active_scroll_canvas
        if canvas is not None and canvas.winfo_exists():
            canvas.yview_scroll(-3, "units")

    def _global_scroll_down(self, event):
        canvas = self.active_scroll_canvas
        if canvas is not None and canvas.winfo_exists():
            canvas.yview_scroll(3, "units")

    def clear(self):
        self.active_scroll_canvas = None
        if self.timer_job:
            try:
                self.after_cancel(self.timer_job)
            except Exception:
                pass
            self.timer_job = None
        for widget in self.container.winfo_children():
            widget.destroy()

    def make_button(self, parent, text, command, bg=ACCENT, fg="white", width=16, font=("Segoe UI", 12, "bold")):
        btn = tk.Button(
            parent, text=text, command=command, bg=bg, fg=fg,
            activebackground=ACCENT_2 if bg == ACCENT else bg,
            activeforeground=APP_BG if bg == ACCENT else fg,
            relief="flat", bd=0, cursor="hand2",
            font=font, width=width, padx=10, pady=10
        )
        return btn

    def show_welcome(self):
        """Premium dark-neon landing screen."""
        self.clear()

        bg = "#070A12"
        panel = "#0D1220"
        panel2 = "#11182A"
        cyan = "#00E5FF"
        purple = "#8B5CF6"
        pink = "#FF3CAC"
        white = "#F5F7FF"
        muted = "#8D99B8"

        # Root background
        self.container.configure(bg=bg)

        # Subtle animated neon grid/background
        canvas = tk.Canvas(self.container, bg=bg, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        def draw_background():
            canvas.delete("bg")
            w = max(canvas.winfo_width(), 900)
            h = max(canvas.winfo_height(), 650)

            # soft neon glow bands
            for i in range(10):
                alpha_x = int(w * (0.18 + i * 0.075))
                canvas.create_line(
                    alpha_x, 0, alpha_x - int(h * 0.35), h,
                    fill="#0B1830", width=1, tags="bg"
                )

            # grid
            step = 42
            for x in range(0, w, step):
                canvas.create_line(x, 0, x, h, fill="#0B1222", tags="bg")
            for y in range(0, h, step):
                canvas.create_line(0, y, w, y, fill="#0B1222", tags="bg")

            # neon corner accents
            canvas.create_oval(
                w-260, -160, w+160, 260,
                outline="#102B45", width=3, tags="bg"
            )
            canvas.create_oval(
                -180, h-260, 240, h+160,
                outline="#171034", width=3, tags="bg"
            )

            # top accent line
            canvas.create_rectangle(
                0, 0, w, 3, fill=cyan, outline="", tags="bg"
            )

        def redraw(_=None):
            draw_background()
            canvas.after(70, redraw)

        canvas.bind("<Configure>", draw_background)

        # Main centered card
        card = tk.Frame(
            canvas, bg=panel,
            highlightbackground="#1A2945",
            highlightthickness=1
        )
        card_window = canvas.create_window(0, 0, window=card, anchor="center")

        def center_card(event=None):
            canvas.coords(
                card_window,
                canvas.winfo_width() // 2,
                canvas.winfo_height() // 2
            )

        canvas.bind("<Configure>", lambda e: (draw_background(), center_card(e)))

        # Small top status
        status = tk.Frame(card, bg=panel)
        status.pack(pady=(28, 6))

        dot = tk.Label(status, text="●", font=("Segoe UI", 10),
                        fg=cyan, bg=panel)
        dot.pack(side="left", padx=(0, 7))

        tk.Label(
            status,
            text="PYTHON LEARNING • QUIZ SYSTEM",
            font=("Segoe UI", 9, "bold"),
            fg=muted, bg=panel
        ).pack(side="left")

        # Python-inspired neon logo
        logo_wrap = tk.Frame(card, bg=panel)
        logo_wrap.pack(pady=(10, 2))

        logo = tk.Canvas(
            logo_wrap, width=128, height=128,
            bg=panel, highlightthickness=0
        )
        logo.pack()

        # Glow layers
        logo.create_oval(8, 8, 120, 120, outline="#112B42", width=2)
        logo.create_oval(16, 16, 112, 112, outline="#172052", width=2)
        logo.create_oval(25, 25, 103, 103, outline=cyan, width=2)

        # Stylized Python-like mark
        logo.create_rectangle(39, 31, 89, 67, fill=cyan, outline="")
        logo.create_rectangle(39, 61, 89, 97, fill=purple, outline="")
        logo.create_oval(54, 38, 61, 45, fill=bg, outline="")
        logo.create_oval(67, 83, 74, 90, fill=bg, outline="")
        logo.create_line(89, 48, 101, 48, fill=cyan, width=4)
        logo.create_line(39, 80, 27, 80, fill=purple, width=4)

        # Brand
        tk.Label(
            card, text="PYTHON",
            font=("Segoe UI", 34, "bold"),
            fg=white, bg=panel
        ).pack(pady=(0, 0))

        tk.Label(
            card, text="QUIZ PRO",
            font=("Segoe UI", 18, "bold"),
            fg=cyan, bg=panel
        ).pack(pady=(0, 8))

        tk.Label(
            card,
            text="Test your Python skills. Track your progress. Master the fundamentals.",
            font=("Segoe UI", 11),
            fg=muted, bg=panel
        ).pack(pady=(0, 22))

        # Feature chips
        chips = tk.Frame(card, bg=panel)
        chips.pack(pady=(0, 24))

        features = [
            ("150", "QUESTIONS", cyan),
            ("10", "SETS", purple),
            ("30s", "PER QUESTION", pink),
        ]

        for value, label, accent in features:
            chip = tk.Frame(
                chips, bg=panel2,
                highlightbackground="#202C46",
                highlightthickness=1
            )
            chip.pack(side="left", padx=6, ipadx=13, ipady=8)

            tk.Label(
                chip, text=value,
                font=("Segoe UI", 14, "bold"),
                fg=accent, bg=panel2
            ).pack()
            tk.Label(
                chip, text=label,
                font=("Segoe UI", 7, "bold"),
                fg=muted, bg=panel2
            ).pack()

        # Start button with hover effect
        btn = tk.Button(
            card,
            text="  START QUIZ  ➜",
            command=self.show_set_selection,
            font=("Segoe UI", 14, "bold"),
            fg="#061018",
            bg=cyan,
            activeforeground="#061018",
            activebackground="#63F1FF",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=42,
            pady=14
        )
        btn.pack(pady=(0, 14))

        def enter(_):
            btn.configure(bg="#63F1FF")

        def leave(_):
            btn.configure(bg=cyan)

        btn.bind("<Enter>", enter)
        btn.bind("<Leave>", leave)

        # Secondary hint
        tk.Label(
            card,
            text="Choose a set • Answer • Review your performance",
            font=("Segoe UI", 9),
            fg="#65718F", bg=panel
        ).pack(pady=(0, 22))

        # Footer
        footer = tk.Frame(self.container, bg=bg)
        footer.place(relx=0.5, rely=0.97, anchor="s")

        tk.Label(
            footer,
            text="BUILT FOR PYTHON LEARNERS  •  COLLEGE PROJECT",
            font=("Segoe UI", 8, "bold"),
            fg="#46516B", bg=bg
        ).pack()

        # Gentle pulsing accent — subtle, not flashy.
        def pulse(step=0):
            colors = ["#00AFC4", "#00C4D8", "#00E5FF", "#00C4D8"]
            dot.configure(fg=colors[step % len(colors)])
            self.after(420, lambda: pulse(step + 1))

        pulse()
    def _position_welcome_card(self, event):
        if hasattr(self, "welcome_window"):
            self.welcome_canvas.coords(
                self.welcome_window,
                event.width // 2,
                event.height // 2
            )

    def _animate_welcome(self):
        if not hasattr(self, "welcome_canvas") or not self.welcome_canvas.winfo_exists():
            return

        self.welcome_phase += 1

        # Very subtle breathing effect on the start button.
        if self.welcome_phase % 30 < 15:
            self.start_button.configure(bg=ACCENT)
        else:
            self.start_button.configure(bg="#326B9E")

        self.after(90, self._animate_welcome)

    def show_set_selection(self):
        self.clear()

        header = tk.Frame(self.container, bg=APP_BG)
        header.pack(fill="x", padx=50, pady=(25, 8))

        tk.Label(
            header, text="Choose a Question Set", bg=APP_BG, fg=TEXT,
            font=("Segoe UI", 28, "bold")
        ).pack()

        tk.Label(
            header, text="Each set contains 15 Python questions.",
            bg=APP_BG, fg=MUTED, font=("Segoe UI", 12)
        ).pack(pady=4)

        # Scrollable set-selection area
        area = tk.Frame(self.container, bg=APP_BG)
        area.pack(fill="both", expand=True, padx=35, pady=8)

        canvas = tk.Canvas(area, bg=APP_BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(area, orient="vertical", command=canvas.yview)
        grid = tk.Frame(canvas, bg=APP_BG)

        grid.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        window_id = canvas.create_window((0, 0), window=grid, anchor="nw")

        def resize_grid(event):
            canvas.itemconfigure(window_id, width=event.width)

        canvas.bind("<Configure>", resize_grid)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Register this canvas as the active scroll target. The global
        # wheel handler above receives events even when the pointer is over
        # a child widget inside the scrollable area.
        self.active_scroll_canvas = canvas

        descriptions = [
            "Python Basics", "Data Types & Collections", "Conditions & Loops",
            "Functions", "Object-Oriented Python", "Modules & Exceptions",
            "Files & Data", "Iterators & Functional Tools", "Python Practices",
            "Advanced & Mixed"
        ]

        for i in range(10):
            r, c = divmod(i, 2)

            card = tk.Frame(
                grid, bg=PANEL,
                highlightthickness=1,
                highlightbackground="#223451"
            )
            card.grid(
                row=r, column=c,
                padx=12, pady=10,
                ipadx=10, ipady=8,
                sticky="nsew"
            )

            tk.Label(
                card, text=f"SET {i+1}", bg=PANEL, fg=ACCENT_2,
                font=("Segoe UI", 12, "bold")
            ).pack(pady=(8, 2))

            tk.Label(
                card, text=descriptions[i], bg=PANEL, fg=TEXT,
                font=("Segoe UI", 13, "bold")
            ).pack()

            tk.Label(
                card, text="15 Questions • 30 sec each",
                bg=PANEL, fg=MUTED, font=("Segoe UI", 9)
            ).pack(pady=2)

            self.make_button(
                card, "Attempt Set",
                lambda s=i+1: self.start_quiz(s),
                width=15
            ).pack(pady=(6, 10))

        grid.grid_columnconfigure(0, weight=1)
        grid.grid_columnconfigure(1, weight=1)

        # Keep Home visible outside the scroll area
        self.make_button(
            self.container, "← Home",
            self.show_welcome,
            bg=PANEL_2, width=14
        ).pack(pady=(5, 15))

    def start_quiz(self, set_no):
        self.selected_set = set_no
        self.quiz_questions = [q for q in ALL_QUESTIONS if q["set"] == set_no]
        self.current_index = 0
        self.answers = {}
        self.time_left = 30
        self.show_question()

    def show_question(self):
        self.clear()
        q = self.quiz_questions[self.current_index]

        top = tk.Frame(self.container, bg=PANEL, height=85)
        top.pack(fill="x")
        top.pack_propagate(False)

        self.make_button(
            top, "⌂ Home", self.confirm_home,
            bg=PANEL_2, width=10
        ).pack(side="left", padx=(20, 12), pady=17)

        tk.Label(top, text=f"PYTHON QUIZ PRO  •  SET {self.selected_set}",
                 bg=PANEL, fg=ACCENT_2, font=("Segoe UI", 15, "bold")).pack(side="left", padx=10, pady=25)

        self.timer_label = tk.Label(top, text="", bg=PANEL, fg=SUCCESS, font=("Segoe UI", 16, "bold"))
        self.timer_label.pack(side="right", padx=35)

        progress = tk.Frame(self.container, bg=APP_BG)
        progress.pack(fill="x", padx=45, pady=(20, 10))
        tk.Label(progress, text=f"Question {self.current_index + 1} of {len(self.quiz_questions)}",
                 bg=APP_BG, fg=TEXT, font=("Segoe UI", 12, "bold")).pack(side="left")
        tk.Label(progress, text=f"Answered: {len(self.answers)}/15",
                 bg=APP_BG, fg=MUTED, font=("Segoe UI", 10)).pack(side="right")

        bar_bg = tk.Frame(progress, bg="#24344D", height=8)
        bar_bg.pack(fill="x", pady=(12, 0))
        bar_bg.update_idletasks()
        pct = (self.current_index + 1) / len(self.quiz_questions)
        tk.Frame(bar_bg, bg=ACCENT, height=8, width=max(1, int(bar_bg.winfo_width() * pct))).pack(side="left", fill="y")

        content = tk.Frame(self.container, bg=APP_BG)
        content.pack(fill="both", expand=True, padx=45, pady=10)

        qcard = tk.Frame(content, bg=PANEL, highlightthickness=1, highlightbackground="#223451")
        qcard.pack(fill="both", expand=True)

        tk.Label(qcard, text=q["question"], bg=PANEL, fg=TEXT,
                 font=("Segoe UI", 20, "bold"), wraplength=900, justify="left").pack(
                     anchor="w", padx=35, pady=(30, 25)
                 )

        self.option_var = tk.IntVar(value=self.answers.get(self.current_index, -1))
        self.option_buttons = []

        for idx, option in enumerate(q["options"]):
            rb = tk.Radiobutton(
                qcard, text=f"{chr(65+idx)}.  {option}", variable=self.option_var, value=idx,
                bg=PANEL_2, fg=TEXT, selectcolor=ACCENT, activebackground=PANEL_2,
                activeforeground=TEXT, anchor="w", justify="left", wraplength=850,
                font=("Segoe UI", 12), padx=15, pady=12, indicatoron=True,
                cursor="hand2"
            )
            rb.pack(fill="x", padx=35, pady=5)
            self.option_buttons.append(rb)

        nav = tk.Frame(self.container, bg=APP_BG)
        nav.pack(fill="x", padx=45, pady=(5, 25))

        self.make_button(nav, "⌂ Home", self.confirm_home,
                         bg=PANEL_2, width=11).pack(side="left", padx=5)
        self.make_button(nav, "← Previous", self.previous_question,
                         bg=PANEL_2, width=13).pack(side="left", padx=5)
        self.make_button(nav, "Skip →", self.skip_question,
                         bg="#334155", width=13).pack(side="left", padx=5)
        self.make_button(nav, "Next →", self.next_question,
                         bg=ACCENT, width=13).pack(side="right", padx=5)
        self.make_button(nav, "✓ Submit", self.submit_quiz,
                         bg=SUCCESS, fg="#06230F", width=13).pack(side="right", padx=5)

        self.time_left = 30
        self.update_timer()

    def confirm_home(self):
        self.save_current_answer()
        if self.answers:
            ok = messagebox.askyesno(
                "Return Home",
                "Your current quiz progress will be lost.\n\nReturn to Home?"
            )
            if not ok:
                return
        self.show_welcome()

    def confirm_home(self):
        if messagebox.askyesno(
            "Leave Quiz?",
            "Are you sure you want to leave the quiz?\n\n"
            "Your current quiz progress will be lost."
        ):
            self.show_welcome()

    def save_current_answer(self):
        value = self.option_var.get()
        if value >= 0:
            self.answers[self.current_index] = value

    def previous_question(self):
        self.save_current_answer()
        if self.current_index > 0:
            self.current_index -= 1
            self.show_question()

    def next_question(self):
        self.save_current_answer()
        if self.current_index < len(self.quiz_questions) - 1:
            self.current_index += 1
            self.show_question()
        else:
            messagebox.showinfo("Last Question", "You are on the last question. Click Submit to finish.")

    def skip_question(self):
        self.answers.pop(self.current_index, None)
        if self.current_index < len(self.quiz_questions) - 1:
            self.current_index += 1
            self.show_question()
        else:
            messagebox.showinfo("Last Question", "This is the last question. Click Submit to finish.")

    def update_timer(self):
        if not self.winfo_exists():
            return
        color = SUCCESS if self.time_left > 10 else WARNING if self.time_left > 5 else DANGER
        self.timer_label.configure(text=f"⏱ {self.time_left:02d}s", fg=color)
        if self.time_left <= 0:
            self.save_current_answer()
            if self.current_index < len(self.quiz_questions) - 1:
                self.current_index += 1
                self.show_question()
            else:
                self.submit_quiz(auto=True)
            return
        self.time_left -= 1
        self.timer_job = self.after(1000, self.update_timer)

    def submit_quiz(self, auto=False):
        self.save_current_answer()
        if not auto:
            unanswered = len(self.quiz_questions) - len(self.answers)
            if unanswered:
                ok = messagebox.askyesno(
                    "Submit Quiz",
                    f"You have {unanswered} unanswered question(s).\n\nSubmit anyway?"
                )
                if not ok:
                    return
            else:
                ok = messagebox.askyesno("Submit Quiz", "Submit your quiz now?")
                if not ok:
                    return

        if self.timer_job:
            try:
                self.after_cancel(self.timer_job)
            except Exception:
                pass
            self.timer_job = None

        self.show_results()

    def show_results(self):
        self.clear()

        correct = sum(
            1 for i, q in enumerate(self.quiz_questions)
            if self.answers.get(i, -1) == q["answer"]
        )
        total = len(self.quiz_questions)
        percentage = (correct / total) * 100

        header = tk.Frame(self.container, bg=PANEL)
        header.pack(fill="x")

        tk.Label(header, text="Quiz Completed!", bg=PANEL, fg=TEXT,
                 font=("Segoe UI", 28, "bold")).pack(pady=(28, 5))
        tk.Label(header, text=f"Set {self.selected_set} • Python Programming",
                 bg=PANEL, fg=MUTED, font=("Segoe UI", 11)).pack(pady=(0, 20))

        score_card = tk.Frame(self.container, bg=APP_BG)
        score_card.pack(fill="x", padx=45, pady=20)

        for value, label in [(f"{correct}/{total}", "Score"), (f"{percentage:.1f}%", "Percentage")]:
            c = tk.Frame(score_card, bg=PANEL_2, highlightthickness=1, highlightbackground="#223451")
            c.pack(side="left", expand=True, fill="x", padx=8, ipady=14)
            tk.Label(c, text=value, bg=PANEL_2, fg=ACCENT_2,
                     font=("Segoe UI", 24, "bold")).pack()
            tk.Label(c, text=label, bg=PANEL_2, fg=MUTED,
                     font=("Segoe UI", 10)).pack()

        review_title = tk.Label(self.container, text="Answer Review",
                                bg=APP_BG, fg=TEXT, font=("Segoe UI", 18, "bold"))
        review_title.pack(anchor="w", padx=55, pady=(0, 8))

        review_outer = tk.Frame(self.container, bg=PANEL)
        review_outer.pack(fill="both", expand=True, padx=45, pady=(0, 15))

        canvas = tk.Canvas(review_outer, bg=PANEL, highlightthickness=0)
        scrollbar = ttk.Scrollbar(review_outer, orient="vertical", command=canvas.yview)
        review = tk.Frame(canvas, bg=PANEL)
        review.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=review, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True, padx=8, pady=8)
        scrollbar.pack(side="right", fill="y")

        # Register the review canvas as the active scroll target.
        self.active_scroll_canvas = canvas

        for i, q in enumerate(self.quiz_questions):
            selected = self.answers.get(i, None)
            is_correct = selected == q["answer"]
            row = tk.Frame(review, bg="#10233A" if is_correct else "#2A1720",
                           highlightthickness=1,
                           highlightbackground=SUCCESS if is_correct else DANGER)
            row.pack(fill="x", padx=12, pady=7)

            status = "✓ Correct" if is_correct else "✗ Incorrect"
            status_color = SUCCESS if is_correct else DANGER
            tk.Label(row, text=f"Q{i+1}. {status}", bg=row["bg"], fg=status_color,
                     font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=14, pady=(10, 3))
            tk.Label(row, text=q["question"], bg=row["bg"], fg=TEXT,
                     font=("Segoe UI", 11, "bold"), wraplength=850, justify="left").pack(
                         anchor="w", padx=14, pady=2
                     )

            selected_text = "Not answered" if selected is None else q["options"][selected]
            correct_text = q["options"][q["answer"]]

            tk.Label(row, text=f"Your answer: {selected_text}",
                     bg=row["bg"], fg=TEXT if is_correct else "#FCA5A5",
                     font=("Segoe UI", 10), wraplength=850, justify="left").pack(anchor="w", padx=14, pady=2)
            tk.Label(row, text=f"Correct answer: {correct_text}",
                     bg=row["bg"], fg=SUCCESS, font=("Segoe UI", 10),
                     wraplength=850, justify="left").pack(anchor="w", padx=14, pady=(2, 10))

        footer = tk.Frame(self.container, bg=APP_BG)
        footer.pack(fill="x", padx=45, pady=(0, 25))
        self.make_button(footer, "⌂ Home", self.show_welcome, bg=PANEL_2, width=14).pack(side="left")
        self.make_button(footer, "↻ Try Another Set", self.show_set_selection, width=20).pack(side="right")


if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
