movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
                ["Graham Chapman", ["Michael Palin", "John Cleese",
                        "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print(movies)

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    if isinstance(deeper_item, list):
                                                for deepest_item in deeper_item:
                                                    print(deepest_item)
                    else:
                        print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)