import bpm_finder
import csv

headerList = ['Name','BPM','Type','Tempogram']
with open('data.csv', 'w' ,newline='') as data:
    data = csv.writer(data, delimiter=';', quotechar='|',
                           quoting=csv.QUOTE_MINIMAL)
    data.writerow([bpm_finder.name, str(bpm_finder.tempo),'',bpm_finder.tg_csv])
 #   song_data.writerow([str(bpm_finder.tempo), str(bpm_finder.tg_csv) ,str(bpm_finder.tgr)])

