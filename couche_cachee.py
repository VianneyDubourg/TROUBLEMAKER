import random
import time

class MarkovChain:
    def __init__(self):
        self.lookup_dict = {}
        self.state_ratings = {}
        self.beginnings = []

    def add_sentences(self, sentences):
        for sentence in sentences:
            self.add_sentence(sentence)

    def add_sentence(self, sentence):
        sentence = sentence[0].upper() + sentence[1:]
        if sentence[-1] != '.':
            sentence += '.'
        words = sentence.split()
        self.beginnings.append(words[0])
        for i, word in enumerate(words):
            if i == len(words)-1:
                self.lookup_dict.setdefault(word, []).append('END')
            else:
                next_word = words[i+1]
                self.lookup_dict.setdefault(word, []).append(next_word)

    def generate_sentence(self, min_rating=3):
        sentence = ''
        attempt = 0
        while True:
            words = [random.choice(self.beginnings)]
            while True:
                next_word_options = self.lookup_dict[words[-1]]
                next_word = random.choice(next_word_options)
                if next_word == 'END':
                    break
                words.append(next_word)
            sentence = ' '.join(words)
            if self.get_average_rating(' '.join(words[:-1])) >= min_rating or attempt > 5:
                break
            attempt += 1
        return sentence

    def rate_sentence(self, sentence, rating):
        words = sentence.split()
        for word in words:
            if word not in self.state_ratings:
                self.state_ratings[word] = []
            self.state_ratings[word].append(rating)

    def get_average_rating(self, sentence):
        ratings = []
        for word in sentence.split():
            if word in self.state_ratings and self.state_ratings[word]:
                ratings.append(sum(self.state_ratings[word]) / len(self.state_ratings[word]))
        if not ratings:
            return 0
        return sum(ratings) / len(ratings)

def main():
    markov = MarkovChain()
    sentences_to_add = [
    "Le soleil se lève à l'est et se couche à l'ouest.",
    "Elle adore lire des romans policiers les soirs d'hiver.",
    "La tour Eiffel est l'un des monuments les plus visités au monde.",
    "Mon chat s'endort toujours sur le canapé après avoir mangé.",
    "La pluie tombait doucement sur les toits de la ville.",
    "Nous partirons en vacances dès que l'école sera terminée.",
    "Il est important de boire beaucoup d'eau chaque jour.",
    "J'ai trouvé ce livre passionnant du début à la fin.",
    "L'océan Pacifique est le plus vaste des océans.",
    "Ils ont décidé de se marier l'été prochain.",
    "Le marché local propose des fruits et légumes frais tous les matins.",
    "Elle a peint ce tableau en utilisant uniquement des couleurs vives.",
    "J'aime me promener dans le parc pour me détendre.",
    "Nous avons regardé un film captivant hier soir.",
    "La neige a recouvert les montagnes d'un manteau blanc.",
    ]

    markov.add_sentences(sentences_to_add)

    for i in range(10):
        print(markov.generate_sentence())

if __name__ == "__main__":
    main()
