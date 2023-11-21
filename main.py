#Below code can be used in any file
#Where Instance/Object will be created for Inshorts class
#And instance methods can be called to perform any specific task.

#

print('-'*30)
print("News Selection can be of All type or Category type")
print("Enter 1 for All type news")
print("Enter 2 for Category type news")

type = int(input("Please Enter the News type: "))
max_limit = int(input("Please enter the News Max limit : "))
print('-'*30)

if type == 1:
    obj1 = Inshorts("obj1_name")
    obj1.all_news(max_limit)

elif type == 2:
    obj2 = Inshorts("obj2_name")
    types = [
        'all',
        'national',
        'business',
        'sports',
        'world',
        'politics',
        'technology',
        'startup',
        'entertainment',
        'miscellaneous',
        'hatke',
        'science',
        'automobile'
    ]
    [print(i) for i in types]
    print('-'*30)
    category_type = input("Please enter the Category type of News from the above printed varities : ")
    obj2.category_news(category_type,max_limit)