import time
import os
import subprocess
import logging
from multiprocessing import Pool

# --- Configuration ---
INPUT_FILE = '/home/ec2-user/inputfile.txt'
LOG_FILE = 'url_process.log'

# Setup logging to create columnar output
# Formats: Timestamp | Level | Message (which we will format as columns)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

# Print Header for the log file to define columns
header = f"{'STATUS':<15} | {'URL'}"
logging.info("-" * 50)
logging.info(header)
logging.info("-" * 50)

def checkurl(url):
    url = url.strip()
    if not url:
        return
    
    try:
        # Using subprocess for better control than os.system
        # Redirecting output to devnull to keep the console clean
        result = subprocess.run(
            ['youtube-dl', '--all-formats', '-A', url],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            logging.info(f"{'SUCCESS':<15} | {url}")
        else:
            logging.error(f"{'FAILED':<15} | {url}")
            
    except Exception as e:
        logging.error(f"{'ERROR':<15} | {url} -> {str(e)}")

if __name__ == "__main__":
    start = time.time()

    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
    else:
        with open(INPUT_FILE, 'r', encoding="ISO-8859-1") as f:
            urls = f.readlines()

        # Defining connection pool (7 concurrent processes)
        with Pool(processes=7) as p:
            p.map(checkurl, urls)

        end_time = time.time() - start
        logging.info("-" * 50)
        logging.info(f"{'TOTAL TIME':<15} | {end_time:.2f} seconds")
