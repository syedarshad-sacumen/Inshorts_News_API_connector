# main module code can be used in any file for the clients,
# via this module customer get the refrence to create an Instance/Object for Inshorts class,
# And instance methods can be called to perform specific task related to Inshorts API.

# imported classes
from inshorts import Inshorts

print("News Selection can be of All type or Category type")
print("Enter 1 for All type news")
print("Enter 2 for Category type news")

try:
    type = int(input("Please Enter the News type: "))
    max_limit = int(input("Please enter the News Max limit : "))
    print("-" * 30)
except Exception:
    print("Invalid input, Please enter Numerical Characters")

if type == 1:
    obj1 = Inshorts()
    obj1.all_news(max_limit)

elif type == 2:
    obj2 = Inshorts()
    types = [
        "all",
        "national",
        "business",
        "sports",
        "world",
        "politics",
        "technology",
        "startup",
        "entertainment",
        "miscellaneous",
        "hatke",
        "science",
        "automobile",
    ]
    try:
        [print(i) for i in types]
        print("-" * 30)
        category_type = input(
            "Please enter the Category type of News from the above printed varities : "
        )
        obj2.category_news(category_type, max_limit)
    except Exception:
        print(
            "Invalid input, Expected input format is Alphabetical characters as displayed above."
        )
