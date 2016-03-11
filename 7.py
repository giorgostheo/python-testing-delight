import urllib2
import re
x = raw_input("enter latitude:")
y = raw_input("enter longitude:")
html = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&appid=b1b15e88fa797225412429c1c50c122a' .format (x,y)) .read()
#!!!!!!!!!
#ERROR STO AUTHENTICATION SHMAINEI OTI EXEI ALLAJEI J DIEYUYNSH API , GIA NA LEITOURGHSEI PREPEI NA ALLAJEI H DIEYUYNSH STHN KAINOYRGEIA KAI NA ISAX8OUN JANA OI METABLHTES {0} kai {1}
#!!!!!!!
z= 'rain' in html
#to z einai mia logikh metablhth pou bgazei true mono otan yparxei mesa sto arxeio h lejh rain
if (z == True):
    print "I'm singing in the rain!"
w = re.findall(r'temp":(\d+)', html)[0]
#me to [0] sto telos mporw kai pernw to apotelesma se string kai oxi se list
#to w[6] einai string opote prepei na to metatrepsw se int gia na leitourghsei h sugkrish ths if , gia auto xrhshmopoiw to int()
if (int(w) > 293 ):
    print "nice..."
elif ( int (w) < 278 ):
    print "brrrr"
