import the_cooler_json
with the_cooler_json.reddit('test.json') as efg:
    d = efg.decode()
    d.sowhatsit()
    d.nowamredty()
print(efg.result())