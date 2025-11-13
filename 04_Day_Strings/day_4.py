## Exercises

## Concat basics
# thirty = "Thirty "
# days = "Days "
# of = "Of "
# python = "Python."

# sentence = thirty + days + of + python

# print(sentence)

# coding = "Coding "
# For = "For "
# All = "All."

# sentence = coding + For + All
# print(sentence)

## String Methods

company = "Coding For All"
# print(company)
# print(len(company))
# print(str.upper(company))
# print(str.lower(company))

# print(str.capitalize(company))
# print(str.title(company))
# lower = str.lower(company)
# print(str.swapcase(lower))

# print(company[0:6])

# print(company.index('Coding'))
# print(company.startswith('Coding'))
# print(company.find('Coding'))
# print(company.rindex('Coding'))

print(company.replace('Coding', 'Python'))

python = "Python For Everyone"
python_replace = python.replace('Everyone', 'All')
print(python)
print(python_replace)

list_words = company.split(' ')
print(list_words)

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies_split = companies.split(', ')
print(companies_split)

print(company[0])
print(company[-1])
print(company[10])


acronym_list = python.split(' ')
print(acronym_list)
acronym = ''
for i in acronym_list:
    acronym += i[0]

print(acronym)

acronym_list = company.split(' ')
print(acronym_list)
acronym = ''
for i in acronym_list:
    acronym += i[0]

print(acronym)
