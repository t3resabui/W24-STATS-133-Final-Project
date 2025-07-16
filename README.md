# W24-STATS-133-Final-Project

## Trump News Media Analysis

**Authors:** Andrew Arteaga, Teresa Bui, Kyle Lee  
**Course:** STATS 133 Final Project
**Winter 2024**

## 📖 Overview

This project investigates how liberal and conservative media outlets report on former President Donald Trump. We examine whether there is bias in news coverage by comparing the language, sentiment, and topics presented by two major news sources: CNN and the NY Post.

The project combines **web scraping**, **text processing**, **sentiment analysis**, and **machine learning classification** to uncover meaningful patterns.

---

### 🕸 Web Scraping Tools

- **scrapy spiders** (`cnnspider.py`, `myspider.py`):  
  Used for efficiently scraping article texts from static HTML pages on CNN and NY Post.

- **Selenium (`webscraping.py`)**:  
  Used for scraping dynamic content where JavaScript loads additional links or data.  
  Selenium opens a real browser, interacts with elements like “Load More” buttons, waits for JavaScript to render content, and then extracts the needed data.

Together, these tools allowed us to fully collect both the static and dynamic parts of the news websites.

---

## 🔗 Data Collection

We used Python `scrapy` spiders to scrape:

- Article links, headlines, dates, and descriptions into CSV files.
- Full article texts by visiting the scraped links.

Specifically:
- [`cnnspider.py`](scraping/scraping/spiders/cnnspider.py): Scrapes article texts from CNN.
- [`myspider.py`](scraping/scraping/spiders/myspider.py): Scrapes article texts from the NY Post.

The final datasets:
- `cnn.csv` - CNN Links 
- `cnn_text.csv` → CNN dataset.
- `nypost.csv` - NY Post Links 
- `scraped.csv` → NY Post dataset.

---

## 🔬 Analysis (in R)

We performed analysis and modeling in R, documented in:

- [`133 final project.Rmd`](133 final project.Rmd)
- [`133 final project (N-grams).Rmd`](133 final project (N-grams).Rmd)

**Key steps:**
- Text cleaning (lowercasing, punctuation removal, stopword removal, stemming).
- Vocabulary breakdown (total terms, unique terms, vocabulary density).
- Sentiment analysis (NRC lexicon) on both headlines and article bodies.
- Bigram (two-word phrase) analysis and word correlation plots.
- Topic modeling using LDA (Latent Dirichlet Allocation).
- Machine learning classification (Random Forest, Logistic Regression, KNN) to classify articles by source.

---

## 📊 Findings

- Both CNN and NY Post articles leaned slightly positive overall in sentiment, despite expectations of negative coverage.
- Headlines were notably more negative than the article bodies.
- Topic modeling revealed key themes like legal proceedings, political campaigns, and constitutional issues.
- Random Forest classification achieved ~93.6% accuracy distinguishing between CNN and NY Post articles.

For detailed visualizations and results, see:
- [`STATS 133 Final Project (1).pdf`](STATS%20133%20Final%20Project%20(1).pdf)

---

## 📁 Project Files

- `scraping/` → Python webscraping code.
- `data/` → Scraped CSV datasets.
- `.Rmd` files → R analysis scripts.
- `.ipynb` → Jupyter notebook with additional exploration.
- `.pdf` → Final presentation slides.

---

## 🚀 How to Run

1. **Web scraping:**
   - Install Python, `scrapy`, and dependencies.
   - Run spiders:
     ```bash
     scrapy crawl cnnspider
     scrapy crawl myspider
     ```

2. **R analysis:**
   - Open `.Rmd` files in RStudio.
   - Knit to HTML or run chunks interactively.

---

## 💡 Credits

- Slides template by [Slidesgo](https://slidesgo.com).
- Icons by [Flaticon](https://flaticon.com).
- Infographics & images by [Freepik](https://freepik.com).

---

Thank you!