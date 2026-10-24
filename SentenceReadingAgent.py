import re

NAMES = {"serena", "andrew", "bobbie", "cason", "david", "farzana", "frank","hannah", "ida", "irene", "jim", "jose", "keith", "laura", "lucy",
         "meredith", "nick", "ada", "yeeling", "yan"}

PERSON_NOUNS = {"man", "men", "boy", "girl", "mother", "father", "friend","children", "people", "king", "adult", "adults", "person",
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


        print(f'sentence: {sent}, question: {ques}')
        print(f'sentence_lowercase: {sentence_lowercase}, questio_lowercase: {question_lowercase}')

        ##parsing the question to see if it asks who/what/where/when/why/how
        answer = None

        if first_question_word == "when":
            answer = self.when(sentence_lowercase)
        # elif first_question_word == "where":
        #     #
        # elif first_question_word == "who":
        #     #
        # elif first_question_word == "what":
        #     #
        # elif first_question_word == "how":
        #     #

        if answer is not None:
            return answer
        return sent[0]

    def when(self, sentence):
        for word in sentence:
            if word.lower() in TIME_WORDS:
                return word
        return None