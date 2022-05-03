#Importing Libraries
import urllib.request
import urllib.error
import time
from multiprocessing import Pool
import os
#Capturing start time
start = time.time()

# Open the file containing URLs in new lines
file = open('/home/ec2-user/inputfile.txt', 'r', encoding="ISO-8859-1")
# here s3.txt contains the URLs which are to be warmed
#Load URLs
urls = file.readlines()
#Printing URLs so that one can see the progress while it progresses.
print(urls)

# Logic to hit URL and for warming the cache
def checkurl(url):
    try:
        a = 'youtube-dl --all-formats -A {}'.format(url)
        os.system(a)
#        os.system('rm *m4a*')
#        os.system('rm *mp4*')
    except urllib.error.HTTPError as e:
        # Return 4xx or 5xx error
        print('HTTPError: {}'.format(e.code) + ', ' + url)
    except urllib.error.URLError as e:
        # If network layer error
        print('URLError: {}'.format(e.reason) + ', ' + url)
    else:
        # For 200 response
        print('Success with ' + ', ' + url)

# Main function
if __name__ == "__main__":
    #Defining connection pool
    p = Pool(processes=7)
    #The above line defines the number of consurrent threads you want to run
    result = p.map(checkurl, urls)
#Completion of program and printing time to execute this program
print("Time to execute this program : ", time.time()-start)
