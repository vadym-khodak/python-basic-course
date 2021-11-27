# dict

users_by_id = {1: {"name": "Bill"}, 2: {"name": "Rob"}}

new_users_by_id = {
    "70bc7af1-fc25-4393-b1de-b8aa264e76d1": {"name": "Bill"},
    "13d826b8-5752-4874-8edf-9a46831b2c35": {"name": "Rob"}
}
country_by_code = dict(us="The United States of America", uk="The United Kingdom")
new_country_by_code = dict([("us", "The United States of America"), ("uk", "The United Kingdom")])

print(country_by_code)
print(new_country_by_code)


if __name__ == "__main__":
    pass
