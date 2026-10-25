import re

NAMES = {"serena", "andrew", "bobbie", "cason", "david", "farzana", "frank","hannah", "ida", "irene", "jim", "jose", "keith", "laura", "lucy",
         "meredith", "nick", "ada", "yeeling", "yan"}

PEOPLE = {"man", "men", "boy", "girl", "mother", "father", "friend","children", "people", "king", "adult", "adults", "person",
                "family", "dog", "fish", "bird", "horse", "animal"}

DETERMINERS = {"the", "a", "an", "his", "her", "their", "my", "our", "your","this", "that", "these", "those", "some", "every", "each"}

PREPOSITIONS = {"to", "in", "at", "on", "with", "from", "for", "by", "of","under", "over", "near", "through", "between", "before",
            "after", "during", "toward", "above", "behind", "against","among", "into", "until", "since"}

AUXILIARIES = {"do", "does", "did", "is", "are", "was", "were", "am", "be","been", "will", "would", "can", "could", "should", "must", "may", "might", "has", "have", "had"}

VERBS = {"bring", "go", "walk", "run", "take", "give", "make", "see", "come","eat", "read", "write", "play", "find", "get", "like", "want",
         "live", "work", "help", "show", "look", "call", "say", "tell","ask", "carry", "drive", "ride", "sing", "learn", "study", "leave",
         "keep", "open", "close", "stop", "start", "begin", "put", "turn" "move", "build", "hold", "watch", "listen", "hear", "draw", "feel",
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
TIME_WORDS = {"morning", "night", "day", "evening", "noon", "week", "year","today", "early", "late", "always", "often", "never", "once"}
NUMBERS = {"one", "two", "three", "four", "five", "six", "ten", "hundred","thousand", "half"}
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
    if word in NAMES or word in PEOPLE:
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
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass


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

        sentence_lowercase = lowercase_words(sent)
        question_lowercase = lowercase_words(ques)
        first_question_word = question_lowercase[0]


        # print(f'sentence: {sent}, question: {ques}')
        # print(f'sentence_lowercase: {sentence_lowercase}, questio_lowercase: {question_lowercase}')

        ##parsing the question to see if it asks who/what/where/when/why/how
        answer = None

        if first_question_word == "when":
            answer = self.when(sentence_lowercase)
        elif first_question_word == "where":
            answer = self.where(sentence,question_lowercase)
        elif first_question_word == "who":
           answer = self.who(sentence,question, question_lowercase)
        # elif first_question_word == "what":
        #     #
        # elif first_question_word == "how":
        #     #

        if answer is not None:
            return answer
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
                        return next_word

        # step 2: questoin has a verb
        verb_pos = self.get_verb_position(sentence, question)

        if verb_pos is not None:
            for i in range(verb_pos - 1, -1, -1):
                if is_a_person(sentence[i]) and sentence[i].lower() not in question_lowercase:
                    return sentence[i]


        # step 3, just grab the first person in the sentence
        for word in sentence:
            if is_a_person(word) and word.lower() not in question_lowercase:
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
                return word
        return None

    def what(self, sentence, question, question_lowercase):
        ####
        #find the verb in the sentene, then iterate through e ah word after the verb until
        # the next preposition, skipping names and determiners
        ####
        answer = None

        verb_pos = self.get_verb_position(sentence, question)
        if verb_pos is None:
            return None

        for word in sentence[verb_pos + 1:]:
            if word.lower() in PREPOSITIONS:
                break
            if word.lower() not in DETERMINERS and word.lower() not in NAMES:
                answer = word
        return answer

