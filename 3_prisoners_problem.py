import random

def three_prisoners(n=100000):
    a_survives = 0
    c_survives_given_b_revealed = 0

    for _ in range(n):
        # Randomly choose who will be freed
        prisoners = ['A', 'B', 'C']
        freed = random.choice(prisoners)

        # A asks the jailer to name one who will be executed (not A and not the freed one if it's B or C)
        possible_to_name = [p for p in prisoners if p != 'A' and p != freed]
        revealed_by_jailer = random.choice(possible_to_name)

        # If jailer reveals B, what is the chance C is the one to be freed?
        if revealed_by_jailer == 'B' and freed == 'C':
            c_survives_given_b_revealed += 1

        if freed == 'A':
            a_survives += 1

    print("Probability A is freed:", a_survives / n)
    print("Probability C is freed given B was revealed:", c_survives_given_b_revealed / n)

three_prisoners()
