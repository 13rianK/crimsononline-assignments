#import modules for urllib and json use
import urllib
import json

# function to find next 3 shuttle times from Quad to Mass Ave/Garden St
def shuttle_times () : 

	file_data = urllib.open( http://shuttleboy.cs50.net/api/1.2/trips?a=Quad&b=Mass Ave Garden St&sdt=2009-12-02&output=json)

	shuttle_data = json.load(file_data)

	print shuttle_data

shuttle_times()

