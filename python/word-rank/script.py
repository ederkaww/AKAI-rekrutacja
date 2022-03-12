from collections import Counter
import string
# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2


# Good luck! You can write all the code in this file.
choice = "test"


def find_most_common_words(sentences_list):
    for sentence in sentences_list:
        sentence_words = sentence.split()
        for sentence_word in sentence_words:
            sentence_word = sentence_word.translate(str.maketrans('','', string.punctuation))
            words_list.append(sentence_word.lower())

    for word in words_list:
        if word not in already_checked_words:
            occurrences = words_list.count(word)
            words_occurrences[word] = occurrences
            already_checked_words.append(word)

    k = Counter(words_occurrences)
    

    return k.most_common(3)


while choice.lower() != "q":
    words_list = []
    already_checked_words = []
    words_occurrences = {}  
    customer_sentences = []
    choice = input('\nChcesz sprawdzic jakie wyrazy wystepuja najczesciej w Twoich sentencjach? Wpisz "y".\nW celu przetestowania na gotowych sentencjach wpisz "test". Aby wyjsc nacisnij "Q": ')
    if choice.lower() == 'y':
        number = int(input('Ile sentecji chcesz podac? '))
        for i in range(number):
            sentence = input(f'{i+1}. sentencja: ')
            customer_sentences.append(sentence)
        common_words = find_most_common_words(customer_sentences)
    elif choice.lower() == 'test':
        common_words = find_most_common_words(sentences)
    elif choice.lower() == 'q':
        print('Do zobaczenia!')
    else:
        print('Wpisz "y" albo "test"')

    if choice.lower() == 'y' or choice.lower() == 'test':
        print('\n3 najczesciej wystepujace slowa:')
        for count, value in enumerate(common_words):
            print(f'{count+1}. "{value[0]}" : {value[1]}')
