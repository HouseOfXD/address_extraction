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

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

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
    realAddresses = []
    for subtree in tagged_tree.subtrees(filter=tree_filter):
        addresses.append(untag(subtree.leaves()))
    for address in addresses:
      try:
        houseNum = int(address[0])
        realAddresses.append(address)
      except ValueError:
        continue
    return {"ADDRESSES": addresses, "PARSEDADDRESSES": realAddresses}

print("Loading dataset...")
chunker = get_address_chunker('dataset/IOB_tagged_addresses.pkl')
print("Done.")
test = '''Advertise Sign In / Register RENT BUY  SELL BUILDINGS RESOURCES BLOG Sales  New Jersey  Hoboken  1425 Hudson Street #7C 1 of 15 1425 Hudson Street #7C $724,995 FOR SALE 832 ft²$871 per ft²2 rooms1 bed1 bath Condo in Hoboken  SAVE  SHARE This sale has been saved by 53 users. See a problem with this listing? Report it here. LISTED AT: Toll Brothers Real Estate Inc. John-Paul Vera  CONTACT AGENT  Learn more about dual agency DAYS ON MARKET 106 Days LAST PRICE CHANGE No Recorded Changes ESTIMATED PAYMENT $2,411  MONTHLY TAXES N/A MONTHLY COMMON CHARGES N/A TAX ABATEMENT No Data Available About the Listing DESCRIPTION  Welcome home to 1425 Hudson, the latest new construction from Toll Brothers City Living. This west facing 832 sq. ft. 1 bedroom / 1 bath home offers an open concept . Floor to ceiling windows throughout the home, bay window in the living room offers a north / south exposure – as well. Our luxury amenities include rooftop plunge pool, 24 hr. concierge, fireplace, outdoor grills & tv, fitness center, children's playroom and shuttle service to the PATH. Parking available, please inquire. 1425 offers waterfront living in an exclusive boutique building featuring floor to ceiling windows (on some homes) & views of the Empire State Building up to Hudson Yards -Manhattan (on some homes). Homes are available for immediate occupancy. We offer Studio, 1, 2, 3 & 4 bedroom homes. Copyright Hudson County MLS. All rights reserved. Information is deemed reliable but not guaranteed.  READ LESS Amenities HIGHLIGHTS Doorman Elevator Pets Allowed Washer/Dryer In-Unit BUILDING AMENITIES Gym Laundry in Building Parking Available Swimming Pool LISTING AMENITIES Central Air Conditioning Dishwasher About the Building 1425 Hudson Street  Hoboken, NJ 07030 Condo in Hoboken 99 Units12 Stories2018 Built Sales listings: 10 active and 41 previous Rentals listings: 1 active and 5 previous MORE ABOUT THE BUILDING Price History 07/02/2020	Listed by Toll Brothers Real Estate Inc	$724,995  WANT TO ANALYZE THIS PROPERTY WITH OUR COMPS REPORT GENERATOR? Similar Sales SALE IN TURTLE BAY 210 East 47th Street #7C $750,000  $48,800  1 Bed  1 Bath  780 ft² SALE IN TURTLE BAY 240 East 46th Street #10D $749,000  1 Bed  1 Bath  720 ft² FEATURED Listed at Toll Brothers Real Estate Inc. SALE IN HOBOKEN 1000 Maxwell Lane #8J $650,000  Studio  1 Bath  692 ft² SALE IN HOBOKEN 1125 Maxwell Lane #519 $649,000  1 Bed  1 Bath  - - - ft² SALE IN HOBOKEN 1300 Grand Street #418 $639,000  1 Bed  1 Bath  - - - ft² SALE IN TURTLE BAY 330 East 49th Street #6D $699,888  $50,111  1 Bed  1 Bath  - - - ft² SALE IN TURTLE BAY 100 United Nations Plaza #7F $700,000  $45,000  1 Bed  1 Bath  678 ft² SALE IN MIDTOWN SOUTH 100 West 39th Street #37H $799,000  $26,000  1 Bed  1 Bath  501 ft² SALE IN HOBOKEN 1125 Maxwell Lane #605 $779,000  $21,000  1 Bed  1+ Bath  895 ft² SALE IN HUDSON YARDS 433 West 34th Street #13K $740,000  1 Bed  1 Bath  - - - ft² Nearby TRANSPORTATION  HBLR at Lincoln Harbor  0.58 miles  HBLR at 9th Street/Congress St  0.76 miles  View subway lines on Google Maps  SCHOOLS There is no data available Disclaimer: School attendance zone boundaries are not guaranteed to be accurate – they are provided by a third party and subject to change. Check with the applicable school district prior to making a decision based on these boundaries. COLLEGES  College Of New Rochelle, The / School Of New Resources/New York Theological Seminary Campus  1.58 miles  Fashion Institute Of Technology (Suny)  1.68 miles  New School University / Jazz And Contemporary Music Program  1.88 miles  New School University / Eugene Lang College  1.89 miles  New School University / The New School  1.9 miles  PARKS  The High Line  1.1 miles  Clement Clarke Moore Park  1.17 miles  Corporal John A. Seravalli Playground  1.43 miles  Dr. Gertrude B. Kelly Playground  1.44 miles  Penn South Playground  1.44 miles  MUSEUMS  John J. Harvey Fireboat  0.8 miles  Chelsea Art Museum  0.99 miles  Dia Art Foundation  1.05 miles  Intrepid Sea-Air-Space Museum  1.5 miles  The Museum at FIT  1.68 miles  Map data ©2020 Google Terms of Use Report a map error VIEW ON GOOGLE Latest Discussions BE THE FIRST TO CREATE A DISCUSSION ABOUT THIS LISTING REPORT A PROBLEM  MLS # 202012592  Hoboken Sales Studios in Hoboken 1 Bedrooms in Hoboken 2 Bedrooms in Hoboken 3 Bedrooms in Hoboken Nearby Hoboken Jersey City Real Estate for sale The Heights Real Estate for sale Union City Real Estate for sale Weehawken Real Estate for sale More Condos for sale Co-ops for sale Houses for sale Pet friendly for sale BLOG WE'RE HIRING! SUBMIT YOUR LISTINGS WORK WITH US NYC RENTAL NETWORK PRESS BROWSE ALL HOMES Help Terms of Use & Privacy Policy Ad Choice App Store Play Market +  SHOW NYC NEIGHBORHOODS MANHATTAN Roosevelt Island All Downtown Civic Center Financial District Fulton/Seaport Tribeca Stuyvesant Town/PCV Soho Hudson Square Little Italy + Show more - Hide Lower East Side Two Bridges Chinatown Battery Park City Gramercy Park Chelsea West Chelsea Greenwich Village Noho East Village West Village Flatiron NoMad Nolita All Midtown Midtown Central Park South Midtown South Midtown East Murray Hill Sutton Place Turtle Bay Beekman Kips Bay Midtown West Hudson Yards Hell's Kitchen All Upper West Side Upper West Side Lincoln Square Manhattan Valley All Upper East Side Upper East Side Lenox Hill Yorkville Carnegie Hill Upper Carnegie Hill All Upper Manhattan Morningside Heights Hamilton Heights Washington Heights Hudson Heights Fort George Inwood West Harlem Manhattanville Central Harlem South Harlem East Harlem Marble Hill BRONX Mott Haven North New York Melrose Port Morris Hunts Point Longwood Morrisania Claremont Crotona Park East Highbridge + Show more - Hide Concourse Morris Heights University Heights Fordham East Tremont West Farms Belmont Bedford Park Kingsbridge Kingsbridge Heights Riverdale Fieldston Spuyten Duyvil Soundview Castle Hill Parkchester Throgs Neck Locust Point Pelham Bay Co-op City City Island Morris Park Pelham Parkway Van Nest Laconia Williamsbridge Baychester Woodlawn Wakefield Eastchester Tremont Mt. Hope Norwood Bronxwood Pelham Gardens Woodstock Westchester Village Westchester Square Country Club Schuylerville Edenwald BROOKLYN Greenpoint Williamsburg East Williamsburg Downtown Brooklyn Fort Greene Brooklyn Heights Boerum Hill DUMBO Vinegar Hill Bedford-Stuyvesant + Show more - Hide Stuyvesant Heights Ocean Hill Bushwick East New York New Lots City Line Starrett City Red Hook Park Slope Gowanus Carroll Gardens Cobble Hill Sunset Park Windsor Terrace Crown Heights Weeksville Prospect Heights Columbia St Waterfront District Prospect Lefferts Gardens Bay Ridge Fort Hamilton Dyker Heights Bensonhurst Bath Beach Gravesend Borough Park Mapleton Ocean Parkway Kensington Coney Island Brighton Beach Ditmas Park Fiske Terrace Seagate Flatbush Midwood Sheepshead Bay Homecrest Madison Manhattan Beach Brownsville Prospect Park South East Flatbush Farragut Wingate Canarsie Flatlands Marine Park Mill Basin Bergen Beach Clinton Hill Old Mill Basin Greenwood Gerritsen Beach QUEENS Astoria Ditmars-Steinway Long Island City Hunters Point Sunnyside Woodside Jackson Heights East Elmhurst North Corona Elmhurst + Show more - Hide Corona Maspeth Middle Village Ridgewood Glendale Rego Park Forest Hills Flushing East Flushing Murray Hill (Queens) Whitestone Malba Beechhurst College Point Fresh Meadows Kew Gardens Hills Jamaica Hills Woodhaven Richmond Hill Kew Gardens Howard Beach Hamilton Beach Ramblersville Rockwood Park Lindenwood Old Howard Beach Ozone Park South Ozone Park Bayside Bay Terrace (Queens) Douglaston Little Neck Auburndale Jamaica South Jamaica Hollis St. Albans Laurelton Cambria Heights Queens Village Glen Oaks Floral Park Bellerose Rosedale Springfield Gardens Briarwood Jamaica Estates New Hyde Park South Richmond Hill Oakland Gardens Hillcrest Pomonok Utopia Clearview Rockaway All Far Rockaway Broad Channel Arverne Rockaway Park Bayswater Belle Harbor Breezy Point Neponsit Edgemere Hammels Brookville STATEN ISLAND North Shore Arlington Clifton Elm Park Grymes Hill Howland Hook Mariners Harbor New Brighton Park Hill Port Richmond + Show more - Hide Rosebank Shore Acres Silver Lake Saint George Stapleton Tompkinsville West Brighton South Shore Annadale Arden Heights Charleston Eltingville Great Kills Greenridge Huguenot Pleasant Plains Princes Bay Richmond Valley Rossville Tottenville Woodrow East Shore Arrochar Bay Terrace Dongan Hills Egbertville Emerson Hill Fort Wadsworth Grant City Grasmere Lighthouse Hill Midland Beach New Dorp Oakwood Ocean Breeze Richmondtown South Beach Todt Hill New Dorp Beach Oakwood Beach West Shore Bloomfield Chelsea (Staten Island) Travis Mid-Island Bulls Head Castleton Corners Graniteville Manor Heights Meiers Corners New Springville Sunnyside (Staten Island) Westerleigh Willowbrook NEW JERSEY Cliffside Park Edgewater Fort Lee Jersey City Historic Downtown Waterfront Paulus Hook The Heights Journal Square West Side + Show more - Hide Newport Bergen/Lafayette Bayonne Hoboken East Newark Union City North Bergen Weehawken Guttenberg Harrison Kearny Secaucus West New York    StreetEasy is a brand and registered trademark of Zillow, Inc. Zillow, Inc. has a real estate brokerage license in multiple states. A list of these real estate licenses can be found here. ZILLOW · TRULIA · HOTPADS · OUT EAST Zillow Inc. Sites © 2006-2020 Zillow · Made In NYC · Powered by Bikes, Coffee and Doughnuts.'''
print(extract_address(chunker, test))
