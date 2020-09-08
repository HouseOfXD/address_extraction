# Extract address from unstructured text

import pickle
import nltk
import string

from nltk import pos_tag
from nltk import word_tokenize
from nltk.chunk import ChunkParserI
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk.tag import ClassifierBasedTagger
from nltk.tag.util import untag
from nltk.stem.snowball import SnowballStemmer

# **********************************************
# make sure to uncomment the following line when
# running this script for the first time
# **********************************************

# nltk.download()

# IOB tag name for specifying address
GPE_TAG = "GPE"

class AddressChunker(ChunkParserI):
    def __init__(self, train_sents, **kwargs):
        self.tagger = ClassifierBasedTagger(
            train=train_sents,
            feature_detector=self.features,
            **kwargs)

    def parse(self, tagged_sent):
        chunks = self.tagger.tag(tagged_sent)

        # Transform the result from [((w1, t1), iob1), ...]
        # to the preferred list of triplets format [(w1, t1, iob1), ...]
        iob_triplets = [(w, t, c) for ((w, t), c) in chunks]

        # Transform the list of triplets to nltk.Tree format
        return conlltags2tree(iob_triplets)

    def features(self, tokens, index, history):
        # for more details see: http://nlpforhackers.io/named-entity-extraction/

        """
        `tokens`  = a POS-tagged sentence [(w1, t1), ...]
        `index`   = the index of the token we want to extract features for
        `history` = the previous predicted IOB tags
        """

        # init the stemmer
        stemmer = SnowballStemmer('english')

        # Pad the sequence with placeholders
        tokens = [('[START2]', '[START2]'), ('[START1]', '[START1]')] + list(tokens) + [('[END1]', '[END1]'), ('[END2]', '[END2]')]
        history = ['[START2]', '[START1]'] + list(history)

        # shift the index with 2, to accommodate the padding
        index += 2

        word, pos = tokens[index]
        prevword, prevpos = tokens[index - 1]
        prevprevword, prevprevpos = tokens[index - 2]
        nextword, nextpos = tokens[index + 1]
        nextnextword, nextnextpos = tokens[index + 2]
        previob = history[index - 1]
        contains_dash = '-' in word
        contains_dot = '.' in word
        allascii = all([True for c in word if c in string.ascii_lowercase])

        allcaps = word == word.capitalize()
        capitalized = word[0] in string.ascii_uppercase

        prevallcaps = prevword == prevword.capitalize()
        prevcapitalized = prevword[0] in string.ascii_uppercase

        nextallcaps = prevword == prevword.capitalize()
        nextcapitalized = prevword[0] in string.ascii_uppercase

        f = {
            'word': word,
            'lemma': stemmer.stem(word),
            'pos': pos,
            'all-ascii': allascii,

            'next-word': nextword,
            'next-lemma': stemmer.stem(nextword),
            'next-pos': nextpos,

            'next-next-word': nextnextword,
            'nextnextpos': nextnextpos,

            'prev-word': prevword,
            'prev-lemma': stemmer.stem(prevword),
            'prev-pos': prevpos,

            'prev-prev-word': prevprevword,
            'prev-prev-pos': prevprevpos,

            'prev-iob': previob,

            'contains-dash': contains_dash,
            'contains-dot': contains_dot,

            'all-caps': allcaps,
            'capitalized': capitalized,

            'prev-all-caps': prevallcaps,
            'prev-capitalized': prevcapitalized,

            'next-all-caps': nextallcaps,
            'next-capitalized': nextcapitalized,
        }

        return f

def get_address_chunker(dataset_file_name):
    """
    returns AddressChunker instance with dataset_file_name as training samples

    `dataset_file_name` = file name of pickled list of CoNLL IOB format sentences
    """

    with open(dataset_file_name, 'rb') as fp:
        dataset = pickle.load(fp)
        print(len(dataset))
        chunker = AddressChunker(dataset)

    return chunker

def get_chuncker_accuracy(chunker, test_samples):
    """
    returns score of the chunker against the gold standard
    """
    score = chunker.evaluate([
        conlltags2tree([(w, t, iob) for (w, t), iob in iobs])
        for iobs in test_samples
        ])
    return score.accuracy()

def get_tagged_sentence(chunker, sentence):
    """
    returns IOB tagged tree of sentence
    """
    return chunker.parse(pos_tag(word_tokenize(sentence)))

def extract_address(chunker, sentence):
    """
    returns all addresses in sentence
    """
    def tree_filter(tree):
        return GPE_TAG == tree.label()

    tagged_tree = get_tagged_sentence(chunker, sentence)
    addresses = list()
    for subtree in tagged_tree.subtrees(filter=tree_filter):
        addresses.append(untag(subtree.leaves()))
    return addresses

print("Loading dataset...")
chunker = get_address_chunker('dataset/IOB_tagged_addresses.pkl')
print("Done.")
test = u'Price: $779,000 Location: Tudor City, Manhattan Tudor City, the historic 1920s enclave in Midtown East, has been called “a city within a city” for its somewhat secluded location on a hill and its two landscaped parks. This apartment at 333 East 41st Street is on the top floor of Prospect Hill, a six-story brick co-op built in 1926. Though the elevator building slightly predates its neighbors, which are mostly Tudor Revival-style apartment high-rises, it is still included in the historic district. It sits right next to one of said landscaped parks on a one-way street that has no through-traffic — and ends at an elevated lookout with benches facing the East River. Grand Central is only a ten-minute walk away. Specs: 1 bed, 1 bath, 650 square feet This unit has 10.5-foot ceilings and huge, 7.5-foot casement windows overlooking the park. The asking price is on the higher end for one-bedroom co-ops in the area, likely because it comes with recent renovations, like hand-cut, hand-painted tiles in the kitchen and bathroom, new appliances (including a Bertazzoni range), a rain shower, and built-in shelves. There’s a wood-burning fireplace in the living room, bar seating in the kitchen, and a breakfast nook next to more casement windows. The building is pet-friendly on a case-by-case basis and has a basement laundry room. Monthly dues are $1,700. See a video tour here.'
print(extract_address(chunker, test))
