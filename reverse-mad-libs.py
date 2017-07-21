
EASY = dict(
    text = """{0} is a widely used high-level programming language for
general-purpose programming, created by Guido van Rossum and first released
in 1991. An interpreted language, {0} has a design philosophy which emphasizes
{1} readability (notably using whitespace indentation to delimit code blocks
rather than curly brackets or keywords), and a syntax which allows programmers
to express concepts in fewer lines of code than might be used in {2} such as
C++ or Java. The language provides constructs intended to enable writing clear
programs on both a {3} and large scale.""",
    answers = ["Python", "code", "languages", "small"]
)

MEDIUM = dict(
    text = """Django's primary {0} is to ease the creation of complex,
database-driven websites. Django emphasizes reusability and "pluggability"
of components, rapid {1}, and the principle of don't repeat yourself. Python
is used throughout, even for settings files and data {2}. Django also provides
an optional administrative create, read, update and delete interface that
is generated {3} through introspection and configured via admin models.""",
    answers = ["goal", "development", "models", "dynamically"]
)

HARD = dict(
    text = """Flask is called a {0} framework because it does not require
particular tools or libraries. It has no database abstraction layer, form
validation, or any other components where pre-existing {1} libraries provide
common functions. However, Flask supports extensions that can add application
features as if they were implemented in Flask itself. Extensions exist for
object-relational {2}, form validation, upload handling, various open
authentication {3} and several common framework related tools. Extensions are
updated far more regularly than the core Flask program.""",
    answers = ["micro", "third-party", "mappers", "technologies"]
)

JEDI = dict(
    text = """{0} is the subfield of computer science that, according to Arthur
Samuel in 1959, gives "computers the ability to learn without being explicitly
programmed." Evolved from the study of pattern recognition and computational
learning theory in {1}, {0} explores the study and construction of algorithms
that can learn from and make predictions on data - such algorithms overcome
following strictly static program instructions by making data-driven {2} or
decisions, through building a model from sample inputs. {0} is employed in a
range of computing {3} where designing and programming explicit algorithms
with good performance is difficult or infeasible; example applications include
email {4}, detection of network intruders or malicious insiders working towards
a data {5}, optical character recognition (OCR), learning to rank, and computer
vision.""",
    answers = ["Machine learning", "artificial intelligence", "predictions",
        "tasks", "filtering", "breach"]
)

GAME = dict(
    easy = EASY,
    medium = MEDIUM,
    hard = HARD,
    jedi = JEDI
)
LEVELS = ['easy', 'medium', 'hard', 'jedi']

def correct_answer(game_level, blank_index):
    """Returns the correct answer for that game level for an specific blank space"""
    return game_level['answers'][blank_index]

def is_guess_correct(game_level, guess, blank_index):
    """Checks whether the guess is correct or not. Return True when it's correct,
    False otherwise"""
    return correct_answer(game_level, blank_index).lower() == guess

def build_missing_guesses(start, size):
    """Builds the list with the missing blanks to be used as replacement in
    the text and returns it"""
    return ["__{0}__".format(i) for i in range(start+1, size+1)]

def text_with_correct_guesses(game_level, correct_guesses, number_of_blanks):
    """Constructs the text to be printed for the user in each step of the game.
    When the user has correctly guesses some of the blanks, the answer will be
    displayed instead of the blank space"""
    missing_guesses = build_missing_guesses(len(correct_guesses), number_of_blanks)
    formatted_guesses = correct_guesses + missing_guesses

    return game_level['text'].format(*formatted_guesses)

def play(level):
    """Play the game for the selected level. Give unlimited tries for the user
    to guess until all blank spaces has been correctly guessed."""
    prompt_message = 'What should go in blank number {0}? '

    number_of_blanks = len(GAME[level]['answers'])
    correct_guesses = []

    i = 0
    while i < number_of_blanks:
        print
        print text_with_correct_guesses(GAME[level], correct_guesses, number_of_blanks)
        print
        guess = raw_input(prompt_message.format(i+1)).lower().strip()
        if is_guess_correct(GAME[level], guess, i):
            correct_guesses.append(correct_answer(GAME[level], i))
            i = i + 1
        else:
            print 'Wrong answer. Try again!'

    print text_with_correct_guesses(GAME[level], correct_guesses, number_of_blanks)
    print
    print 'Congratulations! You won the game.'


def select_level():
    """Prompts user to choose level between easy, medium, hard or jedi, and
    returns the chosen one. Repeats until the user selects a valid level"""
    prompt_message = 'Please select which level you want to play ({0}): '
    prompt_message = prompt_message.format(', '.join(LEVELS))
    while True:
        level = raw_input(prompt_message).lower().strip()
        if level in LEVELS:
            return level
        else:
            print '{0} is not a valid level'.format(level)

def main():
    """Start playing the reverse mad-libs game, asks the user
    for a level and start the game for that level"""
    level = select_level()
    play(level)

#Invoking the main program
main()
