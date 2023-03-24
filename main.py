"""Gues the number game. You pick number from 0 to 1000 and I will guess it"""


def _get_answer() -> int:
    """
    Function get answer and validate the value.
    :return: one of the cases
    """
    good_answers = ["too small", "too big", "you win"]
    while True:
        answer_ = input("Enter your answer: ").lower()
        try:
            answer_ = int(answer_)
        except ValueError:
            for id_, values_ in enumerate(good_answers):
                if answer_ == values_:
                    return id_
            print("Incorrect answer!")
        else:
            if 0 < answer_ < 4:
                return answer_ - 1
            print("Incorrect answer!")


def main() -> None:
    """
    Explain rules and start guessing. Check case from answer funktion and keep guessing.
    :return: None
    """
    print("Think about integer number from 0 to 1000, and I will have guessed in maximum 10 tries")
    print("You can answer \n1 - too small \n2 - too big \n3 - you win\n\n")
    min_ = 0
    max_ = 1000
    guess_num = 500

    while True:

        print(f"Your number is: {guess_num}")
        case_ = _get_answer()

        if not case_:
            min_ = guess_num + 1
        elif case_ == 1:
            max_ = guess_num - 1
        else:
            print("Wygrałem!")
            return None
        if guess_num == (max_ - min_) // 2 + min_:
            print("\nDo not cheat! \nTry again.\n")
            print("Think about integer number from 0 to 1000.")
            print("I will have guessed in maximum 10 tries\n")
            print("You can answer \n1 - too small \n2 - too big \n3 - you win\n\n")

            min_ = 0
            max_ = 1000
        guess_num = (max_ - min_) // 2 + min_


main()
