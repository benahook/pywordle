import wordle_utils
import pandas as pd


class Word:

    def __init__(self, word):
        self.word = word
        self.letters = list()
        self.solved = False
        for letter in word:
            self.letters.append(Letter(letter, 'unknown'))

    def update(self):
        print('For each letter enter: [r/w/m] for right, wrong, or misplaced')
        retry = False
        correct_count = 0
        for letter in self.letters:

            choice = input(f'{letter.letter}:')

            if choice == 'r':
                letter.state = 'right'
                correct_count += 1

            elif choice == 'w':
                letter.state = 'wrong'

            elif choice == 'm':
                letter.state = 'misplaced'

            else:
                print(
                    'Invalid choice. The only options are [r/w/m] try again.')
                retry = True
                self.update()
                # break out if the user has retried the input.
                if retry:
                    break

        if correct_count == 5:
            print('SOLVED!')
            self.solved = True


class Letter:

    def __init__(self, letter, state):
        self.letter = letter
        self.state = state


def get_remaining_words(word_list, word=Word):

    for index, letter in enumerate(word.letters):

        if letter.state == 'right':
            word_list = wordle_utils.letter_at_pos(
                word_list, letter.letter, index)
        elif letter.state == 'wrong':
            word_list = wordle_utils.subwords_not_containing(
                word_list, [letter.letter])
        elif letter.state == 'misplaced':
            word_list = wordle_utils.subwords_containing(
                word_list, [letter.letter])
            word_list = wordle_utils.letter_not_at_pos(
                word_list, letter.letter, index)

    return(word_list)


def main():
    """
    main entry point to the progam

    Returns
    -------
    None.

    """
    print('Loading full wordlist(s)...')

    # read in our full list of english words
    with open('words_alpha.txt', 'r') as words_file:
        words = words_file.readlines()

    # keep only the five letter words
    five_letter_words = list()

    for word in words:
        if len(word.strip()) == 5:
            five_letter_words.append(word.strip().lower())

    # Load list of common words to show a relative frequency
    try:
        df = pd.read_excel('frequency_list.xlsx', sheet_name=2,
                           skiprows=1, index_col=1)
    except OSError:
        print('failed to find or load the the word frequency list.')
        print('setting the frequency list to an empty dataframe.')
        df = pd.DataFrame()

    df.drop_duplicates(inplace=False)

    # initialize the word list
    word_list = five_letter_words

    print('Done.')

    # you get 6 tries...
    for i in range(6):

        # ask the user for their initial guess
        guess_word = input(
            'Input your word (or type \"random\") then hit [ENTER]: ')

        guess_word = guess_word.strip()

        if guess_word.lower() == 'random':
            guess_word = wordle_utils.get_starting_word(word_list)

        guess_word = guess_word.lower()

        assert len(guess_word) == 5, 'Passed word must have 5 letters only.'

        if guess_word in five_letter_words:

            word = Word(guess_word)

            print(f'Check \"{word.word}\" on Wordle then:\n')

            word.update()

            if word.solved:
                print(f'{word.word} is the answer! Congrats!')
                with open('wordle_solutions.txt', 'a') as outfile:
                    outfile.write(word.word)
                break
            else:
                # find new words from process of elimination()
                word_list = get_remaining_words(word_list, word)
                
                if len(word_list) > 0:

                    print('\nLatest words to chose from:')
    
                    for index, word in enumerate(word_list):
                        try:
                            print(index, '. ', word, '\t',
                                  df.loc[word, 'FREQUENCY'].max())
                        except KeyError:
                            print(index, '. ', word)
                else:
                    print('Out of words to guess. Double check your inputs.')
                    break

        else:
            print(f'{guess_word} doesn\'t appear to be in the wordlist. exit.')
            break


if __name__ == '__main__':
    main()
