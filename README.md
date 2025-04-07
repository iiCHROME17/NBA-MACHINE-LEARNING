# 🏀 NBA Season Predictor (2024–2025)

A Machine Learning project that analyzes **player and team performance** data from the 2024–2025 NBA season to make high-level predictions using historical stats, team dynamics, and game outcomes.

---

## 🔍 What This Project Does

Using NBA game logs, player stats, and team data, we train models to **predict end-of-season outcomes**. The project includes multiple focused applications:

### 🎖️ Accolade Predictor
Predicts which players are most likely to receive **end-of-season accolades** such as:
- MVP (Most Valuable Player)
- DPOY (Defensive Player of the Year)
- MIP (Most Improved Player)

This model uses per-game and cumulative player statistics to find high-impact players.

---

### 🏆 Playoff Team Predictor
Determines whether a given team is likely to **qualify for the playoffs** based on:
- Win-loss record
- Advanced team stats (FG%, REB, AST, etc.)
- Season momentum


---

### 👑 NBA Champion Predictor
Trained on team-level stats, win streaks, and playoff seeds to estimate the **probability of a team winning the championship**.

This model simulates playoff matchups using bracket logic and strength metrics.

---

## 🛠️ Tech Stack
- **Python** & `pandas`, `numpy`
- **Scikit-learn** for ML models
- CSV datasets from full 2024–2025 NBA season (Up until 7/4/2025)

---

## 📂 Datasets
- `NBA_GAMES.csv` – Team performance per game
- `NBA_PLAYER_GAMES.csv` – Individual player game logs
- `NBA_PLAYERS.csv` – Player metadata (active/inactive)
- `NBA_TEAMS.csv` – Team metadata

---