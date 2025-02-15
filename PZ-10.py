'''
В30
Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,
Италия,США. РейнаТур – Англия,Япония,Канада,ЮАР. Радуга – США,Испания,Швеция,
Австралия.
Определить в каких турагенствах можно приобрести туры в Канаду, а в каких в США.
'''

tours = {
    "Вояж": {"Мексика", "Канада", "Израиль", "Италия", "США"},
    "РейнаТур": {"Англия", "Япония", "Канада", "ЮАР"},
    "Радуга": {"США", "Испания", "Швеция", "Австралия"}
}


def find_agencies(tours, country):
    agencies = []
    for agency, countries in tours.items():
        if country in countries:
            agencies.append(agency)
    return agencies


canada_agencies = find_agencies(tours, "Канада")
usa_agencies = find_agencies(tours, "США")


print("Туры в Канаду предлагают:", canada_agencies)
print("Туры в США предлагают:", usa_agencies)
