#!usr/bin/python3
# -*- coding: utf-8 -*-

import enchant
import re
from nltk.corpus import wordnet
import random
import nltk as nltk




"""

    Manual setup:
    install - nltk
    install - python3
    install - PyEnchant
    In your python3 shell type these to download needed data sets:
    >>>import nltk
    >>>nltk.download('wordnet')
    >>>nltk.download('punkt')
    >>>nltk.download('averaged_perceptron_tagger')
    noun responses -- nouns.txt
    verb responses -- verbs.txt
    yes responses -- yes_no.txt
    questionable -- queries.txt
    adjectives -- adjectives.txt
    Interject -- interjections.txt
"""


class Wiwa(object):
    def __init__(self):
        self.nounscript = "/home/NelliesNoodles/nelliesnoodles_mysite/nouns.txt"
        self.noun_script_order = create_script_line_order(self.nounscript)
        self.verbscript = "/home/NelliesNoodles/nelliesnoodles_mysite/verbs.txt"
        self.verb_script_order = create_script_line_order(self.verbscript)
        self.simplescript = "/home/NelliesNoodles/nelliesnoodles_mysite/yes_no.txt"
        self.simple_script_order = create_script_line_order(self.simplescript)
        self.questionable = "/home/NelliesNoodles/nelliesnoodles_mysite/queries.txt"
        self.question_script_order = create_script_line_order(self.questionable)
        self.adjectives = "/home/NelliesNoodles/nelliesnoodles_mysite/adjectives.txt"
        self.adj_script_order = create_script_line_order(self.adjectives)
        self.error_script = "/home/NelliesNoodles/nelliesnoodles_mysite/to_err.txt"
        self.err_script_order = create_script_line_order(self.error_script)
        self.dictionary = enchant.Dict("en_US")
        self.line_get = 0

    def run_wiwa(self, user_input):
        """intro = Welcome to the whispering wall, Wiwa is here to respond
        and question your perspective. She is just a program, and
        will respond according to her script.
        If you wish to stop program, type EXIT or QUIT.
        Have fun! *Used in bash run*"""
        make = user_input
        stripped = make.lower()
        newstring = re.sub("[^a-zA-Z| |]+", "", stripped)
        if make in ['QUIT', 'EXIT', 'exit', 'quit', 'q']:
            return "Goodbye, thanks for stopping in!"
        else:
            choice = self.pick_response(make)
            #print(choice)
            question = self.check_question(make)
            if question:
                discusanswer = self.get_script_line(self.questionable)
                return discusanswer
            elif newstring in ['yes', 'no', 'maybe']:
                response = self.get_script_line(self.simplescript)
                return response
            else:
                if choice[0] == 'noun':
                    response = self.get_script_line(self.nounscript)
                    return response.format(choice[1])
                elif choice[0] =='verb':
                    response = self.get_script_line(self.verbscript)
                    verbasity = response.format(choice[1])
                    return verbasity
                elif choice[0] == 'adv':
                    response = "I don't have a script for adverbs yet."
                    return response
                elif choice[0] == 'adj':
                    response = self.get_script_line(self.adjectives)

                    if '{}' in response:
                        adjective = response.format(choice[1])
                        return adjective
                    else:
                        return response
                elif choice[0] == 'err':
                    response = self.get_script_line(self.error_script)

                    if '{}' in response:
                        too_error = response.format(choice[1])
                        return too_error
                    else:
                        return response

                else:

                    return("Wiwa:  ... ... ")


    def pick_response(self, raw_input):
        """ Create lists of possible valid words for response mechanism,
            Then uses random to choose one to send back to run_wiwa() """
        make = raw_input.lower()
        nouns, verbs, adj, adv, errors = self.make_tag_lists(make)
        n = len(nouns)
        v = len(verbs)
        aj = len(adj)
        av = len(adv)
        er = len(errors)
        words_found = False
        options = {'noun': [], 'verb': [], 'adj': [], 'adv': [], 'err': []}
        if n > 0:
            words_found = True
            for item in nouns:
                options['noun'].append(item)
        if v > 0:
            words_found = True
            for item in verbs:
                options['verb'].append(item)
        if aj > 0:
            words_found = True
            for item in adj:
                options['adj'].append(item)
        if av > 0:
            words_found = True
            for item in adv:
                options['adv'].append(item)
        if er > 0:
            words_found = True
            for item in errors:
                options['err'].append(item)

        done = False
        if words_found == True:
            while not done:
                # it might be bad to trust random.choice to not run idle while finding a choice in the list
                # the options dict is tiny so it shouldn't get stuck picking one
                word_type = random.choice(list(options.keys()))
                word_list = options[word_type]
                if len(word_list) > 0:
                    choice_tup = (word_type, word_list[0])
                    done = True
                    return choice_tup
        else:
            return ('error', 'not identified')

    def get_script_line(self, arg):
        """ Chooses a random script line to give back to user """
        # is often not random *sad face*
        #print(self.line_get)

        if arg == "/home/NelliesNoodles/nelliesnoodles_mysite/nouns.txt":
            order = self.noun_script_order
        elif arg == "/home/NelliesNoodles/nelliesnoodles_mysite/queries.txt":
            order = self.question_script_order
        elif arg ==  "/home/NelliesNoodles/nelliesnoodles_mysite/verbs.txt":
            order = self.verb_script_order
        elif arg == "/home/NelliesNoodles/nelliesnoodles_mysite/yes_no.txt":
            order = self.simple_script_order
        elif arg == "/home/NelliesNoodles/nelliesnoodles_mysite/adjectives.txt":
            order = self.adj_script_order
        elif arg == "/home/NelliesNoodles/nelliesnoodles_mysite/to_err.txt":
            order = self.err_script_order
        else:
            order = None
        if order != None:
            if self.line_get >= len(order):
                self.line_get = 0
            get_line = order[self.line_get]
            with open(arg) as f:
                lines = f.readlines()
                x = int(get_line)
                #print(lines[x])
                self.line_get += 1
                return lines[x]

        else:
            return "script file could not be found"

    def strip_stop_words(self, arg):
        stops = ['i', 'me', 'you', 'of', 'he', 'she', 'it', 'some', 'all', 'a', 'lot',
        'have', 'about', 'been', 'to', 'too', 'from', 'an', 'at',
        'above', 'before', 'across', 'against', 'almost', 'along', 'aslo',
        'although', 'always', 'am', 'among', 'amongst', 'amount', 'and',
        'another', 'any', 'anyhow', 'anyone', 'anything', 'around', 'as',
        'be', 'maybe', 'being', 'beside', 'besides', 'between', 'beyond', 'both',
        'but', 'by', 'can', 'could', 'done', 'during', 'each', 'either',
        'else', 'even', 'every', 'everyone', 'everything', 'everywhere',
        'except', 'few', 'for', 'had', 'has', 'hence', 'here', 'in', 'into', 'is',
        'it', 'its', 'it\'s', 'keep', 'last', 'latter', 'many', 'may', 'more', 'most',
        'much', 'name', 'next', 'none', 'not', 'nothing', 'now', 'nowhere',
        'often', 'other', 'others', 'over', 'rather', 'perhaps', 'seems', 'then',
        'there', 'these', 'they', 'though', 'the', 'this', 'thru', 'too', 'to', 'under', 'until',
        'upon', 'very', 'was', 'were' 'which', 'while', 'will', 'with', 'i\'ll', 'lets', 'n\'t']
        new_arg = []
        for item in arg:
            if item in stops:
                pass
            else:
                new_arg.append(item)
        #print(new_arg)
        return new_arg

    def make_tag_lists(self, arg):
        """
           Use nltk to tag the input, then clean up the lists to return
           A mechanism that will chose one of the items at random to return to
           Whispering walls response loop.
        """
        tokens = nltk.word_tokenize(arg)
        tags = nltk.pos_tag(tokens)
        errors, clean_tags = self.remove_bad_tags(tags)
        nouns = []
        verbs = []
        adj = []
        adv = []
        for item in clean_tags:
          x = item[1]
          #print(item)
          if x.startswith("VB"):
            verbs.append(item[0])
          elif x.startswith("NN"):
            nouns.append(item[0])
          elif x.startswith("JJ"):
            adj.append(item[0])
          elif x.startswith("RB"):
            adv.append(item[0])
          else:
            pass
        nouns = self.strip_stop_words(nouns)
        verbs = self.strip_stop_words(verbs)
        adj = self.strip_stop_words(adj)
        adv = self.strip_stop_words(adv)
        return nouns, verbs, adj, adv, errors

    def remove_bad_tags(self, tags_list):
        """ Use pyEnchant to remove unidentifiable words from tags list"""
        new_tags = []
        errors = []
        for item in tags_list:
            word = item[0]

            if self.enchant_check(word):
                new_tags.append(item)
            else:
                errors.append(word)

        return errors, new_tags

    def enchant_check(self, arg):
        """ using the PyEnchant English dictionary to check validity of a word."""
        x = self.dictionary.check(arg)
        return x

    def check_question(self, arg):
        questions = ['why', '?']
        if questions[0] in arg or questions[1] in arg:
          return True
        else:
          return False




#########   get count for number of lines in the txt file  ############
#################  make a list with range of number of lines in file ##
#########################              random.shuffle and return     ##

def create_script_line_order(somescript):
    """ make a list with randomized order of line numbers from script."""
    # get count:
    count = None
    #print(somescript)
    if somescript.endswith('.txt'):
        try:
            with open(somescript) as f:
                for i, l in enumerate(f):
                    pass
                    count = i
        except:
            print("file is Empty.")
            raise ValueError
    else:
        print("***file is not a txt file***")
        print("\t file=", somescript)
        raise ValueError
    if count != None:
        first_list = []
        # create a list with all line numbers in it
        for x in range(1, i):
            first_list.append(x)
        # shuffle those items:
        random.shuffle(first_list)
    return first_list




