from bs4 import BeautifulSoup
import requests
import os

#== To do list:==
#Add feature to pass website link as an argument to each method (DONE)
#Determine if multiple methods will still be necessary for only text(With my current knowledge, yes.)
#Output data to file using a method that appends data to file and doesn't overwrite exsting data (DONE)
#Find a way to fix the spacing when the data is printed to a text file. It's troublesome because I find_all makes a list and-
    #-I can't make it ignore specific lines with no space because it's a list and not a string.
    #- Best bet is maybe trying to make it iterate through the list and see if I can make it ignore the empty ones. (DONE? Did what I can for now)

# == Next steps == 
#See if you can get images off of the site
#Consult with Rahman or Kathya on what exactly they want besides text. 
#See if you can add GUI prompts for running the program
#scraping links specifically maybe? 

#=====================================================================================================================================================

#=====================================================================================================================================================
#== For div class == 
def text_scrape_div(link):
    html_txt = requests.get(link).text
    soup = BeautifulSoup(html_txt, "html.parser")
    div_info = soup.find_all("div")
    file_path = r"C:\Users\chris\Documents\VSCode\Write-to-File-CENTRO\Scrapeout.txt"
    
    # Check if the file exists, create it if it doesn't
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding='utf-8'):
            pass  # Create an empty file
    
    # Open the file in append mode
    with open(file_path, "a+", encoding='utf-8') as f:
        for elements in div_info:
            # Extracts everything including nested elements
            elements_text = elements.text.strip()  # Remove leading and trailing whitespaces
            if elements_text:  # Check if element text is not empty
                print(elements_text)
                f.write(elements_text)
#=====================================================================================================================================================
# == For Paragraphs <p> == 
def text_scrape_p(link):
    html_txt = requests.get(link).text
    soup = BeautifulSoup(html_txt, "html.parser")
    p_info = soup.find_all("p")
    file_path = r"C:\Users\chris\Documents\VSCode\Write-to-File-CENTRO\Scrapeout.txt"
    
    # Check if the file exists, create it if it doesn't
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding='utf-8'):
            pass  # Create an empty file
    
    # Open the file in append mode
    with open(file_path, "a+", encoding='utf-8') as f:
        for paragraph in p_info:
            # Extracts only plain text and excludes nested elements
            paragraph_text = paragraph.text.lstrip()  # Remove leading and trailing whitespaces
            if paragraph_text:  # Check if paragraph text is not empty
                print(paragraph_text)
                f.write(paragraph_text)
#getting an encoding error for some of the stuff so might need to see about forcing utf-8 tp see of that works
#=====================================================================================================================================================
#==For Lists == 
def text_scrape_li(link):
    html_txt = requests.get(link).text
    soup = BeautifulSoup(html_txt, "html.parser")
    list_item = soup.find_all("li")
    file_path = r"C:\Users\chris\Documents\VSCode\Write-to-File-CENTRO\Scrapeout.txt"
    
    # Check if the file exists, create it if it doesn't
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding='utf-8'):
            pass  # Create an empty file
    
    # Open the file in append mode
    with open(file_path, "a+", encoding='utf-8') as f:
        for elements in list_item:
            # Extracts only plain text and excludes nested elements
            elements_text = elements.text.strip()  # Remove leading and trailing whitespaces
            if elements_text:  # Check if element text is not empty
                print(elements_text)
                f.write(elements_text)
    
#=====================================================================================================================================================
# == Grabs entire HTML of that page ==
def text_scrape_full(link):
    html_txt = requests.get(link).text
    soup = BeautifulSoup(html_txt, "html.parser")
    file_path = r"C:\Users\chris\Documents\VSCode\Write-to-File-CENTRO\Scrapeout.txt"
    
    # Check if the file exists, create it if it doesn't
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding='utf-8'):
            pass  # Create an empty file
    
    # Open the file in append mode
    with open(file_path, "a+", encoding='utf-8') as f:
        for elements in soup:
            # Extracts everything including nested elements
            elements_text = elements.text.strip()  # Remove leading and trailing whitespaces
            if elements_text:  # Check if element text is not empty
                print(elements_text)
                f.write(elements_text)
#Extracts all the text in this specific page for this website. 
#=====================================================================================================================================================
#==  MAIN ==                                    
# >Prompts user for which function they want to run.
select = int(input("Type a number for the the class type to search:\
                      \n 1 for div(includes nested elements): \
                      \n 2 for <p>: \
                      \n 3 for lists (ordered & unordered): \
                      \n 4 for everything on the webpage: "))


if (select == 1):
    try:
        text_scrape_div(input("\nInput website link: ")) #Multiple different webpages so there's multiple options depending on needs.
    except:
        print("An error occured.")
    
elif (select == 2):
    try:
        text_scrape_p(input("\nInput website link: "))
    except:
        print("An error occured.")

elif (select == 3):
    try:
        text_scrape_li(input("\nInput website link: "))
    except:
        print("An error occured.")

elif (select == 4):
    try:
        text_scrape_full(input("\nInput website link: "))
    except:
        print("An error occured.")

else:
    print("None of the options were selected.")

