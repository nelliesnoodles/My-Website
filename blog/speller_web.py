# spell-check and word suggestion:  Attempt #2

import re
import enchant


class WordFinder(object):
    def __init__(self):
        self.ench_dictionary = enchant.Dict("en-US")
        self.get_words = self.ench_dictionary.suggest


#######    validation and cleaning of input  #########
    def check_word(self, word):
        """
        returns true if word exists in dictionary
        returns false if word is not found
        """
        return self.ench_dictionary.check(word)

    def validate_string(self, sentence):
        """
        using a whitespace counter, check if the string is made
        up of only whitespace. raises enchant ValueError
        'can not spellcheck an empty string'
        This step needs to be done before the regex removal
        of non-alphanumeric's or a whitespace might remain
        undetected in a malicious/fuzzy string such as:
        '   &^%# *&#^ '
        Doubles as a check for empty string
        """
        if sentence:
            contents = list(sentence)

            length = len(contents)
            whitespace_count = 0
            for word in contents:
                if word != " ":
                    pass
                else:
                    whitespace_count += 1
            if length == whitespace_count:
                return False
            else:
                return True
        else:
            return False


    def remove_preceeding_whitespace(self, sentence):
        """
        remove all whitespace before the first character appears
        Done after regex.  Can be done before or after the whitespace
        check.   If it's all whitespace, and this removes it,
        the validation from validate_string will return false
        delete the whitespace outside of the detection for loop.
        otherwise the index's of items in the list change upon
        a deletion.
        """
        sentence_list = list(sentence)
        index = 0
        indexs_to_be_deleted = []
        for character in sentence_list:
            if not character.isspace():
                #print("breaking at:", index)
                break
            else:
                #print("placing index in list: ", index)
                indexs_to_be_deleted.append(index)
                index += 1
        #print(sentence_list)
        if len(indexs_to_be_deleted) > 0:
            placement = 0
            for integer in indexs_to_be_deleted:
                del sentence_list[integer + placement]
                placement -= 1
            #print(sentence_list)
            #new_sentence = ''.join(i) for i in sentence_list
            new_sentence = ''
            for words in sentence_list:
                new_sentence += words
            return new_sentence
        # default return original sentence, head whitespace not found
        return sentence

    def remove_non_alphanumeric(self, sentence):

        """
        Whispering wall checks for a question first, then
        processes the string, so a regex strip would happen after
        the string has been checked for any '?'.
        """
        # stack overflow answers to the rescue!
        # a lot of times there are multiple answers you can put
        # together to make what you are looking for.
        # link:
        # https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python

        newstring = re.sub(r'\W+', ' ', sentence, flags=re.UNICODE)
        return newstring


    def clean_input(self, user_input):
        """
        Clean the user input outside of the while loop.
        return clean valid sentence to use enchant's
        dictionary.check() on.
        """
        # convert any input to string
        user_input = str(user_input)

        # strip out all non alphanumerics with regex
        user_input = self.remove_non_alphanumeric(user_input)
        #print("after regex: \n", user_input)

        # clean any whitespace in the head of the user_input
        ##  IMPORTANT  ##
        ## this needs to be done AFTER regex or a whitespace might remain
        user_input = self.remove_preceeding_whitespace(user_input)


        ########  development purposes, return only first word ###
        # make only one word is accessed with split
        user_input = user_input.split(" ")
        # lower case only the first word given in request
        user_input = user_input[0].lower()
        #process word with enchant.suggest

        return user_input
############## end cleaning ################

###########  core loops for word processing ########

    def build_suggestion(self, error, word):
        # This is where we will replace words that are mispelled
        # and return a suggested sentence.

        # use clean on the sentence
        # if a word is spelled wrong, use the enchant suggest
        # replace word with the first one listed
        # return the suggested sentence
        """
        return a suggested list of corrections from enchant's
        dictionary.suggest()
        """
        message1 = "I recieved : " + error
        message2 = "Did you mean this  ?  --  " + word

        return message1, message2



    def get_suggestions(self, error_word):
        """
        Return a boolean for wether or not the error word
        was a valid string,  and a message with correction
        options if it is True (valid string).
        """

        error_word = self.clean_input(error_word)
        valid = self.validate_string(error_word)
        if error_word and valid:
            #user_request = self.clean_input(user_request)
            if self.check_word(error_word):
                #print("Your word is correct.\n")
                message = "Your word is correctly spelled."
                alist = ["This word was found by Python enchant dictionary."]
                error = " No error. " + error_word
                return message, error, alist
            else:
                result = self.get_words(error_word)
                if len(result) > 0:
                    first_word = result[0]
                    message1, message2 = self.build_suggestion(error_word, first_word)
                    alist = result
                else:
                    alist = ['no suggestion']
                    message1 = "The error enchant found: " + error_word
                    message2 = "Enchant could not come up with a suggestion."
                #print(result, "\n")
                return message1, message2, alist
        else:
            # print error for empty request
            #print("No word given in previous request.")
            message = "No valid input entered for the Word Finder."
            error = " "
            alist = [" Not valid input "]
            return message, error, alist
