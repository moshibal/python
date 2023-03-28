travel_log = [
    {
        "country": "France",
        "cities_visited": ["paris", "lille", "dijon"],
        "total_visits":12},
    {
        "country": "Germany",
        "cities_visited": ["berlin", "hamber", "stuttgart"],
        "total_visits":14}]


def add_new_country(country, number_of_visits, visitd_places):
    new_data = {
        "country": country, "cities_visited": visitd_places, "total_visits": number_of_visits
    }
    travel_log.append(new_data)


add_new_country("Russia", 2, ["moscow"])
print(travel_log)
