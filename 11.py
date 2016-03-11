import urllib2
import re
x = raw_input("enter the first account:")
y = raw_input("enter the second account:")
acc1 = urllib2.urlopen('https://twitter.com/{0}' .format (x) ).read()
acc2 = urllib2.urlopen('https://twitter.com/{0}' .format (y) ).read()


def getData(ac1,ac2):
    tw1 = re.findall(r'statuses_count&quot;:(\d+)', ac1)[0]
    f11 = re.findall(r'friends_count&quot;:(\d+)', ac1)[0]
    f21 = re.findall(r'followers_count&quot;:(\d+)', ac1)[0]
    li1 = re.findall(r'favourites_count&quot;:(\d+)', ac1)[0]

    tw2 = re.findall(r'statuses_count&quot;:(\d+)', ac2)[0]
    f12 = re.findall(r'friends_count&quot;:(\d+)', ac2)[0]
    f22 = re.findall(r'followers_count&quot;:(\d+)', ac2)[0]
    li2 = re.findall(r'favourites_count&quot;:(\d+)', ac2)[0]



    sc1=0
    sc2=0

    if (int(tw1) > int (tw2)):
        sc1=sc1+1

    if (int(f11) > int (f12)):
        sc1=sc1+1

    if (int(f21) > int(f22)):
        sc1=sc1+1

    if (int(li1) > int(li2)):
        sc1=sc1+1



    if (int(tw1) < int (tw2)):
            sc2=sc2+1

    if (int(f11) < int (f12)):
            sc2=sc2+1

    if (int(f21) < int(f22)):
            sc2=sc2+1

    if (int(li1) < int(li2)):
            sc2=sc2+1

    print ("{0}-{1} ".format (sc1,sc2))
    return 0

getData(acc1,acc2)
