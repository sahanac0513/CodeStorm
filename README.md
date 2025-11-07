Career Compass AI
=================

This is a Streamlit web application that analyzes resumes and provides career guidance, learning plans, and career roadmaps.

What I changed (frontend polish)
- Added a consistent header and footer and wrapped page content in a glass-like `content-container` for a professional, modern look.
- Introduced CSS variables for the primary blue accent and subtle animations (shimmer, float, background pulse) with accessibility-friendly `prefers-reduced-motion` support.
- Improved typography and spacing, and added a small logo block in the header.

Deployment (recommended)

1) Streamlit Community Cloud (fastest, easiest):
- Make sure this repository has a `requirements.txt` (it does).
- Push your repo to GitHub.
- Go to https://streamlit.io/cloud and click "New app" → connect your GitHub repo → select the branch and `app.py` as the main file → deploy.

2) Docker (portable; good for VPS or other providers):
- Create a Dockerfile (example below) and build an image.

Example Dockerfile:

```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8501
CMD ["streamlit","run","app.py","--server.port","8501","--server.address","0.0.0.0"]
```

Build and run locally:

```bash
docker build -t careercanvas:latest .
docker run -p 8501:8501 careercanvas:latest
```

3) Other platforms (Heroku / Railway / Render):
- Use Docker or the `streamlit` command. These platforms usually accept a Docker image or can run a web process that launches Streamlit.

Notes and limitations
- Netlify is designed for static sites and cannot directly host a Streamlit server app. Use Streamlit Cloud, Docker, or container-friendly PaaS instead.
- Backend logic was intentionally NOT modified. All changes are presentation-only.

Troubleshooting
- If you see stale CSS after editing, open the app in an incognito window or clear the browser cache. Streamlit sometimes caches assets.
- Ensure `requirements.txt` is up-to-date; Streamlit Cloud installs packages from it.

Want me to:
- Add a Docker Compose file and a small `Procfile` for convenience?
- Create an automatic GitHub Actions workflow that deploys to a provider when you push to `main`?

If yes, tell me which deployment target you prefer and I'll add the necessary files and CI workflow.
