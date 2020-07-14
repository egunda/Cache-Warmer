import urllib.request
import urllib.error
import time
from multiprocessing import Pool

start = time.time()

file = open('s3.txt', 'r', encoding="ISO-8859-1")
# here s3.txt contains the URLs which are to be warmed
urls = file.readlines()

print(urls)


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


if __name__ == "__main__":
    p = Pool(processes=100)
    result = p.map(checkurl, urls)

print("done in : ", time.time()-start)
