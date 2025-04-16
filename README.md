This Python script scrapes job listings from VacancyMail Zimbabwe and saves the data into a CSV file.

🚀 Features
Scrapes job titles, companies, descriptions, and links.

Loops through multiple pages (default: 5 pages).

Outputs results in a clean CSV file.

Easily customizable.

📁 Project Structure
bash
Copy
Edit
📁 your-project/
├── vacancymail_scraper.py     # Main Python script
├── vacancymail_jobs.csv       # Output CSV file
└── README.md                  # This file
⚙️ Setup & Usage
1. Clone or Download
Clone this repo or just copy the Python script into your local folder.

2. Install Required Packages
bash
Copy
Edit
pip install requests beautifulsoup4
3. Run the Script
bash
Copy
Edit
python vacancymail_scraper.py
The script will scrape the first 5 pages of jobs and save the output to:

Copy
Edit
vacancymail_jobs.csv
📝 Output Format
The CSV file includes:


Title	Company	Description	Link	Location	Expiry	Job Type	Posted Time	Salary
Job title	Company name	Job details	Full URL to job page	blank	blank	blank	blank	TBA
Some fields like location, expiry, and posted time are not available in the current structure and will remain blank for now.

🔄 Customization
To scrape more pages, update this line:

python
Copy
Edit
all_jobs = scrape_all_jobs(pages=5)
To change the output filename:

python
Copy
Edit
save_jobs_to_csv(all_jobs, filename='my_jobs.csv')
🛠 Requirements
Python 3.x

Libraries:

requests

beautifulsoup4

Install them all using:

bash
Copy
Edit
pip install -r requirements.txt
(Optional: create requirements.txt with requests and beautifulsoup4 inside.)

👨‍💻 Author
Built by THABANI MANUHWA 💻
