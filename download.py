import urllib

testfile = urllib.URLopener()
for i in range(1,352):
    loc = str(i)
    print(loc)
    testfile.retrieve("http://wsgw.mass.gov/data/gispub/shape/contours5k/hp" + loc +".zip", "contours/hp" + loc +".zip")