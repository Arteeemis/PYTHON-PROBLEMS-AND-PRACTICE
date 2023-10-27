# используется для сортировки
from operator import itemgetter


class Library:
    def __init__(self, id, name, size, language_id):
        self.id = id
        self.name = name
        self.size = size  # in Mb
        self.language_id = language_id


class ProgrammingLanguage:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class LanguageLibrary:
    def __init__(self, language_id, library_id):
        self.language_id = language_id
        self.library_id = library_id



# Языки программирования
languages = [
    ProgrammingLanguage(1, "Python"),
    ProgrammingLanguage(2, "JavaScript"),
    ProgrammingLanguage(3, "Java")
]

# Библиотеки
libraries = [
    Library(1, "NumPy", 512, 1),
    Library(2, "Pandas", 1024, 1),
    Library(3, "React", 2048, 2),
    Library(4, "Node.js", 256, 2),
    Library(5, "Spring", 4096, 3),
    Library(6, "Angular.js", 128, 2)
]


language_library = [
    LanguageLibrary(1, 1),
    LanguageLibrary(1, 2),
    LanguageLibrary(2, 3),
    LanguageLibrary(2, 4),
    LanguageLibrary(3, 5),
    LanguageLibrary(2, 6)
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(library.name, library.size, language.name)
                   for language in languages
                   for library in libraries
                   if library.language_id == language.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(language.name, LangLibs.language_id, LangLibs.library_id)
                         for language in languages
                         for LangLibs in language_library
                         if language.id == LangLibs.language_id]

    many_to_many = [(library.name, library.size, lang_name)
                    for lang_name, lang_id, lib_id in many_to_many_temp
                    for library in libraries
                    if library.id == lib_id]

    print('\n')
    print('Задание А1\n')
    res_11 = []
    for i in range(len(one_to_many)):
        if one_to_many[i][0][0] == 'A':
            res_11.append((one_to_many[i][0], one_to_many[i][2]))
    for i in range(len(res_11)):
        print(*res_11[i])


    print('\nЗадание А2\n')
    res_12 = {}
    for i in range(len(one_to_many)):
        if one_to_many[i][2] not in res_12:
            res_12[one_to_many[i][2]] = one_to_many[i][1]
        elif one_to_many[i][1] < res_12[one_to_many[i][2]]:
            res_12[one_to_many[i][2]] = one_to_many[i][1]
    res_12 = sorted(res_12.items(), key=lambda x:x[1])
    for i in range(len(res_12)):
        print(*res_12[i])

    
    print('\nЗадание А3\n')
    res_13 = sorted(many_to_many, key=itemgetter(0))
    for i in range(len(res_13)):
        print(*res_13[i])
    print('\n')

if __name__ == "__main__":
    main()
