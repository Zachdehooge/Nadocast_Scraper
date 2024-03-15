# Nadocast Scraper

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![BeautifulSoup version](https://badge.fury.io/py/beautifulsoup4.svg)](https://badge.fury.io/py/beautifulsoup4)
![Python Version](https://img.shields.io/badge/python-3.12.1-yellow)
[![Python Snyk Check](https://github.com/Zachdehooge/Nadocast_Scraper/actions/workflows/snyk.yml/badge.svg)](https://github.com/Zachdehooge/Nadocast_Scraper/actions/workflows/snyk.yml)

# Installation

1. Download Github repo
2. Extract folder and open a new command prompt window in the extracted folder
3. Run `Install_Dependencies.bat`
4. Run `Nadocast.bat`

# Task Scheduler Automation (Optional)
There will be 3 different tasks that need to be created in Windows Task Scheduler to automate the fetch process

0Z Nadocast Fetch
1. Click `Action` and `Create Basic Task`
2. Enter name and description and click next
3. Click `Daily` option
4. Recur ever `1 day` and start at `12am` and click next
5. `Start a Program`
6. `Program/Script` // `Browse` // Enter location of the `Nadocast.bat` file
7. Finish

12Z Nadocast Fetch
1. Click `Action` and `Create Basic Task`
2. Enter name and description and click next
3. Click `Daily` option
4. Recur ever `1 day` and start at `4pm` and click next
5. `Start a Program`
6. `Program/Script` // `Browse` // Enter location of the `Nadocast.bat` file
7. Finish

18Z Nadocast Fetch
1. Click `Action` and `Create Basic Task`
2. Enter name and description and click next
3. Click `Daily` option
4. Recur ever `1 day` and start at `9:15pm` and click next
5. `Start a Program`
6. `Program/Script` // `Browse` // Enter location of the `Nadocast.bat` file
7. Finish
