#!/usr/bin/env python3
import random
from collections import Counter
from pprint import pprint

ALPHABET = {l: None for l in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"}

def can_spell_word(word, rings):
    """
    Check if a word can be spelled using the current set of rings.
    Warning: this uses a greedy algorithm which means that often it won't
    find a way to spell a word even though it exists.
    For this problem it just increases the optimization time.

    Args:
        word (str): The word to check.
        rings (list[set]): A list of sets, where each set represents the letters on a ring.

    Returns:
        bool: True if the word can be spelled, False otherwise.
    """
    # Create a list of flags to track used rings
    used_rings = [False] * len(rings)
    
    for letter in word:
        # Try to find a ring that contains the letter and is not used yet
        for i, ring in enumerate(rings):
            if letter in ring and not used_rings[i]:
                used_rings[i] = True  # Mark the ring as used
                break
        else:
            # If no ring can provide the letter, the word cannot be spelled
            return False
    
    # All letters were successfully matched
    return True

def add_to_size(s, size):
    assert size - len(s) > 0
    absent = set(ALPHABET.keys()) - s
    to_add = random.sample(sorted(absent), size - len(s))
    s.update(to_add)
    return s

def new_ring(base_letters, size):
    return add_to_size(set(base_letters), size)

N_RINGS = 10
# number of positions on every ring
N_LETTERS = 26
# number of most frequent letters to use on every ting
N_MOST_COMMON = 16

if __name__ == "__main__":
    random.seed(41)
    with open("5000lemma.num.unicode") as f:
        words = [l.split()[2] for l in f if len(l.split()[2]) <= N_RINGS]
        long_words = [l.split()[2] for l in f if len(l.split()[2]) > N_RINGS]
    print("{} words longer than {} letters".format(len(long_words), N_RINGS))


    c = Counter((len(w) for w in words))
    print("Word lenghts:")
    pprint(c.most_common())

    letter_counter = Counter()
    for w in words:
        letter_counter.update(w)


    base_letters = [l for l, _ in letter_counter.most_common(N_MOST_COMMON)]
    print("Most common letters:", "".join(base_letters))

    # initial set of letters
    rings = [new_ring(base_letters, N_LETTERS) for _ in range(N_RINGS)]

    for ring in rings:
        assert len(ring) == N_LETTERS

    non_trivial_words = sorted(w for w in words if len(set(w) - set(base_letters)) > 0)
    print(len(non_trivial_words))

    last_can_not_spell = len(non_trivial_words)

    print("starting optimization")
    old_rings = [r.copy() for r in rings]
    for i in range(1000):
        can_not_spell = 0
        for w in non_trivial_words:
            if not can_spell_word(w, rings):
                can_not_spell += 1
        if can_not_spell == 0:
            print(f"solution found (i={i})")
            break
        elif can_not_spell < last_can_not_spell:
            old_rings = rings.copy()
            last_can_not_spell = can_not_spell
            print(f"score ({i:>5}): {can_not_spell}")
        else:
            rings = old_rings.copy()
        j = random.randint(0, 9)
        rings[j] = new_ring(base_letters, N_LETTERS)
        rings[(j + 1) % N_RINGS] = new_ring(base_letters, N_LETTERS)
    else:
        print("no exact solution found")

    for ring in rings:
        s = "".join([l for l in ALPHABET.keys() if l in ring]).upper()
        s_no_jo = [l for l in s if l != "Ё"]
        # confirm that letter order is correct, note: Ё should be after Е
        # in the alphabet but in unicode it's not
        assert "".join(s_no_jo) == "".join(sorted(s_no_jo))

