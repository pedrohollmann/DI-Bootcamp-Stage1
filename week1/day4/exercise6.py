#Exercise 6: Magicians

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians(names):
    for magician in names:
        print(magician)


def make_great(names):
    for i in range(len(names)):
        names[i] = names[i] + " the Great"



make_great(magician_names)

show_magicians(magician_names)