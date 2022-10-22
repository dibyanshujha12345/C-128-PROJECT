from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import csv

empty_list=[]

url='https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page=requests.get(url)
soup=bs(page.text,'html.parser')
star_table=soup.find_all('table')
table_rows=star_table[7].find_all('tr')

	for tr in table_rows:
	    td = tr.find_all('td')
	    row = [i.text.rstrip() for i in td]
	    temp_list.append(row)


	Star_names = []
	Distance =[]
	Mass = []
	Radius =[]
	

    
	for i in range(1,len(temp_list)):
	    Star_names.append(temp_list[i][0])
	    Distance.append(temp_list[i][5])
	    Mass.append(temp_list[i][7])
	    Radius.append(temp_list[i][8])
        
	   
	df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius')
	print(df2)
	
	df2.to_csv('dwarf_stars.csv')       