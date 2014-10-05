from question1 import *
import datetime

today = datetime.date(2014,10,04)

article1 = Article("Harvard student wins Nobel Prize",
					"Wow!!",
					"Brian Krentz",
					today)

picture1 = Picture("Harvard student wins Nobel Prize",
					"Wow!!",
					"Brian Krentz",
					today,
					'/path/to/picture/'
					)

article1.show()

if article1.matches_url(
	"http://thecrimson.com/Article/2014/10/04/Harvard student wins Nobel Prize/"
	) : print "matches_url works!"
else : print "matches_url is broken!"

print "http://thecrimson.com/{0}/{1}/{2}/{3}/{4}/".format(
                    article1.__class__.__name__, 
                    article1.pubdate.year, 
                    article1.pubdate.month, 
                    article1.pubdate.day,
                    article1.title
                    )

#picture1.show()
