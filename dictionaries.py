# dict = {"key":"value"}
# keys can be a string, an integer or a float
# values can be anything

a = {"name": "Symon", "age": 125, "my_temperature": 98.7, "list": [112, "Hello"], "my_internal_dic": {'first': 1},
     67: "sixty-seven", 3.14: "Pi", (1, 45): "Hello"}

# print(a)

my_info = {"name": "Ibrahim", "Age": 27, "temperature": 98.9, "email_for_me": "ibrahim@gmail.com"}
print(my_info)
print(my_info.values())
# print(my_info.pop("name"))  # removes the key from the dictionary
print(my_info.get("Age"))
print(my_info.update({'address': "2910 Brando Dr"}))
print(my_info.keys())
