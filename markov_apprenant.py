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
    sentences_to_add = ["Ty ran no sau rus Rex.",
    "Ve lo ci ra ptor.",
    "Tri ce ra tops.",
    "Ste go sau rus.",
    "Bra chi o sau rus.",
    "Di plo do cus.",
    "Al lo sau rus.",
    "Spi no sau rus.",
    "An ky lo sau rus.",
    "Pte ra no don.",
    "Ar chae op te ryx.",
    "Pa ra sau ro lo phus.",
    "Pach y ce pha lo sau rus.",
    "I gua no don.",
    "Car no tau rus.",
    "Dei no ny chus.",
    "Di lo pho sau rus.",
    "A pa to sau rus.",
    "Ba ryo nyx.",
    "Coe lo phy sis.",
    "Comp so gna thus.",
    "Di me tro don.",
    "Ed mon to sau rus.",
    "Gal li mi mus.",
    "Mi cro rap tor.",
    "O vi rap tor.",
    "Pla te o sau rus.",
    "Que tza lcoa tlus.",
    "Sau ro pha ga nax.",
    "The ri zi no sau rus.",
    "Tro o don.",
    "U tah ra ptor.",
    "Euo plo ce pha lus.",
    "Bron to sau rus.",
    "Co ry tho sau rus.",
    "Gi ga no to sau rus.",
    "Mo sau rus.",
    "Su cho mi mus.",
    "Sar co su chus.",
    "Sty ra co sau rus.",
    "Te non to sau rus.",
    "Tsin tao sau rus.",
    "I gua no don.",
    "Pa ra li ti tan.",
    "Coe lu rus.",
    "Lam beo sau rus.",
    "Ni ge r sau rus.",
    "A mar ga sau rus.",
    "Ei nio sau rus.",
    "Mai a sau ra.",
    "Al lo mas saurus.",
    "Ar cae on yx.",
    "Ba si le is chius.",
    "Brach yp sil ophus.",
    "Cam pto saurus.",
    "Chi ma era..",
    "De ino saurus.",
    "Drac orex.",
    "Eo tro pte rix.",
    "Galla mium.",
    "Ha dros au rus.",
    "Hya pas saurus.",
    "Icho thy saurus.",
    "Jan ens chi a.",
    "Jen oro pte ryx.",
    "Kai ta saurus.",
    "La o par a do ceps.",
    "Las ymo saurus.",
    "Li bi tus.",
    "Li man tros au rus.",
    "Ma a san thur sium.",
    "Mar gas au rus.",
    "Mon to san tis.",
    "Ne su tat o sus.",
    "Ony cho pte ryx.",
    "Or no thom i mus.",
    "Oth nei la spis.",
    "Pach y le o saurus.",
    "Par a ben thos au rus.",
    "Pla ti phy chius.",
    "Poly pte rix.",
    "Pra yan chi a.",
    "Pro a saur op ter yx.",
    "Psit tac o sau rus.",
    "Qua es it ris.",
    "Rha bdo saurus.",
    "Rug o saurus.",
    "Sai chin saurus.",
    "Sau ro phag i tus.",
    "Skel e to saurus.",
    "Sono ra saurus.",
    "Styg i mo lauch.",
    "Styraco ti tan.",
    "Syn an tho saurus.",
    "Ta pe ja ra.",
    "Ten on thu ris.",
    "Thyl a cael i os.",
    "Tys to ce ra tops.",
    "Vel lo pte rix.",
    "Wi pro cau dias.",
    "Ab e ta sau rus.",
    "Aga no do nax.",
    "An cho rio sau rus.",
    "Ba gua saurus.",
    "Ca be ra phas ma.",
    "Ci chi moko sau rus.",
    "Cyp re sau rus.",
    "Dio ny cho saurus.",
    "Dra coceph alosaurus.",
    "Ech in o saurus.",
    "Gal lo mius.",
    "Gom pho ther ium.",
    "Hel i o saurus.",
    "Ic thyo saurus.",
    "Isoch iro saurus.",
    "La plo saurus.",
    "Lao saur op ter yx.",
    "Lep i di sau rus.",
    "Mam mo scom pus.",
    "Meg a rach ni tor.",
    "Met rio saurus.",
    "On y cho po des.",
    "Orth ac anthus.",
    "Pel i cian imus.",
    "Po di o saurus.",
    "Ach ille saurus.",
    "Am bly pod cer a top.",
    "Ana ssi o sau rus.",
    "Aro nyo sau rus.",
    "Brach yse pha lo saurus.",
    "Car di no saurus.",
    "Chei lo saurus.",
    "Coe lo ce ratus.",
    "Cra ta eo saurus.",
    "Cry o lo pho saurus.",
    "Dein ony chel us.",
    "Dil lo te ti tan.",
    "Ed mon ti cer a top.",
    "Grav i pa rous.",
    "Hec tor sau rus.",
    "Hy a ci tho saurus.",
    "Iguan o rhyn chus.",
    "Ju go saurus.",
    "La chla no saurus.",
    "Meg a pyg my sau rus.",
    "Mer c saurus.",
    "Mon o ce ra tops.",
    "Ne uro saurus.",
    "Pla to saurus.",
    "Struth io mi mus.",
    "Thal eo saurus.",
    "Thy ra cod on.",
    "Tyr an no sau rus.",
    "Var i ri rus.",
    "Ver ti ce phan ti an.",
    "Vi vi pa rous.",
    "Wy a yau sau rus.",
    "Zeph yro saurus.",
    "Zyx om pho ce ra tops.",
    "Xa no sau rus.",
    "Acan thop ti rius.",
    "An chi so saurus.",
    "Archo rio saurus.",
    "Brox is sau rus.",
    "Ce pha lon sau rus.",
    "Cych lo sau rus.",
    "Do los sau rus.",
    "Gon gyo sau rus.",
    "He te ro sau rus.",
    "Hy plo sau rus.",
    "Ic thy o saurus.",
    "Iso saurus.",
    "Kai ro saurus.",
    "Lani saurus.",
    "Lopho sau rus.",
    "Mai sau rus.",
    "Met rio saurus.",
    "My os sau rus.",
    "Neur o saurus.",
    "Ortho ce ra tops.",
    "Pel lo saurus.",
    "Ple si sau rus.",
    "Poly sau rus.",
    "Pseu do sau rus.",
    "Rancho sau rus.",
    "Sarco sau rus.",
    "Sau ro saurus.",
    "Sten o sau rus.",
    "Struth i o mi mus.",
    "Ten on sau rus.",
    "Thy re saurus.",
    "Trach e o saurus.",
    "Tro o saurus.",
    "Uru saurus.",
    "Var i rus.",
    "Xip hacti rius.",
    "Zan cli saurus.",
    "Zyg o sau rus.",
    "Iguan o don.",
    "Sau ro mi mus.",
    ]

    markov.add_sentences(sentences_to_add)
    return(markov.generate_sentence())

if __name__ == "__main__":
    main()