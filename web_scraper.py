import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = 'https://www.vacancymail.co.zw/jobs?page='

def scrape_jobs_from_page(page_number):
    url = f"{BASE_URL}{page_number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Updated selector to match current site layout
    job_listings = soup.select('div.job-listing-details')
    jobs = []

    for job in job_listings:
        # Extract job title
        title_tag = job.find('h3', class_='job-listing-title')
        title = title_tag.get_text(strip=True) if title_tag else ''

        # Extract company name
        company_tag = job.find('h4', class_='job-listing-company')
        company = company_tag.get_text(strip=True) if company_tag else ''

        # Extract job description
        description_tag = job.find('p', class_='job-listing-text')
        description = description_tag.get_text(strip=True) if description_tag else ''

        # Extract job link
        link_tag = job.find('a', href=True)
        link = "https://www.vacancymail.co.zw" + link_tag['href'] if link_tag else ''

        # Default values for location, expiry, job type, posted time, and salary
        location = ''  # No location found in this structure
        expiry = ''  # No expiry found in this structure
        job_type = ''  # No job type found in this structure
        posted_time = ''  # No posted time found in this structure
        salary = 'TBA'  # Default value if salary is not found

        jobs.append({
            'Title': title,
            'Company': company,
            'Description': description,
            'Link': link,
            'Location': location,
            'Expiry': expiry,
            'Job Type': job_type,
            'Posted Time': posted_time,
            'Salary': salary
        })

    return jobs

def scrape_all_jobs(pages=5):
    all_jobs = []
    for page in range(1, pages + 1):
        print(f"Scraping page {page}...")
        jobs = scrape_jobs_from_page(page)
        all_jobs.extend(jobs)
    return all_jobs

def save_jobs_to_csv(jobs, filename='vacancymail_jobs.csv'):
    if not jobs:
        print("No jobs to save.")
        return
    
    keys = jobs[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(jobs)

    print(f"Jobs saved to {filename}")

if __name__ == "__main__":
    all_jobs = scrape_all_jobs(pages=5)
    save_jobs_to_csv(all_jobs)


