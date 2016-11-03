from statistics import median
"""
Josue Ruiz Lab 6
Using dictionaries and sets
"""


def make_dict(list1, list2):
    new_dictionary = dict(zip(list1, list2))
    return new_dictionary


def sets(list1, list2):
    new_set = set(zip(list1, list2))
    return new_set


def frozen_sets(list1, list2):
    new_frozenset = frozenset(zip(list1, list2))
    return new_frozenset


def get_median(scores_dict):
    return median(scores_dict.values())


def get_score(name, scores_dict):
    if name in scores_dict.keys():
        return scores_dict.get(name)
    else:
        return -1


def main():
    # Information for the lab
    names = ['joe', 'tom', 'barb', 'sue', 'sally']
    scores = [10, 17, 20, 18, 15]
    age = [20, 17, 19, 18, 22]
    scores_dict = make_dict(names, scores)

    # Printing out Dictionary
    print("Initial Dictionary of Students with there scores:", scores_dict)
    # Printing a set list with students and their scores
    print("Set list:", sets(names, scores))
    # Printing a frozen set list with Students and their age
    print("Frozen set list:", frozen_sets(names, age))

    # Adding an entry with 'john' with the score of 19
    scores_dict['john'] = 19
    print("Adding 'john' with a score of 19", scores_dict)
    """
    When you enter the key for sue again it will simply update the original value
    in this case.
    """
    scores_dict['sue'] = 20
    print("Overwriting the value for 'sue' from 18 to 20 since the key ('sue') already exists", scores_dict)
    # Changing sally's score from 15 to 19
    scores_dict['sally'] = 19
    print("Changing score for 'sally' from 15 to 19")
    # Removing Student Tom
    scores_dict.pop('tom')
    print("Removing the student 'tom'", scores_dict)
    print("Remaining students sorted\n", sorted(scores_dict.items()))

    name = input("Get the score for a student\nEnter the student name: ")
    if name == -1:
       print(name, "is not listed in the student table")
    else:
        print("The score for", name, "is", scores_dict.get(name))


if __name__ == "__main__":
    main()
