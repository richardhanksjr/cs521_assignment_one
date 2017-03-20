import sys
list_of_all_mad_libs = []

def main():
    while True:
        # Requirement 2: Promt user for a single number
        number = prompt_user_for_number()
        mad_lib = MadLib(number)
        print("Your mad lib is: ", mad_lib.__str__())
        # Requirement 6: Check that the resulting sentence is unique (has not been used before).
        unique_add_to_list = check_unique_value(mad_lib.__str__(), list_of_all_mad_libs)
        # 6a.  Check that the resulting sentence is unique (has not been used before).
        # 6b cont.  Either way, you have to print a message to the user indicating what happened
        if unique_add_to_list:
            list_of_all_mad_libs.append(mad_lib.__str__())
            print('This is a unique mad lib.  Adding it to the list of unique mad libs!')
        # 6b. If it is not unique, print a message letting the user know and do not save.
        else:
            print('This mad lib has already been used! Not adding it to the list of unique mad libs.')
        # Requirement 7: Print your current mad lib to the user
        # (list of all completed sentences so far, one sentence on its own line).
        print('Your current mad libs are: ', )
        print("\n".join(list_of_all_mad_libs))
        # Requirement 8: Ask user if he/she wants to keep playing
        continue_round = input("To get another mad lib press 'y' or 'n' to exit")
        # Requirement 8a: Validate user input
        validated_input = validate_input(continue_round)
        if validated_input:
            # 8b if 'y' go back to 2
            if continue_round == 'y':
                continue
            # 8c if 'n' exit
            elif continue_round == 'n':
                sys.exit(0)
        # Error handling if user didn't provide valid input
        print("Input not understood. Exiting...")
        sys.exit(1)


def validate_input(continue_round):
    # Requirement 8a continued
    if continue_round in ['y', 'Y', 'yes', 'Yes', 'n', 'N', 'No', 'no']:
        return True
    else:
        return False


def prompt_user_for_number():
    NUM_TIMES_TO_GET_INPUT = 4
    for num in range(NUM_TIMES_TO_GET_INPUT):
        number = input('Please input a single number: ')
        # Requirment 3: Validate the user input that number is positive and is an integer
        if number.isdigit() and int(number) > 0:
            return int(number)
    print('You failed to enter a positive integer.  Exiting program.')
    sys.exit(1)

def check_unique_value(mad_lib, mad_lib_list):
    #if any(mad_lib in s for s in  mad_lib_list):
    if mad_lib in mad_lib_list:
        return False
    else:
        return True

class MadLib():
    '''
    This is a class to be used in constructing mad lib objects.  The constructor takes a single argument (number),
    and uses that number to general object properties that map to the parts of speech and template needed to
    generate the phrases.  The __str__ method or the self.completed_phrase property can be used to represent
    the final string output.
    '''
    def __init__(self, number):
        # Word Lists to choose from
        # Requirement 1: Set up 4 lists: NOUNS, VERBS, ADJECTIVES, SENTENCE_TEMPLATES
        # Requirment 1e: Each list has different lengths
        # Requirement 1f:  All lists are less than 10 items long
        self.NOUNS = ['time', 'year', 'people', 'way', 'day', 'man', 'thing', 'woman']  # Length = 8
        self.VERBS = ['pay', 'put', 'read', 'run', 'say', 'see']  # Length = 6
        self.ADJECTIVES = ['other', 'new', 'good', 'high', 'old']  # Length = 5
        # Requrement 1g: Each sentence should be missing 1 type of each element
        self.SENTENCE_TEMPLATES = ['The {noun} {verb} through the {adjective} hole.', 'He {verb} a {adjective} {noun}',
                                   'Three {noun}s {verb} for the {adjective} job']  # Length = 3
        # Requirement 4: User input will be used to retreive from each of your lists
        self.number = number
        # 4b Get 1 noun from the noun list.
        self.noun = self.get_one_from_list(self.number, self.NOUNS)
        # 4d Get 1 adjective from the adjective list
        self.adjective = self.get_one_from_list(self.number, self.ADJECTIVES)
        #4c Get 1 verb from the verb list.
        self.verb = self.get_one_from_list(self.number, self.VERBS)
        # 4a Get 1 sentence template from the sentence list.
        self.template_phrase = self.get_one_from_list(self.number, self.SENTENCE_TEMPLATES)
        # 5 Insert the selected noun, verb and adjective into the selected sentence template.
        self.completed_phrase = self.template_phrase.format(noun=self.noun, verb=self.verb, adjective=self.adjective)

    def __str__(self):
        return self.completed_phrase

    def get_one_from_list(self, number, list):
        # Because the number may be longer than the list, use the mod to wrap the number around the end of the list.
        number = number % len(list)
        return list[number]


# Needed to call main, above
main()