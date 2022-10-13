
from ast import Dict
import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://knowthychoice.in/blog/')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
content = soup.find_all('h2')

#dictionary to store data
data={}

# function to create topics array and update topics in data
def updateData (s,d,i):
   r2 = requests.get(s)
   soup2 = BeautifulSoup(r2.content, 'html.parser')
   s2 = soup2.find('article')
   lines=s2.find_all('ul') 
   linesUl=lines[3]
   #array to store topics
   arr=[]
   for ln in linesUl:
          arr.append(ln.text)
  
   #updating dictionary
   d.update({content[i].text:arr})



#calling function for each heading
index=0
for item in content:
     if(content[index] and content[index].a):
           updateData(content[index].a.get('href'),data,index)

     index=index+1
    
      


#Printing data
print(data)