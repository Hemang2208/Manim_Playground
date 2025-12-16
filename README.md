# 🎥 Maths & CS Algorithm Visualizations (Manim)

An open-source project focused on visualizing **Mathematics** and **Computer Science algorithms** using Manim.

This repository aims to make abstract concepts intuitive by turning them into clean, meaningful animations — from math fundamentals to core CS algorithms.

**If you believe "seeing is understanding", this project is for you.**

---

## 🌟 Project Vision

- **Visualize Mathematical concepts** (Geometry, Calculus, Linear Algebra, Probability)
- **Animate Computer Science algorithms** (Sorting, Searching, Graphs, DP, etc.)
- **Help learners understand logic, flow, and intuition**
- **Encourage open-source learning through visuals**

This project is built for:

- 🎓 Students
- 👩‍🏫 Educators
- 💻 Developers
- 🧠 Anyone who loves learning visually

---

## 🧰 Requirements

⚠️ **Python 3.12.10 ONLY**

This project strictly uses **Python 3.12.10** to ensure compatibility with Manim.

🔗 **Download**: https://www.python.org/downloads/release/python-31210/

---

## 🚀 Installation & Setup (Using .venv)

### 1️⃣ Create Virtual Environment

```powershell
python -m venv .venv
```

### 2️⃣ Activate Virtual Environment

**PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**CMD:**

```cmd
.venv\Scripts\activate.bat
```

### 3️⃣ Install Dependencies

```powershell
pip install -r requirements.txt
```

**Verify Manim:**

```powershell
manim --version
```

---

## ▶️ Running Animations (Recommended)

We recommend **Medium Quality** for development and previews:

```powershell
manim -pqm main.py BeautifulIntro
```

### Quality Presets

- **`-pql`** → Low (fast preview)
- **`-pqm`** → Medium (recommended)
- **`-pqh`** → High (1080p)
- **`-pqk`** → 4K (final export)

The `-p` flag automatically opens the rendered video.

---

## 🤝 Open Source Contributions

We actively welcome contributions from the community ❤️

### What You Can Contribute

- 📐 **Math visualizations** (formulas, theorems, concepts)
- 🧠 **CS algorithms** (step-by-step logic animations)
- ✨ **Better transitions**, layouts, or explanations
- 📖 **Educational clarity** through visuals

### Contribution Rules

✅ **Please DO:**

- Add new Manim scenes in Python
- Focus on **logic + explanation**
- Write **readable, commented code**
- Test your animation before committing

❌ **Please DO NOT:**

- Upload rendered videos (`.mp4`, `.mov`, etc.)
- Commit the `media/` directory
- Commit `.venv/`, `__pycache__`, or local files

All generated outputs are intentionally ignored via `.gitignore`.

---

## 📁 Project Structure

```
.
├── main.py              # Animation scenes
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── .gitignore           # Ignore rules
├── .venv/               # Virtual environment (ignored)
└── media/               # Rendered videos (ignored)
```

---

## 📚 Useful Resources

- **Manim Docs** → https://docs.manim.community/
- **Manim Examples** → https://docs.manim.community/en/stable/examples.html
- **Manim Discord** → https://www.manim.community/discord/

---

## 🌍 Community & License

This is an **open-source learning project** built with the goal of making  
**Maths & Algorithms beautiful, visual, and intuitive.**

**Fork it. Improve it. Teach with it.**  
Let's learn Maths + CS visually, together 🚀✨
