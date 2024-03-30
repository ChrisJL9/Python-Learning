from bs4 import BeautifulSoup
import requests
#== To do list:==
#Add feature to pass website link as an argument to each method (Done)
#Determine if multiple methods will still be necessary for only text(With my current knowledge, yes.)
#Output data to file using a method that appends data to file and doesn't overwrite exsting data(In progress)
#Find a way to fix the spacing when the data is printed to a text file. It's troublesome because I find_all makes a list and-
    #-I can't make it ignore specific lines with no space because it's a list and not a string.
    #- Best bet is maybe trying to make it iterate through the list and see if I can make it ignore the empty ones.
#
#====================================================================================================================================

#=====================================================================================================================================================
def text_scrape_div(link):
    html_txt = requests.get(link).text
    soup = BeautifulSoup(html_txt, "html.parser")
    div_info = soup.find_all("div")

    
    for elements in div_info:
        #Extracts everything includin nested elements

        print(elements.text)


#=====================================================================================================================================================
def text_scrape_p(link):
    html_txt = requests.get(link).text
    soup = BeautifulSoup(html_txt, "html.parser")
    p_info = soup.find_all("p")
    with open (r"C:\Users\chris\Documents\VSCode\Write-to-File-CENTRO\Scrapeout.txt", "w+") as f:
        for paragraphs in p_info:
            #Extracts only plain text and excludes nested elements
            print(paragraphs.text)
            f.write(paragraphs.text)
#getting an encoding error for some of the stuff so might need to see about forcing utf-8 tp see of that works
#=====================================================================================================================================================
def text_scrape_ol(link):
    html_txt = requests.get(link).text
    soup = BeautifulSoup(html_txt, "html.parser")
    list_item = soup.find_all("ol")

    for elements in list_item:
        #Extracts only plain text and excludes nested elements
        print(elements.text)

    
    
    
#=====================================================================================================================================================
def text_scrape_full(link):
    html_txt = requests.get(link).text
    soup = BeautifulSoup(html_txt, "html.parser")
    
    for elements in soup:
        #Extracts everything includin nested elements

        print(elements.text)
#Extracts all the text in this specific page for this website. 
#=====================================================================================================================================================
 

        print(elements.text)
select = int(input("Type a number for the the class type to search:\
                      \n 1 for div(includes nested elements): \
                      \n 2 for <p>: \
                      \n 3 for ordered lists: "))


if (select == 1):
    text_scrape_div(input("\ninput website link: "))
    

elif (select == 2):
    text_scrape_p(input("\ninput website link: "))

elif (select == 3):
    text_scrape_ol(input("\ninput website link: "))

else:
    None

