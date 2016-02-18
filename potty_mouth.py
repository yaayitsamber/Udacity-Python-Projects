#A small program to check for curse words in a text file. Uses urllib module to access
#wdyl, a google supported website. Also opens, and reads from a file. This was a project
#for Udacity's Programminf Foundations with Python course

import urllib

def read_text():
    quotes = open("/Users/Amber/Desktop/MovieQuotes.rtf")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print ("You potty mouth!")
    elif "false" in output:
        print ("Squeaky clean!")
    else:
        print ("Error reading document")
    
read_text()
