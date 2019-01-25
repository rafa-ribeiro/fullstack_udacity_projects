import inheritance


billy_cyrus = inheritance.Parent("Cyrus", "blue")
billy_cyrus.show_info()


miley_cyrus = inheritance.Child("Cyrus", "blue", 10)
# print(miley_cyrus.last_name)
# print(miley_cyrus.number_of_toys)

miley_cyrus.show_info()