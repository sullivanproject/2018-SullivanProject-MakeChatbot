from schapi import SchoolAPI, Region

api = SchoolAPI(Region.DAEJEON, 'G10000170')

meals = api.get_monthly_menus(2018, 5)
for i in range(len(meals)):
    print(meals[i].breakfast)

# TODO: fix schapi to print successly