# Siddhant Pardeshi — Software Engineer & AI Automation Portfolio

> Modern, responsive developer portfolio featuring interactive computer vision & automation project simulators, contact form integration, and high-performance design.

Live Demo: Deployed via GitHub Pages.

---

## ⚡ Features
- **Modern Cyber & Developer Aesthetics**: Tailored dark theme (`#050a14`) with ambient radial glow, grid mesh background, and JetBrains Mono typography.
- **Interactive Project Demo Simulators (`<dialog>`)**:
  - **Facial Recognition Attendance Simulator**: Interactive webcam stream simulation, real-time bounding box recognition, 128-d encoding match score, and live attendance punch log.
  - **CSR Discovery Pipeline**: Scraper simulation showing lead generation, deduplication, and Google Sheets syncing.
  - **Automated CSR Email Engine**: Mail merge template preview and batch progress simulator with Gmail API token metrics.
  - **Responsive NGO Website**: Architecture overview and links to Mahesh Foundation's production site.
- **Functional Contact Form**: Direct form submission via Formspree with instant client-side validation and automated fallback to `mailto:`.
- **Fast & Responsive**: Mobile-first design, interactive hamburger drawer navigation, and zero heavy framework dependencies (Tailwind CDN + FontAwesome + Native HTML5/JS).
- **Automated GitHub Pages Workflow**: Push to `main` branch automatically builds and hosts your portfolio.

---

## 🚀 How to Deploy to GitHub Pages in 2 Minutes

### 1. Initialize & Push to your GitHub Repository:
Run the following commands in this directory:

```bash
git init
git add .
git commit -m "Initial commit: Siddhant Pardeshi Portfolio with Interactive Demos"
git branch -M main

# Link to your GitHub repository (replace with your repo URL if different):
git remote add origin https://github.com/siddhant835/Sid.git

# Push to GitHub
git push -u origin main --force
```

### 2. Enable GitHub Pages on GitHub:
1. Open your repository on GitHub: **`https://github.com/siddhant835/Sid`**
2. Click **Settings** (tab at the top) > **Pages** (in the left sidebar).
3. Under **Build and deployment** > **Source**, choose:
   - **GitHub Actions** (the included `.github/workflows/deploy.yml` will handle it automatically)
   - *OR* choose **Deploy from a branch** -> select `main` branch -> folder `/ (root)` and click **Save**.
4. Within 1-2 minutes, your website will be live at:
   `https://siddhant835.github.io/Sid/`

---

## 🛠️ Contact Form Configuration (Optional)
The contact form is currently configured to route messages via Formspree:
- If you'd like to receive inquiries directly at your email, create a free endpoint at [formspree.io](https://formspree.io) and replace the form `action` URL in `index.html`:
```html
<form id="contact-form" action="https://formspree.io/f/YOUR_ENDPOINT_ID" method="POST">
```
- If untouched or offline, the form automatically falls back to your default email client (`mailto:siddhantpardeshi137@gmail.com`).
