from bs4 import BeautifulSoup
import requests
import openpyxl
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Webscraping Multiple Pages"
sheet.append(["name","degree","duration","intakes"])   #excel headers
website ="https://www.westminster.ac.uk/course-search?f%5B0%5D=mode_of_study%3A56&course=&page="
for page_number in range(0,29):
    request = requests.get(website+str(page_number)+"/")
    soup = BeautifulSoup(request.text, 'html.parser')
    details = soup.find_all('div', class_="details-pane")
    for program in details:
        name = program.find('span', class_='details-pane__results-title').get_text(strip=True)
        degree = program.find('span', class_="details-pane__results-type").get_text(strip=True)
        duration = program.find('div', class_="details-pane__result-set duration").get_text(strip=True)
        intakes = program.find('div', class_='details-pane__result').get_text(strip=True)
        # get_text(strip=True) prints everything in the same line for easy reading that is it prettifies
        print(name, degree, duration, intakes)
        sheet.append([name, degree, duration, intakes])

excel.save("Webscraping Courses - Multiple Pages.xlsx")

