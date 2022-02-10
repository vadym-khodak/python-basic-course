# dict - словник, ключ - значення
# Ініціалізація dict

users_by_id = {1: {"name": "Bill"}, 2: {"name": "Rob"}}

new_users_by_id = {
    "70bc7af1-fc25-4393-b1de-b8aa264e76d1": {"name": "Bill"},
    "13d826b8-5752-4874-8edf-9a46831b2c35": {"name": "Rob"},
}
country_by_code = dict(us="The United States of America", uk="The United Kingdom")
new_country_by_code = dict([("us", "USA"), ("au", "Australia")])

codes = ["us", "uk"]
dict_from_keys = dict.fromkeys(codes, "null")

# Ініціалізація пустого dict
events_by_date = {}
results = dict()

print(country_by_code)
print(new_country_by_code)
print(dict_from_keys)
print(events_by_date)
print(results)

# Переглянути усі атрибути типу dict
print(dir(dict))
print(dir({}))
print(dir(country_by_code))

# Переглянути довідку по типу dict
print(help(dict))
print(help({}))
print(help(country_by_code))

# Отримання значення за ключем
us = country_by_code["us"]
us_new = country_by_code.get("us")
au = country_by_code.get("au")
au_new = country_by_code.get("au", "Australia")
print(us)
print(us_new)
print(au)
print(au_new)

# Отримання всіх ключів dict
keys = country_by_code.keys()
print(keys)
print(type(keys))
print(list(keys))
print(type(list(keys)))

# Отримання всіх значень dict
values = country_by_code.values()
print(values)
print(type(values))

# Отримання всіх пар (ключ, значення) dict
items = country_by_code.items()
print(items)
print(type(items))

# # Видалення елементу та повернення значення за ключем
us = country_by_code.pop("us")
print(us)
print(country_by_code)
au = country_by_code.pop("au", None)
print(au)
print(country_by_code)


# Видалення елементу та повернення пари (ключ, значення) за ключем
item = country_by_code.popitem()
print(item)
print(country_by_code)

# Оновлення dict
country_by_code.update({"uk": "The United Kingdom", "us": us})
print(country_by_code)
country_by_code.update(new_country_by_code)
print(country_by_code)

# Встановлення значення за замовчуванням
us = country_by_code.setdefault("us", "The USA")
print(us)
print(country_by_code)
ua = country_by_code.setdefault("ua", "Ukraine")
print(ua)
print(country_by_code)

# Створення неглибокої копії dict
copy_users_by_id = new_users_by_id.copy()
print(copy_users_by_id)
print(id(new_users_by_id))
print(id(copy_users_by_id))
new_users_by_id["70bc7af1-fc25-4393-b1de-b8aa264e76d1"].update({"last_name": "doe"})

print(copy_users_by_id)
print(new_users_by_id)

# Очищення dict
new_users_by_id.clear()
print(new_users_by_id)


if __name__ == "__main__":
    pass
