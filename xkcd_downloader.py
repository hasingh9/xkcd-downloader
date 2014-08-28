import requests
import json
import sys
import os
import re


class Xkcd:
    """
    Create object of class 'Xkcd', call GetUrls specifying range and then call Download().
    """
    def __init__(self):
        self.urls=[]

    def GetUrls(self):
    	#Specify the range of comics to download
        self.urls=["http://xkcd.com/"+str(i)+"/info.0.json" for i in range(1100,1201)]

    def Download(self):
        for url in self.urls:
            target=requests.get(url)
            if target.status_code!=200:
                print("Cannot Retreive web page.\n")
                continue
            j=json.loads(target.text)
            title=j['title']
            title=title.replace(" ","")
            title=re.sub(r'[\W_]+','',title)              
            image=j['img']
            #add path to the imagename
            imagename=title+"."+image[len(image)-3:]
            #--check if file already exists
            if os.path.isfile(imagename):
                print("File "+imagename+" already exists.")
                continue
            #---
            r=requests.get(image)
            if r.status_code!=200:
                print("Cannot Retreive Image\n")
                continue
            with open(imagename,'wb') as f:
                print("Downloading image -- "+title)
                for chunk in r.iter_content(1024):
                    f.write(chunk)
            
        
### ---START HERE--- ###
if __name__=="__main__":
    obj=Xkcd()
    obj.GetUrls()
    obj.Download()
    print("Done")
