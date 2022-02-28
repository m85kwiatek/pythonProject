

print('Hello World')

name = input('Podaj swoje imię: ')
wiek = int(input('Podaj ile masz lat: '))
print('Twoje imię to ' + name + ' i masz ' + str(wiek) + ' lat')
if wiek < 18:
    print('Jesteś nie letni')
else:
    print('Jesteś pełnoletni')
