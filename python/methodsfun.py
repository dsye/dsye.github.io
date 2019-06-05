# def intro(name):
#     print(name + " is Master of the Universe!")
#
# def not_d(name):
#     intro(name)
#     print("According to the New York Times this is factually incorrect.")
#
# people = ["David", "Leeah", "Ethan"]
# for name in people:
#     if name == "David":
#         intro(name)
#         print("Long may he reign!")
#     else:
#         not_d(name)

# def method_one():
#     print("look I'm a method")
#
# def method_two(name):
#     print("about to call our first method " + name)
#     method_one()
#
# method_two("Brandon")

def workpub(works):
    for title, date in works.items():
        print(title + " was published in " + date + ".")

works = {"Jane Eyre": "1847", "Cane": "1923", "Wide Sargasso Sea":"1966", "Citizen: An American Lyric":"2014"}
workpub(works)
