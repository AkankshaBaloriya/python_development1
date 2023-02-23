# dictionary comprehension  = create dictionaries using an expression 
                            #  can repalce for loops and certain lambda functions
                            
# dictionry = {key:expression for(key,value)in iterable}
# dictionry = {key:expression for(key,value)in iterable if conditional}
# dictionry = {key: (if/else) for (key,value)in iterable}
# ------------------------------------------------------------------------------
cities={"new york":32,"boston":54,"los anglos":87,"chicago":99}
cities_c={key: round((value-32)*(5/9)) for (key,value) in cities.items()}
print(cities_c)

# ---------------------------------------------------------------------------------
# another example
weather ={"new york":"snowing","boston":"sunny","los angeles":"sunny","chicago":"cloudy"}
sunny_weather={key :value for (key,value)in weather.items() if value =="sunny"}
print(sunny_weather)

# -----------------------------------------------------------------------------------------
cities={"new york":32,"boston":54,"los anglos":87,"chicago":99}
cities_c={key:("warm" if value >= 40 else "cold") for (key,value) in cities.items()}
print(cities_c)