import csv
from faker import Factory
import random


n=Factory.create()
file=open("input_data.csv","a")
w=csv.writer(file)
w.writerow(('ID#','Name','College','Age'))
for i in range(1000*350*100):
  
    w.writerow((i+1,n.name(),random.choice(['ITU','Stanford','SJSU','SCU']),random.choice(range(18,35))))
file.close()

