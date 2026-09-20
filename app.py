import streamlit as st
import time

st.set_page_config(page_title="Python Master Quiz", page_icon="🐍", layout="centered")

# Custom CSS for styling and UI layout
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #306998 0%, #FFD43B 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-header {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 20px;
    }
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        background: linear-gradient(135deg, #306998 0%, #1e415b 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }
    .logo-text {
        font-size: 3rem;
        font-weight: 900;
        letter-spacing: 2px;
        color: #FFD43B;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .timer-box {
        font-size: 1.2rem;
        font-weight: bold;
        color: #ff4b4b;
        background-color: #ffe6e6;
        padding: 8px 15px;
        border-radius: 8px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# 10 Question Sets (10 Questions each)
QUESTION_SETS = {
    "Set 1: Basics & Syntax 🟢": [
        {"q": "Who created the Python programming language?", "options": ["Guido van Rossum", "Dennis Ritchie", "James Gosling", "Bjarne Stroustrup"], "ans": "Guido van Rossum"},
        {"q": "Which character is used for single-line comments in Python?", "options": ["//", "/*", "#", "--"], "ans": "#"},
        {"q": "What is the correct file extension for Python files?", "options": [".pt", ".pyt", ".py", ".python"], "ans": ".py"},
        {"q": "Which keyword is used to declare a variable in Python?", "options": ["var", "int", "None", "No keyword needed"], "ans": "No keyword needed"},
        {"q": "Which function is used to output text to the console?", "options": ["print()", "echo()", "cout", "System.out.println()"], "ans": "print()"},
        {"q": "Which of the following is NOT a valid variable name?", "options": ["my_var", "_myvar", "2myvar", "myVar"], "ans": "2myvar"},
        {"q": "How is a block of code defined in Python?", "options": ["Curly brackets", "Indentation", "Semicolons", "Parentheses"], "ans": "Indentation"},
        {"q": "What is used for multi-line comments/docstrings in Python?", "options": ["''' '''", "//", "<!-- -->", "/* */"], "ans": "''' '''"},
        {"q": "Which function takes user input in Python 3?", "options": ["raw_input()", "input()", "get()", "scan()"], "ans": "input()"},
        {"q": "What data type does the input() function return by default?", "options": ["int", "float", "str", "bool"], "ans": "str"}
    ],
    "Set 2: Data Types & Operators 🔢": [
        {"q": "Which of the following data types is immutable in Python?", "options": ["List", "Dictionary", "Tuple", "Set"], "ans": "Tuple"},
        {"q": "Which operator is used for exponentiation (power)?", "options": ["^", "**", "//", "%"], "ans": "**"},
        {"q": "Which operator is used for floor division?", "options": ["/", "//", "%", "**"], "ans": "//"},
        {"q": "Which operator returns the remainder of a division?", "options": ["%", "/", "//", "#"], "ans": "%"},
        {"q": "What is the output of type(5.0)?", "options": ["<class 'int'>", "<class 'float'>", "<class 'double'>", "<class 'str'>"], "ans": "<class 'float'>"},
        {"q": "What is the output of type(True)?", "options": ["<class 'bool'>", "<class 'int'>", "<class 'str'>", "<class 'Boolean'>"], "ans": "<class 'bool'>"},
        {"q": "How is the imaginary part of a complex number denoted in Python?", "options": ["i", "j", "x", "img"], "ans": "j"},
        {"q": "What is the output of len('Hello')?", "options": ["4", "5", "6", "Error"], "ans": "5"},
        {"q": "What is the output of str(10)?", "options": ["10", "'10'", "Error", "10.0"], "ans": "'10'"},
        {"q": "What happens when you execute int('10.5')?", "options": ["10", "10.5", "ValueError", "11"], "ans": "ValueError"}
    ],
    "Set 3: Lists & Tuples 📋": [
        {"q": "Which brackets are used to create a List?", "options": ["( )", "[ ]", "{ }", "< >"], "ans": "[ ]"},
        {"q": "Which brackets are used to create a Tuple?", "options": ["( )", "[ ]", "{ }", "< >"], "ans": "( )"},
        {"q": "Which method adds an element to the end of a List?", "options": ["add()", "append()", "insert()", "push()"], "ans": "append()"},
        {"q": "Which method inserts an item at a specific index in a List?", "options": ["append()", "insert()", "add()", "put()"], "ans": "insert()"},
        {"q": "Which method removes and returns the last element of a List?", "options": ["remove()", "delete()", "pop()", "clear()"], "ans": "pop()"},
        {"q": "What is the value of lst after lst = [1, 2, 3]; lst.clear()?", "options": ["None", "[]", "Error", "[0]"], "ans": "[]"},
        {"q": "At what index does Python sequence indexing start?", "options": ["1", "0", "-1", "Depends on list"], "ans": "0"},
        {"q": "Which index refers to the last item in a List?", "options": ["0", "last", "-1", "len()"], "ans": "-1"},
        {"q": "Can elements of a Tuple be modified after creation?", "options": ["Yes", "No", "Only using append", "Only using pop"], "ans": "No"},
        {"q": "What is the data type of a = (1,)?", "options": ["int", "tuple", "list", "set"], "ans": "tuple"}
    ],
    "Set 4: Dictionaries & Sets 🗝️": [
        {"q": "How is data stored in a Python Dictionary?", "options": ["Key-Value pairs", "Only Values", "Index-Value", "Sequential Elements"], "ans": "Key-Value pairs"},
        {"q": "Are duplicate elements allowed in a Set?", "options": ["Yes", "No", "Sometimes", "Only numbers"], "ans": "No"},
        {"q": "Which brackets are used to declare a Dictionary?", "options": ["[ ]", "( )", "{ }", "< >"], "ans": "{ }"},
        {"q": "How do you create an empty Set in Python?", "options": ["{}", "set()", "[]", "()"], "ans": "set()"},
        {"q": "Which method retrieves all keys from a Dictionary?", "options": ["keys()", "values()", "items()", "get_keys()"], "ans": "keys()"},
        {"q": "Which method safely gets a value from a dictionary without raising KeyError?", "options": ["fetch()", "get()", "find()", "search()"], "ans": "get()"},
        {"q": "Which of the following is an unordered collection data type?", "options": ["List", "Tuple", "Set", "String"], "ans": "Set"},
        {"q": "Which method adds an element to a Set?", "options": ["append()", "add()", "insert()", "push()"], "ans": "add()"},
        {"q": "What is the result of d = {'a': 1}; d['b'] = 2?", "options": ["Error", "{'a': 1, 'b': 2}", "{'b': 2}", "{'a': 1}"], "ans": "{'a': 1, 'b': 2}"},
        {"q": "What happens if a duplicate key is added to a Dictionary?", "options": ["Error", "Duplicate allowed", "Value gets overwritten", "Key ignored"], "ans": "Value gets overwritten"}
    ],
    "Set 5: Loops & Conditions 🔄": [
        {"q": "Which keyword is used for 'else if' conditions in Python?", "options": ["else if", "elseif", "elif", "if else"], "ans": "elif"},
        {"q": "Which keyword is used to exit a loop prematurely?", "options": ["stop", "exit", "break", "continue"], "ans": "break"},
        {"q": "Which keyword skips the current iteration and moves to the next?", "options": ["skip", "continue", "pass", "next"], "ans": "continue"},
        {"q": "Which keyword acts as a placeholder for future code?", "options": ["null", "pass", "blank", "continue"], "ans": "pass"},
        {"q": "How many times will 'for i in range(5):' execute?", "options": ["1 to 5", "5 times (0 to 4)", "6 times (0 to 5)", "4 times"], "ans": "5 times (0 to 4)"},
        {"q": "What numbers are generated by range(1, 10, 2)?", "options": ["1, 2, 3, 4", "1, 3, 5, 7, 9", "2, 4, 6, 8", "1, 10, 2"], "ans": "1, 3, 5, 7, 9"},
        {"q": "When does a 'while True:' loop terminate without a break statement?", "options": ["After 10 loops", "Never (Infinite)", "After error", "After 1 loop"], "ans": "Never (Infinite)"},
        {"q": "Can an 'else' block be attached to a 'for' loop?", "options": ["Yes", "No", "Syntax Error", "Only in Python 2"], "ans": "Yes"},
        {"q": "Which operator is used to test equality?", "options": ["=", "==", "===", "is"], "ans": "=="},
        {"q": "Which operator represents 'Not Equal To' in Python?", "options": ["!=", "<>", "not =", "=/="], "ans": "!="}
    ],
    "Set 6: Functions & Modules ⚙️": [
        {"q": "Which keyword is used to define a function?", "options": ["function", "def", "fun", "define"], "ans": "def"},
        {"q": "Which keyword returns a value from a function?", "options": ["give", "return", "output", "send"], "ans": "return"},
        {"q": "Which keyword is used to create anonymous/inline functions?", "options": ["lambda", "anonymous", "func", "short"], "ans": "lambda"},
        {"q": "What is the data type of *args inside a function?", "options": ["List", "Tuple", "Dictionary", "Set"], "ans": "Tuple"},
        {"q": "What is the data type of **kwargs inside a function?", "options": ["List", "Tuple", "Dictionary", "Set"], "ans": "Dictionary"},
        {"q": "Which keyword is used to import external modules?", "options": ["using", "import", "include", "require"], "ans": "import"},
        {"q": "How do you access pi value from the math module?", "options": ["math.pi", "math(pi)", "import pi", "pi()"], "ans": "math.pi"},
        {"q": "Which keyword allows modifying a variable outside the current scope?", "options": ["global", "extern", "var", "public"], "ans": "global"},
        {"q": "What is a function calling itself called?", "options": ["Recursion", "Looping", "Iteration", "Overloading"], "ans": "Recursion"},
        {"q": "Which of the following is NOT a built-in Python function?", "options": ["print()", "len()", "math()", "type()"], "ans": "math()"}
    ],
    "Set 7: Strings & Slicing 🔤": [
        {"q": "What is the result of 'Python'[1:4]?", "options": ["Pyt", "yth", "ytho", "pyt"], "ans": "yth"},
        {"q": "Which method converts a string to uppercase?", "options": ["upper()", "uppercase()", "toUpper()", "CAPS()"], "ans": "upper()"},
        {"q": "Which method removes whitespace from start and end?", "options": ["clean()", "strip()", "trim()", "remove()"], "ans": "strip()"},
        {"q": "Which method splits a string into a list of substrings?", "options": ["split()", "slice()", "divide()", "break()"], "ans": "split()"},
        {"q": "How are variables referenced inside f-strings?", "options": ["%var", "$var", "{var}", "var"], "ans": "{var}"},
        {"q": "Are Python strings mutable or immutable?", "options": ["Mutable", "Immutable", "Both", "Depends on length"], "ans": "Immutable"},
        {"q": "What is the output of 'a' + 'b'?", "options": ["ab", "a b", "Error", "2"], "ans": "ab"},
        {"q": "What is the output of 'a' * 3?", "options": ["aaa", "a3", "Error", "3a"], "ans": "aaa"},
        {"q": "Which method finds the first occurrence of a substring?", "options": ["find()", "search()", "locate()", "get()"], "ans": "find()"},
        {"q": "What does '123'.isdigit() return?", "options": ["True", "False", "123", "Error"], "ans": "True"}
    ],
    "Set 8: OOPs Concepts 🧱": [
        {"q": "Which keyword is used to define a Class?", "options": ["class", "struct", "object", "define"], "ans": "class"},
        {"q": "Which method is the constructor of a Python class?", "options": ["__construct__", "__init__", "init()", "main()"], "ans": "__init__"},
        {"q": "What is the first parameter of instance methods in a class?", "options": ["this", "self", "cls", "object"], "ans": "self"},
        {"q": "What core OOP concept does Inheritance promote?", "options": ["Code Reusability", "Slower Speed", "More Errors", "Higher Memory"], "ans": "Code Reusability"},
        {"q": "Which function calls a method from the parent class?", "options": ["parent()", "super()", "base()", "upper()"], "ans": "super()"},
        {"q": "What does OOP stand for?", "options": ["Object-Oriented Programming", "Optimal Output Python", "Open Object Protocol", "Order Of Python"], "ans": "Object-Oriented Programming"},
        {"q": "How do you denote private variables in a Python class?", "options": ["__ (Double Underscore)", "#", "private keyword", "@"], "ans": "__ (Double Underscore)"},
        {"q": "What is an instance of a Class called?", "options": ["Variable", "Function", "Object", "Module"], "ans": "Object"},
        {"q": "Having methods with the same name behaving differently is called?", "options": ["Polymorphism", "Encapsulation", "Inheritance", "Abstraction"], "ans": "Polymorphism"},
        {"q": "Wrapping data and methods into a single unit is called?", "options": ["Encapsulation", "Abstraction", "Inheritance", "Polymorphism"], "ans": "Encapsulation"}
    ],
    "Set 9: File & Exception Handling 📁": [
        {"q": "Which block catches exceptions in Python?", "options": ["catch", "except", "error", "handle"], "ans": "except"},
        {"q": "Which block always executes regardless of errors?", "options": ["finally", "always", "end", "done"], "ans": "finally"},
        {"q": "Which keyword is used to explicitly trigger an exception?", "options": ["throw", "raise", "error", "dispatch"], "ans": "raise"},
        {"q": "Which mode is used to open a file for reading?", "options": ["'r'", "'w'", "'a'", "'x'"], "ans": "'r'"},
        {"q": "What happens when you open a file in write ('w') mode?", "options": ["Overwrites existing content", "Appends content", "Raises Error", "Creates backup"], "ans": "Overwrites existing content"},
        {"q": "Which mode appends data to the end of a file?", "options": ["'a'", "'w'", "'r'", "'x'"], "ans": "'a'"},
        {"q": "What is the safest way to open files (auto-closes them)?", "options": ["with open()", "try open()", "file.open()", "auto.open()"], "ans": "with open()"},
        {"q": "Which method reads a single line from a file?", "options": ["readline()", "readlines()", "read()", "get_line()"], "ans": "readline()"},
        {"q": "Which exception is raised when dividing by zero?", "options": ["ZeroDivisionError", "MathError", "ValueError", "DivideError"], "ans": "ZeroDivisionError"},
        {"q": "Which exception is raised when accessing an undefined variable?", "options": ["NameError", "TypeError", "ValueError", "KeyError"], "ans": "NameError"}
    ],
    "Set 10: Advanced Python ⚡": [
        {"q": "What is the standard syntax for List Comprehension?", "options": ["[expression for item in iterable]", "(expression for item)", "{expression}", "for item in list"], "ans": "[expression for item in iterable]"},
        {"q": "Which keyword does a Generator function use instead of return?", "options": ["yield", "produce", "generate", "send"], "ans": "yield"},
        {"q": "What is used to modify function behavior using '@' syntax?", "options": ["Decorator", "Generator", "Iterator", "Lambda"], "ans": "Decorator"},
        {"q": "What does PIP stand for?", "options": ["Preferred Installer Program", "Python Import Package", "Python Installation Path", "Program In Python"], "ans": "Preferred Installer Program"},
        {"q": "Which Python framework is widely used for Web Development?", "options": ["Django", "NumPy", "Pandas", "Matplotlib"], "ans": "Django"},
        {"q": "Which library is most popular for Data Analysis in Python?", "options": ["Pandas", "Flask", "Tkinter", "Pygame"], "ans": "Pandas"},
        {"q": "Which standard library is used for building Desktop GUIs?", "options": ["Tkinter", "Requests", "BeautifulSoup", "PyPDF2"], "ans": "Tkinter"},
        {"q": "Command to create a Virtual Environment in Python?", "options": ["python -m venv env", "pip install env", "create virtualenv", "python new env"], "ans": "python -m venv env"},
        {"q": "Which built-in function pairs elements from two iterables?", "options": ["zip()", "combine()", "merge()", "pair()"], "ans": "zip()"},
        {"q": "Which function applies a transformation function to all items in an iterable?", "options": ["map()", "apply()", "for_each()", "execute()"], "ans": "map()"}
    ]
}

TIME_PER_QUESTION = 30  # 30 seconds per question

# Session State Initialization
if 'page' not in st.session_state:
    st.session_state.page = "welcome"
if 'game_started' not in st.session_state:
    st.session_state.game_started = False

# -------------------------------------------------------------------------
# PAGE 1: WELCOME SCREEN (Logo Banner & Start Button)
# -------------------------------------------------------------------------
if st.session_state.page == "welcome":
    st.markdown("""
        <div class="logo-container">
            <div class="logo-text">🐍 PYTHON QUIZ 🎯</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p class='sub-header'>Test your knowledge across 10 exciting topics with 100+ questions!</p>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 START", type="primary", use_container_width=True):
            st.session_state.page = "select_set"
            st.rerun()

# -------------------------------------------------------------------------
# PAGE 2: SELECT QUESTION SET SCREEN (10 Sets & Start Quiz Button at Bottom)
# -------------------------------------------------------------------------
elif st.session_state.page == "select_set":
    st.markdown("<h2 style='text-align: center;'>📌 Choose Your Question Set</h2>", unsafe_allow_html=True)
    st.write("")

    selected_set_name = st.selectbox("Select one of the 10 sets:", options=list(QUESTION_SETS.keys()))
    
    st.info(f"You selected: **{selected_set_name}** (Contains 10 Questions, 30s timer each)")
    st.write("---")

    col_back, col_start = st.columns([1, 1])
    with col_back:
        if st.button("⬅️ Back", use_container_width=True):
            st.session_state.page = "welcome"
            st.rerun()
    with col_start:
        if st.button("🚀 Start Quiz", type="primary", use_container_width=True):
            st.session_state.questions = QUESTION_SETS[selected_set_name]
            st.session_state.selected_topic = selected_set_name
            st.session_state.q_idx = 0
            st.session_state.answers = {}
            st.session_state.quiz_over = False
            st.session_state.q_start_time = time.time()
            st.session_state.page = "quiz"
            st.rerun()

# -------------------------------------------------------------------------
# PAGE 3: QUIZ SCREEN (Interactive 10 Questions with Timer)
# -------------------------------------------------------------------------
elif st.session_state.page == "quiz" and not st.session_state.get('quiz_over', False):
    q_num = st.session_state.q_idx
    curr_q = st.session_state.questions[q_num]

    elapsed = int(time.time() - st.session_state.q_start_time)
    time_left = max(0, TIME_PER_QUESTION - elapsed)

    # Auto-advance if timer hits 0
    if time_left == 0:
        if q_num < len(st.session_state.questions) - 1:
            st.session_state.q_idx += 1
            st.session_state.q_start_time = time.time()
            st.rerun()
        else:
            st.session_state.quiz_over = True
            st.rerun()

    c1, c2 = st.columns([3, 1])
    with c1:
        st.write(f"**Topic:** `{st.session_state.selected_topic}`")
        st.write(f"**Question {q_num + 1} of {len(st.session_state.questions)}**")
    with c2:
        st.markdown(f"<div class='timer-box'>⏳ {time_left}s</div>", unsafe_allow_html=True)

    st.progress((q_num + 1) / len(st.session_state.questions))
    st.subheader(f"Q{q_num + 1}: {curr_q['q']}")

    default_idx = None
    if q_num in st.session_state.answers:
        default_idx = curr_q['options'].index(st.session_state.answers[q_num])

    selected_option = st.radio(
        "Select your answer:",
        curr_q['options'],
        index=default_idx,
        key=f"radio_{q_num}"
    )

    if selected_option:
        st.session_state.answers[q_num] = selected_option

    st.write("")
    btn1, btn2, btn3 = st.columns([1, 1, 1])
    with btn1:
        if q_num > 0 and st.button("⬅️ Previous"):
            st.session_state.q_idx -= 1
            st.session_state.q_start_time = time.time()
            st.rerun()
    with btn2:
        if q_num < len(st.session_state.questions) - 1 and st.button("Next ➡️"):
            st.session_state.q_idx += 1
            st.session_state.q_start_time = time.time()
            st.rerun()
    with btn3:
        if q_num == len(st.session_state.questions) - 1 and st.button("Submit 🏁", type="primary"):
            st.session_state.quiz_over = True
            st.rerun()

# -------------------------------------------------------------------------
# PAGE 4: RESULT SCREEN & REVIEW
# -------------------------------------------------------------------------
elif st.session_state.page == "quiz" and st.session_state.get('quiz_over', False):
    st.balloons()
    st.header("🏆 Quiz Completed!")
    st.write(f"**Topic:** {st.session_state.selected_topic}")

    total_q = len(st.session_state.questions)
    score = sum(1 for idx, q in enumerate(st.session_state.questions) if st.session_state.answers.get(idx) == q['ans'])
    percentage = (score / total_q) * 100

    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Score", f"{score} / {total_q}")
    with col_b:
        st.metric("Percentage", f"{percentage:.0f}%")

    st.write("---")
    st.subheader("📝 Detailed Answer Review")

    for i, q in enumerate(st.session_state.questions):
        user_a = st.session_state.answers.get(i, "Not Answered (Timeout)")
        correct_a = q['ans']
        
        if user_a == correct_a:
            st.success(f"**Q{i+1}: {q['q']}**\n- Your Answer: `{user_a}` ✅")
        else:
            st.error(f"**Q{i+1}: {q['q']}**\n- Your Answer: `{user_a}` ❌\n- Correct Answer: `{correct_a}`")

    st.write("")
    if st.button("🔄 Choose Another Topic Set", type="primary", use_container_width=True):
        st.session_state.page = "select_set"
        st.rerun()