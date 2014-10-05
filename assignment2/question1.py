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

    def matches_url (self):
        ...



class Article(Content):
    '''
    Required properties:
        - All properties of Content
        - related_image
    Required methods:
        - All methods of Content
    '''
    
    def __init__(self, title, subtitle, creator, pubdate):
        super(Content, self).__init__(title,subtitle, creator, pubdate)



class Picture(Content):
    '''
    Required properties:
        - All properties of Content
        - image_file
    Required methods:
        - All methods of Content
    '''
    
    def __init__(self, title, subtitle, creator, pubdate, related_image=None):
        super(Content, self).__init__(title, subtitle, creator, pubdate)
        self.related_image = related_image

    def show(self):
        print '{0}\n{1}\n{2}\n{3}'.format(
                self.title, self.subtitle, self.creator, self.pubdate
                )
        #open the image file from the path given
        try : image = Image.open(self.image_path)
        except IOError : 
            print "IOError"

        image.show()
        

    def matches_url(self):


'''
Question 1e
'''
def from_url(c_lst, url):
    pass

'''
Question 1e
'''
def posted_after(c_lst, dt):
    pass