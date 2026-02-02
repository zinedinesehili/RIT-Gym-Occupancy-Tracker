import time, os, csv, requests, sqlite3
from datetime import datetime
from bs4 import BeautifulSoup

Columns = ['Timestamp', 'Date', 'Time', 'Occupancy' ]

def scrape():
    print("Scraping Data...")
    res = requests.get("https://recwell.rit.edu/facilityoccupancy")
    status_code = res.status_code
    if status_code == 200:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")  # full timestamp
        date = now.strftime("%Y-%m-%d")                # just date
        time_str = now.strftime("%H:%M:%S")            # just time

        soup = BeautifulSoup(res.content, 'html.parser') # parse html of page
        current_occupancy = int(soup.select('p > strong')[1].text.strip())

        file_exists = os.path.exists('occupancy.csv')
        
        with open ('occupancy.csv', 'a', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=Columns)
            if not file_exists: # write header just once
                dict_writer.writeheader()
            dict_writer.writerow({
                'Timestamp': timestamp,
                'Date': date,
                'Time': time_str,
                'Occupancy': current_occupancy
            })
        
    else:
        print("Scrape Failed")


def main():
    while True:
        scrape()
        time.sleep(1800)

if __name__ == "__main__":
    main()