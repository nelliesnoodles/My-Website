#!usr/bin/python3
# -*- coding: utf-8 -*-

import enchant
import re
#from nltk.corpus import wordnet
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
    Interject -- interjections.txt <-- not used yet
    Adverbs -- adverbs.txt

    Testing
        >>> import WW_online
        >>> WW_test()
"""


class Wiwa(object):
    def __init__(self): # added a initiated value for session to access (line_numb) 1-9-18
        self.nounscript = "/home/NelliesNoodles/nelliesnoodles_mysite/nouns.txt"
        self.verbscript = "/home/NelliesNoodles/nelliesnoodles_mysite/verbs.txt"
        self.simplescript = "/home/NelliesNoodles/nelliesnoodles_mysite/yes_no.txt"
        self.questionable = "/home/NelliesNoodles/nelliesnoodles_mysite/queries.txt"
        self.adjectives = "/home/NelliesNoodles/nelliesnoodles_mysite/adjectives.txt"
        self.error_script = "/home/NelliesNoodles/nelliesnoodles_mysite/to_err.txt"
        self.adverbs = "/home/NelliesNoodles/nelliesnoodles_mysite/adverbs.txt"
        self.dictionary = enchant.Dict("en_US")
        self.line_get = 1

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
                    response = self.get_script_line(self.adverbs)
                    if '{}' in response:
                        adverb = response.format(choice[1])
                        return adverb
                    else:
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

    def _test_response_making(self, test_sentence):
            make = test_sentence
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
                        response = self.get_script_line(self.adverbs)
                        if '{}' in response:
                            adverb = response.format(choice[1])
                            return adverb
                        else:
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
        #return "getting line"
        if arg.startswith("/home/NelliesNoodles/nelliesnoodles_mysite/"):
            if self.line_get > 22:
                self.line_get = 0
            with open(arg) as f:
                lines = f.readlines()
                x = int(self.line_get)
                #print(lines[x])
                #self.line_get += 1 ##  Views.py and sessions handles the line_get attribute
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
        'it', 'its', "it's", 'keep', 'last', 'latter', 'many', 'may', 'more', 'most',
        'much', 'name', 'next', 'none', 'not', 'nothing', 'now', 'nowhere',
        'often', 'other', 'others', 'over', 'rather', 'perhaps', 'seems', 'then',
        'there', 'these', 'they', 'though', 'the', 'this', 'thru', 'too', 'to', 'under', 'until',
        'upon', 'very', 'was', 'were' 'which', 'while', 'will', 'with', "'s"]
        new_arg = []
        for item in arg:
            item_list = list(item)
            if item in stops:
                pass
            elif "'" in item_list:  # 1-12-19  removing contractions
                pass                # can not get it to ignore/remove contractions.  Might have to fiddle with NLTK
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

    def _test_attributes(self):
        scripts = [self.nounscript, self.verbscript, self.adjectives, self.simplescript, self.questionable, self.error_script, self.adverbs]
        index = 0
        for script in scripts:
            try:
                with open(script) as f:
                    print('SUCCESS')
                    print('script index: ', index)
                    index += 1
            except:
                message = "unable to open file at index {} in scripts of test_attributes"
                error_message = message.format(index)
                print(error_message)

        index = 0
        for script in scripts:
            result = self.get_script_line(script)
            if result == "script file could not be found":
                message = "unable to open file at index {} in scripts of test_attributes"
                error_message = message.format(index)
                print(error_message)
            else:
                print('get line success @ :', index)
                index += 1



def WW_test():
    test_sentences = [
        "Where are the goats?", #questionable.txt
        "The goats are jumping", #Noun, verb
        "The frog jumped.", #noun, verb
        "No", #simpleScript.txt
        "Tree.", #Noun
        "Kill it", # Verb
        "Pretty Octopus.", #Adjective
        "Edible button.", #adjective
        "Beautifully done.", #adverb
        "It is simply magnificent.", #adverb
        "fjskdflskjdflsjjslkfj", #error script
        ]
    WW = Wiwa()
    WW._test_attributes()
    ###  run testing of sentences  ###
    ### should produce any result except: "Wiwa:  ... ... " ###
    index = 0
    for data in test_sentences:
        try:
            response = WW._test_response_making(data)
            if response != "Wiwa:  ... ... ":
                print("successful sentence response, index= ", index)
                index += 1
            else:
                print("Unsuccessful test sentence response, index= ", index)
                index += 1
        except:
            print("Whispering wall failed to process sentence at index= ", index)

