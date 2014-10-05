from datetime import *
from PIL import Image

class Content(object):
    '''
    Required properties:
        - title
        - subtitle
        - creator
        - publication date
    Required methods:
        - show
        - matches_url (question 1d)
    '''
    def __init__(self, title, subtitle, creator, pubdate):
        self.title = title
        self.subtitle = subtitle
        self.creator = creator
        self.pubdate = pubdate

    def show(self):
        print '{0}\n{1}\n{2}\n{3}'.format(
                self.title, self.subtitle, self.creator, self.pubdate
                )

    def matches_url (self, url):
        # I took slug to mean title
        if "http://thecrimson.com/{0}/{1}/{2}/{3}/{4}/".format(
                    self.__class__.__name__, 
                    self.pubdate.year, 
                    self.pubdate.month, 
                    self.pubdate.day,
                    self.title
                    ) == url : True
        else : False



class Article(Content):
    '''
    Required properties:
        - All properties of Content
        - related_image
    Required methods:
        - All methods of Content
    '''
    
    def __init__(self, title, subtitle, creator, pubdate):
        Content.__init__(self,title,subtitle,creator,pubdate)



class Picture(Content):
    '''
    Required properties:
        - All properties of Content
        - image_file
    Required methods:
        - All methods of Content
    '''
    
    #initializer for Picture class
    def __init__(self, title, subtitle, creator, pubdate, image_path):
        Content.__init__(self,title, subtitle, creator, pubdate)
        self.path = image_path

    def show(self):
        #print article content
        print '{0}\n{1}\n{2}\n{3}'.format(
                self.title, self.subtitle, self.creator, self.pubdate
                )
        #open the image file from the path given and display
        Image.open(self.path).show()


'''
Question 1e
'''

#finds content from a given URL
def from_url(c_lst, url):
    count = 0
    place = 0

    for i in range(c_lst.len()) :
        if c_lst[i].matches_url(url) : 
            count += 1
            place = i

    if count == 1 : return c_lst[place]
    else: print "Multiple Content matches"


'''
Question 1e
'''
def posted_after(c_lst, dt):
    return [i for i in range(c_lst.len()) if c_lst[i].pubdate > dt]



