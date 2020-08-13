#Importing Libraries
import urllib.request
import urllib.error
import time
from multiprocessing import Pool
#Capturing start time
start = time.time()

# Open the file containing URLs in new lines
file = open('s3.txt', 'r', encoding="ISO-8859-1")
# here s3.txt contains the URLs which are to be warmed
#Load URLs
urls = file.readlines()
#Printing URLs so that one can see the progress while it progresses.
print(urls)

# Logic to hit URL and for warmingthe cache
def checkurl(url):
    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        # ...
        print('HTTPError: {}'.format(e.code) + ', ' + url)
    except urllib.error.URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        # ...
        print('URLError: {}'.format(e.reason) + ', ' + url)
    else:
        # 200
        # ...
        print('good' + ', ' + url)

# Main function
if __name__ == "__main__":
    #Defining connection pool
    p = Pool(processes=100)
    #The above line defines the number of consurrent threads you want to run
    result = p.map(checkurl, urls)
#Completion of program and printing time to execute this program
print("done in : ", time.time()-start)
