import the_cooler_json
with the_cooler_json.bil('{"abc": 12}') as efg:
    d = efg.decode()
    d.sowhatsit()
    d.nowamredty()
print(efg.result())