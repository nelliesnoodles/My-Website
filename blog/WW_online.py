#!usr/bin/python3
# -*- coding: utf-8 -*-

import re
import enchant
from nltk.corpus import wordnet
from random import randint
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
    Interject -- interjections.txt
"""


class Wiwa(object):
  def __init__(self):
    self.nounscript = "/home/NelliesNoodles/nelliesnoodles_mysite/nouns.txt"
    self.verbscript = "/home/NelliesNoodles/nelliesnoodles_mysite/verbs.txt"
    self.simplescript = "/home/NelliesNoodles/nelliesnoodles_mysite/yes_no.txt"
    self.questionable = "/home/NelliesNoodles/nelliesnoodles_mysite/queries.txt"
    self.dictionary = enchant.Dict("en_US")

  def run_wiwa(self, user_input):
    """intro = Welcome to the whispering wall, Wiwa is here to respond
    and question your perspective. She is just a program, and
    will respond according to her script.
    If you wish to stop program, type EXIT or QUIT.
    Have fun! *Used in bash run*"""
    make = user_input
    if make in ['QUIT', 'EXIT', 'exit', 'quit', 'q']:
        return "Goodbye, thanks for stopping in!"
    else:
      make = make.lower()
      nouns, verbs, adj, adv, errors = self.make_tag_lists(make)
      n = len(nouns)
      v = len(verbs)
      aj = len(adj)
      av = len(adv)
      er = len(errors)
      question = self.check_question(make)
      if question:
        # Maybe use simple script for these too?
        print("Wiwa:")
        discusanswer = self.get_script_line(self.questionable)
        return discusanswer
      elif make in ['yes', 'no', 'maybe']:
        response = self.get_script_line(self.simplescript)
        return response
      elif n < 1 and v < 1 and er > 0:
        response = (f" I do not know this: {errors[0]}, is the cat on the keyboard?")
        #print(f" I do not know this: {errors[0]}, is the cat on the keyboard?")
        return response
      elif v > 0:
        response = self.get_script_line(self.verbscript)
        verbosity = response.format(verbs[0])
        return verbosity
      elif n > 0:
        response = self.get_script_line(self.nounscript)
        nountacular = response.format(nouns[0])
        return nountacular
      elif v > 0:
        response = self.get_script_line(self.verbscript)
        verbasity = response.format(verbs[0])
        return verbasity
      elif aj > 0:
        adjective = ("Can a chatbot be: %s")
        response = adjective.format(adj[0])
        return response
      elif av > 0:
        adverbs = ("It would be nifty to see it done -- %s")
        response = adverbs.format(adv[0])
      else:
        return "The Whispering Wall is confused."

  def get_script_line(self, arg):
    with open(arg) as f:
      for i, l in enumerate(f):
        pass
      count = i
    if count != None:
      with open(arg) as f:
        lines = f.readlines()
        x = randint(0, count)
        return lines[x]

  def strip_stop_words(self, arg):
    stops = ['the', 'of', 'he', 'she', 'it', 'some', 'all', 'a', 'lot',
        'have', 'about', 'been', 'to', 'too', 'from', 'an', 'at',
        'above', 'before', 'across', 'against', 'almost', 'along', 'aslo',
        'although', 'always', 'am', 'among', 'amongst', 'amount', 'and',
        'another', 'any', 'anyhow', 'anyone', 'anything', 'around', 'as',
        'be', 'maybe', 'being', 'beside', 'besides', 'between', 'beyond', 'both',
        'but', 'by', 'can', 'could', 'done', 'during', 'each', 'either',
        'else', 'even', 'every', 'everyone', 'everything', 'everywhere',
        'except', 'few', 'for', 'had', 'has', 'hence', 'here', 'in', 'into', 'is',
        'it', 'its', 'keep', 'last', 'latter', 'many', 'may', 'more', 'most',
        'much', 'name', 'next', 'none', 'not', 'nothing', 'now', 'nowhere',
        'often', 'other', 'others', 'over', 'rather', 'perhaps', 'seems', 'then',
        'there', 'these', 'they', 'though', 'thru', 'too', 'under', 'until',
        'upon', 'very', 'was', 'were' 'which', 'while', 'will', 'with', 'ill', 'lets']
    new_arg = []
    for item in arg:
      if item in stops:
        pass
      else:
        new_arg.append(item)
    #print(new_arg)
    return new_arg

  def make_tag_lists(self, arg):
  #With string as arg, return lists of Adj, adv, noun, verb
  #    Empty lists mean no found type-noun(verb, adv, adj)
    clean_arg, errors = self.clean_string(arg)
    tokens = nltk.word_tokenize(clean_arg)
    tags = nltk.pos_tag(tokens)
    nouns = []
    verbs = []
    adj = []
    adv = []
    for item in tags:
      x = item[1]
      #print(item)
      if x == ("VB"):
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

  def clean_string(self, astring):
    """ Take the string and clear out all irrelevant data.
    Goal: to identify main verbs and nouns, any adjectives, adverbs
    Only tag words that are in the PyEnchant English dictionary. """
    astring = str(astring)
    #astring = astring.lower() put in main _run_wiwa loop
    #print(astring)
    newstring = re.sub("[^a-zA-Z| |]+", "", astring)
    stringlist = newstring.split()
    cleaned = ""
    errors = []
    for word in stringlist:
      if self.enchant_check(word) == True:
        cleaned = cleaned + word + " "
      else:
        #print(f"word not found {word}")
        errors.append(word)

    return cleaned, errors

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



