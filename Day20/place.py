import googlemaps

gm = googlemaps.Client(key="AIzaSyA8VRK8GqobS2yWJHn4Aj7-VDnqei_H82g")

result = gm.places_nearby(
    location={'lat': 37.55515, 'lng':126.93691},
    keyword='스시',
    radius=25000,
    type='restaurant'
)

for i in result.get('results',[]):

    if float(i.get('rating')) > 4.4:
        print(i.get('name'))
        print(i.get('rating'))

