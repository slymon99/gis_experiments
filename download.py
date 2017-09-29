import urllib
import zipfile

def download():
    testfile = urllib.URLopener()
    for first in range(189, 547, 4):
        for last in range(862,942, 4):
            f = str(first)
            l = str(last)
            try:
                print("retrieving: d" + f + l)
                testfile.retrieve("http://wsgw.mass.gov/data/gispub/dtm/d" + f + l +".zip", "dtm/dl/d" + f+ l +".zip")
            except IOError:
                print("File d"+f + l +" does not exist on server.")

def extract():
    for first in range(181, 547, 4):
        for last in range(862,942, 4):
                f = str(first)
                l = str(last)
                try:
                    with zipfile.ZipFile("dtm/dl/d" + f + l + ".zip", "r") as z:
                        print("extracting: d" + f + l)
                        z.extractall("dtm")
                        z.close()
                except IOError:
                    print("File d" + f + l + " does not exist in folder dl.")
extract()