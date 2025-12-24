# � Maths & CS Algorithm Visualizations

An open-source project focused on visualizing **Mathematics** and **Computer Science algorithms** using **Manim** with an interactive **Streamlit** web interface.

This repository aims to make abstract concepts intuitive by turning them into clean, meaningful animations — from math fundamentals to core CS algorithms.

**If you believe "seeing is understanding", this project is for you.**

---

## 🌟 Project Vision

- **Visualize Mathematical concepts** (Geometry, Calculus, Linear Algebra, Probability)
- **Animate Computer Science algorithms** (Sorting, Searching, Graphs, DP, etc.)
- **Interactive web interface** for easy rendering and playback
- **Help learners understand logic, flow, and intuition**
- **Encourage open-source learning through visuals**

This project is built for:

- 🎓 Students
- 👩‍🏫 Educators
- 💻 Developers
- 🧠 Visual Learners

---

## ✨ Features

### 🎬 Streamlit Web Interface (`app.py`)

- **Interactive rendering**: Render animations directly from the browser
- **Quality selection**: Choose from low, medium, high, or production quality
- **Video gallery**: Browse and play all rendered animations
- **Code viewer**: View animation source code within the app
- **Real-time feedback**: See rendering progress and errors

### 🎥 Animation Scenes (`main.py`)

- **BeautifulIntro**: A comprehensive introduction animation showcasing:
  - Project title and tagline
  - Visual representations of math concepts and CS algorithms
  - Target audience presentation
  - Open-source learning message
  - Beautiful closing with animated shapes

---

## 🧰 Requirements

### System Requirements

- **Python 3.12.10** (recommended for full compatibility)
- **FFmpeg** (required for video rendering)
- **System packages** (for Linux/Unix):
  - `libcairo2-dev`
  - `pkg-config`
  - `python3-dev`
  - `libpango1.0-dev`

### Python Dependencies

- **Manim** 0.19.1+ (animation engine)
- **Streamlit** (web interface)
- **Additional libraries**: NumPy, SciPy, Pillow, etc. (see `requirements.txt`)

---

## 🚀 Installation & Setup

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

**Linux/Mac:**

```bash
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4️⃣ Verify Installation

```powershell
manim --version
streamlit --version
```

---

## ▶️ Usage

### 🌐 Option 1: Streamlit Web Interface (Recommended)

Launch the interactive web application:

```powershell
streamlit run app.py
```

This opens a browser interface where you can:

- 🎬 Render animations with custom quality settings
- 📁 View all previously rendered videos
- 📝 Browse the source code
- 🎥 Watch animations directly in the browser

### 💻 Option 2: Command Line

Render animations directly using Manim CLI:

```powershell
manim -pqm main.py BeautifulIntro
```

#### Quality Presets

- **`-pql`** → Low quality (480p15 - fast preview)
- **`-pqm`** → Medium quality (720p30 - recommended)
- **`-pqh`** → High quality (1080p60 - high definition)
- **`-pqk`** → 4K quality (2160p60 - production)

The `-p` flag automatically opens the rendered video after creation.

---

## 📁 Project Structure

```
Manim_Final_GitHub/
├── app.py                  # Streamlit web interface
├── main.py                 # Manim animation scenes
├── requirements.txt        # Python dependencies
├── packages.txt            # System packages (Linux)
├── README.md               # Project documentation
├── .gitignore              # Ignore rules
├── .venv/                  # Virtual environment (ignored)
├── __pycache__/            # Python cache (ignored)
└── media/                  # Rendered outputs (ignored)
    ├── images/             # Rendered images
    ├── texts/              # Text outputs
    └── videos/             # Rendered videos
        └── main/
            └── 720p30/     # Quality-specific videos
```

---

## 🎨 Available Scenes

### BeautifulIntro

A comprehensive introduction scene that showcases:

- **Project Title & Tagline**: "Seeing is Understanding"
- **Vision Section**: Mathematical concepts and CS algorithms visualization
- **Target Audience**: Students, Educators, Developers, Visual Learners
- **Open Source Message**: Community-driven visual education
- **Final Message**: Making math and algorithms beautiful and intuitive

**Render command:**

```powershell
manim -pqm main.py BeautifulIntro
```

---

## 🤝 Open Source Contributions

We actively welcome contributions from the community ❤️

### What You Can Contribute

- 📐 **Math visualizations** (formulas, theorems, concepts)
- 🧠 **CS algorithms** (step-by-step logic animations)
- ✨ **Better transitions**, layouts, or explanations
- 🎨 **UI/UX improvements** for the Streamlit interface
- 📖 **Educational clarity** through visuals
- 🐛 **Bug fixes** and performance improvements

### Contribution Guidelines

✅ **Please DO:**

- Add new Manim scenes in `main.py`
- Focus on **logic + explanation** in animations
- Write **readable, commented code**
- Test your animation before committing
- Update this README if adding new features
- Follow existing code style and structure

❌ **Please DO NOT:**

- Upload rendered videos (`.mp4`, `.mov`, etc.)
- Commit the `media/` directory
- Commit `.venv/`, `__pycache__/`, or local files
- Include personal or sensitive information

All generated outputs are intentionally ignored via `.gitignore`.

---

## 📚 Useful Resources

- **Manim Documentation** → https://docs.manim.community/
- **Manim Examples** → https://docs.manim.community/en/stable/examples.html
- **Manim Discord Community** → https://www.manim.community/discord/
- **Streamlit Documentation** → https://docs.streamlit.io/
- **3Blue1Brown** (Manim creator) → https://www.3blue1brown.com/

---

## 🐛 Troubleshooting

### Common Issues

**Manim not found:**

- Ensure virtual environment is activated
- Reinstall: `pip install manim`

**FFmpeg errors:**

- Install FFmpeg: https://ffmpeg.org/download.html
- Verify: `ffmpeg -version`

**Streamlit won't start:**

- Check port availability (default: 8501)
- Try: `streamlit run app.py --server.port 8502`

**Rendering fails:**

- Check scene name matches class name in `main.py`
- Verify Python version: `python --version`
- Check Manim logs for specific errors

---

## 📄 License

This is an **open-source learning project** built with the goal of making  
**Maths & Algorithms beautiful, visual, and intuitive.**

**Fork it. Improve it. Teach with it.**

---

## 🌍 Community

Let's learn Maths + CS visually, together 🚀✨

Made with ❤️ using **Manim** & **Streamlit**

---

## 🔗 Quick Links

- **Report Issues**: [GitHub Issues](https://github.com/Hemang2208/Manim_Playground/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Hemang2208/Manim_Playground/discussions)
- **Pull Requests**: [Contribute](https://github.com/Hemang2208/Manim_Playground/pulls)

---
