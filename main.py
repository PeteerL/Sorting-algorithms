import Manage

Manage = Manage.Manage()

print("Number size must be more than 5000 to notice the difference among the algorithms! \n"
      "Output is measured in seconds")
while True:
    Manage.FillRandom(int(input("Numbers size: ")))
    Time = Manage.Sort()
    for Type, TypeValue in Time.items():
        print("--------------------\n"
              "-", Type, "-\n"
              "--------------------")
        for Sort, SortValue in TypeValue.items():
            print(Sort, " : ", SortValue)