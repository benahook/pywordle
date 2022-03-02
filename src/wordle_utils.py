import random


def subwords_containing(wordlist, letters=['e', 't', 'a', 's']):

    return_list = list()
    match_count = len(letters)
    count = 0
    for word in wordlist:
        for letter in letters:
            if letter in word:
                count += 1
            else:
                break

        if count == match_count:
            return_list.append(word.strip())
            count = 0
        else:
            count = 0

    return return_list


def letter_at_pos(wordlist, letter, pos):
    return_list = list()
    for word in wordlist:
        if word[pos] == letter:
            return_list.append(word)

    return return_list


def letter_not_at_pos(wordlist, letter, pos):
    return_list = list()
    for word in wordlist:
        if word[pos] == letter:
            pass
        else:
            return_list.append(word)

    return return_list


def subwords_not_containing(wordlist, letters=[]):
    match_count = len(letters)
    count = 0
    return_list = list()
    for word in wordlist:
        for letter in letters:
            if letter not in word:
                count += 1
            else:
                break

        if count == match_count:
            return_list.append(word.strip())
            count = 0
        else:
            count = 0

    return sorted(return_list)


def get_starting_word(five_letter_words):
    #good_starting_words = subwords_containing(
    #    five_letter_words, letters=['e', 't', 'i'])

    while True:
        starting_word = five_letter_words[random.randint(
            0, len(five_letter_words))-1]
        choice = input(
            f'Press [c] to continue with [{starting_word.upper()}] as your starting word, or enter to generate a new one: ').strip()
        if choice == 'c':
            return starting_word.strip()


def remove_words_with_letter_at_pos(word_list, letter, pos):
    # remove words with letters in the wrong positions
    words_to_exclude = letter_at_pos(word_list, letter, pos)

    for word in words_to_exclude:
        if word in word_list:
            word_list.remove(word)

    return word_list


def remove_duplicates_of(word_list, letter):
    return_list = list()
    for word in word_list:
        letter_count = 0
        for l in word:
            if l == letter:
                letter_count += 1
        if letter_count <= 1:
            # print(word)
            #p = input('pause')
            return_list.append(word)

    return return_list


def main():

    # read in our full list of english words
    with open('words_alpha.txt', 'r') as wf:
        words = wf.readlines()

    # keep only the five letter words
    five_letter_words = list()

    for word in words:
        if len(word.strip()) == 5:
            five_letter_words.append(word)

    print(len(five_letter_words))

    #starting_word = get_starting_word(five_letter_words)
    # print(starting_word)

    # keep words containing the specific letters
    word_list = subwords_containing(five_letter_words, letters=['u', 's', 'e'])

    # remove words containing the incorrect letters
    word_list = subwords_not_containing(word_list, ['m', 't', 'o'])

    word_list = remove_duplicates_of(word_list, 's')

    #word_list = letter_not_at_pos(word_list,'s',0)
    #word_list = letter_not_at_pos(word_list,'s',4)
    #word_list = letter_not_at_pos(word_list,'e',2)

    word_list = letter_at_pos(word_list, 'u', 2)
    word_list = letter_at_pos(word_list, 's', 3)
    word_list = letter_at_pos(word_list, 'e', 4)
    #word_list = letter_not_at_pos(word_list,'h',1)
    #word_list = letter_not_at_pos(word_list,'i',2)

    # for i in range(1,5):
    #    word_list = remove_words_with_letter_at_pos(word_list, 's', i)

    #total_word_list = list()

    #   word_list = letter_at_pos(word_list,'s',0)

    # there is only 1 S
    # word_list = remove_duplicates_of(word_list,'s')

    #total_word_list = sorted(word_list_1+word_list_4)

    # for word in a_words_to_remove:
    #    if word in total_word_list:
    #        i = total_word_list.index(word)
    #        total_word_list.pop(i)
    #print(f'I removed {total_word_list[i]}')

    #total_word_list = subwords_not_containing(total_word_list,'a')

    i = 0

    for index, word in enumerate(word_list):
        # if word.startswith('t') and word.endswith('se'):
        i += 1
        print(f'{i}.\t{word}')


if __name__ == '__main__':
    main()
