import json
from PIL import Image
import datetime

class Article:
    '''
    Question 2a
        Properties:
            - headline
            - content
            - creator (author)
        Methods:
            - show (print contents)
            - save (save to text file)

    Question 2b
        Methods:
            - Load article from text file

    Question 2d
        Properties:
            - related_image
        Methods:
            - modify save to save info about related picture (if it exists)
            - modify load to load info about related picture (if it exists)
            - modify show to also show the related picture (if it exist)
    '''
    
    def __init__(self, headline, author, content, related_image=None):
        self.headline = headline
        self.content = content
        self.author = author
        self.related_image = related_image


    def show(self):
        #print out article information
        print '{0}\n{1}\n{2}'.format(self.headline,self.author,self.content)
        #show image if it exists
        if related_image : self.related_image.show()

    def save(self):
            # open a file to write to
           f = open(self.author+'_'+self.headline+'_'+datetime.now()+'.json', 'w')

           #format into json before writing to the file
           article = json.dumps({
                                    'Headline' : self.headline,
                                    'Authors' : self.author,
                                    'Content' : self.content,
                                    'Related_Image' : self.related_image
                                })
           

           f.write(article)
           f.close

    @classmethod
    def load(filename): 
        #open the file and load it in through json
        try : 
            f = open(filename)
            article = json.loads(f)
            f.close
        except IOError : 
            print "IOError"
            return

        #assign values
        return Article(
                        article['Headline'],
                        article['Authors'],
                        article['Content'],
                        article['Related_Image']
                        )

        f.close

class Picture:
    '''
    Question 2c
        Properties:
            - image_file (path to original image relative to this file)
            - creator (photographer)
         Methods
            - show (show image)
    '''
    
    def __init__(self, image_file, creator) :
        self.image_path = image_file
        self.creator = creator

    def show(self) :
        #open the image file from the path given
        try : image = Image.open(self.image_path)
        except IOError : 
            print "IOError"
            return

        image.show()
