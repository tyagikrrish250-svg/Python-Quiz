import time
import streamlit as st
from quiz_data import QUESTIONS

st.set_page_config(
    page_title="Python Quiz Pro",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Dark Neon styling
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 12% 8%, rgba(0,229,255,.10), transparent 28%),
        radial-gradient(circle at 88% 14%, rgba(139,92,246,.12), transparent 30%),
        linear-gradient(135deg, #05070d 0%, #080d18 48%, #070914 100%);
    color: #f5f7ff;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.neon-top {
    height: 4px;
    width: 100%;
    background: linear-gradient(90deg, #00e5ff, #8b5cf6, #ff3cac);
    border-radius: 20px;
    box-shadow: 0 0 18px rgba(0,229,255,.45);
    margin-bottom: 1.5rem;
}

.hero {
    padding: 3rem 2rem 2.6rem;
    border: 1px solid #1a2945;
    border-radius: 28px;
    background: linear-gradient(145deg, rgba(13,18,32,.97), rgba(10,14,25,.93));
    box-shadow: 0 25px 80px rgba(0,0,0,.35), inset 0 0 50px rgba(0,229,255,.025);
    text-align: center;
}

.python-logo {
    width: 108px;
    height: 108px;
    margin: 0 auto 1rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 58px;
    background: radial-gradient(circle, #111b31 20%, #0b1220 72%);
    border: 2px solid #00e5ff;
    box-shadow: 0 0 18px rgba(0,229,255,.4), 0 0 45px rgba(139,92,246,.2);
}

.hero h1 {
    margin: 0;
    font-size: clamp(2.4rem, 6vw, 4.7rem);
    font-weight: 800;
    letter-spacing: -2px;
    color: #f5f7ff;
}

.hero h1 span {
    color: #00e5ff;
    text-shadow: 0 0 20px rgba(0,229,255,.28);
}

.hero p {
    color: #8d99b8;
    font-size: 1.05rem;
    margin: .8rem auto 0;
    max-width: 720px;
}

.chips {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 1.8rem;
}

.chip {
    padding: .55rem .9rem;
    border: 1px solid #202c46;
    border-radius: 999px;
    background: #11182a;
    color: #b9c4dc;
    font-size: .82rem;
}

.chip b { color: #00e5ff; }

.section-title {
    font-size: 1.65rem;
    font-weight: 800;
    color: #f5f7ff;
    margin: .8rem 0 .3rem;
}

.muted { color: #8d99b8; }

.set-card {
    min-height: 150px;
    padding: 1.15rem;
    border: 1px solid #1b2942;
    border-radius: 20px;
    background: linear-gradient(145deg, #0d1220, #101729);
    box-shadow: 0 12px 30px rgba(0,0,0,.18);
}

.set-number {
    font-size: .78rem;
    font-weight: 800;
    color: #00e5ff;
    letter-spacing: 1px;
}

.set-name {
    font-size: 1.15rem;
    font-weight: 800;
    margin-top: .25rem;
    color: #f5f7ff;
}

.progress-shell {
    background: #10182a;
    border: 1px solid #1d2a43;
    border-radius: 999px;
    height: 10px;
    overflow: hidden;
    margin: .6rem 0 1rem;
}

.progress-bar {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #00e5ff, #8b5cf6);
    box-shadow: 0 0 14px rgba(0,229,255,.35);
}

.timer {
    padding: .7rem 1rem;
    border: 1px solid #283654;
    border-radius: 14px;
    background: #0d1424;
    text-align: center;
}

.timer strong {
    color: #00e5ff;
    font-size: 1.4rem;
}

.question-card {
    padding: 1.7rem;
    border-radius: 22px;
    border: 1px solid #1b2942;
    background: linear-gradient(145deg, #0d1220, #0e1525);
    box-shadow: 0 18px 55px rgba(0,0,0,.25);
}

.question-label {
    color: #00e5ff;
    font-size: .82rem;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.question-text {
    color: #f5f7ff;
    font-size: 1.45rem;
    line-height: 1.45;
    font-weight: 700;
    margin: .65rem 0 1.2rem;
}

.result-card {
    padding: 1.6rem;
    border-radius: 22px;
    border: 1px solid #1b2942;
    background: #0d1220;
}

.score {
    font-size: 4.5rem;
    font-weight: 800;
    color: #00e5ff;
    line-height: 1;
    text-shadow: 0 0 22px rgba(0,229,255,.25);
}

.correct {
    border-left: 4px solid #22c55e;
    background: rgba(34,197,94,.06);
}

.incorrect {
    border-left: 4px solid #ef4444;
    background: rgba(239,68,68,.06);
}

.review-item {
    padding: 1rem 1.1rem;
    border-radius: 14px;
    margin: .65rem 0;
    border-top: 1px solid #1a2945;
    border-right: 1px solid #1a2945;
    border-bottom: 1px solid #1a2945;
}

div.stButton > button {
    border-radius: 12px;
    border: 1px solid #243452;
    background: #11182a;
    color: #f5f7ff;
    font-weight: 700;
    min-height: 44px;
    transition: .18s ease;
}

div.stButton > button:hover {
    border-color: #00e5ff;
    color: #00e5ff;
    box-shadow: 0 0 18px rgba(0,229,255,.14);
}

div.stButton > button[kind="primary"] {
    background: linear-gradient(90deg, #00d9f5, #00b8d4);
    color: #061018;
    border: none;
    box-shadow: 0 0 22px rgba(0,229,255,.2);
}

[data-testid="stRadio"] label {
    color: #d9e1f2 !important;
}

hr { border-color: #1a2945 !important; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Session state
# -----------------------------
def init_state():
    defaults = {
        "page": "home",
        "selected_set": None,
        "question_index": 0,
        "answers": [],
        "start_time": None,
        "result": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

def go_home():
    st.session_state.page = "home"
    st.session_state.selected_set = None
    st.session_state.question_index = 0
    st.session_state.answers = []
    st.session_state.start_time = None
    st.session_state.result = None

def start_set(set_no):
    st.session_state.page = "quiz"
    st.session_state.selected_set = set_no
    st.session_state.question_index = 0
    st.session_state.answers = [None] * 15
    st.session_state.start_time = time.time()
    st.session_state.result = None

def finish_quiz():
    set_no = st.session_state.selected_set
    answers = st.session_state.answers
    questions = QUESTIONS[set_no]
    score = sum(
        1 for i, ans in enumerate(answers)
        if ans is not None and ans == questions[i][2]
    )
    st.session_state.result = score
    st.session_state.page = "result"
    st.session_state.start_time = None

SET_NAMES = [
    "Python Basics",
    "Data Types & Collections",
    "Conditionals & Loops",
    "Functions & Arguments",
    "Object-Oriented Programming",
    "Modules & Libraries",
    "File Handling",
    "Iterators & Comprehensions",
    "Python Tools & PEP 8",
    "Built-ins & Complexity",
]

SET_DESCRIPTIONS = [
    "Syntax, variables, operators and core Python concepts",
    "Booleans, lists, tuples, sets and dictionaries",
    "if/elif/else statements, loops and loop control",
    "Functions, parameters, arguments, *args and **kwargs",
    "Classes, objects, inheritance, polymorphism and self",
    "Imports, standard libraries, JSON, regex and random",
    "Reading, writing, appending and working with files",
    "Comprehensions, generators, iterators, iter() and next()",
    "PEP 8, Python philosophy, terminal commands and environments",
    "Built-ins, sorting, min/max and algorithmic complexity",
]

# -----------------------------
# HOME
# -----------------------------
if st.session_state.page == "home":
    st.markdown('<div class="neon-top"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="hero">
        <div class="python-logo">🐍</div>
        <h1>PYTHON <span>QUIZ PRO</span></h1>
        <p>Test your Python knowledge with a professional timed quiz experience.</p>
        <div class="chips">
            <div class="chip"><b>150</b> QUESTIONS</div>
            <div class="chip"><b>10</b> SETS</div>
            <div class="chip"><b>30s</b> PER QUESTION</div>
            <div class="chip"><b>DETAILED</b> REVIEW</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    _, center, _ = st.columns([1, 2, 1])
    with center:
        if st.button("🚀  START QUIZ", type="primary", use_container_width=True):
            st.session_state.page = "sets"
            st.rerun()

# -----------------------------
# SET SELECTION
# -----------------------------
elif st.session_state.page == "sets":
    st.markdown('<div class="neon-top"></div>', unsafe_allow_html=True)

    # Names displayed for the 10 quiz sets.
    # Change only these 10 strings if you want different names later.
    set_names = [
        "Python Fundamentals",
        "Variables & Data Types",
        "Operators & Expressions",
        "Conditional Statements",
        "Loops & Iterations",
        "Functions",
        "Lists, Tuples & Sets",
        "Dictionaries & Strings",
        "File Handling & Exceptions",
        "OOP & Advanced Python",
    ]

    header_col, home_col = st.columns([4, 1])

    with header_col:
        st.markdown(
            '<div class="section-title">Choose Your Quiz Set</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="muted">Each set contains 15 questions with a 30-second timer per question.</div>',
            unsafe_allow_html=True
        )

    with home_col:
        if st.button("⌂ Home", key="sets_home", use_container_width=True):
            go_home()
            st.rerun()

    st.write("")

    # 10 sets = 5 rows × 2 columns
    for row in range(5):
        cols = st.columns(2)

        for col_idx in range(2):
            set_no = row * 2 + col_idx

            with cols[col_idx]:
                st.markdown(
                    f"""
                    <div class="set-card">
                        <div class="set-number">SET {set_no + 1:02d}</div>
                        <div class="set-name">{set_names[set_no]}</div>
                        <div class="muted">15 questions • 30 sec each</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    f"▶ Start Set {set_no + 1}",
                    key=f"set_{set_no}",
                    use_container_width=True
                ):
                    start_set(set_no)
                    st.rerun()

# -----------------------------
# QUIZ
# -----------------------------
elif st.session_state.page == "quiz":
    set_no = st.session_state.selected_set
    q_index = st.session_state.question_index
    questions = QUESTIONS[set_no]
    q_text, options, correct = questions[q_index]

    # 1-second refresh for the timer.
    try:
        from streamlit_autorefresh import st_autorefresh
        st_autorefresh(interval=1000, key=f"timer_{set_no}_{q_index}")
    except ImportError:
        pass

    elapsed = time.time() - (st.session_state.start_time or time.time())
    remaining = max(0, 30 - int(elapsed))

    if remaining <= 0:
        # Time expired: leave unanswered, then advance.
        if q_index < 14:
            st.session_state.question_index += 1
            st.session_state.start_time = time.time()
            st.rerun()
        else:
            finish_quiz()
            st.rerun()

    top1, top2, top3 = st.columns([3, 2, 1])
    with top1:
        st.markdown(f'<div class="section-title">Set {set_no + 1} • {SET_NAMES[set_no]}</div>', unsafe_allow_html=True)
    with top2:
        progress = q_index / 15
        st.markdown(f"""
        <div class="progress-shell"><div class="progress-bar" style="width:{progress*100:.1f}%"></div></div>
        """, unsafe_allow_html=True)
        st.caption(f"Question {q_index + 1} of 15")
    with top3:
        st.markdown(f'<div class="timer">⏱ <strong>{remaining:02d}s</strong></div>', unsafe_allow_html=True)

    st.markdown('<div class="question-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="question-label">Question {q_index + 1}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="question-text">{q_text}</div>', unsafe_allow_html=True)

    current_answer = st.session_state.answers[q_index]
    option_labels = [f"{chr(65+i)}. {opt}" for i, opt in enumerate(options)]
    default_index = current_answer if current_answer is not None else None

    selected = st.radio(
        "Select your answer:",
        option_labels,
        index=default_index,
        key=f"answer_{set_no}_{q_index}",
        label_visibility="collapsed",
    )
    if selected is not None:
        st.session_state.answers[q_index] = option_labels.index(selected)

    st.markdown('</div>', unsafe_allow_html=True)
    st.write("")

    nav1, nav2, nav3, nav4, nav5 = st.columns([1, 1, 1, 1, 1.3])

    with nav1:
        if st.button("← Previous", disabled=(q_index == 0), use_container_width=True):
            st.session_state.question_index -= 1
            st.session_state.start_time = time.time()
            st.rerun()

    with nav2:
        if st.button("Skip →", use_container_width=True):
            if q_index < 14:
                st.session_state.question_index += 1
                st.session_state.start_time = time.time()
                st.rerun()
            else:
                finish_quiz()
                st.rerun()

    with nav3:
        if st.button("Next →", disabled=(q_index == 14), use_container_width=True):
            st.session_state.question_index += 1
            st.session_state.start_time = time.time()
            st.rerun()

    with nav4:
        if st.button("⌂ Home", use_container_width=True):
            go_home()
            st.rerun()

    with nav5:
        if st.button("✓ Submit Quiz", type="primary", use_container_width=True):
            finish_quiz()
            st.rerun()

    st.caption("Tip: Skipped or unanswered questions count as incorrect. You can use Previous to review earlier questions.")

# -----------------------------
# RESULT
# -----------------------------
elif st.session_state.page == "result":
    set_no = st.session_state.selected_set
    score = st.session_state.result
    percentage = score / 15 * 100
    questions = QUESTIONS[set_no]
    answers = st.session_state.answers

    st.markdown('<div class="neon-top"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="hero">
        <div class="python-logo">🏆</div>
        <h1>QUIZ <span>RESULT</span></h1>
        <p>Your performance summary and detailed answer review.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="result-card"><div class="score">{score}/15</div><div class="muted">Score</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="result-card"><div class="score">{percentage:.0f}%</div><div class="muted">Percentage</div></div>', unsafe_allow_html=True)
    with c3:
        correct_count = score
        wrong_count = 15 - score
        st.markdown(f'<div class="result-card"><div style="font-size:1.25rem;font-weight:800;color:#22c55e">✓ {correct_count} Correct</div><div style="font-size:1.25rem;font-weight:800;color:#ef4444;margin-top:.5rem">✕ {wrong_count} Incorrect</div></div>', unsafe_allow_html=True)

    st.write("")
    x, y, z = st.columns([1, 1, 1])
    with x:
        if st.button("🔁 Try Another Set", type="primary", use_container_width=True):
            st.session_state.page = "sets"
            st.session_state.result = None
            st.rerun()
    with y:
        if st.button("🏠 Home", use_container_width=True):
            go_home()
            st.rerun()
    with z:
        st.empty()

    st.markdown('<div class="section-title">Detailed Review</div>', unsafe_allow_html=True)
    st.markdown('<div class="muted">See your selected answer and the correct answer for every question.</div>', unsafe_allow_html=True)
    st.write("")

    for i, (q, opts, correct) in enumerate(questions):
        selected_idx = answers[i]
        selected_text = "Not answered" if selected_idx is None else opts[selected_idx]
        correct_text = opts[correct]
        ok = selected_idx == correct

        status = "✓ Correct" if ok else "✕ Incorrect"
        cls = "correct" if ok else "incorrect"
        st.markdown(f"""
        <div class="review-item {cls}">
            <div style="font-weight:800;color:#f5f7ff">Q{i+1}. {q}</div>
            <div style="margin-top:.55rem;color:#b9c4dc">
                <b>Your answer:</b> {selected_text}
            </div>
            <div style="margin-top:.25rem;color:#b9c4dc">
                <b>Correct answer:</b> {correct_text}
            </div>
            <div style="margin-top:.45rem;font-weight:800"> {status}</div>
        </div>
        """, unsafe_allow_html=True)
