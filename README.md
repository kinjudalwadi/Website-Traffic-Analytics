# Website Traffic Analytics Dashboard

## Project Overview

This project analyzes website traffic data to understand user behavior, traffic acquisition channels, website engagement, and conversion performance using Python and SQL.

The objective is to transform raw website traffic data into meaningful business insights that help improve website performance and support data-driven decision making.

---

## Business Problem

Organizations receive website visitors from multiple traffic sources including Organic Search, Direct, Social Media, Referral, Email Marketing, and Paid Campaigns.

The objective of this project is to answer the following business questions:

- Which traffic source generates the highest number of users?
- Which devices contribute the most website traffic?
- What is the website's average bounce rate?
- How many users complete conversions?
- Which countries generate the highest traffic?
- What trends can be identified over time?

---

## Project Structure

```text
Website-Traffic-Analytics/
│
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── data/
│   └── website_traffic.csv
│
├── python/
│   └── analysis.py
│
├── sql/
│   └── traffic_analysis.sql
│
├── notebooks/
│   └── Website_Traffic_Analytics.ipynb
│
├── dashboard/
│   ├── dashboard.png
│   └── Tableau_Dashboard.twb
│
└── images/
```

---

## Dataset

The dataset contains website performance metrics collected over a period of time.

| Column | Description |
|----------|-------------|
| Date | Website activity date |
| Users | Total unique visitors |
| Sessions | Total website sessions |
| PageViews | Total pages viewed |
| BounceRate | Percentage of visitors leaving after one page |
| SessionDuration | Average session duration (seconds) |
| Conversions | Number of successful conversions |
| TrafficSource | Source of website traffic |
| Device | Desktop, Mobile or Tablet |
| Country | Visitor country |

---

## Technologies Used

- Python
- Pandas
- NumPy
- SQL
- CSV
- Tableau (Planned)
- Matplotlib (Planned)

---

## Project Workflow

### 1. Data Collection

- Imported website traffic dataset from CSV.

### 2. Data Cleaning

- Checked missing values
- Removed duplicate records
- Converted date columns
- Verified data types

### 3. Exploratory Data Analysis (EDA)

Performed analysis on:

- Total Users
- Total Sessions
- Total Page Views
- Bounce Rate
- Session Duration
- Conversion Rate
- Traffic Source Performance
- Device Distribution
- Country-wise Traffic

### 4. SQL Analysis

Executed SQL queries to analyze:

- Total Users
- Average Bounce Rate
- Traffic Sources
- Device Performance
- Conversion Metrics

---

## Key Performance Indicators (KPIs)

- Total Users
- Total Sessions
- Total Page Views
- Bounce Rate
- Average Session Duration
- Conversion Rate
- Traffic Source Performance
- Device Distribution
- Country Distribution

---

## Business Insights

The analysis provides insights into:

- Top-performing traffic sources
- User engagement trends
- Device-wise website usage
- Geographic distribution of visitors
- Website conversion performance
- Opportunities to improve user experience

---

## Business Recommendations

Based on the analysis:

- Increase investment in high-performing traffic sources.
- Improve landing pages to reduce bounce rate.
- Optimize website performance for mobile users.
- Monitor key performance indicators regularly.
- Use dashboard reporting for business decision making.

---

## Future Enhancements

- Connect with Google Analytics API
- Build an interactive Tableau dashboard
- Develop a Power BI dashboard
- Automate data refresh using Python
- Apply predictive analytics using Machine Learning

---

## Author

**Kinjal Dalwadi**

Data Analytics | Python | SQL | Tableau | Agentic AI

Ahmedabad, Gujarat, India

LinkedIn: https://linkedin.com/in/your-linkedin-profile

GitHub: https://github.com/kinjudalwadi

---

## License

This project is licensed under the MIT License.
