# Web Extractiom and analysis using selenium


# Football Corners Data Scraper

## Overview
This Python script uses Selenium to scrape detailed football match information from the website [Adam Choi - Corners](https://www.adamchoi.co.uk/corners/detailed). The script extracts data for matches, including date, home team, away team, and score, for the specified country (Germany in this case).

## Requirements
- Python
- Selenium
- ChromeDriver
- pandas

Install the required packages using the following:
```bash
pip install -r requirements.txt
```

## Usage

1)Download the ChromeDriver executable and place it in the same directory as the script.

2)Run the script:
```bash
python script_name.py
```

3)The script will open a Chrome browser, navigate to the specified website, select matches for Germany, scrape the data, and save it to a CSV file (tutorial.csv).


## Configuration
1)You can modify the website variable in the script to point to a different URL if needed.
<br>

2)Adjust the sleep time (currently set to 5 seconds) based on the website's loading time and your network speed.


## Output
The scraped data will be saved to a CSV file named tutorial.csv in the same directory as the script.

## Dependencies
1)[Selenium](https://selenium.dev/)  
<br>
2)[pandas](https://pandas.pydata.org/)

