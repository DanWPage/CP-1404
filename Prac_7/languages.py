from Prac_7.programminglanguage import ProgrammingLanguage

RUBY = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
PYTHON = ProgrammingLanguage("Python", "Dynamic", True, 1991)
VB = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
JAVA = ProgrammingLanguage('Java', 'Static', True, 1995)
CPLUSPLUS = ProgrammingLanguage('C++', 'Static', False, 1983)

languages = [RUBY, PYTHON, VB, JAVA, CPLUSPLUS]
print("The Dynamically typed languages are;")
for language in languages:
    if language.is_dynamic():
        print(language.name)