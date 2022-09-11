import requests
import json
def request():
    a =  requests.get("http://saral.navgurukul.org/api/courses")
    print(a)
    with open("courses.json","w") as f:
        dict = json.loads(a.text)
        json.dump(dict,f,indent = 4)
    with open("courses.json","r") as f:
        data = json.load(f)
    id = []
    i=0
    while i<len(data['availableCourses']):
        print(i,data['availableCourses'][i]['name'],"  ",data['availableCourses'][i]['id']) 
        id.append(data["availableCourses"][i]['id'])
        i=i+1
    user = int(input("** Select the serial number: "))
    b = requests.get("http://saral.navgurukul.org/api/courses/"+str(id[user]+"/exercise"))
    a = b.json()
    j = 0
    l = 0
    slug = []
    while j<len(a["data"]):
        print(l,a['data'][j]["name"])
        slug.append(a['data'][j]["slug"])
        l=l+1
        j=j+1
    slugnumber = int(input("enter your slugnumber: "))
    sluglist = requests.get("http://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug? slug="+slug[slugnumber])
    c=sluglist.json()
    print("CONTENET",c["content"])
request()






   