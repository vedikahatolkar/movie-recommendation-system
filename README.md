# 🎬 Popcorn & Scripts – Movie Recommendation System

Popcorn & Scripts is a **hybrid movie recommendation system** that suggests movies based on user preferences using both **collaborative filtering** and **content-based filtering**. It also integrates with the **TMDb API** to display posters and enhance user experience.

---

## 🚀 Features

- 🎯 Hybrid Recommendation System (Collaborative + Content-based)
- 👤 User Authentication (Login / Signup)
- ⭐ Movie Rating System
- 🧠 Personalized Recommendations
- 🔍 Live Movie Search with Suggestions
- 🎥 TMDb Integration (Posters & Movie Info)
- 🎨 Modern UI (Glassmorphism + Dark Theme)
- 📊 Scalable Architecture (Flask + ML + API layers)

---

## 🧠 Recommendation Techniques

### 1. Collaborative Filtering
- Uses user-movie interaction matrix
- Suggests movies based on similar user behavior

### 2. Content-Based Filtering
- Uses TF-IDF on movie genres + titles
- Computes similarity using cosine similarity

### 3. Hybrid Model
- Combines both approaches
- Improves recommendation accuracy

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- SQLAlchemy

### Machine Learning
- Pandas
- Scikit-learn (TF-IDF, Cosine Similarity)

### Frontend
- HTML
- CSS (Glassmorphism UI)
- JavaScript (Search suggestions)

### APIs
- TMDb API (for posters & trailers)

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
TMDB_API_KEY=your_api_key_here
python -m app.app
Open in browser:
http://127.0.0.1:5000
