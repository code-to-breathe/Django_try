import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
#this is just configuring settings of project , needed before we can
#manipulate models

import django
django.setup()
## fake script
import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen=Faker()
topics=['search','social','marketplace','news','games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic for entry
        top=add_topic()
        #create the fake data for that entry
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fakename=fakegen.company()

        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fakename)[0]

        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
if __name__=='__main__':
    print("populating script")
    populate(20)
    print("populating complete!")
    print(but the harsh truth is you have to stay it straight without any prior consideration )
