# Siddhant Pardeshi — Software Engineer & AI Automation Portfolio

> **100% Python Web Portfolio** powered by **Streamlit**, featuring interactive computer vision & automation project simulators, live data pipelines, and instant hosting.

---

## ⚡ Features (100% Python)
- **Built in Pure Python (`app.py`)**: Zero HTML/CSS required to build or modify — designed directly in Python using Streamlit.
- **Interactive Project Demos & Simulators**:
  - **Facial Recognition Attendance Simulator**: Real-time webcam integration with `st.camera_input`, simulated bounding box rendering, confidence scoring (98.4%), and interactive attendance database with CSV export.
  - **CSR Discovery Pipeline**: Live lead ingestion and deduplication table using pandas.
  - **Automated CSR Email Engine**: Dynamic mail merge template preview (`{{Company_Name}}`) and progress batch simulator.
  - **Responsive NGO Website**: Architecture overview and links to Mahesh Foundation's production site.
- **Interactive Contact Form**: Direct form submission built in Python with email dispatch.
- **Modern Dark Aesthetic**: Custom theme with metric cards, status badges, and terminal snapshot.

---

## 🚀 Running Locally

### 1. Setup Virtual Environment & Install Dependencies:
```bash
# Create virtual environment (if not already created)
python -m venv .venv

# Activate virtual environment
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Launch Streamlit Portfolio:
```bash
streamlit run app.py
```
Your browser will open automatically at `http://localhost:8501`.

---

## 🌐 Deploy Free on Streamlit Community Cloud (1-Click)

1. Ensure your latest code is pushed to GitHub:
   ```bash
   git add .
   git commit -m "feat: 100% python streamlit portfolio"
   git push origin main
   ```
2. Go to **[share.streamlit.io](https://share.streamlit.io)** and log in with GitHub.
3. Click **"New App"** and select:
   - **Repository:** `siddhant835/Sid`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Click **Deploy!** Your Python portfolio will be live worldwide in ~1 minute at a custom URL (e.g. `siddhant-pardeshi.streamlit.app`).
