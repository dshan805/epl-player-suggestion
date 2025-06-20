# English Premier League Player Suggestion

In the highly competitive world of professional football, strategic player recruitment and squad management are paramount. This English Premier League Player Suggestion tool was developed to address a critical challenge faced by scouting departments and clubs: efficiently identifying statistically similar players. This is particularly vital when seeking a replacement for a key player who has been sold, or when exploring alternative transfer targets after an initial preferred option becomes unavailable.

The tool analyzes historical player statistics and FIFA 21 data to provide data-driven recommendations. It combines comprehensive EPL Statistics (all-time performance) with detailed FIFA 21 Player Attributes (e.g., positions) to create a robust dataset. The system then utilizes the K-Nearest Neighbors (KNN) algorithm to find the most statistically similar players to a given input player. It handles user input, validates player names using fuzzy matching, and suggests similar players based on their comprehensive statistical profile.

---

## Table of Contents
- [Introduction](#introduction)
- [Data Sources](#data-sources)
- [How It Works](#how-it-works)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction
The EPL Player Suggestion tool analyzes player statistics and finds similar players based on performance. It combines data from two datasets:
1. **EPL Statistics**: Comprehensive player statistics updated daily, covering all-time EPL performance.
2. **FIFA 21 Data**: Detailed player attributes (e.g., positions) to complement the EPL dataset.

The system handles user input, validates player names, and suggests similar players based on their statistical profile.

---

## Data Sources
- **EPL Statistics Dataset**:
  - URL: [Kaggle EPL Dataset](https://www.kaggle.com/datasets/rishikeshkanabar/premier-league-player-statistics-updated-daily/data)
  - Contains all-time player statistics in the EPL.

- **FIFA 21 Player Data**:
  - URL: [Kaggle FIFA 21 Dataset](https://www.kaggle.com/datasets/aayushmishra1512/fifa-2021-complete-player-data)
  - Adds detailed player positions and attributes to the EPL dataset.

**Note**: The data represents players' cumulative statistics across all their seasons in the EPL. Therefore, players with longer careers may have more data than those with shorter careers.

---

## How It Works
1. **Data Reading**:
   - The `read_data.py` script reads the EPL and FIFA datasets.

2. **Data Cleaning**:
   - The `clean_data.py` script removes unnecessary columns, handles missing values, and integrates the two datasets.

3. **Model Training**:
   - The `model.py` script builds a K-Nearest Neighbors (KNN) model using cleaned data to identify similar players.

4. **Player Recommendations**:
   - The `app.py` script:
     - Prompts the user to enter a player's name.
     - Validates the input, using fuzzy matching for misspelled names.
     - Suggests the most similar players based on the KNN model.

---

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- Required Python libraries:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `rapidfuzz`
  - `joblib`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/epl-player-suggestion.git
   cd epl-player-suggestion
