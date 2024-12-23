import the_cooler_json
with the_cooler_json.reddit('test.json') as efg:
    d = efg.decode()
    d.sowhatsit()
    d.nowamredty()
print(efg.result())



# class Amazing(metaclass=JS):
#     def __init__() -> None:
#         print("ok")
#     a = 2
#     def somemethod():
#         print(this.a)

# am = Amazing()
# am.somemethod()