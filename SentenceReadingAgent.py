import re

NAMES = {"serena", "andrew", "bobbie", "cason", "david", "farzana", "frank","hannah", "ida", "irene", "jim", "jose", "keith", "laura", "lucy",
         "meredith", "nick", "ada", "yeeling", "yan"}
SUBJECT_PRONOUNS = {"she", "he", "they", "we", "i", "you"}
PEOPLE = {"man", "men", "boy", "girl", "mother", "father", "friend","children", "people", "king", "adult", "adults", "person",
                "family", "dog", "fish", "bird", "horse", "animal"}

DETERMINERS = {"the", "a", "an", "his", "her", "their", "my", "our", "your","this", "that", "these", "those", "some", "every", "each"}

PREPOSITIONS = {"to", "in", "at", "on", "with", "from", "for", "by", "of","under", "over", "near", "through", "between", "before",
            "after", "during", "toward", "above", "behind", "against","among", "into", "until", "since"}

AUXILIARIES = {"do", "does", "did", "is", "are", "was", "were", "am", "be","been", "will", "would", "can", "could", "should", "must", "may", "might", "has", "have", "had"}

VERBS = {"bring", "go", "walk", "run", "take", "give", "make", "see", "come","eat", "read", "write", "play", "find", "get", "like", "want",
         "live", "work", "help", "show", "look", "call", "say", "tell","ask", "carry", "drive", "ride", "sing", "learn", "study", "leave",
         "keep", "open", "close", "stop", "start", "begin", "put", "turn" ,"move", "build", "hold", "watch", "listen", "hear", "draw", "feel",
         "need", "know", "think", "try", "use", "love", "sit", "stand","travel", "fly", "wait", "teach", "plant", "grow", "cut", "cover",
         "follow", "fill", "pull", "cross", "pass", "serve", "check","measure", "add", "answer", "remember", "laugh", "sleep", "decide",
         "press", "form", "happen", "swim", "reach", "sound", "seem","cry", "fall", "rest", "lay", "spell", "change"}

IRREGULAR = {"brought": "bring", "went": "go", "goes": "go", "took": "take","gave": "give", "ran": "run", "wrote": "write", "saw": "see",
             "came": "come", "said": "say", "ate": "eat", "got": "get","found": "find", "made": "make", "began": "begin",
             "told": "tell", "knew": "know", "thought": "think","heard": "hear", "left": "leave", "kept": "keep", "put": "put",
             "sat": "sit", "stood": "stand", "drew": "draw", "felt": "feel","held": "hold", "slept": "sleep", "flew": "fly", "swam": "swim",
             "rode": "ride", "fell": "fall", "has": "have", "had": "have","does": "do", "did": "do"}

MANNER_VERBS = {"walk", "run", "drive", "ride", "fly", "swim", "travel",  "sing", "carry"}

PLACES = {"school", "home", "house", "city", "town", "room", "river","farm", "country", "street", "island", "mountain", "sea", "world",
        "land", "park", "road", "church", "store", "table", "door", "earth", "field", "boat", "ship", "car"}

UNITS_DISTANCE = {"mile", "miles", "feet", "foot", "inch", "inches"}
UNITS_TIME = {"hour", "hours", "minute", "minutes", "second", "seconds","day", "days", "week", "weeks", "year", "years", "night"}
TIME_WORDS = {"soon", "morning", "night", "day", "evening", "noon", "week", "year","today", "early", "late", "always", "often", "never", "once"}
NUMBERS = {"all","one", "two", "three", "four", "five", "six", "ten", "hundred","thousand", "half"}
COLORS = {"red", "blue", "green", "black", "white", "gold", "yellow"}
ADJECTIVES = {"long", "short", "big", "large", "small", "little", "old","young", "high", "low", "hot", "cold", "fast", "slow", "hard",
              "good", "great", "new", "warm", "cool", "deep", "dark", "busy","quick", "strong", "free", "full", "simple", "real", "best",
            "better", "true"}
CLOCK = re.compile(r"^\d{1,2}:\d{2}(AM|PM|am|pm)?$")


def lowercase_words(words):
    lower = []
    for w in words:
        lower.append(w.lower())
    return lower

def is_a_person(word):
    word = word.lower()
    if word in NAMES or word in PEOPLE or word in SUBJECT_PRONOUNS:
        return True
    return False

def get_verb(word):
    word = word.lower()
    if word in IRREGULAR:
        return IRREGULAR[word]
    if word in VERBS:
        return word
    for ending in ["ing", "ed", "es", "s"]:
        if word.endswith(ending):
            base = word[:-len(ending)]
            if base in VERBS:
                return base
            if base + "e" in VERBS:  #
                return base + "e"
    #return VERBS.get(word.lower())
    return None

def find_next_word(words, iter):
    for word in words[iter + 1:]:
        if word.lower() not in DETERMINERS:
            return word
    return None

class SentenceReadingAgent:
    def __init__(self, debug = False):
        #If you want to do any initial processing, add it here.
        self.debug = debug  # set to True to print debugging info

    def log(self, *args):
        if self.debug:
            print("[DEBUG]", *args)


    def solve(self, sentence, question):
        '''
          You can use a library like spacy (https://spacy.io/usage/linguistic-features) to preprocess the
            mostcommon.txt file. There are others that could be used but you must use them in preprocessing only.
            You CANNOT import the library into Gradescope.
          
          You must include whatever preprocessing you've done into your SentenceReadingAgent.py.
          
          DO NOT use another file .txt or .csv. Hard code your DICTS | LISTS into this .py file
          
          While the supplied mostcommon.txt contains most of the common words you will need
            you can (and SHOULD) expand the file as you find cases that the agent has problems
            processing. 
            
          Also not all words will be processed using the correct lexing for every possible problem the 
            agent might encounter and you are ENCOURAGED to expand these in your agents knowledge representation.
        '''
        # Add your code here! Your solve method should receive
        # two strings as input: sentence and question. It should
        # return a string representing the answer to the question.
        sent = sentence.strip().rstrip(".?!").split()
        ques = question.strip().rstrip(".?!").split()

        lowercase_sentence = lowercase_words(sent)
        question_lowercase = lowercase_words(ques)
        first_question_word = question_lowercase[0]
        self.log("sentence:", sent)
        self.log("question:", ques)
        # print(f'sentence: {sent}, question: {ques}')
        # print(f'lowercase_sentence: {lowercase_sentence}, questio_lowercase: {question_lowercase}')
        ##parsing the question to see if it asks who/what/where/when/why/how
        answer = None

        if first_question_word == "when" or "time" in question_lowercase:
            answer = self.when(sent)
        elif first_question_word == "where":
            answer = self.where(sent, question_lowercase)
        elif first_question_word == "who":
            answer = self.who(sent, ques, question_lowercase)
        elif first_question_word == "what":
            answer = self.what(sent, ques, question_lowercase)
        elif first_question_word == "how":
            answer = self.how(sent, lowercase_sentence, question_lowercase)
        if answer is not None:
            self.log("answer:", answer)
            return answer
        self.log("no rule found an answer, falling back to first word:", sent[0])
        return sent[0]

    def get_verb_position(self, sentence, question):
        s_bases = [get_verb(word) for word in sentence]

        for qw in question[1:]:
            q_base = get_verb(qw)
            if q_base is not None and q_base in s_bases:
                return s_bases.index(q_base)

        return None

    def who(self, sentence, question, question_lowercase):
        ##
        #for who, there are a several ways that the question can be phrased so we have to iterate through
        # 1. the question ends in a preposition like to, from, with.
        # 2. the question has a verb, and we look one word to the left of the verb and get the answer
        # 3. if 1 and 2 dont work, then we just find the first person in the sentence and return that
        ##
        last_word =  question_lowercase[-1]
        # step 1, get last word and see if its a preposition
        if last_word in PREPOSITIONS:
            for i in range(len(sentence)):
                if sentence[i].lower() == last_word:
                    next_word = find_next_word(sentence, i)
                    if next_word is not None and is_a_person(next_word) and next_word.lower() not in question_lowercase:
                        self.log("who step 1: question ends in", last_word, "-> word after it:", next_word)
                        return next_word
        # step 2: questoin has a verb
        verb_pos = self.get_verb_position(sentence, question)
        if verb_pos is not None:
            for i in range(verb_pos - 1, -1, -1):
                if is_a_person(sentence[i]) and sentence[i].lower() not in question_lowercase:
                    self.log("who step 2: verb at position", verb_pos, "-> person to its left:", sentence[i])
                    return sentence[i]
        # step 3, just grab the first person in the sentence
        for word in sentence:
            if is_a_person(word) and word.lower() not in question_lowercase:
                self.log("who step 3: first person not in question:", word)
                return word
        return None

    def when(self, sentence):
        for word in sentence:
            if CLOCK.match(word):
                return word
        for word in sentence:
            if word.lower() in TIME_WORDS:
                return word
        return None

    def where(self, sentence, question_lowercase):
        for word in sentence:
            if word.lower() in PLACES and word.lower() not in question_lowercase:
                self.log("where: found place word:", word)
                return word
        return None

    def what(self, sentence, question, question_lowercase):
        ####
        #find the verb in the sentene, then iterate through the word after the verb until
        # the next preposition, skipping names and determiners
        ####
       # answer = None
        lowercase_sentence = lowercase_words(sentence)
        second_word = question_lowercase[1]
        last_word = question_lowercase[-1]

        #questions about color
        if "color" in question_lowercase:
            for word in sentence:
                if word.lower() in COLORS:
                    return word

        #Sentence: The sound of rain is cool.
        #Question: What has a cool sound?
        if second_word in ("has", "have"):
            for word in sentence:
                if word.lower() not in question_lowercase and word.lower() not in DETERMINERS | PREPOSITIONS | AUXILIARIES:
                    return word

        #Sentence: The white dog and the blue horse play together.
        #Question: What do the dog and horse do?
        if last_word in ("do", "does", "did"):
            for word in sentence:
                if get_verb(word) is not None and word.lower() not in question_lowercase:
                    return word

        #Sentence: A tree is made of wood.
        #Question: What is made of wood?
        if last_word in PREPOSITIONS and last_word in lowercase_sentence:
            next_word = find_next_word(sentence, lowercase_sentence.index(last_word))
            if next_word is not None and next_word.lower() not in question_lowercase:
                return next_word

        # Sentence: My dog Red is very large.
        # Question: What animal is Red?
        if (len(question_lowercase) >= 4 and question_lowercase[2] in ("is", "are", "was", "were")) \
                or (len(question_lowercase) == 3 and second_word in ("is", "are", "was", "were")):
            if last_word in lowercase_sentence:
                ind = lowercase_sentence.index(last_word)
                if ind > 0 and sentence[ind][0].isupper():
                    return sentence[ind - 1]
                if ind + 1 < len(sentence):
                    return sentence[ind + 1]

        ##what is/was/were/are ___ or what will be/been
        if second_word in ("is", "are", "was", "were") or last_word in ("be", "been"):
            result = self.what_is_blank(sentence, question_lowercase)
            self.log("what: is/be question, what_is_blank returned:", result)
            if result is not None:
                return result

        verb_pos = self.get_verb_position(sentence, question)
        self.log("what: verb position in sentence:", verb_pos)
        if verb_pos is None:
            return None
        matched_words = []
        for word in sentence[verb_pos + 1:]:
            word_low = word.lower()
            if word_low in PREPOSITIONS:
                break
            if word_low not in DETERMINERS and word_low not in NAMES and word_low not in TIME_WORDS:
                 matched_words.append(word)

        if matched_words:
            return matched_words[-1]

        #Sentence: The blue bird will sing in the morning.
        #Question: What will sing in the morning?
        for word in reversed(sentence[:verb_pos]):
            if word.lower() not in DETERMINERS and word.lower() not in AUXILIARIES:
                return word
        return None

    def what_is_blank(self, sentence, question_lowercase):
        ##failing a lot of what is ___ or what was ....
        #Sentence: A tree is made of wood.
        #Question: What is made of wood?

        lowercase_sentence = lowercase_words(sentence)
        catch_words = {"is", "are", "was", "were", "am", "be", "been"}
        #first "is" or   "be" in the sentence
        catch_positions = [i for i, w in enumerate(lowercase_sentence) if w in catch_words]
        if not catch_positions:
            return None
        trace = catch_positions[0]

        filler_word = [word for word in question_lowercase[1:]
                   if word not in AUXILIARIES | DETERMINERS | catch_words]

        if any(word in lowercase_sentence[:trace] for word in filler_word): return find_next_word(sentence, trace)

        subject = [word for word in sentence[:trace]
                   if word.lower() not in DETERMINERS and word.lower() not in AUXILIARIES]
        return subject[-1] if subject else None


    def how(self, sentence, lowercase_sentence, question_lowercase):
        second_word = question_lowercase[1]
        self.log("how: second word is", second_word)
        if second_word in ADJECTIVES:
            for word in question_lowercase[2:]:
                if word in AUXILIARIES or word in DETERMINERS or word in NAMES or word == "and":
                    continue
                if get_verb(word) is not None:
                    continue
                if word in lowercase_sentence:
                    ind = lowercase_sentence.index(word)
                    if ind > 0:
                        before = lowercase_sentence[ind - 1]
                        if before not in DETERMINERS and before not in PREPOSITIONS:
                            return sentence[ind - 1]
            if second_word == "long":
                return self.get_first_word_in_sentence(sentence, UNITS_TIME)
            return self.get_first_word_in_sentence(sentence, ADJECTIVES)
            # noun_in_sentence = any(
            #     w in lowercase_sentence and w not in AUXILIARIES and w not in DETERMINERS and w not in NAMES
            #     for w in question_lowercase[2:]
            # )
            # if not noun_in_sentence:
            #     for word in sentence:
            #         if word.lower() in UNITS_TIME:
            #             return word
        elif second_word == "far":
            return self.get_first_word_in_sentence(sentence, UNITS_DISTANCE)
            # for word in sentence:
            #     if word.lower() in UNITS_DISTANCE:
            #         return word
        elif second_word in ("many", "much"):
            #Sentence: There are one hundred adults in that city.
            #Question: How many adults are in this city?
            if len(question_lowercase) > 2 and question_lowercase[2] in lowercase_sentence:
                ind = lowercase_sentence.index(question_lowercase[2])
                if ind > 0 and (lowercase_sentence[ind - 1] in NUMBERS or sentence[ind - 1].isdigit()):
                    return sentence[ind - 1]
            numbers = [w for w in sentence if w.lower() in NUMBERS or w.isdigit()]
            if numbers:
                return numbers[-1]
        ##
        #question_8
        #Sentence: David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow.
        #Question: How do David and Lucy get to school?
        ##
        elif second_word in AUXILIARIES:
            if "by" in lowercase_sentence:
                return find_next_word(sentence, lowercase_sentence.index("by"))
            for word in sentence:
                if get_verb(word) in MANNER_VERBS and word.lower() not in question_lowercase:
                    return word


    def get_first_word_in_sentence(self, words, word_list):
        for word in words:
            if word.lower() in word_list:
                return word
        return None


