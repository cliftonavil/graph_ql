import os
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'learn_graphql.settings')

import django
django.setup()

from movies.models import *
from faker import Faker

fakegen = Faker()


def populate(N=10):
    for entry in range(N):
        #new entry
        random_year = int(random.randint(2010, 2019))
        random_actor = random.sample(range(50), 4)
        print(type(random_actor))
        print(random_actor)
        user = Movie.objects.create(title=fakegen.text()[:12],year=random_year)
        actors_obj = Actor.objects.filter(id__in=random_actor)
        user.actors.set(actors_obj)
        user.save()
        print("Added :",user)

if __name__ == '__main__':
    print("POPULATE DATABASES")
    populate(10)
    print("COMPLETE")
