import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api = "https://address-extractor-v1-nypxtcywhq-ue.a.run.app/extract"

text = '''Advertise Sign In / Register RENT BUY  SELL BUILDINGS RESOURCES BLOG Sales  Brooklyn  DUMBO  85 Jay Street 16F-FRONT 1 of 29  FLOOR PLAN  85 Jay Street 16F-FRONT $2,050,000 FOR SALE 1,291 ft²$1,587 per ft²4 rooms2 beds2 baths Sponsor Unit•Condo in DUMBO  SAVE  SHARE This sale has been saved by 49 users. See a problem with this listing? Report it here. LISTED AT: CIM / LIVWRK Front And York Sales Gallery  CONTACT AGENT  View listing at CIM / LIVWRK   SALES LAUNCH DATE September 2019 LAST PRICE CHANGE No Recorded Changes ESTIMATED PAYMENT $10,004  MONTHLY TAXES $1,671 MONTHLY COMMON CHARGES $1,516  TAX ABATEMENT No Data Available About the Listing SELLER'S AGENT Front & York Sales Gallery DESCRIPTION  Designed inside and out by Morris Adjmi, an Architect celebrated for honoring the New York Vernacular while adding a fresh, contemporary spin. Residences at Front & York pay homage to the industrial and historic character of DUMBO, inspired by the past and designed for the future.  Residence 16F is a 1,291sf light-filled corner two bedroom and two bathroom home offering a gracious layout and immense divided light windows that boast sweeping views of the Brooklyn skyline to the south and east. Elegant and refined interiors are graced with approximately 10’ ceilings and chevron-patterned white oak flooring. The custom designed chef’s kitchen seamlessly integrates with the great room and is equipped with a full suite of state-of-the-art Gaggenau appliances adding luster to the custom Morris Adjmi designed white oak cabinetry in a tobacco finish and hand-selected Caldia marble counter tops and back-splash.  The primary bedroom suite features a large walk-in closet and wide-plank white oak flooring. The en suite bath is a luxurious oasis that is adorned with Bianco Bello marble stone and radiant heated Grey River marble floors in a chevron pattern. The bespoke white oak double vanity and cast-iron soaking tub are complemented by custom Waterworks fittings. The secondary bathroom features Bianco Bello white marble in a polished, honed and hammered finish. Custom Italian white oak mill work and vanity, Waterworks fixtures and Strada porcelain floors. All homes will have filtered water and NEST thermostats.  With residences that feature breath-taking views of the city, the waterfront and nature, Front & York’s designation as a true urban resort is firmly established and enjoyed across a staggering array of resort-style amenities.  LEVEL EIGHT  Located approximately 100’ in the sky, Level Eight offers two vast wings of indoor and outdoor programming. Spend your days in the Coffee Lounge, Co-working Lounge, Children’s Playroom or Music Room. Relax by the Pool or play in the Game Room. Start your evening at the Outdoor Fireplace Terrace, cook dinner on the BBQ Deck, or Garden Lounge & Kitchen. Serve your friends and family from your own wine locker in the Wine Tasting Room with and enjoy dinner around the Chef’s Tasting Table. Retire to the Bar & Billiards Lounge or watch a film at the Outdoor Cinema or Indoor Screening Room and Lounge.  THE PARK  Celebrated landscape designer, Michael van Valkenburgh, has brought Brooklyn Bridge Park into the heart of Front & York. Spanning over 25,000 square feet, the Park is a lush urban oasis that is to be enjoyed year-round by residents.  LIFE TIME FITNESS  Health and Wellness at Front & York is taken to the next level. In addition to homes that feature filtered water throughout and an environment immersed with nature and green, residents at Front & York will also have direct access to an unprecedented three floors and over 77,000 square feet of Life Time Fitness. With a full-sized indoor basketball court, full-sized indoor pool with lap lanes, saunas, steam rooms, luxurious locker rooms, a robust schedule of classes led by world-class trainers, massage treatment rooms, LifeSpa, Life Café with healthy offerings and juices, programming for children with Life Time Kid’s Academy, resort style living is truly experienced.  Delivery anticipated 2021.  The complete Offering Terms are in an Offering Plan available from Sponsor. File No. CD18-0223. Sponsor: 85 Jay Street (Brooklyn), LLC c/o CIM Group 540 Madison Avenue, 8th Floor, New York, New York 10022. This advertising material is not an offer to sell nor a solicitation of an offer to buy to residents of any jurisdiction in which registration requirements have not been fulfilled. Equal Housing Opportunity. Sponsor reserves the right to make changes in accordance with the terms of the Offering Plan. Images are a combination of photographs and artist renderings.  READ MORE Amenities HIGHLIGHTS Doorman Elevator Pets Allowed BUILDING AMENITIES Bike Room Children's Playroom Cold Storage Concierge Gym Laundry in Building Media Room Package Room Smoke-free Storage Available Swimming Pool Valet Parking OUTDOOR SPACE Garden Roof Deck About the Building Front & York 85 Jay Street  Brooklyn, NY 11201 Condo in DUMBO 408 Units21 Stories2021 Built Sales listings: 19 active and 50 previous Documents and Permits: 9116 139 St Queens, NY 11435 21 documents MORE ABOUT THE BUILDING Price History 07/16/2020	Listed by CIM / LIVWRK	$2,050,000  WANT TO ANALYZE THIS PROPERTY WITH OUR COMPS REPORT GENERATOR? Similar Sales FEATURED Listed at Nest Seekers International SALE IN FINANCIAL DISTRICT 101 Wall Street #20B $2,249,000  $246,000  2 Beds  2.5 Baths  1,612 ft² FEATURED Listed at Alloy Advisory LLC SALE IN DUMBO 168 Plymouth Street #5B $2,100,000  2 Beds  2 Baths  1,210 ft² SALE IN FINANCIAL DISTRICT 25 Broad Street #20I $2,085,000  2 Beds  2 Baths  1,532 ft² SALE IN DUMBO 168 Plymouth Street #5B $2,100,000  2 Beds  2 Baths  1,210 ft² SALE IN DUMBO 51 Jay Street #5E $2,145,000  2 Beds  2.5 Baths  1,382 ft² FEATURED Listed at Nest Seekers International SALE IN FINANCIAL DISTRICT 101 Wall Street #12B $1,895,000  2 Beds  2.5 Baths  1,417 ft² SALE IN FINANCIAL DISTRICT 15 Broad Street #2700 $1,950,000  $15,000  2 Beds  2 Baths  1,734 ft² FEATURED Listed at Berkshire Hathaway HomeServices New York Properties SALE IN VINEGAR HILL 102 Gold Street #3F $1,850,000  $50,000  2 Beds  2 Baths  1,361 ft² SALE IN DUMBO 70 Washington Street #3R $2,259,000  $136,000  2 Beds  3 Baths  1,675 ft² Nearby TRANSPORTATION  F at York St  under 500 feet  A C at High St  0.23 miles  at Fulton Ferry Landing  0.48 miles  2 3 at Clark St  0.49 miles  A C F R at Jay St - MetroTech  0.59 miles  View subway lines on Google Maps  SCHOOLS District 13 - Schools zoned for this address: P.S. 307 Daniel Hale Williams (PK,0K,01,02,03,04,05,SE)  Disclaimer: School attendance zone boundaries are not guaranteed to be accurate – they are provided by a third party and subject to change. Check with the applicable school district prior to making a decision based on these boundaries. COLLEGES  Nyc Technical College (Cuny)  0.45 miles  Polytechnic University / Brooklyn-Metrotech Campus  0.5 miles  Institute Of Design And Construction  0.68 miles  St. Francis College  0.7 miles  Long Island University / Brooklyn Campus  0.74 miles  PARKS  Brooklyn Bridge Park  0.24 miles  Anchorage Plaza  0.24 miles  Cadman Plaza Park  0.25 miles  Park  0.25 miles  Walt Whitman Park  0.32 miles  MUSEUMS  Brooklyn Historical Society  0.6 miles  New York Transit Museum  0.82 miles  South Street Seaport Museum  1.0 miles  New York City Police Museum  1.18 miles  Tenement Museum  1.18 miles  Map data ©2020 Google Terms of Use Report a map error VIEW ON GOOGLE Latest Discussions BE THE FIRST TO CREATE A DISCUSSION ABOUT THIS LISTING About DUMBO LEARN MORE REPORT A PROBLEM DUMBO Sales Studios in DUMBO 1 Bedrooms in DUMBO 2 Bedrooms in DUMBO 3 Bedrooms in DUMBO Nearby DUMBO Downtown Brooklyn Real Estate for sale Brooklyn Heights Real Estate for sale Vinegar Hill Real Estate for sale More Condos for sale Co-ops for sale Houses for sale Pet friendly for sale BLOG WE'RE HIRING! SUBMIT YOUR LISTINGS WORK WITH US NYC RENTAL NETWORK PRESS BROWSE ALL HOMES Help Terms of Use & Privacy Policy Ad Choice App Store Play Market +  SHOW NYC NEIGHBORHOODS MANHATTAN Roosevelt Island All Downtown Civic Center Financial District Fulton/Seaport Tribeca Stuyvesant Town/PCV Soho Hudson Square Little Italy + Show more - Hide Lower East Side Two Bridges Chinatown Battery Park City Gramercy Park Chelsea West Chelsea Greenwich Village Noho East Village West Village Flatiron NoMad Nolita All Midtown Midtown Central Park South Midtown South Midtown East Murray Hill Sutton Place Turtle Bay Beekman Kips Bay Midtown West Hudson Yards Hell's Kitchen All Upper West Side Upper West Side Lincoln Square Manhattan Valley All Upper East Side Upper East Side Lenox Hill Yorkville Carnegie Hill Upper Carnegie Hill All Upper Manhattan Morningside Heights Hamilton Heights Washington Heights Hudson Heights Fort George Inwood West Harlem Manhattanville Central Harlem South Harlem East Harlem Marble Hill BRONX Mott Haven North New York Melrose Port Morris Hunts Point Longwood Morrisania Claremont Crotona Park East Highbridge + Show more - Hide Concourse Morris Heights University Heights Fordham East Tremont West Farms Belmont Bedford Park Kingsbridge Kingsbridge Heights Riverdale Fieldston Spuyten Duyvil Soundview Castle Hill Parkchester Throgs Neck Locust Point Pelham Bay Co-op City City Island Morris Park Pelham Parkway Van Nest Laconia Williamsbridge Baychester Woodlawn Wakefield Eastchester Tremont Mt. Hope Norwood Bronxwood Pelham Gardens Woodstock Westchester Village Westchester Square Country Club Schuylerville Edenwald BROOKLYN Greenpoint Williamsburg East Williamsburg Downtown Brooklyn Fort Greene Brooklyn Heights Boerum Hill DUMBO Vinegar Hill Bedford-Stuyvesant + Show more - Hide Stuyvesant Heights Ocean Hill Bushwick East New York New Lots City Line Starrett City Red Hook Park Slope Gowanus Carroll Gardens Cobble Hill Sunset Park Windsor Terrace Crown Heights Weeksville Prospect Heights Columbia St Waterfront District Prospect Lefferts Gardens Bay Ridge Fort Hamilton Dyker Heights Bensonhurst Bath Beach Gravesend Borough Park Mapleton Ocean Parkway Kensington Coney Island Brighton Beach Ditmas Park Fiske Terrace Seagate Flatbush Midwood Sheepshead Bay Homecrest Madison Manhattan Beach Brownsville Prospect Park South East Flatbush Farragut Wingate Canarsie Flatlands Marine Park Mill Basin Bergen Beach Clinton Hill Old Mill Basin Greenwood Gerritsen Beach QUEENS Astoria Ditmars-Steinway Long Island City Hunters Point Sunnyside Woodside Jackson Heights East Elmhurst North Corona Elmhurst + Show more - Hide Corona Maspeth Middle Village Ridgewood Glendale Rego Park Forest Hills Flushing East Flushing Murray Hill (Queens) Whitestone Malba Beechhurst College Point Fresh Meadows Kew Gardens Hills Jamaica Hills Woodhaven Richmond Hill Kew Gardens Howard Beach Hamilton Beach Ramblersville Rockwood Park Lindenwood Old Howard Beach Ozone Park South Ozone Park Bayside Bay Terrace (Queens) Douglaston Little Neck Auburndale Jamaica South Jamaica Hollis St. Albans Laurelton Cambria Heights Queens Village Glen Oaks Floral Park Bellerose Rosedale Springfield Gardens Briarwood Jamaica Estates New Hyde Park South Richmond Hill Oakland Gardens Hillcrest Pomonok Utopia Clearview Rockaway All Far Rockaway Broad Channel Arverne Rockaway Park Bayswater Belle Harbor Breezy Point Neponsit Edgemere Hammels Brookville STATEN ISLAND North Shore Arlington Clifton Elm Park Grymes Hill Howland Hook Mariners Harbor New Brighton Park Hill Port Richmond + Show more - Hide Rosebank Shore Acres Silver Lake Saint George Stapleton Tompkinsville West Brighton South Shore Annadale Arden Heights Charleston Eltingville Great Kills Greenridge Huguenot Pleasant Plains Princes Bay Richmond Valley Rossville Tottenville Woodrow East Shore Arrochar Bay Terrace Dongan Hills Egbertville Emerson Hill Fort Wadsworth Grant City Grasmere Lighthouse Hill Midland Beach New Dorp Oakwood Ocean Breeze Richmondtown South Beach Todt Hill New Dorp Beach Oakwood Beach West Shore Bloomfield Chelsea (Staten Island) Travis Mid-Island Bulls Head Castleton Corners Graniteville Manor Heights Meiers Corners New Springville Sunnyside (Staten Island) Westerleigh Willowbrook NEW JERSEY Cliffside Park Edgewater Fort Lee Jersey City Historic Downtown Waterfront Paulus Hook The Heights Journal Square West Side + Show more - Hide Newport Bergen/Lafayette Bayonne Hoboken East Newark Union City North Bergen Weehawken Guttenberg Harrison Kearny Secaucus West New York    StreetEasy is a brand and registered trademark of Zillow, Inc. Zillow, Inc. has a real estate brokerage license in multiple states. A list of these real estate licenses can be found here. ZILLOW · TRULIA · HOTPADS · OUT EAST Zillow Inc. Sites © 2006-2020 Zillow · Made In NYC · Powered by Bikes, Coffee and Doughnuts.'''

html = '''<body id="application" class="macintosh_platform webkit_engine chrome_browser desktop site_nyc site_home sales_home isFullbleed">
    <!-- START Google TagManager -->
<script defer="">

        var slot_FranchiseBox_1;var slot_Carousel_1;var slot_Carousel_2;var slot_Carousel_3;var slot_FeaturedBuild_1;var slot_FeaturedBuild_2;
        googletag.cmd.push(function() {
          googletag.pubads().disableInitialLoad();
          slot_FranchiseBox_1 = googletag.defineSlot('/7449/Streeteasy/search_main/buy_general/FranchiseBox_1', ["fluid"], 'FranchiseBox_1').addService(googletag.pubads());slot_Carousel_1 = googletag.defineSlot('/7449/Streeteasy/search_main/buy_general/Carousel_1', ["fluid"], 'Carousel_1').addService(googletag.pubads());slot_Carousel_2 = googletag.defineSlot('/7449/Streeteasy/search_main/buy_general/Carousel_2', ["fluid"], 'Carousel_2').addService(googletag.pubads());slot_Carousel_3 = googletag.defineSlot('/7449/Streeteasy/search_main/buy_general/Carousel_3', ["fluid"], 'Carousel_3').addService(googletag.pubads());slot_FeaturedBuild_1 = googletag.defineSlot('/7449/Streeteasy/search_main/buy_general/FeaturedBuild_1', ["fluid"], 'FeaturedBuild_1').addService(googletag.pubads());slot_FeaturedBuild_2 = googletag.defineSlot('/7449/Streeteasy/search_main/buy_general/FeaturedBuild_2', ["fluid"], 'FeaturedBuild_2').addService(googletag.pubads());
          googletag.pubads().setTargeting('dma', "43");
googletag.pubads().setTargeting('env', "prod");
googletag.pubads().setTargeting('pis', "7");
googletag.pubads().setTargeting('listtp', "buy_general");
googletag.pubads().setTargeting('state', "ny");
googletag.pubads().setTargeting('state', "nj");
googletag.pubads().setTargeting('zguidh', "24981553690009484353714901823485062833340181409112866998553");

        [].slice.call(document.querySelectorAll('[data-dfp-key]')).forEach(function(el) {
          var trackingKey = el.dataset.dfpKey,
              trackingValue = el.dataset.dfpValue;

          googletag.pubads().setTargeting(trackingKey, trackingValue);
        })


        function forceEagerLoadingOnAds(event) {
          var domId = event.slot.getSlotId().getDomId();
          var element = document.getElementById(domId);

          if (!element) {
            return;
          }

          var iframe = element.getElementsByTagName("iframe")[0];

          if (!iframe) {
            return;
          }

          iframe.setAttribute("loading", "eager");
        }
        googletag.pubads().addEventListener("slotRenderEnded", forceEagerLoadingOnAds);

          googletag.pubads().setTargeting('page_type', 'search_main');
          googletag.pubads().enableSingleRequest()
          googletag.pubads().collapseEmptyDivs();
          googletag.enableServices();
        });

</script>
<script type="text/javascript">
  dataLayer = [{"zguidh":"24981553690009484353714901823485062833340181409112866998553","site":"nyc","userType":"anonymous","pageCat":"sales","session_q_c":0,"cookie_q_c":0}];
</script>
<!-- END Google TagManager -->

          <!-- Google Tag Manager -->
  <noscript>
    <iframe src="//www.googletagmanager.com/ns.html?id=GTM-MKTT9R"
            height="0"
            width="0"
            style="display:none;visibility:hidden">
    </iframe>
  </noscript>
  <script type="text/javascript">
      (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
              new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
          j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
          '//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
      })(window,document,'script','dataLayer','GTM-MKTT9R');
  </script>
<!-- End Google Tag Manager -->

      <iframe height="0" width="0" style="display: none; visibility: hidden;" src="//8246315.fls.doubleclick.net/activityi;src=8246315;type=unive0;cat=allpa0;ord=2439956174184;gtm=2wg9u1;auiddc=1753115262.1602823850;~oref=https%3A%2F%2Fstreeteasy.com%2F?"></iframe><div id="site-wrapper" class="SiteBlock ">
        <div id="site-canvas" class="SiteBlock-canvas">
          <div id="site-shadow" class="SiteBlock-shadow"></div>
          <header class="HeaderBlock jsHeader ">


<div class="Header jsHeader">

  <a href="#" class="MenuMobileButton MenuMobileButton--hideDesktop u-noBorder u-noMargin" data-toggle="menu">
    <span class="MenuMobileButton-icon"></span>
  </a><div style="display: none;"><a href="fuxzqcyqdcvwucde.html" id="ubbfccwz" rel="file">fvtabqxeexc</a></div>

  <div class="Container">
    <div class="Header-logoDesktop">
      <a href="/" class="Logo">
        <img class="Logo-image" alt="StreetEasy Logo" src="//cdn-assets-s3.streeteasy.com/assets/logos/streeteasy-logo-white-1ab418223836c9074eb6f68857ad68a697eb31d2c86a98e597a467a7e527ac94.svg">
      </a>
    </div>

    <div class="Header-mWebBox jsMobileNavbar">
      <nav class="navbar navbar-default visible-xs-block visible-sm-block navbar-fixed-top jsMobileNavbar u-width--full">
        <div class="container-fluid hide-print">
            <div class="Logo">
              <a href="/">
                <img class="Logo-image" alt="StreetEasy Logo" src="//cdn-assets-s3.streeteasy.com/assets/logos/streeteasy-logo-white-1ab418223836c9074eb6f68857ad68a697eb31d2c86a98e597a467a7e527ac94.svg">
              </a>
            </div>


            <ul class="nav navbar-nav navbar-right">

            </ul>


        </div>
      </nav>


    </div>

    <ul class="Header-nav">
          <li class="Header-navListItem">
    <a href="https://streeteasy.com/agent-resources/advertise/" class="Header-navText">
      Advertise
    </a>
  </li>


<li class="Header-navListItem">
  <span class="Header-navText jsGoogleOneTap" onclick="window.gon.state.analyticsData = {'source':'nav'}; window.gon.state.triggerScenario('');">
    Sign In / Register
  </span>
</li>

    </ul>
  </div>
</div>
  <script type="text/javascript">
    window.addEventListener('load', () => {
      const clientId = '147313643782-6g6eiu6pva3rofhad6e7csk4r701hbpf.apps.googleusercontent.com';
      const loginButton = document.querySelectorAll('.jsGoogleOneTap');
      const saveItemButtons = document.querySelectorAll('.saveItemAfterAuthentication');

      loginButton.forEach(button => {
        button.addEventListener('click', () => {
          handleGoogleOneTap(clientId, 'nav');
        })
      });

      saveItemButtons.forEach(button => {
        button.addEventListener('click', () => {
          handleGoogleOneTapOnSave(clientId, 'save');
        });
      });
    });
  </script>


            <div id="site-menu" class="SiteBlock-menu">


    <div class="MainNav">
      <div class="Container">
          <ul class="MainNav-list isHoverable">
      <li class="MainNav-listItem isTrackingMenuItem" data-trending-id="3268940" data-type="Rentals">
        <a class="MainNav-text" data-toggle="nav_popup" href="/rentals">Rent</a>
        <div class="MainNav-popup">
          <div class="Container">
            <div class="MainNav-popupColumn">
              <h6 class="MainNav-popupTitle">
                Areas
              </h6>
              <ul class="MainNav-popupList">
                <li class="MainNav-popupListItem">
                  <a class="MainNav-popupColumnLink" data-gtm-header-menu="Rentals" href="/for-rent/manhattan">Manhattan</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a class="MainNav-popupColumnLink" data-gtm-header-menu="Rentals" href="/for-rent/brooklyn">Brooklyn</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a class="MainNav-popupColumnLink" data-gtm-header-menu="Rentals" href="/for-rent/queens">Queens</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a class="MainNav-popupColumnLink" data-gtm-header-menu="Rentals" href="/for-rent/bronx">Bronx</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a class="MainNav-popupColumnLink" data-gtm-header-menu="Rentals" href="/for-rent/staten-island">Staten Island</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a class="MainNav-popupColumnLink" data-gtm-header-menu="Rentals" href="/for-rent/new-jersey">New Jersey</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a class="MainNav-popupColumnLink" data-gtm-header-menu="Rentals" href="/for-rent/nyc">All NYC + NJ</a>
                </li>
              </ul>
            </div>
            <div class="MainNav-popupColumn MainNav-popupColumn--last">
              <h6 class="MainNav-popupTitle">Popular neighborhoods</h6>
              <ul class="MainNav-popupList">
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Rentals" href="/for-rent/tribeca" class="MainNav-popupColumnLink">
      Tribeca
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Rentals" href="/for-rent/upper-east-side" class="MainNav-popupColumnLink">
      Upper East Side
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Rentals" href="/for-rent/upper-west-side" class="MainNav-popupColumnLink">
      Upper West Side
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Rentals" href="/for-rent/east-village" class="MainNav-popupColumnLink">
      East Village
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Rentals" href="/for-rent/williamsburg" class="MainNav-popupColumnLink">
      Williamsburg
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Rentals" href="/for-rent/astoria" class="MainNav-popupColumnLink">
      Astoria
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Rentals" href="/for-rent/hoboken" class="MainNav-popupColumnLink">
      Hoboken
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Rentals" href="/for-rent/jersey-city" class="MainNav-popupColumnLink">
      Jersey City
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Rentals" href="/rentals/all" class="MainNav-popupColumnLink">
      View All
    </a>
  </li>
</ul>

            </div>
            <div class="MainNav-popupColumn MainNav-popupColumn--ads">

                <div class="MostViewedItem">
  <div class="MostViewedItem-imgBox">
    <a data-gtm-header-listing-id="3268940" data-gtm-header-listing-type="rental" href="/building/75-wall-street-new_york/19r"><img alt="75 Wall Street" class="MostViewedItem-img" src="https://cdn-img-feed.streeteasy.com/nyc/image/87/407733387.jpg"></a>
  </div>
  <div class="MostViewedItem-content">
    <a class="MostViewedItem-titleLink" data-gtm-header-listing-id="3268940" data-gtm-header-listing-type="rental" href="/building/75-wall-street-new_york/19r">75 Wall Street</a>
    <div>

        <span class="MostViewedItem-price">
          $2,890
        </span>
        <span class="MostViewedItem-for">
          for rent
        </span>
    </div>

    <div>3 beds<span class="MostViewedItem-bullet">•</span>1 bath<span class="MostViewedItem-bullet">•</span>889 ft²</div>
    <div>Rental Unit in <a href="/area/financial-district">Financial District</a></div>
  </div>
</div>

            </div>
          </div>
        </div>
      </li>
      <li class="MainNav-listItem isTrackingMenuItem" data-trending-id="1499470" data-type="Sales">
        <a class="MainNav-text" data-toggle="nav_popup" href="/">Buy</a>
        <div class="MainNav-popup">
          <div class="Container">
            <div class="MainNav-popupColumn">
              <h6 class="MainNav-popupTitle">
                Areas
              </h6>
              <ul class="MainNav-popupList">
                <li class="MainNav-popupListItem">
                  <a data-gtm-header-menu="Sales" class="MainNav-popupColumnLink" href="/for-sale/manhattan">Manhattan</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a data-gtm-header-menu="Sales" class="MainNav-popupColumnLink" href="/for-sale/brooklyn">Brooklyn</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a data-gtm-header-menu="Sales" class="MainNav-popupColumnLink" href="/for-sale/queens">Queens</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a data-gtm-header-menu="Sales" class="MainNav-popupColumnLink" href="/for-sale/bronx">Bronx</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a data-gtm-header-menu="Sales" class="MainNav-popupColumnLink" href="/for-sale/staten-island">Staten Island</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a data-gtm-header-menu="Sales" class="MainNav-popupColumnLink" href="/for-sale/new-jersey">New Jersey</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a data-gtm-header-menu="Sales" class="MainNav-popupColumnLink" href="/for-sale/nyc">All NYC + NJ</a>
                </li>
              </ul>
            </div>
            <div class="MainNav-popupColumn MainNav-popupColumn--last">
              <h6 class="MainNav-popupTitle">Popular neighborhoods</h6>
              <ul class="MainNav-popupList">
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Sales" href="/for-sale/upper-east-side" class="MainNav-popupColumnLink">
      Upper East Side
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Sales" href="/for-sale/tribeca" class="MainNav-popupColumnLink">
      Tribeca
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Sales" href="/for-sale/williamsburg" class="MainNav-popupColumnLink">
      Williamsburg
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Sales" href="/for-sale/brooklyn-heights" class="MainNav-popupColumnLink">
      Brooklyn Heights
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Sales" href="/for-sale/park-slope" class="MainNav-popupColumnLink">
      Park Slope
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Sales" href="/for-sale/ditmas-park" class="MainNav-popupColumnLink">
      Ditmas Park
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Sales" href="/for-sale/hoboken" class="MainNav-popupColumnLink">
      Hoboken
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Sales" href="/for-sale/jersey-city" class="MainNav-popupColumnLink">
      Jersey City
    </a>
  </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Sales" href="/sales/all" class="MainNav-popupColumnLink">
      View All
    </a>
  </li>
</ul>

            </div>
            <div class="MainNav-popupColumn MainNav-popupColumn--ads">

                <div class="MostViewedItem">
  <div class="MostViewedItem-imgBox">
    <a data-gtm-header-listing-id="1499470" data-gtm-header-listing-type="sale" href="/building/the-regatta/222"><img alt="21 South End Avenue #222" class="MostViewedItem-img" src="https://cdn-img-feed.streeteasy.com/nyc/image/77/407835577.jpg"></a>
  </div>
  <div class="MostViewedItem-content">
    <a class="MostViewedItem-titleLink" data-gtm-header-listing-id="1499470" data-gtm-header-listing-type="sale" href="/building/the-regatta/222">21 South End Avenue #222</a>
    <div>

        <span class="MostViewedItem-price">
          $1,695,000
        </span>
        <span class="MostViewedItem-for">
          for sale
        </span>
    </div>

    <div>2 beds<span class="MostViewedItem-bullet">•</span>2.5 baths<span class="MostViewedItem-bullet">•</span>1,200 ft²</div>
    <div>Condo in <a href="/area/battery-park-city">Battery Park City</a></div>
  </div>
</div>

            </div>
          </div>
        </div>
      </li>
    <li class="MainNav-listItem MainNav-listItem--new">
      <span aria-hidden="true" class="MainNav-accent MainNav-accent--new" title="New"></span>
      <a class="MainNav-text" aria-label="Sell Your Home" href="/sell-your-home">Sell</a>
    </li>
    <li class="MainNav-listItem isTrackingMenuItem" data-trending-id="110" data-type="Buildings">
      <a class="MainNav-text" data-toggle="nav_popup" href="/nyc/newdevs">Buildings</a>
      <div class="MainNav-popup">
        <div class="Container">
          <div class="MainNav-popupColumn">
            <h6 class="MainNav-popupTitle">Browse</h6>
            <ul class="MainNav-popupList MainNav-popupList--paddingBottom">
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/new-developments" class="MainNav-popupColumnLink">
                  New Developments
                </a>
              </li>
            </ul>
            <h6 class="MainNav-popupTitle">
              Areas
            </h6>
            <ul class="MainNav-popupList">
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/buildings/manhattan" class="MainNav-popupColumnLink">
                  Manhattan
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/buildings/brooklyn" class="MainNav-popupColumnLink">
                  Brooklyn
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/buildings/queens" class="MainNav-popupColumnLink">
                  Queens
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/buildings/bronx" class="MainNav-popupColumnLink">
                  Bronx
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/buildings/staten-island" class="MainNav-popupColumnLink">
                  Staten Island
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a class="MainNav-popupColumnLink" href="/buildings/new-jersey">New Jersey</a>
              </li>
              <li class="MainNav-popupListItem">
                <a class="MainNav-popupColumnLink" data-gtm-header-menu="Buildings" href="/buildings/nyc">All NYC + NJ</a>
              </li>
            </ul>
          </div>
          <div class="MainNav-popupColumn">
            <h6 class="MainNav-popupTitle">Popular buildings</h6>

              <ul class="MainNav-popupList">
    <li class="MainNav-popupListItem">
      <a data-gtm-header-menu="Buildings" href="/building/the-dakota" class="MainNav-popupColumnLink">
        The Dakota
      </a>
    </li>
    <li class="MainNav-popupListItem">
      <a data-gtm-header-menu="Buildings" href="/building/15-hudson-yards" class="MainNav-popupColumnLink">
        15 Hudson Yards
      </a>
    </li>
    <li class="MainNav-popupListItem">
      <a data-gtm-header-menu="Buildings" href="/building/the-rheingold" class="MainNav-popupColumnLink">
        The Rheingold
      </a>
    </li>
    <li class="MainNav-popupListItem">
      <a data-gtm-header-menu="Buildings" href="/building/1-prospect-park-west-brooklyn" class="MainNav-popupColumnLink">
        1 Prospect Park West
      </a>
    </li>
    <li class="MainNav-popupListItem">
      <a data-gtm-header-menu="Buildings" href="/building/575-4-avenue-brooklyn" class="MainNav-popupColumnLink">
        575 Fourth Avenue
      </a>
    </li>
    <li class="MainNav-popupListItem">
      <a data-gtm-header-menu="Buildings" href="/building/111-murray-street" class="MainNav-popupColumnLink">
        111 Murray Street
      </a>
    </li>
    <li class="MainNav-popupListItem">
      <a data-gtm-header-menu="Buildings" href="/building/1-ocean-drive-brooklyn" class="MainNav-popupColumnLink">
        1 Ocean Drive
      </a>
    </li>
    <li class="MainNav-popupListItem">
      <a data-gtm-header-menu="Buildings" href="/building/50-west-street-new_york" class="MainNav-popupColumnLink">
        50 West Street
      </a>
    </li>
  <li class="MainNav-popupListItem">
    <a data-gtm-header-menu="Buildings" href="/buildings/all" class="MainNav-popupColumnLink">
      View All
    </a>
  </li>
</ul>

          </div>
          <div class="MainNav-popupColumn MainNav-popupColumn--lastShort">
            <h6 class="MainNav-popupTitle">New developments</h6>
            <ul class="MainNav-popupList">
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/building/one-manhattan-square" class="MainNav-popupColumnLink">
                  252 South Street
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/building/111-murray-street" class="MainNav-popupColumnLink">
                  111 Murray Street
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/building/130-william-street-new_york" class="MainNav-popupColumnLink">
                  130 William Street
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/building/one-west-end" class="MainNav-popupColumnLink">
                  1 West End Avenue
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/building/565-broome-soho" class="MainNav-popupColumnLink">
                  565 Broome Street
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/building/11-hoyt" class="MainNav-popupColumnLink">
                  11 Hoyt Street
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/building/the-park-loggia" class="MainNav-popupColumnLink">
                  15 West 61st Street
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/building/91-leonard" class="MainNav-popupColumnLink">
                  91 Leonard Street
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/building/madison-house" class="MainNav-popupColumnLink">
                  15 East 30th Street
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Buildings" href="/buildings/nyc/new_development:new%20development" class="MainNav-popupColumnLink">
                  View All
                </a>
              </li>
            </ul>
          </div>
          <div class="MainNav-popupColumn MainNav-popupColumn--adsShort">
            <div class="MostViewedItem">
              <div class="MostViewedItem-img">
                <a href="/new-developments"><img srcset="//cdn-assets-s3.streeteasy.com/assets/header/buildings/NewDev_AdUnit@2x-b19c460e4f916c3ac26d1bd43fb6b1fb1c9f9278a74777978995d59132c077f3.png 2x" alt="new developments" src="//cdn-assets-s3.streeteasy.com/assets/header/buildings/NewDev_AdUnit-4e49e33b80bc9e72690b964ce70758bdac68bdef39efd0807bdb8404d0617956.png"></a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </li>
  <li class="MainNav-listItem isTrackingMenuItem" data-type="Resourses">
      <span class="MainNav-text" data-toggle="nav_popup">Resources</span>
      <div class="MainNav-popup">
        <div class="Container">
          <div class="MainNav-popupColumn">
            <h6 class="MainNav-popupTitle">Browse</h6>
            <ul class="MainNav-popupList MainNav-popupList--paddingBottom">
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Resources" href="/no-fee-rentals/nyc" class="MainNav-popupColumnLink">
                  No-fee Apartments
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Resources" href="/pet-friendly-rentals/nyc" class="MainNav-popupColumnLink">
                  Pet-Friendly Rentals
                </a>
              </li>
            </ul>
            <h6 class="MainNav-popupTitle">Guides</h6>
            <ul class="MainNav-popupList">
              <li class="MainNav-popupListItem">
                <a class="MainNav-popupColumnLink" data-gtm-header-menu="Resources" href="/guides/">NYC Real Estate Guides</a>
              </li>
              <li class="MainNav-popupListItem">
                <a class="MainNav-popupColumnLink" data-gtm-header-menu="Resources" href="/neighborhoods/">Neighborhood Guides</a>
              </li>
              <li class="MainNav-popupListItem">
                <a class="MainNav-popupColumnLink" data-gtm-header-menu="Resources" href="/guides/moving-nyc/">Moving to NYC Guide</a>
              </li>
            </ul>
          </div>
          <div class="MainNav-popupColumn">
            <h6 class="MainNav-popupTitle">Mortgage</h6>
            <ul class="MainNav-popupList MainNav-popupList--paddingBottom">
              <li class="MainNav-popupListItem">
                <a class="MainNav-popupColumnLink" data-gtm-header-menu="Resources" rel="nofollow" href="/nyc/mortgage_rates">Mortgage Rates</a>
              </li>
              <li class="MainNav-popupListItem">
                <a class="MainNav-popupColumnLink" data-gtm-header-menu="Resources" href="/nyc/calculator/index">Mortgage Calculator</a>
              </li>
            </ul>
            <h6 class="MainNav-popupTitle">Tools</h6>
            <ul class="MainNav-popupList">
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Resources" href="/talk" class="MainNav-popupColumnLink">
                  StreetEasy Forums
                </a>
              </li>
                <li name="open_house_planner" class="MainNav-popupListItem">
                    <a data-modal-class="modal-signin" data-gtm-login-required="true" data-gtm-rendered-from="site_nav" data-gtm-origin="open_house" data-gtm-track="resources-menu" data-gtm-header-menu="Resources" class="MainNav-popupColumnLink" data-toggle="modal" data-modal-source="/nyc/user/register_dialog?return_to=%2Fnyc%2Fopen_house_planner&amp;origin=open_house" href="#">Open House Planner</a>
                </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Resources" href="//streeteasy.com/agent-resources" class="MainNav-popupColumnLink">
                  Agent Resource Center
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a href="https://streeteasy.com/blog/data-dashboard/" class="MainNav-popupColumnLink">
                  Data Dashboard
                </a>
              </li>
            </ul>
          </div>
          <div class="MainNav-popupColumn MainNav-popupColumn--lastShort">
            <h6 class="MainNav-popupTitle">Market Data</h6>
            <ul class="MainNav-popupList MainNav-popupList--paddingBottom">
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Resources" href="/blog/market-reports" class="MainNav-popupColumnLink">
                  Market Reports
                </a>
              </li>
                <li class="MainNav-popupListItem">
                    <a onclick="window.gon.state.analyticsData = {'source':'comparables_report'};window.gon.state.triggerScenario('EmailCapture', { redirectTo: '/my/comparables' });" data-modal-class="modal-signin" data-gtm-login-required="true" data-gtm-rendered-from="site_nav" data-gtm-origin="comparables_report" data-gtm-track="resources-menu" data-gtm-header-menu="Resources" class="MainNav-popupColumnLink" href="#">Comparables Reports</a>
                </li>
            </ul>
            <h6 class="MainNav-popupTitle">Q&amp;A</h6>
            <ul class="MainNav-popupList">
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Resources" href="//streeteasy.com/guides/buyers-guide/should-you-rent-or-buy/" class="MainNav-popupColumnLink">
                  Should You Rent or Buy?
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Resources" href="//streeteasy.com/guides/buyers-guide/what-are-maintenance-fees/" class="MainNav-popupColumnLink">
                  What are Maintenance Fees
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Resources" href="//streeteasy.com/guides/renters-guide/how-much-rent-can-you-afford/" class="MainNav-popupColumnLink">
                  How Much Rent Can You Afford?
                </a>
              </li>
              <li class="MainNav-popupListItem">
                <a data-gtm-header-menu="Resources" href="//streeteasy.com/guides/renters-guide/how-to-find-a-roommate-in-nyc/" class="MainNav-popupColumnLink">
                  How to Find a Roommate
                </a>
              </li>
            </ul>
          </div>
          <div class="MainNav-popupColumn MainNav-popupColumn--adsShort">
            <a class="MainNav-popupColumnLink" data-gtm-header-menu="Resources" data-gtm-header-resource-ad="true" href="/guides/"><img srcset="//cdn-assets-s3.streeteasy.com/assets/menu_resources/resources@2x-0776ad734b8b4eb1dd5227b96e464ff26ff48d9d9c49d98e569d9b2751868d2e.png 2x" src="//cdn-assets-s3.streeteasy.com/assets/menu_resources/resources-1625adac14f2152e57d38aeef2777f910250b6a801f80bb4ee7a70ddc779e94d.png"></a>
          </div>
        </div>
      </div>
  </li>
  <li class="MainNav-listItem isTrackingMenuItem" data-type="Blog">
    <a class="MainNav-text" data-toggle="nav_popup" href="/blog/">Blog</a>
    <div class="MainNav-popup">
      <div class="Container">
        <div class="MainNav-popupColumn">
          <h6 class="MainNav-popupTitle">Browse</h6>
          <ul class="MainNav-popupList">
            <li class="MainNav-popupListItem">
              <a class="MainNav-popupColumnLink" data-gtm-header-menu="Blog" href="/blog/research/">Trends &amp; Data</a>
            </li>
            <li class="MainNav-popupListItem">
              <a class="MainNav-popupColumnLink" data-gtm-header-menu="Blog" href="/blog/good-deals/">Good Deals</a>
            </li>
            <li class="MainNav-popupListItem">
              <a class="MainNav-popupColumnLink" data-gtm-header-menu="Blog" href="/blog/nyc-living/">NYC Living</a>
            </li>
            <li class="MainNav-popupListItem">
              <a class="MainNav-popupColumnLink" data-gtm-header-menu="Blog" href="/blog/tips-advice/">Tips &amp; Advice</a>
            </li>
            <li class="MainNav-popupListItem">
              <a class="MainNav-popupColumnLink" data-gtm-header-menu="Blog" href="/guides/">NYC Guides</a>
            </li>
          </ul>
        </div>
        <div class="MainNav-popupColumn MainNav-popupColumn--lastLong">
            <h6 class="MainNav-popupTitle">The latest</h6>
            <ul class="MainNav-popupList MainNav-popupList--paddingBottom">
                <li class="MainNav-popupListItem">
                  <a class="MainNav-popupColumnLink" data-gtm-header-menu="Blog" href="https://streeteasy.com/blog/nyc-apartments-for-800k/">The 5 Best $800K Listings in NYC Right Now</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a class="MainNav-popupColumnLink" data-gtm-header-menu="Blog" href="https://streeteasy.com/blog/nyc-apartments-for-a-november-move-in/">10 Rentals Ready for a November 1 Move-In</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a class="MainNav-popupColumnLink" data-gtm-header-menu="Blog" href="https://streeteasy.com/blog/nyc-apartments-for-1500/">The Best $1,500 Rentals in NYC Right Now</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a class="MainNav-popupColumnLink" data-gtm-header-menu="Blog" href="https://streeteasy.com/blog/jackson-heights-1br-big-style-for-319k/">Big Style, Small Price: Jackson Heights 1BR Asks $319K</a>
                </li>
            </ul>

            <h6 class="MainNav-popupTitle">Most popular</h6>
            <ul class="MainNav-popupList">
                <li class="MainNav-popupListItem">
                  <a class="MainNav-popupColumnLink" data-gtm-header-menu="Blog" href="https://streeteasy.com/blog/tudor-city-1br-with-river-views-asks-2250/">Views for Days! A Sun-Soaked Tudor City 1BR for $2,250</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a class="MainNav-popupColumnLink" data-gtm-header-menu="Blog" href="https://streeteasy.com/blog/streeteasy-home-buyer-seminars/">Announcing the StreetEasy Home Buyer Seminars</a>
                </li>
                <li class="MainNav-popupListItem">
                  <a class="MainNav-popupColumnLink" data-gtm-header-menu="Blog" href="https://streeteasy.com/blog/nyc-apartments-with-major-price-cuts/">A $255K Discount? 6 NYC Homes With Huge Price Cuts</a>
                </li>
            </ul>
        </div>
        <div class="MainNav-popupColumn MainNav-popupColumn--adsShort">
          <a class="MainNav-popupColumnLink" data-gtm-header-menu="Resources" data-gtm-header-resource-ad="true" href="/blog/"><img srcset="//cdn-assets-s3.streeteasy.com/assets/menu_ads/blog_ad_unit@2x-249be667feb4730b3697543522dd9fa59f27f62aecd2387160de1ba4a025350e.png 2x" src="//cdn-assets-s3.streeteasy.com/assets/menu_ads/blog_ad_unit-e267e05b135b48a1d493c80d072756a6ccc63d5b2bfc11bb381bd8f9a851eb2d.png"></a>
        </div>
      </div>
    </div>
  </li>
</ul>

  <div class="MainNav-search">
    <form class="Search" onsubmit="SE.analytics.submitTextSearch(this)" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="✓">
      <input type="text" name="search" placeholder="e.g. address, building, agent" class="Search-input DefaultField">
      <button name="commit" type="submit" value="" class="fa fa-search Search-button"></button>
</form>  </div>

      </div>
    </div>

  <div class="MainNav MainNav--mWeb jsMenuMobile" id="navbar_block">
    <div id="navbar_menu" class="MainNav-search">
      <form class="Search Search--mWebMenu" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="✓">
        <input type="text" name="search" id="search" placeholder="Search" class="Search-input Search-input--big DefaultField">
        <button name="commit" type="submit" value="" class="Search-button Search-button--icon Search-button--big"></button>
</form>
      <ul class="MainNav-mainMenu">
          <li class="MainNav-mainMenuItem">
            <a class="MainNav-textMobile MainNav-textMobile--big" href="/rentals">Rent</a>
          </li>
          <li class="MainNav-mainMenuItem">
            <a class="MainNav-textMobile MainNav-textMobile--big" href="/">Buy</a>
          </li>
          <li class="MainNav-mainMenuItem MainNav-mainMenuItem--new">
            <span aria-hidden="true" class="MainNav-accent MainNav-accent--new" title="New"></span>
            <a class="MainNav-textMobile MainNav-textMobile--big" aria-label="Sell Your Home" href="/sell-your-home">Sell</a>
          </li>
        <li class="MainNav-mainMenuItem">
          <a class="MainNav-textMobile MainNav-textMobile--big" href="/nyc/newdevs">Buildings</a>
        </li>
        <li class="MainNav-mainMenuItem">
          <span class="MainNav-textMobile MainNav-textMobile--big isWithArrow" data-toggle="submenu">
  Resources
</span>
<div class="MainNav-subMenuPopup">
  <div class="MainNav-subMenuHeader">Main Menu</div>
  <h6 class="MainNav-subMenuTitle">Browse</h6>
  <ul class="MainNav-subMenuList">
    <li>
      <a href="/blog/" class="MainNav-textMobile MainNav-textMobile--small">
        StreetEasy Blog
      </a>
    </li>
  </ul>
  <h6 class="MainNav-subMenuTitle">Guides</h6>
  <ul class="MainNav-subMenuList">
    <li>
      <a class="MainNav-textMobile MainNav-textMobile--small" href="/guides/">NYC Real Estate Guides</a>
    </li>
    <li>
      <a class="MainNav-textMobile MainNav-textMobile--small" href="/neighborhoods">Neighborhood Guides</a>
    </li>
    <li>
      <a class="MainNav-textMobile MainNav-textMobile--small" href="/guides/moving-nyc/">Moving to NYC Guide</a>
    </li>
  </ul>
  <h6 class="MainNav-subMenuTitle">Tools</h6>
  <ul class="MainNav-subMenuList">
    <li>
      <a class="MainNav-textMobile MainNav-textMobile--small" href="/blog/market-reports">Market Reports</a>
    </li>
      <li>
          <a onclick="window.gon.state.analyticsData = {'source':'comparables_report'};window.gon.state.triggerScenario('EmailCapture', { redirectTo: '/my/comparables' });" class="MainNav-textMobile MainNav-textMobile--small" data-modal-class="modal-signin" data-gtm-login-required="true" data-gtm-rendered-from="site_nav" data-gtm-origin="comparables_report" href="#">Comparables Reports</a>
      </li>
    <li>
      <a class="MainNav-textMobile MainNav-textMobile--small" href="/talk">StreetEasy Forums</a>
    </li>
    <li>
      <a class="MainNav-textMobile MainNav-textMobile--small" href="//streeteasy.com/agent-resources">Agent Resource Center</a>
    </li>
    <li>
      <a href="https://streeteasy.com/blog/data-dashboard/" class="MainNav-textMobile MainNav-textMobile--small">
        Data Dashboard
      </a>
    </li>
  </ul>
</div>

        </li>
      </ul>
      <ul class="MainNav-signinMenu" id="singin-menu">
          <li>
            <a class="MainNav-textMobile MainNav-textMobile--signIn jsGoogleOneTap" onclick="window.gon.state.analyticsData = {'source':'nav'}; window.gon.state.triggerScenario('EmailCapture'); return false;" data-toggle="menu" href="#">Sign In / Register</a>
          </li>
      </ul>

    </div>
  </div>

            </div>
          </header>
          <div id="site-content" class="SiteBlock-content ">


            <div id="content">






                <div id="covid-banner" class="Flash flash_notice flexBox-row flexBox-alignMiddle ">
  <div class="Container Flash-wrapper" id="">
    <div class="Flash-content" style="align-items: center; position: relative;">
      <div style="">
      In-person home showings are now permitted in NYC. Read
        <a target="_blank" rel="noopener noreferrer" href="https://streeteasy.com/agent-resources/covid-19-nyc-real-estate/nyc-phase-2-guide-for-real-estate-agents"> state mandates for safe showings</a>
        and the
        <a target="_blank" rel="noopener noreferrer" href="https://streeteasy.com/agent-resources/covid-19-nyc-real-estate/streeteasy-and-covid-19-updates/"> latest StreetEasy policies</a>.
      </div>
    </div>
  </div>
</div>

<script type="text/javascript">
  // This is needed to prevent Chrome from scrolling to the previous
  // scroll position before the page refreshes
  history.scrollRestoration = "manual";
  (function($){
    $(".CloseX").click(function(){
      $('#covid-banner').hide();
    })
  })(jQuery);
</script>




              <main class="Home">
                <div id="header_print_info" class="only-print">
                  Printed from StreetEasy.com at 12:20 AM, Oct 18 2020
                </div>






<section class="Home-search Home-section">
  <div class="u-width--984 u-centered">
    <h1 class="Title Title--secondarySmCaps u-color-koalaGrey u-noMargin">
      New York City Real Estate
    </h1>

    <div class="Home-searchTypeContainer">

          <span class="Home-searchType Title Title--primaryMd isCurrent">Sales</span>
          <a class="Home-searchType Title Title--primaryMd" href="/rentals">Rentals</a>

    </div>

    <!-- Search -->

    <form class="u-noMargin criteria large" data-current-site="nyc" data-search-key="sales" data-form-with-analytics-criteria="true" data-criteria-url="/nyc/sales/search_criteria" se:behavior="form_validatable_on_coordinate" se:coordinator="criteria_expander" action="/nyc/process/sales/update_search" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="wslp8xtP2wLbozUqnK6vxZD/VsUd2bvpvJobzobF3NgQiiZnDVdOzbDPbCYmKjpNeOMU72EXzGe+vvdRT1a8Tw==">

      <div class="Home-searchFieldsContainer">
        <div class="Home-searchFields">

    <div class="Home-searchAreaWrapper">
      <div class="Home-searchAreaEnhanced Home-searchField">

  <div class="SearchAreasDropdown jsSearchAreaDropdown">
    <div class="SearchAreasDropdown-textInputContainer jsSearchAreaInputContainer">
      <div class="SearchAreasDropdown-selectedAreas jsSearchAreaSelectedAreas">
        <input class="SearchAreasDropdown-textInput jsSearchAreaInput" type="text" placeholder="Neighborhood, Address, Building, Keyword" autocomplete="off">
      </div>
    </div>

    <div class="SearchAreasDropdown-areasListContainer">
      <ul class="Collapsible jsCollapsible">
  <li class="jsTrigger">
    <div class="Collapsible-checkbox jsSearchAreaItem jsSearchAllItem">
      <label class="Collapsible-checkboxLabel" for="area-1">
        <input type="checkbox" name="area[]" id="area-1" value="1" class="Checkbox jsSearchAreaCheckbox jsCheckAll" data-area="1" data-area-name="All NYC and NJ">
        Search All (NYC and NJ&nbsp;<span class="u-color-brightBlue u-italic">New!</span>)
      </label>
    </div>
  </li>
    <li class="jsTrigger">
      <div class="Collapsible-trigger jsCollapsibleTrigger jsSearchAreaItem" data-collapsible-trigger-area="Manhattan">
          Manhattan
        <span class="Collapsible-triggerIcon">
          <i class="fa fa-angle-down u-text--bold"></i>
        </span>
      </div>
        <div class="Collapsible-body">
          <ul>
            <li class="jsCollapsibleChild">
              <div class="Collapsible-checkbox jsSearchAreaItem">
                <label class="Collapsible-checkboxLabel u-text--bold" for="area-100">
                  <input type="checkbox" name="area[]" id="area-100" value="100" class="Checkbox jsSearchAreaCheckbox" data-area="100" data-area-name="All Manhattan" data-children-ids="102,119,139,144,135,101">
                  All Manhattan
                </label>
              </div>
            </li>
              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level1">
    <label class="Collapsible-checkboxLabel" for="area-102">
      <input type="checkbox" name="area[]" id="area-102" value="102" class="Checkbox jsSearchAreaCheckbox" data-area="102" data-area-name="All Downtown" data-parent-id="100" data-children-ids="112,115,110,103,117,104,158,113,116,108,109,162,107,106,105,157">
      All Downtown
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-112">
      <input type="checkbox" name="area[]" id="area-112" value="112" class="Checkbox jsSearchAreaCheckbox" data-area="112" data-area-name="Battery Park City" data-parent-id="102" data-children-ids="">
      Battery Park City
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-115">
      <input type="checkbox" name="area[]" id="area-115" value="115" class="Checkbox jsSearchAreaCheckbox" data-area="115" data-area-name="Chelsea" data-always-checked-with="146" data-parent-id="102" data-children-ids="163">
      Chelsea
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-163">
      <input type="checkbox" name="area[]" id="area-163" value="163" class="Checkbox jsSearchAreaCheckbox" data-area="163" data-area-name="West Chelsea" data-always-checked-with="146" data-parent-id="115" data-children-ids="">
      West Chelsea
    </label>
  </div>

</li>


    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-110">
      <input type="checkbox" name="area[]" id="area-110" value="110" class="Checkbox jsSearchAreaCheckbox" data-area="110" data-area-name="Chinatown" data-parent-id="102" data-children-ids="">
      Chinatown
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-103">
      <input type="checkbox" name="area[]" id="area-103" value="103" class="Checkbox jsSearchAreaCheckbox" data-area="103" data-area-name="Civic Center" data-parent-id="102" data-children-ids="">
      Civic Center
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-117">
      <input type="checkbox" name="area[]" id="area-117" value="117" class="Checkbox jsSearchAreaCheckbox" data-area="117" data-area-name="East Village" data-parent-id="102" data-children-ids="">
      East Village
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-104">
      <input type="checkbox" name="area[]" id="area-104" value="104" class="Checkbox jsSearchAreaCheckbox" data-area="104" data-area-name="Financial District" data-parent-id="102" data-children-ids="114">
      Financial District
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-114">
      <input type="checkbox" name="area[]" id="area-114" value="114" class="Checkbox jsSearchAreaCheckbox" data-area="114" data-area-name="Fulton/Seaport" data-parent-id="104" data-children-ids="">
      Fulton/Seaport
    </label>
  </div>

</li>


    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-158">
      <input type="checkbox" name="area[]" id="area-158" value="158" class="Checkbox jsSearchAreaCheckbox" data-area="158" data-area-name="Flatiron" data-parent-id="102" data-children-ids="159">
      Flatiron
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-159">
      <input type="checkbox" name="area[]" id="area-159" value="159" class="Checkbox jsSearchAreaCheckbox" data-area="159" data-area-name="NoMad" data-parent-id="158" data-children-ids="">
      NoMad
    </label>
  </div>

</li>


    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-113">
      <input type="checkbox" name="area[]" id="area-113" value="113" class="Checkbox jsSearchAreaCheckbox" data-area="113" data-area-name="Gramercy Park" data-parent-id="102" data-children-ids="">
      Gramercy Park
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-116">
      <input type="checkbox" name="area[]" id="area-116" value="116" class="Checkbox jsSearchAreaCheckbox" data-area="116" data-area-name="Greenwich Village" data-parent-id="102" data-children-ids="118">
      Greenwich Village
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-118">
      <input type="checkbox" name="area[]" id="area-118" value="118" class="Checkbox jsSearchAreaCheckbox" data-area="118" data-area-name="Noho" data-parent-id="116" data-children-ids="">
      Noho
    </label>
  </div>

</li>


    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-108">
      <input type="checkbox" name="area[]" id="area-108" value="108" class="Checkbox jsSearchAreaCheckbox" data-area="108" data-area-name="Little Italy" data-parent-id="102" data-children-ids="">
      Little Italy
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-109">
      <input type="checkbox" name="area[]" id="area-109" value="109" class="Checkbox jsSearchAreaCheckbox" data-area="109" data-area-name="Lower East Side" data-parent-id="102" data-children-ids="111">
      Lower East Side
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-111">
      <input type="checkbox" name="area[]" id="area-111" value="111" class="Checkbox jsSearchAreaCheckbox" data-area="111" data-area-name="Two Bridges" data-parent-id="109" data-children-ids="">
      Two Bridges
    </label>
  </div>

</li>


    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-162">
      <input type="checkbox" name="area[]" id="area-162" value="162" class="Checkbox jsSearchAreaCheckbox" data-area="162" data-area-name="Nolita" data-parent-id="102" data-children-ids="">
      Nolita
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-107">
      <input type="checkbox" name="area[]" id="area-107" value="107" class="Checkbox jsSearchAreaCheckbox" data-area="107" data-area-name="Soho" data-parent-id="102" data-children-ids="166">
      Soho
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-166">
      <input type="checkbox" name="area[]" id="area-166" value="166" class="Checkbox jsSearchAreaCheckbox" data-area="166" data-area-name="Hudson Square" data-parent-id="107" data-children-ids="">
      Hudson Square
    </label>
  </div>

</li>


    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-106">
      <input type="checkbox" name="area[]" id="area-106" value="106" class="Checkbox jsSearchAreaCheckbox" data-area="106" data-area-name="Stuyvesant Town/PCV" data-parent-id="102" data-children-ids="">
      Stuyvesant Town/PCV
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-105">
      <input type="checkbox" name="area[]" id="area-105" value="105" class="Checkbox jsSearchAreaCheckbox" data-area="105" data-area-name="Tribeca" data-parent-id="102" data-children-ids="">
      Tribeca
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-157">
      <input type="checkbox" name="area[]" id="area-157" value="157" class="Checkbox jsSearchAreaCheckbox" data-area="157" data-area-name="West Village" data-parent-id="102" data-children-ids="">
      West Village
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level1">
    <label class="Collapsible-checkboxLabel" for="area-119">
      <input type="checkbox" name="area[]" id="area-119" value="119" class="Checkbox jsSearchAreaCheckbox" data-area="119" data-area-name="All Midtown" data-parent-id="100" data-children-ids="121,120,123,122,124">
      All Midtown
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-121">
      <input type="checkbox" name="area[]" id="area-121" value="121" class="Checkbox jsSearchAreaCheckbox" data-area="121" data-area-name="Central Park South" data-parent-id="119" data-children-ids="">
      Central Park South
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-120">
      <input type="checkbox" name="area[]" id="area-120" value="120" class="Checkbox jsSearchAreaCheckbox" data-area="120" data-area-name="Midtown" data-parent-id="119" data-children-ids="">
      Midtown
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-123">
      <input type="checkbox" name="area[]" id="area-123" value="123" class="Checkbox jsSearchAreaCheckbox" data-area="123" data-area-name="Midtown East" data-parent-id="119" data-children-ids="133,130,131,132">
      Midtown East
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-133">
      <input type="checkbox" name="area[]" id="area-133" value="133" class="Checkbox jsSearchAreaCheckbox" data-area="133" data-area-name="Kips Bay" data-parent-id="123" data-children-ids="">
      Kips Bay
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-130">
      <input type="checkbox" name="area[]" id="area-130" value="130" class="Checkbox jsSearchAreaCheckbox" data-area="130" data-area-name="Murray Hill" data-parent-id="123" data-children-ids="">
      Murray Hill
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-131">
      <input type="checkbox" name="area[]" id="area-131" value="131" class="Checkbox jsSearchAreaCheckbox" data-area="131" data-area-name="Sutton Place" data-parent-id="123" data-children-ids="">
      Sutton Place
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-132">
      <input type="checkbox" name="area[]" id="area-132" value="132" class="Checkbox jsSearchAreaCheckbox" data-area="132" data-area-name="Turtle Bay" data-parent-id="123" data-children-ids="134">
      Turtle Bay
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level4">
    <label class="Collapsible-checkboxLabel" for="area-134">
      <input type="checkbox" name="area[]" id="area-134" value="134" class="Checkbox jsSearchAreaCheckbox" data-area="134" data-area-name="Beekman" data-parent-id="132" data-children-ids="">
      Beekman
    </label>
  </div>

</li>



    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-122">
      <input type="checkbox" name="area[]" id="area-122" value="122" class="Checkbox jsSearchAreaCheckbox" data-area="122" data-area-name="Midtown South" data-parent-id="119" data-children-ids="">
      Midtown South
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-124">
      <input type="checkbox" name="area[]" id="area-124" value="124" class="Checkbox jsSearchAreaCheckbox" data-area="124" data-area-name="Midtown West" data-parent-id="119" data-children-ids="152,146">
      Midtown West
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-152">
      <input type="checkbox" name="area[]" id="area-152" value="152" class="Checkbox jsSearchAreaCheckbox" data-area="152" data-area-name="Hell's Kitchen" data-parent-id="124" data-children-ids="">
      Hell's Kitchen
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-146">
      <input type="checkbox" name="area[]" id="area-146" value="146" class="Checkbox jsSearchAreaCheckbox" data-area="146" data-area-name="Hudson Yards" data-parent-id="124" data-children-ids="">
      Hudson Yards
    </label>
  </div>

</li>



              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level1">
    <label class="Collapsible-checkboxLabel" for="area-139">
      <input type="checkbox" name="area[]" id="area-139" value="139" class="Checkbox jsSearchAreaCheckbox" data-area="139" data-area-name="All Upper East Side" data-parent-id="100" data-children-ids="140">
      All Upper East Side
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-140">
      <input type="checkbox" name="area[]" id="area-140" value="140" class="Checkbox jsSearchAreaCheckbox" data-area="140" data-area-name="Upper East Side" data-parent-id="139" data-children-ids="143,141,164,142">
      Upper East Side
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-143">
      <input type="checkbox" name="area[]" id="area-143" value="143" class="Checkbox jsSearchAreaCheckbox" data-area="143" data-area-name="Carnegie Hill" data-parent-id="140" data-children-ids="">
      Carnegie Hill
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-141">
      <input type="checkbox" name="area[]" id="area-141" value="141" class="Checkbox jsSearchAreaCheckbox" data-area="141" data-area-name="Lenox Hill" data-parent-id="140" data-children-ids="">
      Lenox Hill
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-164">
      <input type="checkbox" name="area[]" id="area-164" value="164" class="Checkbox jsSearchAreaCheckbox" data-area="164" data-area-name="Upper Carnegie Hill" data-parent-id="140" data-children-ids="">
      Upper Carnegie Hill
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-142">
      <input type="checkbox" name="area[]" id="area-142" value="142" class="Checkbox jsSearchAreaCheckbox" data-area="142" data-area-name="Yorkville" data-parent-id="140" data-children-ids="">
      Yorkville
    </label>
  </div>

</li>



              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level1">
    <label class="Collapsible-checkboxLabel" for="area-144">
      <input type="checkbox" name="area[]" id="area-144" value="144" class="Checkbox jsSearchAreaCheckbox" data-area="144" data-area-name="All Upper Manhattan" data-parent-id="100" data-children-ids="154,155,148,150,226,147,149,153">
      All Upper Manhattan
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-154">
      <input type="checkbox" name="area[]" id="area-154" value="154" class="Checkbox jsSearchAreaCheckbox" data-area="154" data-area-name="Central Harlem" data-parent-id="144" data-children-ids="165">
      Central Harlem
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-165">
      <input type="checkbox" name="area[]" id="area-165" value="165" class="Checkbox jsSearchAreaCheckbox" data-area="165" data-area-name="South Harlem" data-parent-id="154" data-children-ids="">
      South Harlem
    </label>
  </div>

</li>


    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-155">
      <input type="checkbox" name="area[]" id="area-155" value="155" class="Checkbox jsSearchAreaCheckbox" data-area="155" data-area-name="East Harlem" data-parent-id="144" data-children-ids="">
      East Harlem
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-148">
      <input type="checkbox" name="area[]" id="area-148" value="148" class="Checkbox jsSearchAreaCheckbox" data-area="148" data-area-name="Hamilton Heights" data-parent-id="144" data-children-ids="">
      Hamilton Heights
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-150">
      <input type="checkbox" name="area[]" id="area-150" value="150" class="Checkbox jsSearchAreaCheckbox" data-area="150" data-area-name="Inwood" data-parent-id="144" data-children-ids="">
      Inwood
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-226">
      <input type="checkbox" name="area[]" id="area-226" value="226" class="Checkbox jsSearchAreaCheckbox" data-area="226" data-area-name="Marble Hill" data-parent-id="144" data-children-ids="">
      Marble Hill
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-147">
      <input type="checkbox" name="area[]" id="area-147" value="147" class="Checkbox jsSearchAreaCheckbox" data-area="147" data-area-name="Morningside Heights" data-parent-id="144" data-children-ids="">
      Morningside Heights
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-149">
      <input type="checkbox" name="area[]" id="area-149" value="149" class="Checkbox jsSearchAreaCheckbox" data-area="149" data-area-name="Washington Heights" data-parent-id="144" data-children-ids="151,145">
      Washington Heights
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-151">
      <input type="checkbox" name="area[]" id="area-151" value="151" class="Checkbox jsSearchAreaCheckbox" data-area="151" data-area-name="Fort George" data-parent-id="149" data-children-ids="">
      Fort George
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-145">
      <input type="checkbox" name="area[]" id="area-145" value="145" class="Checkbox jsSearchAreaCheckbox" data-area="145" data-area-name="Hudson Heights" data-parent-id="149" data-children-ids="">
      Hudson Heights
    </label>
  </div>

</li>


    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-153">
      <input type="checkbox" name="area[]" id="area-153" value="153" class="Checkbox jsSearchAreaCheckbox" data-area="153" data-area-name="West Harlem" data-parent-id="144" data-children-ids="161">
      West Harlem
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-161">
      <input type="checkbox" name="area[]" id="area-161" value="161" class="Checkbox jsSearchAreaCheckbox" data-area="161" data-area-name="Manhattanville" data-parent-id="153" data-children-ids="">
      Manhattanville
    </label>
  </div>

</li>



              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level1">
    <label class="Collapsible-checkboxLabel" for="area-135">
      <input type="checkbox" name="area[]" id="area-135" value="135" class="Checkbox jsSearchAreaCheckbox" data-area="135" data-area-name="All Upper West Side" data-parent-id="100" data-children-ids="137">
      All Upper West Side
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-137">
      <input type="checkbox" name="area[]" id="area-137" value="137" class="Checkbox jsSearchAreaCheckbox" data-area="137" data-area-name="Upper West Side" data-parent-id="135" data-children-ids="136,138">
      Upper West Side
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-136">
      <input type="checkbox" name="area[]" id="area-136" value="136" class="Checkbox jsSearchAreaCheckbox" data-area="136" data-area-name="Lincoln Square" data-parent-id="137" data-children-ids="">
      Lincoln Square
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-138">
      <input type="checkbox" name="area[]" id="area-138" value="138" class="Checkbox jsSearchAreaCheckbox" data-area="138" data-area-name="Manhattan Valley" data-parent-id="137" data-children-ids="">
      Manhattan Valley
    </label>
  </div>

</li>



              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level1">
    <label class="Collapsible-checkboxLabel" for="area-101">
      <input type="checkbox" name="area[]" id="area-101" value="101" class="Checkbox jsSearchAreaCheckbox" data-area="101" data-area-name="Roosevelt Island" data-parent-id="100" data-children-ids="">
      Roosevelt Island
    </label>
  </div>

</li>

          </ul>
        </div>
    </li>
    <li class="jsTrigger">
      <div class="Collapsible-trigger jsCollapsibleTrigger jsSearchAreaItem" data-collapsible-trigger-area="Brooklyn">
          Brooklyn
        <span class="Collapsible-triggerIcon">
          <i class="fa fa-angle-down u-text--bold"></i>
        </span>
      </div>
        <div class="Collapsible-body">
          <ul>
            <li class="jsCollapsibleChild">
              <div class="Collapsible-checkbox jsSearchAreaItem">
                <label class="Collapsible-checkboxLabel u-text--bold" for="area-300">
                  <input type="checkbox" name="area[]" id="area-300" value="300" class="Checkbox jsSearchAreaCheckbox" data-area="300" data-area-name="All Brooklyn" data-children-ids="336,331,310,334,363,306,338,342,305,354,313,359,321,364,322,328,341,325,307,343,303,332,358,314,346,360,304,370,320,337,301,367,340,350,361,348,362,339,365,319,326,329,355,318,345,349,323,302,324">
                  All Brooklyn
                </label>
              </div>
            </li>
              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-336">
      <input type="checkbox" name="area[]" id="area-336" value="336" class="Checkbox jsSearchAreaCheckbox" data-area="336" data-area-name="Bath Beach" data-parent-id="300" data-children-ids="">
      Bath Beach
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-331">
      <input type="checkbox" name="area[]" id="area-331" value="331" class="Checkbox jsSearchAreaCheckbox" data-area="331" data-area-name="Bay Ridge" data-parent-id="300" data-children-ids="333">
      Bay Ridge
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-333">
      <input type="checkbox" name="area[]" id="area-333" value="333" class="Checkbox jsSearchAreaCheckbox" data-area="333" data-area-name="Fort Hamilton" data-parent-id="331" data-children-ids="">
      Fort Hamilton
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-310">
      <input type="checkbox" name="area[]" id="area-310" value="310" class="Checkbox jsSearchAreaCheckbox" data-area="310" data-area-name="Bedford-Stuyvesant" data-parent-id="300" data-children-ids="353,312">
      Bedford-Stuyvesant
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-353">
      <input type="checkbox" name="area[]" id="area-353" value="353" class="Checkbox jsSearchAreaCheckbox" data-area="353" data-area-name="Ocean Hill" data-parent-id="310" data-children-ids="">
      Ocean Hill
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-312">
      <input type="checkbox" name="area[]" id="area-312" value="312" class="Checkbox jsSearchAreaCheckbox" data-area="312" data-area-name="Stuyvesant Heights" data-parent-id="310" data-children-ids="">
      Stuyvesant Heights
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-334">
      <input type="checkbox" name="area[]" id="area-334" value="334" class="Checkbox jsSearchAreaCheckbox" data-area="334" data-area-name="Bensonhurst" data-parent-id="300" data-children-ids="">
      Bensonhurst
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-363">
      <input type="checkbox" name="area[]" id="area-363" value="363" class="Checkbox jsSearchAreaCheckbox" data-area="363" data-area-name="Bergen Beach" data-parent-id="300" data-children-ids="">
      Bergen Beach
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-306">
      <input type="checkbox" name="area[]" id="area-306" value="306" class="Checkbox jsSearchAreaCheckbox" data-area="306" data-area-name="Boerum Hill" data-parent-id="300" data-children-ids="">
      Boerum Hill
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-338">
      <input type="checkbox" name="area[]" id="area-338" value="338" class="Checkbox jsSearchAreaCheckbox" data-area="338" data-area-name="Borough Park" data-parent-id="300" data-children-ids="335">
      Borough Park
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-335">
      <input type="checkbox" name="area[]" id="area-335" value="335" class="Checkbox jsSearchAreaCheckbox" data-area="335" data-area-name="Mapleton" data-parent-id="338" data-children-ids="">
      Mapleton
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-342">
      <input type="checkbox" name="area[]" id="area-342" value="342" class="Checkbox jsSearchAreaCheckbox" data-area="342" data-area-name="Brighton Beach" data-parent-id="300" data-children-ids="">
      Brighton Beach
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-305">
      <input type="checkbox" name="area[]" id="area-305" value="305" class="Checkbox jsSearchAreaCheckbox" data-area="305" data-area-name="Brooklyn Heights" data-parent-id="300" data-children-ids="">
      Brooklyn Heights
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-354">
      <input type="checkbox" name="area[]" id="area-354" value="354" class="Checkbox jsSearchAreaCheckbox" data-area="354" data-area-name="Brownsville" data-parent-id="300" data-children-ids="">
      Brownsville
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-313">
      <input type="checkbox" name="area[]" id="area-313" value="313" class="Checkbox jsSearchAreaCheckbox" data-area="313" data-area-name="Bushwick" data-parent-id="300" data-children-ids="">
      Bushwick
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-359">
      <input type="checkbox" name="area[]" id="area-359" value="359" class="Checkbox jsSearchAreaCheckbox" data-area="359" data-area-name="Canarsie" data-parent-id="300" data-children-ids="">
      Canarsie
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-321">
      <input type="checkbox" name="area[]" id="area-321" value="321" class="Checkbox jsSearchAreaCheckbox" data-area="321" data-area-name="Carroll Gardens" data-parent-id="300" data-children-ids="">
      Carroll Gardens
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-364">
      <input type="checkbox" name="area[]" id="area-364" value="364" class="Checkbox jsSearchAreaCheckbox" data-area="364" data-area-name="Clinton Hill" data-parent-id="300" data-children-ids="">
      Clinton Hill
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-322">
      <input type="checkbox" name="area[]" id="area-322" value="322" class="Checkbox jsSearchAreaCheckbox" data-area="322" data-area-name="Cobble Hill" data-parent-id="300" data-children-ids="">
      Cobble Hill
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-328">
      <input type="checkbox" name="area[]" id="area-328" value="328" class="Checkbox jsSearchAreaCheckbox" data-area="328" data-area-name="Columbia St Waterfront District" data-parent-id="300" data-children-ids="">
      Columbia St Waterfront District
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-341">
      <input type="checkbox" name="area[]" id="area-341" value="341" class="Checkbox jsSearchAreaCheckbox" data-area="341" data-area-name="Coney Island" data-parent-id="300" data-children-ids="">
      Coney Island
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-325">
      <input type="checkbox" name="area[]" id="area-325" value="325" class="Checkbox jsSearchAreaCheckbox" data-area="325" data-area-name="Crown Heights" data-parent-id="300" data-children-ids="327">
      Crown Heights
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-327">
      <input type="checkbox" name="area[]" id="area-327" value="327" class="Checkbox jsSearchAreaCheckbox" data-area="327" data-area-name="Weeksville" data-parent-id="325" data-children-ids="">
      Weeksville
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-307">
      <input type="checkbox" name="area[]" id="area-307" value="307" class="Checkbox jsSearchAreaCheckbox" data-area="307" data-area-name="DUMBO" data-parent-id="300" data-children-ids="308">
      DUMBO
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-308">
      <input type="checkbox" name="area[]" id="area-308" value="308" class="Checkbox jsSearchAreaCheckbox" data-area="308" data-area-name="Vinegar Hill" data-parent-id="307" data-children-ids="">
      Vinegar Hill
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-343">
      <input type="checkbox" name="area[]" id="area-343" value="343" class="Checkbox jsSearchAreaCheckbox" data-area="343" data-area-name="Ditmas Park" data-parent-id="300" data-children-ids="352">
      Ditmas Park
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-352">
      <input type="checkbox" name="area[]" id="area-352" value="352" class="Checkbox jsSearchAreaCheckbox" data-area="352" data-area-name="Fiske Terrace" data-parent-id="343" data-children-ids="">
      Fiske Terrace
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-303">
      <input type="checkbox" name="area[]" id="area-303" value="303" class="Checkbox jsSearchAreaCheckbox" data-area="303" data-area-name="Downtown Brooklyn" data-parent-id="300" data-children-ids="">
      Downtown Brooklyn
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-332">
      <input type="checkbox" name="area[]" id="area-332" value="332" class="Checkbox jsSearchAreaCheckbox" data-area="332" data-area-name="Dyker Heights" data-parent-id="300" data-children-ids="">
      Dyker Heights
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-358">
      <input type="checkbox" name="area[]" id="area-358" value="358" class="Checkbox jsSearchAreaCheckbox" data-area="358" data-area-name="East Flatbush" data-parent-id="300" data-children-ids="309,330">
      East Flatbush
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-309">
      <input type="checkbox" name="area[]" id="area-309" value="309" class="Checkbox jsSearchAreaCheckbox" data-area="309" data-area-name="Farragut" data-parent-id="358" data-children-ids="">
      Farragut
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-330">
      <input type="checkbox" name="area[]" id="area-330" value="330" class="Checkbox jsSearchAreaCheckbox" data-area="330" data-area-name="Wingate" data-parent-id="358" data-children-ids="">
      Wingate
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-314">
      <input type="checkbox" name="area[]" id="area-314" value="314" class="Checkbox jsSearchAreaCheckbox" data-area="314" data-area-name="East New York" data-parent-id="300" data-children-ids="316,315,317">
      East New York
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-316">
      <input type="checkbox" name="area[]" id="area-316" value="316" class="Checkbox jsSearchAreaCheckbox" data-area="316" data-area-name="City Line" data-parent-id="314" data-children-ids="">
      City Line
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-315">
      <input type="checkbox" name="area[]" id="area-315" value="315" class="Checkbox jsSearchAreaCheckbox" data-area="315" data-area-name="New Lots" data-parent-id="314" data-children-ids="">
      New Lots
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-317">
      <input type="checkbox" name="area[]" id="area-317" value="317" class="Checkbox jsSearchAreaCheckbox" data-area="317" data-area-name="Starrett City" data-parent-id="314" data-children-ids="">
      Starrett City
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-346">
      <input type="checkbox" name="area[]" id="area-346" value="346" class="Checkbox jsSearchAreaCheckbox" data-area="346" data-area-name="Flatbush" data-parent-id="300" data-children-ids="">
      Flatbush
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-360">
      <input type="checkbox" name="area[]" id="area-360" value="360" class="Checkbox jsSearchAreaCheckbox" data-area="360" data-area-name="Flatlands" data-parent-id="300" data-children-ids="">
      Flatlands
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-304">
      <input type="checkbox" name="area[]" id="area-304" value="304" class="Checkbox jsSearchAreaCheckbox" data-area="304" data-area-name="Fort Greene" data-parent-id="300" data-children-ids="">
      Fort Greene
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-370">
      <input type="checkbox" name="area[]" id="area-370" value="370" class="Checkbox jsSearchAreaCheckbox" data-area="370" data-area-name="Gerritsen Beach" data-parent-id="300" data-children-ids="">
      Gerritsen Beach
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-320">
      <input type="checkbox" name="area[]" id="area-320" value="320" class="Checkbox jsSearchAreaCheckbox" data-area="320" data-area-name="Gowanus" data-parent-id="300" data-children-ids="">
      Gowanus
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-337">
      <input type="checkbox" name="area[]" id="area-337" value="337" class="Checkbox jsSearchAreaCheckbox" data-area="337" data-area-name="Gravesend" data-parent-id="300" data-children-ids="">
      Gravesend
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-301">
      <input type="checkbox" name="area[]" id="area-301" value="301" class="Checkbox jsSearchAreaCheckbox" data-area="301" data-area-name="Greenpoint" data-parent-id="300" data-children-ids="">
      Greenpoint
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-367">
      <input type="checkbox" name="area[]" id="area-367" value="367" class="Checkbox jsSearchAreaCheckbox" data-area="367" data-area-name="Greenwood" data-parent-id="300" data-children-ids="">
      Greenwood
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-340">
      <input type="checkbox" name="area[]" id="area-340" value="340" class="Checkbox jsSearchAreaCheckbox" data-area="340" data-area-name="Kensington" data-parent-id="300" data-children-ids="">
      Kensington
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-350">
      <input type="checkbox" name="area[]" id="area-350" value="350" class="Checkbox jsSearchAreaCheckbox" data-area="350" data-area-name="Manhattan Beach" data-parent-id="300" data-children-ids="">
      Manhattan Beach
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-361">
      <input type="checkbox" name="area[]" id="area-361" value="361" class="Checkbox jsSearchAreaCheckbox" data-area="361" data-area-name="Marine Park" data-parent-id="300" data-children-ids="">
      Marine Park
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-348">
      <input type="checkbox" name="area[]" id="area-348" value="348" class="Checkbox jsSearchAreaCheckbox" data-area="348" data-area-name="Midwood" data-parent-id="300" data-children-ids="">
      Midwood
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-362">
      <input type="checkbox" name="area[]" id="area-362" value="362" class="Checkbox jsSearchAreaCheckbox" data-area="362" data-area-name="Mill Basin" data-parent-id="300" data-children-ids="">
      Mill Basin
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-339">
      <input type="checkbox" name="area[]" id="area-339" value="339" class="Checkbox jsSearchAreaCheckbox" data-area="339" data-area-name="Ocean Parkway" data-parent-id="300" data-children-ids="">
      Ocean Parkway
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-365">
      <input type="checkbox" name="area[]" id="area-365" value="365" class="Checkbox jsSearchAreaCheckbox" data-area="365" data-area-name="Old Mill Basin" data-parent-id="300" data-children-ids="">
      Old Mill Basin
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-319">
      <input type="checkbox" name="area[]" id="area-319" value="319" class="Checkbox jsSearchAreaCheckbox" data-area="319" data-area-name="Park Slope" data-parent-id="300" data-children-ids="">
      Park Slope
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-326">
      <input type="checkbox" name="area[]" id="area-326" value="326" class="Checkbox jsSearchAreaCheckbox" data-area="326" data-area-name="Prospect Heights" data-parent-id="300" data-children-ids="">
      Prospect Heights
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-329">
      <input type="checkbox" name="area[]" id="area-329" value="329" class="Checkbox jsSearchAreaCheckbox" data-area="329" data-area-name="Prospect Lefferts Gardens" data-parent-id="300" data-children-ids="">
      Prospect Lefferts Gardens
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-355">
      <input type="checkbox" name="area[]" id="area-355" value="355" class="Checkbox jsSearchAreaCheckbox" data-area="355" data-area-name="Prospect Park South" data-parent-id="300" data-children-ids="">
      Prospect Park South
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-318">
      <input type="checkbox" name="area[]" id="area-318" value="318" class="Checkbox jsSearchAreaCheckbox" data-area="318" data-area-name="Red Hook" data-parent-id="300" data-children-ids="">
      Red Hook
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-345">
      <input type="checkbox" name="area[]" id="area-345" value="345" class="Checkbox jsSearchAreaCheckbox" data-area="345" data-area-name="Seagate" data-parent-id="300" data-children-ids="">
      Seagate
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-349">
      <input type="checkbox" name="area[]" id="area-349" value="349" class="Checkbox jsSearchAreaCheckbox" data-area="349" data-area-name="Sheepshead Bay" data-parent-id="300" data-children-ids="344,366">
      Sheepshead Bay
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-344">
      <input type="checkbox" name="area[]" id="area-344" value="344" class="Checkbox jsSearchAreaCheckbox" data-area="344" data-area-name="Homecrest" data-parent-id="349" data-children-ids="">
      Homecrest
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-366">
      <input type="checkbox" name="area[]" id="area-366" value="366" class="Checkbox jsSearchAreaCheckbox" data-area="366" data-area-name="Madison" data-parent-id="349" data-children-ids="">
      Madison
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-323">
      <input type="checkbox" name="area[]" id="area-323" value="323" class="Checkbox jsSearchAreaCheckbox" data-area="323" data-area-name="Sunset Park" data-parent-id="300" data-children-ids="">
      Sunset Park
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-302">
      <input type="checkbox" name="area[]" id="area-302" value="302" class="Checkbox jsSearchAreaCheckbox" data-area="302" data-area-name="Williamsburg" data-parent-id="300" data-children-ids="373">
      Williamsburg
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-373">
      <input type="checkbox" name="area[]" id="area-373" value="373" class="Checkbox jsSearchAreaCheckbox" data-area="373" data-area-name="East Williamsburg" data-parent-id="302" data-children-ids="">
      East Williamsburg
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-324">
      <input type="checkbox" name="area[]" id="area-324" value="324" class="Checkbox jsSearchAreaCheckbox" data-area="324" data-area-name="Windsor Terrace" data-parent-id="300" data-children-ids="">
      Windsor Terrace
    </label>
  </div>

</li>

          </ul>
        </div>
    </li>
    <li class="jsTrigger">
      <div class="Collapsible-trigger jsCollapsibleTrigger jsSearchAreaItem" data-collapsible-trigger-area="Queens">
          Queens
        <span class="Collapsible-triggerIcon">
          <i class="fa fa-angle-down u-text--bold"></i>
        </span>
      </div>
        <div class="Collapsible-body">
          <ul>
            <li class="jsCollapsibleChild">
              <div class="Collapsible-checkbox jsSearchAreaItem">
                <label class="Collapsible-checkboxLabel u-text--bold" for="area-400">
                  <input type="checkbox" name="area[]" id="area-400" value="400" class="Checkbox jsSearchAreaCheckbox" data-area="400" data-area-name="All Queens" data-children-ids="401,431,428,443,446,479,437,459,418,409,429,406,408,442,416,415,419,439,413,453,434,425,405,432,447,421,424,420,436,430,402,410,411,449,407,451,426,454,438,414,423,412,477,444,433,427,450,445,435,403,455,417,422,404">
                  All Queens
                </label>
              </div>
            </li>
              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-401">
      <input type="checkbox" name="area[]" id="area-401" value="401" class="Checkbox jsSearchAreaCheckbox" data-area="401" data-area-name="Astoria" data-parent-id="400" data-children-ids="474">
      Astoria
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-474">
      <input type="checkbox" name="area[]" id="area-474" value="474" class="Checkbox jsSearchAreaCheckbox" data-area="474" data-area-name="Ditmars-Steinway" data-parent-id="401" data-children-ids="">
      Ditmars-Steinway
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-431">
      <input type="checkbox" name="area[]" id="area-431" value="431" class="Checkbox jsSearchAreaCheckbox" data-area="431" data-area-name="Auburndale" data-parent-id="400" data-children-ids="">
      Auburndale
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-428">
      <input type="checkbox" name="area[]" id="area-428" value="428" class="Checkbox jsSearchAreaCheckbox" data-area="428" data-area-name="Bayside" data-parent-id="400" data-children-ids="480">
      Bayside
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-480">
      <input type="checkbox" name="area[]" id="area-480" value="480" class="Checkbox jsSearchAreaCheckbox" data-area="480" data-area-name="Bay Terrace (Queens)" data-parent-id="428" data-children-ids="">
      Bay Terrace (Queens)
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-443">
      <input type="checkbox" name="area[]" id="area-443" value="443" class="Checkbox jsSearchAreaCheckbox" data-area="443" data-area-name="Bellerose" data-parent-id="400" data-children-ids="">
      Bellerose
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-446">
      <input type="checkbox" name="area[]" id="area-446" value="446" class="Checkbox jsSearchAreaCheckbox" data-area="446" data-area-name="Briarwood" data-parent-id="400" data-children-ids="">
      Briarwood
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-479">
      <input type="checkbox" name="area[]" id="area-479" value="479" class="Checkbox jsSearchAreaCheckbox" data-area="479" data-area-name="Brookville" data-parent-id="400" data-children-ids="">
      Brookville
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-437">
      <input type="checkbox" name="area[]" id="area-437" value="437" class="Checkbox jsSearchAreaCheckbox" data-area="437" data-area-name="Cambria Heights" data-parent-id="400" data-children-ids="">
      Cambria Heights
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-459">
      <input type="checkbox" name="area[]" id="area-459" value="459" class="Checkbox jsSearchAreaCheckbox" data-area="459" data-area-name="Clearview" data-parent-id="400" data-children-ids="">
      Clearview
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-418">
      <input type="checkbox" name="area[]" id="area-418" value="418" class="Checkbox jsSearchAreaCheckbox" data-area="418" data-area-name="College Point" data-parent-id="400" data-children-ids="">
      College Point
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-409">
      <input type="checkbox" name="area[]" id="area-409" value="409" class="Checkbox jsSearchAreaCheckbox" data-area="409" data-area-name="Corona" data-parent-id="400" data-children-ids="">
      Corona
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-429">
      <input type="checkbox" name="area[]" id="area-429" value="429" class="Checkbox jsSearchAreaCheckbox" data-area="429" data-area-name="Douglaston" data-parent-id="400" data-children-ids="">
      Douglaston
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-406">
      <input type="checkbox" name="area[]" id="area-406" value="406" class="Checkbox jsSearchAreaCheckbox" data-area="406" data-area-name="East Elmhurst" data-parent-id="400" data-children-ids="">
      East Elmhurst
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-408">
      <input type="checkbox" name="area[]" id="area-408" value="408" class="Checkbox jsSearchAreaCheckbox" data-area="408" data-area-name="Elmhurst" data-parent-id="400" data-children-ids="">
      Elmhurst
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-442">
      <input type="checkbox" name="area[]" id="area-442" value="442" class="Checkbox jsSearchAreaCheckbox" data-area="442" data-area-name="Floral Park" data-parent-id="400" data-children-ids="">
      Floral Park
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-416">
      <input type="checkbox" name="area[]" id="area-416" value="416" class="Checkbox jsSearchAreaCheckbox" data-area="416" data-area-name="Flushing" data-parent-id="400" data-children-ids="456,457">
      Flushing
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-456">
      <input type="checkbox" name="area[]" id="area-456" value="456" class="Checkbox jsSearchAreaCheckbox" data-area="456" data-area-name="East Flushing" data-parent-id="416" data-children-ids="">
      East Flushing
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-457">
      <input type="checkbox" name="area[]" id="area-457" value="457" class="Checkbox jsSearchAreaCheckbox" data-area="457" data-area-name="Murray Hill (Queens)" data-parent-id="416" data-children-ids="">
      Murray Hill (Queens)
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-415">
      <input type="checkbox" name="area[]" id="area-415" value="415" class="Checkbox jsSearchAreaCheckbox" data-area="415" data-area-name="Forest Hills" data-parent-id="400" data-children-ids="">
      Forest Hills
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-419">
      <input type="checkbox" name="area[]" id="area-419" value="419" class="Checkbox jsSearchAreaCheckbox" data-area="419" data-area-name="Fresh Meadows" data-parent-id="400" data-children-ids="">
      Fresh Meadows
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-439">
      <input type="checkbox" name="area[]" id="area-439" value="439" class="Checkbox jsSearchAreaCheckbox" data-area="439" data-area-name="Glen Oaks" data-parent-id="400" data-children-ids="">
      Glen Oaks
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-413">
      <input type="checkbox" name="area[]" id="area-413" value="413" class="Checkbox jsSearchAreaCheckbox" data-area="413" data-area-name="Glendale" data-parent-id="400" data-children-ids="">
      Glendale
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-453">
      <input type="checkbox" name="area[]" id="area-453" value="453" class="Checkbox jsSearchAreaCheckbox" data-area="453" data-area-name="Hillcrest" data-parent-id="400" data-children-ids="">
      Hillcrest
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-434">
      <input type="checkbox" name="area[]" id="area-434" value="434" class="Checkbox jsSearchAreaCheckbox" data-area="434" data-area-name="Hollis" data-parent-id="400" data-children-ids="">
      Hollis
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-425">
      <input type="checkbox" name="area[]" id="area-425" value="425" class="Checkbox jsSearchAreaCheckbox" data-area="425" data-area-name="Howard Beach" data-parent-id="400" data-children-ids="467,470,471,468,469">
      Howard Beach
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-467">
      <input type="checkbox" name="area[]" id="area-467" value="467" class="Checkbox jsSearchAreaCheckbox" data-area="467" data-area-name="Hamilton Beach" data-parent-id="425" data-children-ids="">
      Hamilton Beach
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-470">
      <input type="checkbox" name="area[]" id="area-470" value="470" class="Checkbox jsSearchAreaCheckbox" data-area="470" data-area-name="Lindenwood" data-parent-id="425" data-children-ids="">
      Lindenwood
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-471">
      <input type="checkbox" name="area[]" id="area-471" value="471" class="Checkbox jsSearchAreaCheckbox" data-area="471" data-area-name="Old Howard Beach" data-parent-id="425" data-children-ids="">
      Old Howard Beach
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-468">
      <input type="checkbox" name="area[]" id="area-468" value="468" class="Checkbox jsSearchAreaCheckbox" data-area="468" data-area-name="Ramblersville" data-parent-id="425" data-children-ids="">
      Ramblersville
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-469">
      <input type="checkbox" name="area[]" id="area-469" value="469" class="Checkbox jsSearchAreaCheckbox" data-area="469" data-area-name="Rockwood Park" data-parent-id="425" data-children-ids="">
      Rockwood Park
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-405">
      <input type="checkbox" name="area[]" id="area-405" value="405" class="Checkbox jsSearchAreaCheckbox" data-area="405" data-area-name="Jackson Heights" data-parent-id="400" data-children-ids="">
      Jackson Heights
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-432">
      <input type="checkbox" name="area[]" id="area-432" value="432" class="Checkbox jsSearchAreaCheckbox" data-area="432" data-area-name="Jamaica" data-parent-id="400" data-children-ids="">
      Jamaica
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-447">
      <input type="checkbox" name="area[]" id="area-447" value="447" class="Checkbox jsSearchAreaCheckbox" data-area="447" data-area-name="Jamaica Estates" data-parent-id="400" data-children-ids="">
      Jamaica Estates
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-421">
      <input type="checkbox" name="area[]" id="area-421" value="421" class="Checkbox jsSearchAreaCheckbox" data-area="421" data-area-name="Jamaica Hills" data-parent-id="400" data-children-ids="">
      Jamaica Hills
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-424">
      <input type="checkbox" name="area[]" id="area-424" value="424" class="Checkbox jsSearchAreaCheckbox" data-area="424" data-area-name="Kew Gardens" data-parent-id="400" data-children-ids="">
      Kew Gardens
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-420">
      <input type="checkbox" name="area[]" id="area-420" value="420" class="Checkbox jsSearchAreaCheckbox" data-area="420" data-area-name="Kew Gardens Hills" data-parent-id="400" data-children-ids="">
      Kew Gardens Hills
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-436">
      <input type="checkbox" name="area[]" id="area-436" value="436" class="Checkbox jsSearchAreaCheckbox" data-area="436" data-area-name="Laurelton" data-parent-id="400" data-children-ids="">
      Laurelton
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-430">
      <input type="checkbox" name="area[]" id="area-430" value="430" class="Checkbox jsSearchAreaCheckbox" data-area="430" data-area-name="Little Neck" data-parent-id="400" data-children-ids="">
      Little Neck
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-402">
      <input type="checkbox" name="area[]" id="area-402" value="402" class="Checkbox jsSearchAreaCheckbox" data-area="402" data-area-name="Long Island City" data-parent-id="400" data-children-ids="478">
      Long Island City
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-478">
      <input type="checkbox" name="area[]" id="area-478" value="478" class="Checkbox jsSearchAreaCheckbox" data-area="478" data-area-name="Hunters Point" data-parent-id="402" data-children-ids="">
      Hunters Point
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-410">
      <input type="checkbox" name="area[]" id="area-410" value="410" class="Checkbox jsSearchAreaCheckbox" data-area="410" data-area-name="Maspeth" data-parent-id="400" data-children-ids="">
      Maspeth
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-411">
      <input type="checkbox" name="area[]" id="area-411" value="411" class="Checkbox jsSearchAreaCheckbox" data-area="411" data-area-name="Middle Village" data-parent-id="400" data-children-ids="">
      Middle Village
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-449">
      <input type="checkbox" name="area[]" id="area-449" value="449" class="Checkbox jsSearchAreaCheckbox" data-area="449" data-area-name="New Hyde Park" data-parent-id="400" data-children-ids="">
      New Hyde Park
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-407">
      <input type="checkbox" name="area[]" id="area-407" value="407" class="Checkbox jsSearchAreaCheckbox" data-area="407" data-area-name="North Corona" data-parent-id="400" data-children-ids="">
      North Corona
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-451">
      <input type="checkbox" name="area[]" id="area-451" value="451" class="Checkbox jsSearchAreaCheckbox" data-area="451" data-area-name="Oakland Gardens" data-parent-id="400" data-children-ids="">
      Oakland Gardens
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-426">
      <input type="checkbox" name="area[]" id="area-426" value="426" class="Checkbox jsSearchAreaCheckbox" data-area="426" data-area-name="Ozone Park" data-parent-id="400" data-children-ids="">
      Ozone Park
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-454">
      <input type="checkbox" name="area[]" id="area-454" value="454" class="Checkbox jsSearchAreaCheckbox" data-area="454" data-area-name="Pomonok" data-parent-id="400" data-children-ids="">
      Pomonok
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-438">
      <input type="checkbox" name="area[]" id="area-438" value="438" class="Checkbox jsSearchAreaCheckbox" data-area="438" data-area-name="Queens Village" data-parent-id="400" data-children-ids="">
      Queens Village
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-414">
      <input type="checkbox" name="area[]" id="area-414" value="414" class="Checkbox jsSearchAreaCheckbox" data-area="414" data-area-name="Rego Park" data-parent-id="400" data-children-ids="">
      Rego Park
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-423">
      <input type="checkbox" name="area[]" id="area-423" value="423" class="Checkbox jsSearchAreaCheckbox" data-area="423" data-area-name="Richmond Hill" data-parent-id="400" data-children-ids="">
      Richmond Hill
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-412">
      <input type="checkbox" name="area[]" id="area-412" value="412" class="Checkbox jsSearchAreaCheckbox" data-area="412" data-area-name="Ridgewood" data-parent-id="400" data-children-ids="">
      Ridgewood
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-477">
      <input type="checkbox" name="area[]" id="area-477" value="477" class="Checkbox jsSearchAreaCheckbox" data-area="477" data-area-name="Rockaway All" data-parent-id="400" data-children-ids="448,462,463,464,441,466,440,473,465,452">
      Rockaway All
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-448">
      <input type="checkbox" name="area[]" id="area-448" value="448" class="Checkbox jsSearchAreaCheckbox" data-area="448" data-area-name="Arverne" data-parent-id="477" data-children-ids="">
      Arverne
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-462">
      <input type="checkbox" name="area[]" id="area-462" value="462" class="Checkbox jsSearchAreaCheckbox" data-area="462" data-area-name="Bayswater" data-parent-id="477" data-children-ids="">
      Bayswater
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-463">
      <input type="checkbox" name="area[]" id="area-463" value="463" class="Checkbox jsSearchAreaCheckbox" data-area="463" data-area-name="Belle Harbor" data-parent-id="477" data-children-ids="">
      Belle Harbor
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-464">
      <input type="checkbox" name="area[]" id="area-464" value="464" class="Checkbox jsSearchAreaCheckbox" data-area="464" data-area-name="Breezy Point" data-parent-id="477" data-children-ids="">
      Breezy Point
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-441">
      <input type="checkbox" name="area[]" id="area-441" value="441" class="Checkbox jsSearchAreaCheckbox" data-area="441" data-area-name="Broad Channel" data-parent-id="477" data-children-ids="">
      Broad Channel
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-466">
      <input type="checkbox" name="area[]" id="area-466" value="466" class="Checkbox jsSearchAreaCheckbox" data-area="466" data-area-name="Edgemere" data-parent-id="477" data-children-ids="">
      Edgemere
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-440">
      <input type="checkbox" name="area[]" id="area-440" value="440" class="Checkbox jsSearchAreaCheckbox" data-area="440" data-area-name="Far Rockaway" data-parent-id="477" data-children-ids="">
      Far Rockaway
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-473">
      <input type="checkbox" name="area[]" id="area-473" value="473" class="Checkbox jsSearchAreaCheckbox" data-area="473" data-area-name="Hammels" data-parent-id="477" data-children-ids="">
      Hammels
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-465">
      <input type="checkbox" name="area[]" id="area-465" value="465" class="Checkbox jsSearchAreaCheckbox" data-area="465" data-area-name="Neponsit" data-parent-id="477" data-children-ids="">
      Neponsit
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-452">
      <input type="checkbox" name="area[]" id="area-452" value="452" class="Checkbox jsSearchAreaCheckbox" data-area="452" data-area-name="Rockaway Park" data-parent-id="477" data-children-ids="">
      Rockaway Park
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-444">
      <input type="checkbox" name="area[]" id="area-444" value="444" class="Checkbox jsSearchAreaCheckbox" data-area="444" data-area-name="Rosedale" data-parent-id="400" data-children-ids="">
      Rosedale
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-433">
      <input type="checkbox" name="area[]" id="area-433" value="433" class="Checkbox jsSearchAreaCheckbox" data-area="433" data-area-name="South Jamaica" data-parent-id="400" data-children-ids="">
      South Jamaica
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-427">
      <input type="checkbox" name="area[]" id="area-427" value="427" class="Checkbox jsSearchAreaCheckbox" data-area="427" data-area-name="South Ozone Park" data-parent-id="400" data-children-ids="">
      South Ozone Park
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-450">
      <input type="checkbox" name="area[]" id="area-450" value="450" class="Checkbox jsSearchAreaCheckbox" data-area="450" data-area-name="South Richmond Hill" data-parent-id="400" data-children-ids="">
      South Richmond Hill
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-445">
      <input type="checkbox" name="area[]" id="area-445" value="445" class="Checkbox jsSearchAreaCheckbox" data-area="445" data-area-name="Springfield Gardens" data-parent-id="400" data-children-ids="">
      Springfield Gardens
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-435">
      <input type="checkbox" name="area[]" id="area-435" value="435" class="Checkbox jsSearchAreaCheckbox" data-area="435" data-area-name="St. Albans" data-parent-id="400" data-children-ids="">
      St. Albans
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-403">
      <input type="checkbox" name="area[]" id="area-403" value="403" class="Checkbox jsSearchAreaCheckbox" data-area="403" data-area-name="Sunnyside" data-parent-id="400" data-children-ids="">
      Sunnyside
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-455">
      <input type="checkbox" name="area[]" id="area-455" value="455" class="Checkbox jsSearchAreaCheckbox" data-area="455" data-area-name="Utopia" data-parent-id="400" data-children-ids="">
      Utopia
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-417">
      <input type="checkbox" name="area[]" id="area-417" value="417" class="Checkbox jsSearchAreaCheckbox" data-area="417" data-area-name="Whitestone" data-parent-id="400" data-children-ids="461,460">
      Whitestone
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-461">
      <input type="checkbox" name="area[]" id="area-461" value="461" class="Checkbox jsSearchAreaCheckbox" data-area="461" data-area-name="Beechhurst" data-parent-id="417" data-children-ids="">
      Beechhurst
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-460">
      <input type="checkbox" name="area[]" id="area-460" value="460" class="Checkbox jsSearchAreaCheckbox" data-area="460" data-area-name="Malba" data-parent-id="417" data-children-ids="">
      Malba
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-422">
      <input type="checkbox" name="area[]" id="area-422" value="422" class="Checkbox jsSearchAreaCheckbox" data-area="422" data-area-name="Woodhaven" data-parent-id="400" data-children-ids="">
      Woodhaven
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-404">
      <input type="checkbox" name="area[]" id="area-404" value="404" class="Checkbox jsSearchAreaCheckbox" data-area="404" data-area-name="Woodside" data-parent-id="400" data-children-ids="">
      Woodside
    </label>
  </div>

</li>

          </ul>
        </div>
    </li>
    <li class="jsTrigger">
      <div class="Collapsible-trigger jsCollapsibleTrigger jsSearchAreaItem" data-collapsible-trigger-area="Bronx">
          Bronx
        <span class="Collapsible-triggerIcon">
          <i class="fa fa-angle-down u-text--bold"></i>
        </span>
      </div>
        <div class="Collapsible-body">
          <ul>
            <li class="jsCollapsibleChild">
              <div class="Collapsible-checkbox jsSearchAreaItem">
                <label class="Collapsible-checkboxLabel u-text--bold" for="area-200">
                  <input type="checkbox" name="area[]" id="area-200" value="200" class="Checkbox jsSearchAreaCheckbox" data-area="200" data-area-name="All Bronx" data-children-ids="243,221,218,265,229,236,234,211,273,209,216,246,276,214,210,204,224,241,205,202,212,237,207,201,260,231,233,266,238,203,225,274,228,232,248,213,240,245,272,242,244,270">
                  All Bronx
                </label>
              </div>
            </li>
              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-243">
      <input type="checkbox" name="area[]" id="area-243" value="243" class="Checkbox jsSearchAreaCheckbox" data-area="243" data-area-name="Baychester" data-parent-id="200" data-children-ids="">
      Baychester
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-221">
      <input type="checkbox" name="area[]" id="area-221" value="221" class="Checkbox jsSearchAreaCheckbox" data-area="221" data-area-name="Bedford Park" data-parent-id="200" data-children-ids="">
      Bedford Park
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-218">
      <input type="checkbox" name="area[]" id="area-218" value="218" class="Checkbox jsSearchAreaCheckbox" data-area="218" data-area-name="Belmont" data-parent-id="200" data-children-ids="">
      Belmont
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-265">
      <input type="checkbox" name="area[]" id="area-265" value="265" class="Checkbox jsSearchAreaCheckbox" data-area="265" data-area-name="Bronxwood" data-parent-id="200" data-children-ids="">
      Bronxwood
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-229">
      <input type="checkbox" name="area[]" id="area-229" value="229" class="Checkbox jsSearchAreaCheckbox" data-area="229" data-area-name="Castle Hill" data-parent-id="200" data-children-ids="">
      Castle Hill
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-236">
      <input type="checkbox" name="area[]" id="area-236" value="236" class="Checkbox jsSearchAreaCheckbox" data-area="236" data-area-name="City Island" data-parent-id="200" data-children-ids="">
      City Island
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-234">
      <input type="checkbox" name="area[]" id="area-234" value="234" class="Checkbox jsSearchAreaCheckbox" data-area="234" data-area-name="Co-op City" data-parent-id="200" data-children-ids="">
      Co-op City
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-211">
      <input type="checkbox" name="area[]" id="area-211" value="211" class="Checkbox jsSearchAreaCheckbox" data-area="211" data-area-name="Concourse" data-parent-id="200" data-children-ids="">
      Concourse
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-273">
      <input type="checkbox" name="area[]" id="area-273" value="273" class="Checkbox jsSearchAreaCheckbox" data-area="273" data-area-name="Country Club" data-parent-id="200" data-children-ids="">
      Country Club
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-209">
      <input type="checkbox" name="area[]" id="area-209" value="209" class="Checkbox jsSearchAreaCheckbox" data-area="209" data-area-name="Crotona Park East" data-parent-id="200" data-children-ids="">
      Crotona Park East
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-216">
      <input type="checkbox" name="area[]" id="area-216" value="216" class="Checkbox jsSearchAreaCheckbox" data-area="216" data-area-name="East Tremont" data-parent-id="200" data-children-ids="219">
      East Tremont
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-219">
      <input type="checkbox" name="area[]" id="area-219" value="219" class="Checkbox jsSearchAreaCheckbox" data-area="219" data-area-name="West Farms" data-parent-id="216" data-children-ids="">
      West Farms
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-246">
      <input type="checkbox" name="area[]" id="area-246" value="246" class="Checkbox jsSearchAreaCheckbox" data-area="246" data-area-name="Eastchester" data-parent-id="200" data-children-ids="">
      Eastchester
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-276">
      <input type="checkbox" name="area[]" id="area-276" value="276" class="Checkbox jsSearchAreaCheckbox" data-area="276" data-area-name="Edenwald" data-parent-id="200" data-children-ids="">
      Edenwald
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-214">
      <input type="checkbox" name="area[]" id="area-214" value="214" class="Checkbox jsSearchAreaCheckbox" data-area="214" data-area-name="Fordham" data-parent-id="200" data-children-ids="">
      Fordham
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-210">
      <input type="checkbox" name="area[]" id="area-210" value="210" class="Checkbox jsSearchAreaCheckbox" data-area="210" data-area-name="Highbridge" data-parent-id="200" data-children-ids="">
      Highbridge
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-204">
      <input type="checkbox" name="area[]" id="area-204" value="204" class="Checkbox jsSearchAreaCheckbox" data-area="204" data-area-name="Hunts Point" data-parent-id="200" data-children-ids="">
      Hunts Point
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-224">
      <input type="checkbox" name="area[]" id="area-224" value="224" class="Checkbox jsSearchAreaCheckbox" data-area="224" data-area-name="Kingsbridge" data-parent-id="200" data-children-ids="220">
      Kingsbridge
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-220">
      <input type="checkbox" name="area[]" id="area-220" value="220" class="Checkbox jsSearchAreaCheckbox" data-area="220" data-area-name="Kingsbridge Heights" data-parent-id="224" data-children-ids="">
      Kingsbridge Heights
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-241">
      <input type="checkbox" name="area[]" id="area-241" value="241" class="Checkbox jsSearchAreaCheckbox" data-area="241" data-area-name="Laconia" data-parent-id="200" data-children-ids="">
      Laconia
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-205">
      <input type="checkbox" name="area[]" id="area-205" value="205" class="Checkbox jsSearchAreaCheckbox" data-area="205" data-area-name="Longwood" data-parent-id="200" data-children-ids="">
      Longwood
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-202">
      <input type="checkbox" name="area[]" id="area-202" value="202" class="Checkbox jsSearchAreaCheckbox" data-area="202" data-area-name="Melrose" data-parent-id="200" data-children-ids="">
      Melrose
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-212">
      <input type="checkbox" name="area[]" id="area-212" value="212" class="Checkbox jsSearchAreaCheckbox" data-area="212" data-area-name="Morris Heights" data-parent-id="200" data-children-ids="">
      Morris Heights
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-237">
      <input type="checkbox" name="area[]" id="area-237" value="237" class="Checkbox jsSearchAreaCheckbox" data-area="237" data-area-name="Morris Park" data-parent-id="200" data-children-ids="">
      Morris Park
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-207">
      <input type="checkbox" name="area[]" id="area-207" value="207" class="Checkbox jsSearchAreaCheckbox" data-area="207" data-area-name="Morrisania" data-parent-id="200" data-children-ids="208">
      Morrisania
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-208">
      <input type="checkbox" name="area[]" id="area-208" value="208" class="Checkbox jsSearchAreaCheckbox" data-area="208" data-area-name="Claremont" data-parent-id="207" data-children-ids="">
      Claremont
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-201">
      <input type="checkbox" name="area[]" id="area-201" value="201" class="Checkbox jsSearchAreaCheckbox" data-area="201" data-area-name="Mott Haven" data-parent-id="200" data-children-ids="271">
      Mott Haven
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-271">
      <input type="checkbox" name="area[]" id="area-271" value="271" class="Checkbox jsSearchAreaCheckbox" data-area="271" data-area-name="North New York" data-parent-id="201" data-children-ids="">
      North New York
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-260">
      <input type="checkbox" name="area[]" id="area-260" value="260" class="Checkbox jsSearchAreaCheckbox" data-area="260" data-area-name="Norwood" data-parent-id="200" data-children-ids="">
      Norwood
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-231">
      <input type="checkbox" name="area[]" id="area-231" value="231" class="Checkbox jsSearchAreaCheckbox" data-area="231" data-area-name="Parkchester" data-parent-id="200" data-children-ids="">
      Parkchester
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-233">
      <input type="checkbox" name="area[]" id="area-233" value="233" class="Checkbox jsSearchAreaCheckbox" data-area="233" data-area-name="Pelham Bay" data-parent-id="200" data-children-ids="">
      Pelham Bay
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-266">
      <input type="checkbox" name="area[]" id="area-266" value="266" class="Checkbox jsSearchAreaCheckbox" data-area="266" data-area-name="Pelham Gardens" data-parent-id="200" data-children-ids="">
      Pelham Gardens
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-238">
      <input type="checkbox" name="area[]" id="area-238" value="238" class="Checkbox jsSearchAreaCheckbox" data-area="238" data-area-name="Pelham Parkway" data-parent-id="200" data-children-ids="">
      Pelham Parkway
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-203">
      <input type="checkbox" name="area[]" id="area-203" value="203" class="Checkbox jsSearchAreaCheckbox" data-area="203" data-area-name="Port Morris" data-parent-id="200" data-children-ids="">
      Port Morris
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-225">
      <input type="checkbox" name="area[]" id="area-225" value="225" class="Checkbox jsSearchAreaCheckbox" data-area="225" data-area-name="Riverdale" data-parent-id="200" data-children-ids="227,249">
      Riverdale
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-227">
      <input type="checkbox" name="area[]" id="area-227" value="227" class="Checkbox jsSearchAreaCheckbox" data-area="227" data-area-name="Fieldston" data-parent-id="225" data-children-ids="">
      Fieldston
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-249">
      <input type="checkbox" name="area[]" id="area-249" value="249" class="Checkbox jsSearchAreaCheckbox" data-area="249" data-area-name="Spuyten Duyvil" data-parent-id="225" data-children-ids="">
      Spuyten Duyvil
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-274">
      <input type="checkbox" name="area[]" id="area-274" value="274" class="Checkbox jsSearchAreaCheckbox" data-area="274" data-area-name="Schuylerville" data-parent-id="200" data-children-ids="">
      Schuylerville
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-228">
      <input type="checkbox" name="area[]" id="area-228" value="228" class="Checkbox jsSearchAreaCheckbox" data-area="228" data-area-name="Soundview" data-parent-id="200" data-children-ids="">
      Soundview
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-232">
      <input type="checkbox" name="area[]" id="area-232" value="232" class="Checkbox jsSearchAreaCheckbox" data-area="232" data-area-name="Throgs Neck" data-parent-id="200" data-children-ids="267">
      Throgs Neck
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-267">
      <input type="checkbox" name="area[]" id="area-267" value="267" class="Checkbox jsSearchAreaCheckbox" data-area="267" data-area-name="Locust Point" data-parent-id="232" data-children-ids="">
      Locust Point
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-248">
      <input type="checkbox" name="area[]" id="area-248" value="248" class="Checkbox jsSearchAreaCheckbox" data-area="248" data-area-name="Tremont" data-parent-id="200" data-children-ids="215">
      Tremont
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-215">
      <input type="checkbox" name="area[]" id="area-215" value="215" class="Checkbox jsSearchAreaCheckbox" data-area="215" data-area-name="Mt. Hope" data-parent-id="248" data-children-ids="">
      Mt. Hope
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-213">
      <input type="checkbox" name="area[]" id="area-213" value="213" class="Checkbox jsSearchAreaCheckbox" data-area="213" data-area-name="University Heights" data-parent-id="200" data-children-ids="">
      University Heights
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-240">
      <input type="checkbox" name="area[]" id="area-240" value="240" class="Checkbox jsSearchAreaCheckbox" data-area="240" data-area-name="Van Nest" data-parent-id="200" data-children-ids="">
      Van Nest
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-245">
      <input type="checkbox" name="area[]" id="area-245" value="245" class="Checkbox jsSearchAreaCheckbox" data-area="245" data-area-name="Wakefield" data-parent-id="200" data-children-ids="">
      Wakefield
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-272">
      <input type="checkbox" name="area[]" id="area-272" value="272" class="Checkbox jsSearchAreaCheckbox" data-area="272" data-area-name="Westchester Village" data-parent-id="200" data-children-ids="235">
      Westchester Village
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-235">
      <input type="checkbox" name="area[]" id="area-235" value="235" class="Checkbox jsSearchAreaCheckbox" data-area="235" data-area-name="Westchester Square" data-parent-id="272" data-children-ids="">
      Westchester Square
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-242">
      <input type="checkbox" name="area[]" id="area-242" value="242" class="Checkbox jsSearchAreaCheckbox" data-area="242" data-area-name="Williamsbridge" data-parent-id="200" data-children-ids="">
      Williamsbridge
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-244">
      <input type="checkbox" name="area[]" id="area-244" value="244" class="Checkbox jsSearchAreaCheckbox" data-area="244" data-area-name="Woodlawn" data-parent-id="200" data-children-ids="">
      Woodlawn
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-270">
      <input type="checkbox" name="area[]" id="area-270" value="270" class="Checkbox jsSearchAreaCheckbox" data-area="270" data-area-name="Woodstock" data-parent-id="200" data-children-ids="">
      Woodstock
    </label>
  </div>

</li>

          </ul>
        </div>
    </li>
    <li class="jsTrigger">
      <div class="Collapsible-trigger jsCollapsibleTrigger jsSearchAreaItem" data-collapsible-trigger-area="Staten Island">
          Staten Island
        <span class="Collapsible-triggerIcon">
          <i class="fa fa-angle-down u-text--bold"></i>
        </span>
      </div>
        <div class="Collapsible-body">
          <ul>
            <li class="jsCollapsibleChild">
              <div class="Collapsible-checkbox jsSearchAreaItem">
                <label class="Collapsible-checkboxLabel u-text--bold" for="area-500">
                  <input type="checkbox" name="area[]" id="area-500" value="500" class="Checkbox jsSearchAreaCheckbox" data-area="500" data-area-name="All Staten Island" data-children-ids="503,505,501,502,504">
                  All Staten Island
                </label>
              </div>
            </li>
              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-503">
      <input type="checkbox" name="area[]" id="area-503" value="503" class="Checkbox jsSearchAreaCheckbox" data-area="503" data-area-name="East Shore" data-parent-id="500" data-children-ids="510,511,522,523,526,527,529,530,540,546,548,591,550,592,551,561,568,575">
      East Shore
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-510">
      <input type="checkbox" name="area[]" id="area-510" value="510" class="Checkbox jsSearchAreaCheckbox" data-area="510" data-area-name="Arrochar" data-parent-id="503" data-children-ids="">
      Arrochar
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-511">
      <input type="checkbox" name="area[]" id="area-511" value="511" class="Checkbox jsSearchAreaCheckbox" data-area="511" data-area-name="Bay Terrace" data-parent-id="503" data-children-ids="">
      Bay Terrace
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-522">
      <input type="checkbox" name="area[]" id="area-522" value="522" class="Checkbox jsSearchAreaCheckbox" data-area="522" data-area-name="Dongan Hills" data-parent-id="503" data-children-ids="">
      Dongan Hills
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-523">
      <input type="checkbox" name="area[]" id="area-523" value="523" class="Checkbox jsSearchAreaCheckbox" data-area="523" data-area-name="Egbertville" data-parent-id="503" data-children-ids="">
      Egbertville
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-526">
      <input type="checkbox" name="area[]" id="area-526" value="526" class="Checkbox jsSearchAreaCheckbox" data-area="526" data-area-name="Emerson Hill" data-parent-id="503" data-children-ids="">
      Emerson Hill
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-527">
      <input type="checkbox" name="area[]" id="area-527" value="527" class="Checkbox jsSearchAreaCheckbox" data-area="527" data-area-name="Fort Wadsworth" data-parent-id="503" data-children-ids="">
      Fort Wadsworth
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-529">
      <input type="checkbox" name="area[]" id="area-529" value="529" class="Checkbox jsSearchAreaCheckbox" data-area="529" data-area-name="Grant City" data-parent-id="503" data-children-ids="">
      Grant City
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-530">
      <input type="checkbox" name="area[]" id="area-530" value="530" class="Checkbox jsSearchAreaCheckbox" data-area="530" data-area-name="Grasmere" data-parent-id="503" data-children-ids="">
      Grasmere
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-540">
      <input type="checkbox" name="area[]" id="area-540" value="540" class="Checkbox jsSearchAreaCheckbox" data-area="540" data-area-name="Lighthouse Hill" data-parent-id="503" data-children-ids="">
      Lighthouse Hill
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-546">
      <input type="checkbox" name="area[]" id="area-546" value="546" class="Checkbox jsSearchAreaCheckbox" data-area="546" data-area-name="Midland Beach" data-parent-id="503" data-children-ids="">
      Midland Beach
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-548">
      <input type="checkbox" name="area[]" id="area-548" value="548" class="Checkbox jsSearchAreaCheckbox" data-area="548" data-area-name="New Dorp" data-parent-id="503" data-children-ids="">
      New Dorp
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-591">
      <input type="checkbox" name="area[]" id="area-591" value="591" class="Checkbox jsSearchAreaCheckbox" data-area="591" data-area-name="New Dorp Beach" data-parent-id="503" data-children-ids="">
      New Dorp Beach
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-550">
      <input type="checkbox" name="area[]" id="area-550" value="550" class="Checkbox jsSearchAreaCheckbox" data-area="550" data-area-name="Oakwood" data-parent-id="503" data-children-ids="">
      Oakwood
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-592">
      <input type="checkbox" name="area[]" id="area-592" value="592" class="Checkbox jsSearchAreaCheckbox" data-area="592" data-area-name="Oakwood Beach" data-parent-id="503" data-children-ids="">
      Oakwood Beach
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-551">
      <input type="checkbox" name="area[]" id="area-551" value="551" class="Checkbox jsSearchAreaCheckbox" data-area="551" data-area-name="Ocean Breeze" data-parent-id="503" data-children-ids="">
      Ocean Breeze
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-561">
      <input type="checkbox" name="area[]" id="area-561" value="561" class="Checkbox jsSearchAreaCheckbox" data-area="561" data-area-name="Richmondtown" data-parent-id="503" data-children-ids="">
      Richmondtown
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-568">
      <input type="checkbox" name="area[]" id="area-568" value="568" class="Checkbox jsSearchAreaCheckbox" data-area="568" data-area-name="South Beach" data-parent-id="503" data-children-ids="">
      South Beach
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-575">
      <input type="checkbox" name="area[]" id="area-575" value="575" class="Checkbox jsSearchAreaCheckbox" data-area="575" data-area-name="Todt Hill" data-parent-id="503" data-children-ids="">
      Todt Hill
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-505">
      <input type="checkbox" name="area[]" id="area-505" value="505" class="Checkbox jsSearchAreaCheckbox" data-area="505" data-area-name="Mid-Island" data-parent-id="500" data-children-ids="514,516,528,543,545,549,573,582,583">
      Mid-Island
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-514">
      <input type="checkbox" name="area[]" id="area-514" value="514" class="Checkbox jsSearchAreaCheckbox" data-area="514" data-area-name="Bulls Head" data-parent-id="505" data-children-ids="">
      Bulls Head
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-516">
      <input type="checkbox" name="area[]" id="area-516" value="516" class="Checkbox jsSearchAreaCheckbox" data-area="516" data-area-name="Castleton Corners" data-parent-id="505" data-children-ids="">
      Castleton Corners
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-528">
      <input type="checkbox" name="area[]" id="area-528" value="528" class="Checkbox jsSearchAreaCheckbox" data-area="528" data-area-name="Graniteville" data-parent-id="505" data-children-ids="">
      Graniteville
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-543">
      <input type="checkbox" name="area[]" id="area-543" value="543" class="Checkbox jsSearchAreaCheckbox" data-area="543" data-area-name="Manor Heights" data-parent-id="505" data-children-ids="">
      Manor Heights
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-545">
      <input type="checkbox" name="area[]" id="area-545" value="545" class="Checkbox jsSearchAreaCheckbox" data-area="545" data-area-name="Meiers Corners" data-parent-id="505" data-children-ids="">
      Meiers Corners
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-549">
      <input type="checkbox" name="area[]" id="area-549" value="549" class="Checkbox jsSearchAreaCheckbox" data-area="549" data-area-name="New Springville" data-parent-id="505" data-children-ids="">
      New Springville
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-573">
      <input type="checkbox" name="area[]" id="area-573" value="573" class="Checkbox jsSearchAreaCheckbox" data-area="573" data-area-name="Sunnyside (Staten Island)" data-parent-id="505" data-children-ids="">
      Sunnyside (Staten Island)
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-582">
      <input type="checkbox" name="area[]" id="area-582" value="582" class="Checkbox jsSearchAreaCheckbox" data-area="582" data-area-name="Westerleigh" data-parent-id="505" data-children-ids="">
      Westerleigh
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-583">
      <input type="checkbox" name="area[]" id="area-583" value="583" class="Checkbox jsSearchAreaCheckbox" data-area="583" data-area-name="Willowbrook" data-parent-id="505" data-children-ids="">
      Willowbrook
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-501">
      <input type="checkbox" name="area[]" id="area-501" value="501" class="Checkbox jsSearchAreaCheckbox" data-area="501" data-area-name="North Shore" data-parent-id="500" data-children-ids="509,519,524,533,537,544,547,553,556,562,569,565,566,571,576,580">
      North Shore
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-509">
      <input type="checkbox" name="area[]" id="area-509" value="509" class="Checkbox jsSearchAreaCheckbox" data-area="509" data-area-name="Arlington" data-parent-id="501" data-children-ids="">
      Arlington
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-519">
      <input type="checkbox" name="area[]" id="area-519" value="519" class="Checkbox jsSearchAreaCheckbox" data-area="519" data-area-name="Clifton" data-parent-id="501" data-children-ids="">
      Clifton
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-524">
      <input type="checkbox" name="area[]" id="area-524" value="524" class="Checkbox jsSearchAreaCheckbox" data-area="524" data-area-name="Elm Park" data-parent-id="501" data-children-ids="">
      Elm Park
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-533">
      <input type="checkbox" name="area[]" id="area-533" value="533" class="Checkbox jsSearchAreaCheckbox" data-area="533" data-area-name="Grymes Hill" data-parent-id="501" data-children-ids="">
      Grymes Hill
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-537">
      <input type="checkbox" name="area[]" id="area-537" value="537" class="Checkbox jsSearchAreaCheckbox" data-area="537" data-area-name="Howland Hook" data-parent-id="501" data-children-ids="">
      Howland Hook
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-544">
      <input type="checkbox" name="area[]" id="area-544" value="544" class="Checkbox jsSearchAreaCheckbox" data-area="544" data-area-name="Mariners Harbor" data-parent-id="501" data-children-ids="">
      Mariners Harbor
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-547">
      <input type="checkbox" name="area[]" id="area-547" value="547" class="Checkbox jsSearchAreaCheckbox" data-area="547" data-area-name="New Brighton" data-parent-id="501" data-children-ids="">
      New Brighton
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-553">
      <input type="checkbox" name="area[]" id="area-553" value="553" class="Checkbox jsSearchAreaCheckbox" data-area="553" data-area-name="Park Hill" data-parent-id="501" data-children-ids="">
      Park Hill
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-556">
      <input type="checkbox" name="area[]" id="area-556" value="556" class="Checkbox jsSearchAreaCheckbox" data-area="556" data-area-name="Port Richmond" data-parent-id="501" data-children-ids="">
      Port Richmond
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-562">
      <input type="checkbox" name="area[]" id="area-562" value="562" class="Checkbox jsSearchAreaCheckbox" data-area="562" data-area-name="Rosebank" data-parent-id="501" data-children-ids="">
      Rosebank
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-569">
      <input type="checkbox" name="area[]" id="area-569" value="569" class="Checkbox jsSearchAreaCheckbox" data-area="569" data-area-name="Saint George" data-parent-id="501" data-children-ids="">
      Saint George
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-565">
      <input type="checkbox" name="area[]" id="area-565" value="565" class="Checkbox jsSearchAreaCheckbox" data-area="565" data-area-name="Shore Acres" data-parent-id="501" data-children-ids="">
      Shore Acres
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-566">
      <input type="checkbox" name="area[]" id="area-566" value="566" class="Checkbox jsSearchAreaCheckbox" data-area="566" data-area-name="Silver Lake" data-parent-id="501" data-children-ids="">
      Silver Lake
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-571">
      <input type="checkbox" name="area[]" id="area-571" value="571" class="Checkbox jsSearchAreaCheckbox" data-area="571" data-area-name="Stapleton" data-parent-id="501" data-children-ids="">
      Stapleton
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-576">
      <input type="checkbox" name="area[]" id="area-576" value="576" class="Checkbox jsSearchAreaCheckbox" data-area="576" data-area-name="Tompkinsville" data-parent-id="501" data-children-ids="">
      Tompkinsville
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-580">
      <input type="checkbox" name="area[]" id="area-580" value="580" class="Checkbox jsSearchAreaCheckbox" data-area="580" data-area-name="West Brighton" data-parent-id="501" data-children-ids="">
      West Brighton
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-502">
      <input type="checkbox" name="area[]" id="area-502" value="502" class="Checkbox jsSearchAreaCheckbox" data-area="502" data-area-name="South Shore" data-parent-id="500" data-children-ids="507,508,517,525,531,532,538,554,557,560,563,577,584">
      South Shore
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-507">
      <input type="checkbox" name="area[]" id="area-507" value="507" class="Checkbox jsSearchAreaCheckbox" data-area="507" data-area-name="Annadale" data-parent-id="502" data-children-ids="">
      Annadale
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-508">
      <input type="checkbox" name="area[]" id="area-508" value="508" class="Checkbox jsSearchAreaCheckbox" data-area="508" data-area-name="Arden Heights" data-parent-id="502" data-children-ids="">
      Arden Heights
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-517">
      <input type="checkbox" name="area[]" id="area-517" value="517" class="Checkbox jsSearchAreaCheckbox" data-area="517" data-area-name="Charleston" data-parent-id="502" data-children-ids="">
      Charleston
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-525">
      <input type="checkbox" name="area[]" id="area-525" value="525" class="Checkbox jsSearchAreaCheckbox" data-area="525" data-area-name="Eltingville" data-parent-id="502" data-children-ids="">
      Eltingville
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-531">
      <input type="checkbox" name="area[]" id="area-531" value="531" class="Checkbox jsSearchAreaCheckbox" data-area="531" data-area-name="Great Kills" data-parent-id="502" data-children-ids="">
      Great Kills
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-532">
      <input type="checkbox" name="area[]" id="area-532" value="532" class="Checkbox jsSearchAreaCheckbox" data-area="532" data-area-name="Greenridge" data-parent-id="502" data-children-ids="">
      Greenridge
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-538">
      <input type="checkbox" name="area[]" id="area-538" value="538" class="Checkbox jsSearchAreaCheckbox" data-area="538" data-area-name="Huguenot" data-parent-id="502" data-children-ids="">
      Huguenot
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-554">
      <input type="checkbox" name="area[]" id="area-554" value="554" class="Checkbox jsSearchAreaCheckbox" data-area="554" data-area-name="Pleasant Plains" data-parent-id="502" data-children-ids="">
      Pleasant Plains
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-557">
      <input type="checkbox" name="area[]" id="area-557" value="557" class="Checkbox jsSearchAreaCheckbox" data-area="557" data-area-name="Princes Bay" data-parent-id="502" data-children-ids="">
      Princes Bay
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-560">
      <input type="checkbox" name="area[]" id="area-560" value="560" class="Checkbox jsSearchAreaCheckbox" data-area="560" data-area-name="Richmond Valley" data-parent-id="502" data-children-ids="">
      Richmond Valley
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-563">
      <input type="checkbox" name="area[]" id="area-563" value="563" class="Checkbox jsSearchAreaCheckbox" data-area="563" data-area-name="Rossville" data-parent-id="502" data-children-ids="">
      Rossville
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-577">
      <input type="checkbox" name="area[]" id="area-577" value="577" class="Checkbox jsSearchAreaCheckbox" data-area="577" data-area-name="Tottenville" data-parent-id="502" data-children-ids="">
      Tottenville
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-584">
      <input type="checkbox" name="area[]" id="area-584" value="584" class="Checkbox jsSearchAreaCheckbox" data-area="584" data-area-name="Woodrow" data-parent-id="502" data-children-ids="">
      Woodrow
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-504">
      <input type="checkbox" name="area[]" id="area-504" value="504" class="Checkbox jsSearchAreaCheckbox" data-area="504" data-area-name="West Shore" data-parent-id="500" data-children-ids="512,518,578">
      West Shore
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-512">
      <input type="checkbox" name="area[]" id="area-512" value="512" class="Checkbox jsSearchAreaCheckbox" data-area="512" data-area-name="Bloomfield" data-parent-id="504" data-children-ids="">
      Bloomfield
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-518">
      <input type="checkbox" name="area[]" id="area-518" value="518" class="Checkbox jsSearchAreaCheckbox" data-area="518" data-area-name="Chelsea (Staten Island)" data-parent-id="504" data-children-ids="">
      Chelsea (Staten Island)
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-578">
      <input type="checkbox" name="area[]" id="area-578" value="578" class="Checkbox jsSearchAreaCheckbox" data-area="578" data-area-name="Travis" data-parent-id="504" data-children-ids="">
      Travis
    </label>
  </div>

</li>


          </ul>
        </div>
    </li>
    <li class="jsTrigger">
      <div class="Collapsible-trigger jsCollapsibleTrigger jsSearchAreaItem" data-collapsible-trigger-area="New Jersey">
          <span>
            New Jersey <span class="u-color-brightBlue u-italic u-text--normal u-capitalize">New!</span>
          </span>
        <span class="Collapsible-triggerIcon">
          <i class="fa fa-angle-down u-text--bold"></i>
        </span>
      </div>
        <div class="Collapsible-body">
          <ul>
            <li class="jsCollapsibleChild">
              <div class="Collapsible-checkbox jsSearchAreaItem">
                <label class="Collapsible-checkboxLabel u-text--bold" for="area-1000000">
                  <input type="checkbox" name="area[]" id="area-1000000" value="1000000" class="Checkbox jsSearchAreaCheckbox" data-area="1000000" data-area-name="All New Jersey" data-children-ids="1003000,856000,1005000,862000,869000,1009000,1010000,1004000,1001000,1011000,1007000,1012000,1006000,1008000,1013000">
                  All New Jersey
                </label>
              </div>
            </li>
              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-1003000">
      <input type="checkbox" name="area[]" id="area-1003000" value="1003000" class="Checkbox jsSearchAreaCheckbox" data-area="1003000" data-area-name="Bayonne" data-parent-id="1000000" data-children-ids="">
      Bayonne
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-856000">
      <input type="checkbox" name="area[]" id="area-856000" value="856000" class="Checkbox jsSearchAreaCheckbox" data-area="856000" data-area-name="Cliffside Park" data-parent-id="1000000" data-children-ids="">
      Cliffside Park
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-1005000">
      <input type="checkbox" name="area[]" id="area-1005000" value="1005000" class="Checkbox jsSearchAreaCheckbox" data-area="1005000" data-area-name="East Newark" data-parent-id="1000000" data-children-ids="">
      East Newark
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-862000">
      <input type="checkbox" name="area[]" id="area-862000" value="862000" class="Checkbox jsSearchAreaCheckbox" data-area="862000" data-area-name="Edgewater" data-parent-id="1000000" data-children-ids="">
      Edgewater
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-869000">
      <input type="checkbox" name="area[]" id="area-869000" value="869000" class="Checkbox jsSearchAreaCheckbox" data-area="869000" data-area-name="Fort Lee" data-parent-id="1000000" data-children-ids="">
      Fort Lee
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-1009000">
      <input type="checkbox" name="area[]" id="area-1009000" value="1009000" class="Checkbox jsSearchAreaCheckbox" data-area="1009000" data-area-name="Guttenberg" data-parent-id="1000000" data-children-ids="">
      Guttenberg
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-1010000">
      <input type="checkbox" name="area[]" id="area-1010000" value="1010000" class="Checkbox jsSearchAreaCheckbox" data-area="1010000" data-area-name="Harrison" data-parent-id="1000000" data-children-ids="">
      Harrison
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-1004000">
      <input type="checkbox" name="area[]" id="area-1004000" value="1004000" class="Checkbox jsSearchAreaCheckbox" data-area="1004000" data-area-name="Hoboken" data-parent-id="1000000" data-children-ids="">
      Hoboken
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-1001000">
      <input type="checkbox" name="area[]" id="area-1001000" value="1001000" class="Checkbox jsSearchAreaCheckbox" data-area="1001000" data-area-name="Jersey City" data-parent-id="1000000" data-children-ids="1117008,1001150,1001600,1117007,1001400,1001250,1002100">
      Jersey City
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-1117008">
      <input type="checkbox" name="area[]" id="area-1117008" value="1117008" class="Checkbox jsSearchAreaCheckbox" data-area="1117008" data-area-name="Bergen/Lafayette" data-parent-id="1001000" data-children-ids="">
      Bergen/Lafayette
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-1001150">
      <input type="checkbox" name="area[]" id="area-1001150" value="1001150" class="Checkbox jsSearchAreaCheckbox" data-area="1001150" data-area-name="Historic Downtown" data-parent-id="1001000" data-children-ids="">
      Historic Downtown
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-1001600">
      <input type="checkbox" name="area[]" id="area-1001600" value="1001600" class="Checkbox jsSearchAreaCheckbox" data-area="1001600" data-area-name="Journal Square" data-parent-id="1001000" data-children-ids="">
      Journal Square
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-1117007">
      <input type="checkbox" name="area[]" id="area-1117007" value="1117007" class="Checkbox jsSearchAreaCheckbox" data-area="1117007" data-area-name="Newport" data-parent-id="1001000" data-children-ids="">
      Newport
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-1001400">
      <input type="checkbox" name="area[]" id="area-1001400" value="1001400" class="Checkbox jsSearchAreaCheckbox" data-area="1001400" data-area-name="The Heights" data-parent-id="1001000" data-children-ids="">
      The Heights
    </label>
  </div>

</li>

    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-1001250">
      <input type="checkbox" name="area[]" id="area-1001250" value="1001250" class="Checkbox jsSearchAreaCheckbox" data-area="1001250" data-area-name="Waterfront" data-parent-id="1001000" data-children-ids="1001270">
      Waterfront
    </label>
  </div>

</li>
    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level4">
    <label class="Collapsible-checkboxLabel" for="area-1001270">
      <input type="checkbox" name="area[]" id="area-1001270" value="1001270" class="Checkbox jsSearchAreaCheckbox" data-area="1001270" data-area-name="Paulus Hook" data-parent-id="1001250" data-children-ids="">
      Paulus Hook
    </label>
  </div>

</li>


    <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level3">
    <label class="Collapsible-checkboxLabel" for="area-1002100">
      <input type="checkbox" name="area[]" id="area-1002100" value="1002100" class="Checkbox jsSearchAreaCheckbox" data-area="1002100" data-area-name="West Side" data-parent-id="1001000" data-children-ids="">
      West Side
    </label>
  </div>

</li>


              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-1011000">
      <input type="checkbox" name="area[]" id="area-1011000" value="1011000" class="Checkbox jsSearchAreaCheckbox" data-area="1011000" data-area-name="Kearny" data-parent-id="1000000" data-children-ids="">
      Kearny
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-1007000">
      <input type="checkbox" name="area[]" id="area-1007000" value="1007000" class="Checkbox jsSearchAreaCheckbox" data-area="1007000" data-area-name="North Bergen" data-parent-id="1000000" data-children-ids="">
      North Bergen
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-1012000">
      <input type="checkbox" name="area[]" id="area-1012000" value="1012000" class="Checkbox jsSearchAreaCheckbox" data-area="1012000" data-area-name="Secaucus" data-parent-id="1000000" data-children-ids="">
      Secaucus
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-1006000">
      <input type="checkbox" name="area[]" id="area-1006000" value="1006000" class="Checkbox jsSearchAreaCheckbox" data-area="1006000" data-area-name="Union City" data-parent-id="1000000" data-children-ids="">
      Union City
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-1008000">
      <input type="checkbox" name="area[]" id="area-1008000" value="1008000" class="Checkbox jsSearchAreaCheckbox" data-area="1008000" data-area-name="Weehawken" data-parent-id="1000000" data-children-ids="">
      Weehawken
    </label>
  </div>

</li>

              <li class="jsCollapsibleChild">
  <div class="Collapsible-checkbox jsSearchAreaItem Collapsible-level2">
    <label class="Collapsible-checkboxLabel" for="area-1013000">
      <input type="checkbox" name="area[]" id="area-1013000" value="1013000" class="Checkbox jsSearchAreaCheckbox" data-area="1013000" data-area-name="West New York" data-parent-id="1000000" data-children-ids="">
      West New York
    </label>
  </div>

</li>

          </ul>
        </div>
    </li>
</ul>

      <button class="SearchAreasDropdown-searchButton u-hidden jsSearchAreaDropdownSearchButton" type="button">
        Search for <span class="SearchAreasDropdown-searchButtonText jsSearchAreaDropdownSearchButtonText"></span>
      </button>

  </div>
</div>

      </div>
    </div>

  <div class="Home-searchRange Home-searchField">

<div class="Home-searchRangeInput">
  <select id="price_from" class="Home-searchRangeSelect jsPriceSelect isEmpty" name="price_from" se:behavior="support_custom_value" data-nochangeonload="">
    <option disabled="disabled" selected="selected" value="">$ Minimum</option>
<option value="">Any</option>
<option value="Custom">» Custom</option>
<option value="100000">$100,000</option>
<option value="150000">$150,000</option>
<option value="200000">$200,000</option>
<option value="250000">$250,000</option>
<option value="300000">$300,000</option>
<option value="400000">$400,000</option>
<option value="500000">$500,000</option>
<option value="600000">$600,000</option>
<option value="700000">$700,000</option>
<option value="750000">$750,000</option>
<option value="800000">$800,000</option>
<option value="900000">$900,000</option>
<option value="1000000">$1,000,000</option>
<option value="1250000">$1,250,000</option>
<option value="1500000">$1,500,000</option>
<option value="1750000">$1,750,000</option>
<option value="2000000">$2,000,000</option>
<option value="2250000">$2,250,000</option>
<option value="2500000">$2,500,000</option>
<option value="2750000">$2,750,000</option>
<option value="3000000">$3,000,000</option>
<option value="3500000">$3,500,000</option>
<option value="4000000">$4,000,000</option>
<option value="4500000">$4,500,000</option>
<option value="5000000">$5,000,000</option>
<option value="6000000">$6,000,000</option>
<option value="7000000">$7,000,000</option>
<option value="8000000">$8,000,000</option>
<option value="9000000">$9,000,000</option>
<option value="10000000">$10,000,000</option>
<option value="12000000">$12,000,000</option>
<option value="14000000">$14,000,000</option>
<option value="16000000">$16,000,000</option>
<option value="20000000">$20,000,000</option>
<option value="25000000">$25,000,000</option>
<option value="30000000">$30,000,000</option>
  </select>
  <input type="text" class="InputText Home-searchRangeCustom" id="price_from_ignore" data-nochangeonload="" name="price_from_ignore" value="$0" se:behavior="comma_separatable" style="display: none;">
</div>

<div class="Home-searchRangeInput">
  <select class="Home-searchRangeSelect jsPriceSelect isEmpty" id="price_to" name="price_to" se:behavior="support_custom_value" data-nochangeonload="">
    <option disabled="disabled" selected="selected" value="">$ Maximum</option>
<option value="">Any</option>
<option value="Custom">» Custom</option>
<option value="100000">$100,000</option>
<option value="150000">$150,000</option>
<option value="200000">$200,000</option>
<option value="250000">$250,000</option>
<option value="300000">$300,000</option>
<option value="400000">$400,000</option>
<option value="500000">$500,000</option>
<option value="600000">$600,000</option>
<option value="700000">$700,000</option>
<option value="750000">$750,000</option>
<option value="800000">$800,000</option>
<option value="900000">$900,000</option>
<option value="1000000">$1,000,000</option>
<option value="1250000">$1,250,000</option>
<option value="1500000">$1,500,000</option>
<option value="1750000">$1,750,000</option>
<option value="2000000">$2,000,000</option>
<option value="2250000">$2,250,000</option>
<option value="2500000">$2,500,000</option>
<option value="2750000">$2,750,000</option>
<option value="3000000">$3,000,000</option>
<option value="3500000">$3,500,000</option>
<option value="4000000">$4,000,000</option>
<option value="4500000">$4,500,000</option>
<option value="5000000">$5,000,000</option>
<option value="6000000">$6,000,000</option>
<option value="7000000">$7,000,000</option>
<option value="8000000">$8,000,000</option>
<option value="9000000">$9,000,000</option>
<option value="10000000">$10,000,000</option>
<option value="12000000">$12,000,000</option>
<option value="14000000">$14,000,000</option>
<option value="16000000">$16,000,000</option>
<option value="20000000">$20,000,000</option>
<option value="25000000">$25,000,000</option>
<option value="30000000">$30,000,000</option>
  </select>
  <input class="InputText Home-searchRangeCustom" type="text" id="price_to_ignore" data-nochangeonload="" name="price_to_ignore" value="$0" se:behavior="comma_separatable" style="display: none">
</div>

  </div>

  <div class="Home-searchBeds Home-searchField">
    <div class="CheckboxGroup Home-searchBedsSelects jsBedsSelection">

    <input id="search-studio" class="CheckboxGroup-input jsBedsInput" value="<1" type="checkbox">
    <label class="CheckboxGroup-label Home-searchBedsLabel" for="search-studio">
      <span class="CheckboxGroup-copy">Studio</span>
    </label>
    <input id="search-1" class="CheckboxGroup-input jsBedsInput" value="1" type="checkbox">
    <label class="CheckboxGroup-label Home-searchBedsLabel" for="search-1">
      <span class="CheckboxGroup-copy">1</span>
    </label>
    <input id="search-2" class="CheckboxGroup-input jsBedsInput" value="2" type="checkbox">
    <label class="CheckboxGroup-label Home-searchBedsLabel" for="search-2">
      <span class="CheckboxGroup-copy">2</span>
    </label>
    <input id="search-3" class="CheckboxGroup-input jsBedsInput" value="3" type="checkbox">
    <label class="CheckboxGroup-label Home-searchBedsLabel" for="search-3">
      <span class="CheckboxGroup-copy">3</span>
    </label>
    <input id="search-4+" class="CheckboxGroup-input jsBedsInput" value=">=4" type="checkbox">
    <label class="CheckboxGroup-label Home-searchBedsLabel" for="search-4+">
      <span class="CheckboxGroup-copy">4+</span>
    </label>

</div>
<input type="hidden" name="beds" id="beds" value="" class="jsBedsValue">

    <div class="Home-searchBox Home-searchBox--mWebColumn">
      <div class="Home-virtualView">
        <div class="Home-virtualViewTooltip">
          <div class="Home-virtualViewTitle">VIRTUAL VIEWING</div>
          <div class="Home-virtualViewTooltipBox jsVirtualViewTooltip">
            <div class="Home-virtualViewTooltipClose jsCloseVirtualViewTooltip"></div>
            <div class="Home-virtualViewTooltipTiangle"></div>
            <b>New ways to view</b>
            <p class="Text Text--disclaimer u-color-pureBlack">Filter to see only listings that have virtual viewing options.</p>
          </div>
        </div>
        <div class="Home-virtualViewInputBox">
          <div class="CheckBox">
            <input type="checkbox" name="has_videos" id="has_videos" value="1" class="CheckBox-input" data-nochangeonload="">
            <label class="CheckBox-label CheckBox-label--outsideInput" for="has_videos">
              <span class="Home-virtualViewVideo">Video</span>
            </label>
          </div>
          <div class="CheckBox">
            <input type="checkbox" name="has_3d_tour" id="has_3d_tour" value="1" class="CheckBox-input" data-nochangeonload="">
            <label class="CheckBox-label CheckBox-label--outsideInput" for="has_3d_tour">
              <span class="Home-virtualView3DTourIcon">3D Tour</span>
            </label>
          </div>
        </div>
      </div>
    </div>
  </div>


  <div class="Home-searchSubmit Home-searchField">
    <button type="submit" class="Button Button--classicBlue" data-gtm-event-category="sales_homepage" data-gtm-event-action="search_form" data-gtm-event-label="submit" data-gtm-event-value="">
      Search
    </button>

    <script>
      document.addEventListener('DOMContentLoaded', function() {
        clientProfiler.setMark('home.Sales.searchButtonVisible');

      })
    </script>

  </div>
</div>



      </div>


<div class="Home-advancedSearch SearchCriteria">
  <div class="se-advancedToggle">
    <a href="javascript:void(0)" class="Home-advancedSearchLink" se:behavior="togglable coordinated" se:coordinator="criteria_expander" se:togglable:cssselector=".se-advancedToggle" se:analytics:params="{&quot;event_category&quot;:&quot;search&quot;,&quot;event_action&quot;:&quot;click&quot;,&quot;event_label&quot;:&quot;advanced_options&quot;}" data-finish-ab-test="filter_on_desktop_homepage_srp_2019" style="cursor: pointer;">+ Advanced Options</a>
  </div>

  <div class="se-advancedToggle u-displayNone">
    <a href="javascript:void(0)" class="Home-advancedSearchLink" se:behavior="togglable coordinated" se:coordinator="criteria_expander" se:togglable:cssselector=".se-advancedToggle" se:analytics:params="{&quot;event_category&quot;:&quot;search&quot;,&quot;event_action&quot;:&quot;click&quot;,&quot;event_label&quot;:&quot;basic_options&quot;}" style="cursor: pointer;">- Basic Options</a>
  </div>

  <div class="SearchCriteria-advancedOptions se-advancedToggle u-displayNone" se:togglable:animation="slide">
    <div se:behavior="loadable:with_slide andale_coordinatable coordinated" se:coordinator="criteria_expander" se:url="/nyc/process/sales/search_fields?context=sale&amp;criteria=&amp;criteria_group=below_fold&amp;location=homepage" rel="nofollow">
    </div>
  </div>
</div>


</form>
    <!-- End Search -->

    <!-- Recent Searches / Explore NYC -->
      <div class="Home-additionalLinksContainer Home-topDivider">

          <h2 class="Title Title--secondarySmCaps u-color-koalaGrey u-noMargin u-nowrap">Explore NYC</h2>
<div class="lSSlideOuter ImagesSlider"><div class="lSSlideWrapper usingCss"><ul class="Home-additionalLinks jsSlider lightSlider lSSlide" data-slider-type="Additional Links" style="width: 960px; height: 77px; padding-bottom: 0%;">
  <li class="Home-additionalLink Home-additionalLink--withImage lslide active" style="margin-right: 0px;">
    <a href="https://www.dos.ny.gov/licensing/docs/FairHousingNotice_new.pdf" target="_blank" data-ga-click="" data-event="custom_event" data-event-category="sales_homepage" data-event-action="fair_housing_notice" data-event-label="click" class="flexBox-row flexBox-noWrap u-text--noDecoration">
      <span class="Home-additionalLinkImage Home-additionalLinkImage--fairHousingIcon"></span>
      <div class="Home-additionalLinkCopy">
        <div class="u-copySize--16 u-ellipsis">Fair Housing in NYC</div>
        <div class="Home-additionalLinkCopy--subtext u-color-wolfGrey">
          Read about your rights
        </div>
      </div>
    </a>
  </li>

  <li class="Home-additionalLink Home-additionalLink--withImage lslide" style="margin-right: 0px;">
    <a href="https://streeteasy.com/blog/data-dashboard/" target="_blank" data-ga-click="" data-event-category="sales_homepage" data-event-action="content_bar" data-event-label="clickslot=1" class="flexBox-row flexBox-noWrap u-text--noDecoration">
      <span class="Home-additionalLinkImage Home-additionalLinkImage--dataDashboardIcon"></span>
      <div class="Home-additionalLinkCopy">
        <div class="u-copySize--16 u-ellipsis">NYC Data Dashboard</div>
        <div class="Home-additionalLinkCopy--subtext u-color-wolfGrey">
          Stay on top of the latest market trends
        </div>
      </div>
    </a>
  </li>

  <li class="Home-additionalLink Home-additionalLink--withImage lslide" style="margin-right: 0px;">
    <a href="https://streeteasy.com/guides/buyers-guide" target="_blank" data-ga-click="" data-event-category="sales_homepage" data-event-action="content_bar" data-event-label="clickslot=2" class="flexBox-row flexBox-noWrap u-text--noDecoration">
      <span class="Home-additionalLinkImage Home-additionalLinkImage--tipsAdviceIcon"></span>
      <div class="Home-additionalLinkCopy">
        <div class="u-copySize--16 u-ellipsis">Tips and Advice</div>
        <div class="Home-additionalLinkCopy--subtext u-color-wolfGrey">
          Find answers about renting, buying, and selling
        </div>
      </div>
    </a>
  </li>

  <li class="Home-additionalLink Home-additionalLink--withImage lslide" style="margin-right: 0px;">
    <a href="https://streeteasy.com/blog/" target="_blank" data-ga-click="" data-event-category="sales_homepage" data-event-action="content_bar" data-event-label="clickslot=3" class="flexBox-row flexBox-noWrap u-text--noDecoration">
      <span class="Home-additionalLinkImage Home-additionalLinkImage--blogIcon"></span>
      <div class="Home-additionalLinkCopy">
        <div class="u-copySize--16 u-ellipsis">StreetEasy Blog</div>
        <div class="Home-additionalLinkCopy--subtext u-color-wolfGrey">
          See curated listings and our guide to NYC living
        </div>
      </div>
    </a>
  </li>
</ul></div></div>

      </div>
    <!-- End Recent Searches / Explore NYC -->
  </div>
</section>

<section class="Home-more Home-section u-background-mouseGrey">

  <div class="Home-featuredContainer grid-container grid-container-9cols-984">


    <!-- Featured Buildings -->

    <ul class="Home-featuredBuildings grid-span-9 grid-container-9cols">
  <li class="Home-featuredBuildingLarge Home-featuredCard Home-featuredCard--large jsFranchiseBoxAd jsGoogleAd">
    <div class="TallCard TallCard--hoverable Home-featuredCardInner">
            <div id="FranchiseBox_1" style="zoom: 1; opacity: 1;">
      <script type="text/javascript">
        googletag.cmd.push(function() {
          googletag.display("FranchiseBox_1");
          googletag.pubads().addEventListener("slotRenderEnded", function(event) {
            var removeContainer = false;
            var els = document.getElementsByClassName("jsFranchiseBoxAd");
            if (event.slot.getSlotElementId() == "FranchiseBox_1") {
              if (event.isEmpty) {
                if(removeContainer) {
                  Array.prototype.forEach.call(els, function (el) {el.remove()})
                } else {
                  // FranchiseBox_1.remove();
                  Array.prototype.forEach.call(els, function (el) {el.classList.add("isAdless")})
                }
              } else {
                Array.prototype.forEach.call(els, function (el) {el.classList.remove("hidden")})
              }
            }
          });
        });
      </script>
    <div id="google_ads_iframe_/7449/Streeteasy/search_main/buy_general/FranchiseBox_1_0__container__" style="border: 0pt none; width: 100%; height: 0%;"></div></div>

    </div>
  </li>
    <li class="Home-featuredBuildingSmall Home-featuredCard jsFeaturedBuild1Ad jsGoogleAd">
      <div class="TallCard TallCard--hoverable Home-featuredCardInner">
            <div id="FeaturedBuild_1" style="zoom: 1; opacity: 1;">
      <script type="text/javascript">
        googletag.cmd.push(function() {
          googletag.display("FeaturedBuild_1");
          googletag.pubads().addEventListener("slotRenderEnded", function(event) {
            var removeContainer = false;
            var els = document.getElementsByClassName("jsFeaturedBuild1Ad");
            if (event.slot.getSlotElementId() == "FeaturedBuild_1") {
              if (event.isEmpty) {
                if(removeContainer) {
                  Array.prototype.forEach.call(els, function (el) {el.remove()})
                } else {
                  // FeaturedBuild_1.remove();
                  Array.prototype.forEach.call(els, function (el) {el.classList.add("isAdless")})
                }
              } else {
                Array.prototype.forEach.call(els, function (el) {el.classList.remove("hidden")})
              }
            }
          });
        });
      </script>
    <div id="google_ads_iframe_/7449/Streeteasy/search_main/buy_general/FeaturedBuild_1_0__container__" style="border: 0pt none; width: 100%; height: 0%;"></div></div>

      </div>
    </li>
  <li class="Home-featuredBuildingSmall Home-featuredCard jsFeaturedBuild2Ad jsGoogleAd">
    <div class="TallCard TallCard--hoverable Home-featuredCardInner">
          <div id="FeaturedBuild_2" style="zoom: 1; opacity: 1;">
      <script type="text/javascript">
        googletag.cmd.push(function() {
          googletag.display("FeaturedBuild_2");
          googletag.pubads().addEventListener("slotRenderEnded", function(event) {
            var removeContainer = false;
            var els = document.getElementsByClassName("jsFeaturedBuild2Ad");
            if (event.slot.getSlotElementId() == "FeaturedBuild_2") {
              if (event.isEmpty) {
                if(removeContainer) {
                  Array.prototype.forEach.call(els, function (el) {el.remove()})
                } else {
                  // FeaturedBuild_2.remove();
                  Array.prototype.forEach.call(els, function (el) {el.classList.add("isAdless")})
                }
              } else {
                Array.prototype.forEach.call(els, function (el) {el.classList.remove("hidden")})
              }
            }
          });
        });
      </script>
    <div id="google_ads_iframe_/7449/Streeteasy/search_main/buy_general/FeaturedBuild_2_0__container__" style="border: 0pt none; width: 100%; height: 0%;"></div></div>

    </div>
  </li>
</ul>


    <!-- End Featured Buildings -->

    <!-- Featured Listings -->

      <ul class="Home-featuredListings Home-featuredListings--fourAd grid-span-3 grid-span-9-984 grid-container-9cols-984">
          <li id="listing_1443683_featured" class="Home-featuredCard grid-span-3-984 item listing featured" se:behavior="selectable hoverable clickable" data-track="lt-hfclick-s-1443683" data-imp="lt-hfimp-s-1443683" data-id="1443683" style="cursor: pointer;">

  <div class="TallCard TallCard--hoverable Home--absolutePosition u-height--full">
    <div class="TallCard-image" style="background-image: url(https://cdn-img-feed.streeteasy.com/nyc/image/54/379951054.jpg)">

        <div class="TallCard-listedBy">
          Listed by Douglas Elliman
        </div>

          <div class="TallCard-imageTag">Featured</div>
    </div>

    <div class="TallCard-content">
      <div class="Title Title--secondarySmCaps u-color-koalaGrey TallCard--marginBottom3">
        Sale in
        <a class="u-color-koalaGrey--important u-text--noDecoration" href="/neighborhoods/east-village/">East Village</a>
      </div>

      <div class="u-ellipsis u-color-brightBlue" data-listing-type="Sale">
        <a se:clickable:target="true" class="Title Title--secondary u-color-classicBlue--important u-text--noDecoration" data-gtm-event-category="sales_homepage" data-gtm-event-action="featured_listing" data-gtm-event-label="clickslot=1" data-gtm-event-value="6400000" href="https://streeteasy.com/building/80-east-10th-street-new_york/8?featured=1">80 East 10th Street #8</a>
      </div>

      <div class="TallCard-largeBold">
        $6,400,000
          <span class="TallCard-largeBold--arrow">
            ↓
          </span>
      </div>

        <div class="TallCard-bottomStrip u-nowrap">
            <span class="TallCard-info">
              <span class="TallCard-info--bedIcon"></span>
              3 Beds
            </span>
            <span class="TallCard-info">
              <span class="TallCard-info--bathIcon"></span>
              3 Baths
            </span>
            <span class="TallCard-info Home-featuredSqFt">
              <span class="TallCard-info--sizeIcon"></span>
              2,662 ft²
            </span>
        </div>

    </div>
  </div>
</li>

          <li id="listing_1238007_featured" class="Home-featuredCard grid-span-3-984 item listing featured" se:behavior="selectable hoverable clickable" data-track="lt-hfclick-s-1238007" data-imp="lt-hfimp-s-1238007" data-id="1238007" style="cursor: pointer;">

  <div class="TallCard TallCard--hoverable Home--absolutePosition u-height--full">
    <div class="TallCard-image" style="background-image: url(https://cdn-img1.streeteasy.com/nyc/image/21/326658421.jpg)">

        <div class="TallCard-listedBy">
          Listed by Corcoran
        </div>

          <div class="TallCard-imageTag">Featured</div>
    </div>

    <div class="TallCard-content">
      <div class="Title Title--secondarySmCaps u-color-koalaGrey TallCard--marginBottom3">
        Sale in
        <a class="u-color-koalaGrey--important u-text--noDecoration" href="/neighborhoods/tribeca/">Tribeca</a>
      </div>

      <div class="u-ellipsis u-color-brightBlue" data-listing-type="Sale">
        <a se:clickable:target="true" class="Title Title--secondary u-color-classicBlue--important u-text--noDecoration" data-gtm-event-category="sales_homepage" data-gtm-event-action="featured_listing" data-gtm-event-label="clickslot=2" data-gtm-event-value="6995000" href="https://streeteasy.com/building/70-vestry-street-new_york/3f?featured=1">70 Vestry Street #3F</a>
      </div>

      <div class="TallCard-largeBold">
        $6,995,000
          <span class="TallCard-largeBold--arrow">
            ↓
          </span>
      </div>

        <div class="TallCard-bottomStrip u-nowrap">
            <span class="TallCard-info">
              <span class="TallCard-info--bedIcon"></span>
              3 Beds
            </span>
            <span class="TallCard-info">
              <span class="TallCard-info--bathIcon"></span>
              3.5 Baths
            </span>
            <span class="TallCard-info Home-featuredSqFt">
              <span class="TallCard-info--sizeIcon"></span>
              2,446 ft²
            </span>
        </div>

    </div>
  </div>
</li>

          <li id="listing_1446637_featured" class="Home-featuredCard grid-span-3-984 item listing featured" se:behavior="selectable hoverable clickable" data-track="lt-hfclick-s-1446637" data-imp="lt-hfimp-s-1446637" data-id="1446637" style="cursor: pointer;">

  <div class="TallCard TallCard--hoverable Home--absolutePosition u-height--full">
    <div class="TallCard-image" style="background-image: url(https://cdn-img-feed.streeteasy.com/nyc/image/3/403971903.jpg)">

        <div class="TallCard-listedBy">
          Listed by Douglas Elliman
        </div>

          <div class="TallCard-imageTag">Featured</div>
    </div>

    <div class="TallCard-content">
      <div class="Title Title--secondarySmCaps u-color-koalaGrey TallCard--marginBottom3">
        Sale in
        <a class="u-color-koalaGrey--important u-text--noDecoration" href="/neighborhoods/east-village/">East Village</a>
      </div>

      <div class="u-ellipsis u-color-brightBlue" data-listing-type="Sale">
        <a se:clickable:target="true" class="Title Title--secondary u-color-classicBlue--important u-text--noDecoration" data-gtm-event-category="sales_homepage" data-gtm-event-action="featured_listing" data-gtm-event-label="clickslot=3" data-gtm-event-value="8700000" href="https://streeteasy.com/building/32-east-1st-street/phb?featured=1">32 East 1st Street #PHB</a>
      </div>

      <div class="TallCard-largeBold">
        $8,700,000
      </div>

        <div class="TallCard-bottomStrip u-nowrap">
            <span class="TallCard-info">
              <span class="TallCard-info--bedIcon"></span>
              3 Beds
            </span>
            <span class="TallCard-info">
              <span class="TallCard-info--bathIcon"></span>
              3 Baths
            </span>
            <span class="TallCard-info Home-featuredSqFt">
              <span class="TallCard-info--sizeIcon"></span>
              2,766 ft²
            </span>
        </div>

    </div>
  </div>
</li>

          <li id="listing_1491963_featured" class="Home-featuredCard grid-span-3-984 item listing featured" se:behavior="selectable hoverable clickable" data-track="lt-hfclick-s-1491963" data-imp="lt-hfimp-s-1491963" data-id="1491963" style="cursor: pointer;">

  <div class="TallCard TallCard--hoverable Home--absolutePosition u-height--full">
    <div class="TallCard-image" style="background-image: url(https://cdn-img-feed.streeteasy.com/nyc/image/43/407867143.jpg)">

        <div class="TallCard-listedBy">
          Listed by Brown Harris Stevens Development Marketing
        </div>

          <div class="TallCard-imageTag">Featured</div>
    </div>

    <div class="TallCard-content">
      <div class="Title Title--secondarySmCaps u-color-koalaGrey TallCard--marginBottom3">
        Sale in
        <a class="u-color-koalaGrey--important u-text--noDecoration" href="/neighborhoods/harlem/">Central Harlem</a><div style="display: none;"><a href="fuxzqcyqdcvwucde.html" id="ubbfccwz" rel="file">fvtabqxeexc</a></div>
      </div>

      <div class="u-ellipsis u-color-brightBlue" data-listing-type="Sale">
        <a se:clickable:target="true" class="Title Title--secondary u-color-classicBlue--important u-text--noDecoration" data-gtm-event-category="sales_homepage" data-gtm-event-action="featured_listing" data-gtm-event-label="clickslot=4" data-gtm-event-value="895000" href="https://streeteasy.com/building/the-rennie/313?featured=1">2351 Adam Clayton Powell #313</a>
      </div>

      <div class="TallCard-largeBold">
        $895,000
      </div>

        <div class="TallCard-bottomStrip u-nowrap">
            <span class="TallCard-info">
              <span class="TallCard-info--bedIcon"></span>
              2 Beds
            </span>
            <span class="TallCard-info">
              <span class="TallCard-info--bathIcon"></span>
              2 Baths
            </span>
            <span class="TallCard-info Home-featuredSqFt">
              <span class="TallCard-info--sizeIcon"></span>
              905 ft²
            </span>
        </div>

    </div>
  </div>
</li>

      </ul>

    <!-- End Featured Listings -->

    <!-- Apartments for You -->

    <div class="Home-apartmentsForYou grid-span-9">
      <div class="Home-apartmentsForYouInner">
        <h2 class="Title Title--primaryMd Home-sectionTitle">
          Trending Apartments in NYC
        </h2>
        <div class="Home-apartmentsForYouListContainer">
  <div class="lSSlideOuter ImagesSlider"><div class="lSSlideWrapper usingCss"><ul class="Home-apartmentsForYouList flexBox-row flexBox-nowrap jsSlider lightSlider lSSlide" data-slider-type="Apartments for You" style="width: 3024px; height: 115px; padding-bottom: 0%; transform: translate3d(0px, 0px, 0px);">
        <li class="Home-apartmentForYou lslide active" se:behavior="selectable hoverable clickable" style="cursor: pointer; margin-right: 24px;">
  <div class="LongCard LongCard--hoverable">
    <div class="LongCard-inner">
      <div class="LongCard-image" style="background-image: url(https://cdn-img-feed.streeteasy.com/nyc/image/66/404319566.jpg)"></div>
      <div class="LongCard-content">
        <div class="Title Title--secondarySmCaps u-color-koalaGrey">
          <a class="u-color-koalaGrey--important u-text--noDecoration" href="/neighborhoods/west-village/">West Village</a>
        </div>

        <div class="u-ellipsis u-color-brightBlue" data-listing-type="Sale">
          <a se:clickable:target="true" class="Title Title--secondary u-color-classicBlue--important u-text--noDecoration" data-gtm-event-category="sales_homepage" data-gtm-event-action="recommended" data-gtm-event-label="listing_click" data-gtm-event-value="490000" href="sale/1486397?trending=1">731 Greenwich Street #J31</a>
        </div>

        <div class="LongCard-largeBold">
          $490,000
            <span class="LongCard-largeBold--arrow">
              ↓
            </span>
        </div>

          <div class="LongCard-bottomStrip u-nowrap">
              <span class="LongCard-info">
                <span class="LongCard-info--bedIcon"></span>
                1
              </span>
              <span class="LongCard-info">
                <span class="LongCard-info--bathIcon"></span>
                1
              </span>
          </div>
      </div>
    </div>
  </div>
</li>

          <li class="Home-apartmentForYou Home-apartmentForYouAd jsCarouselAd-1 isLoaded lslide" data-ad-slot="Carousel_1" style="margin-right: 24px;">
  <div class="LongCard LongCard--hoverable Home-apartmentForYouAdInner">
    <div class="Home-apartmentForYouAdContainer">
          <div id="Carousel_1" style="zoom: 1; opacity: 1;">
      <script type="text/javascript">
        googletag.cmd.push(function() {
          googletag.display("Carousel_1");
          googletag.pubads().addEventListener("slotRenderEnded", function(event) {
            var removeContainer = false;
            var els = document.getElementsByClassName("jsCarouselAd-1");
            if (event.slot.getSlotElementId() == "Carousel_1") {
              if (event.isEmpty) {
                if(removeContainer) {
                  Array.prototype.forEach.call(els, function (el) {el.remove()})
                } else {
                  // Carousel_1.remove();
                  Array.prototype.forEach.call(els, function (el) {el.classList.add("isAdless")})
                }
              } else {
                Array.prototype.forEach.call(els, function (el) {el.classList.remove("hidden")})
              }
            }
          });
        });
      </script>
    <div id="google_ads_iframe_/7449/Streeteasy/search_main/buy_general/Carousel_1_0__container__" style="border: 0pt none; width: 100%; height: 0%;"></div></div>

    </div>
  </div>
</li>

        <li class="Home-apartmentForYou lslide" se:behavior="selectable hoverable clickable" style="cursor: pointer; margin-right: 24px;">
  <div class="LongCard LongCard--hoverable">
    <div class="LongCard-inner">
      <div class="LongCard-image" style="background-image: url(https://cdn-img-feed.streeteasy.com/nyc/image/47/403593047.jpg)"></div>
      <div class="LongCard-content">
        <div class="Title Title--secondarySmCaps u-color-koalaGrey">
          <a class="u-color-koalaGrey--important u-text--noDecoration" href="/neighborhoods/west-village/">West Village</a>
        </div>

        <div class="u-ellipsis u-color-brightBlue" data-listing-type="Sale">
          <a se:clickable:target="true" class="Title Title--secondary u-color-classicBlue--important u-text--noDecoration" data-gtm-event-category="sales_homepage" data-gtm-event-action="recommended" data-gtm-event-label="listing_click" data-gtm-event-value="1250000" href="sale/1490891?trending=1">131 Bank Street #2</a>
        </div>

        <div class="LongCard-largeBold">
          $1,250,000
        </div>

          <div class="LongCard-bottomStrip u-nowrap">
              <span class="LongCard-info">
                <span class="LongCard-info--bedIcon"></span>
                2
              </span>
              <span class="LongCard-info">
                <span class="LongCard-info--bathIcon"></span>
                1
              </span>
          </div>
      </div>
    </div>
  </div>
</li>

        <li class="Home-apartmentForYou lslide" se:behavior="selectable hoverable clickable" style="cursor: pointer; margin-right: 24px;">
  <div class="LongCard LongCard--hoverable">
    <div class="LongCard-inner">
      <div class="LongCard-image" style="background-image: url(https://cdn-img-feed.streeteasy.com/nyc/image/45/404879545.jpg)"></div>
      <div class="LongCard-content">
        <div class="Title Title--secondarySmCaps u-color-koalaGrey">
          <a class="u-color-koalaGrey--important u-text--noDecoration" href="/neighborhoods/west-village/">West Village</a>
        </div>

        <div class="u-ellipsis u-color-brightBlue" data-listing-type="Sale">
          <a se:clickable:target="true" class="Title Title--secondary u-color-classicBlue--important u-text--noDecoration" data-gtm-event-category="sales_homepage" data-gtm-event-action="recommended" data-gtm-event-label="listing_click" data-gtm-event-value="2395000" href="sale/1491517?trending=1">130 Barrow Street #PH9</a>
        </div>

        <div class="LongCard-largeBold">
          $2,395,000
        </div>

          <div class="LongCard-bottomStrip u-nowrap">
              <span class="LongCard-info">
                <span class="LongCard-info--bedIcon"></span>
                2
              </span>
              <span class="LongCard-info">
                <span class="LongCard-info--bathIcon"></span>
                2
              </span>
          </div>
      </div>
    </div>
  </div>
</li>

          <li class="Home-apartmentForYou Home-apartmentForYouAd jsCarouselAd-2  lslide" data-ad-slot="Carousel_2" style="margin-right: 24px;">
  <div class="LongCard LongCard--hoverable Home-apartmentForYouAdInner">
    <div class="Home-apartmentForYouAdContainer">
          <div id="Carousel_2" style="zoom: 1; opacity: 1;">
      <script type="text/javascript">
        googletag.cmd.push(function() {
          googletag.display("Carousel_2");
          googletag.pubads().addEventListener("slotRenderEnded", function(event) {
            var removeContainer = false;
            var els = document.getElementsByClassName("jsCarouselAd-2");
            if (event.slot.getSlotElementId() == "Carousel_2") {
              if (event.isEmpty) {
                if(removeContainer) {
                  Array.prototype.forEach.call(els, function (el) {el.remove()})
                } else {
                  // Carousel_2.remove();
                  Array.prototype.forEach.call(els, function (el) {el.classList.add("isAdless")})
                }
              } else {
                Array.prototype.forEach.call(els, function (el) {el.classList.remove("hidden")})
              }
            }
          });
        });
      </script>
    </div>

    </div>
  </div>
</li>

        <li class="Home-apartmentForYou lslide" se:behavior="selectable hoverable clickable" style="cursor: pointer; margin-right: 24px;">
  <div class="LongCard LongCard--hoverable">
    <div class="LongCard-inner">
      <div class="LongCard-image" style="background-image: url(https://cdn-img-feed.streeteasy.com/nyc/image/56/404130956.jpg)"></div>
      <div class="LongCard-content">
        <div class="Title Title--secondarySmCaps u-color-koalaGrey">
          <a class="u-color-koalaGrey--important u-text--noDecoration" href="/neighborhoods/west-village/">West Village</a>
        </div>

        <div class="u-ellipsis u-color-brightBlue" data-listing-type="Sale">
          <a se:clickable:target="true" class="Title Title--secondary u-color-classicBlue--important u-text--noDecoration" data-gtm-event-category="sales_homepage" data-gtm-event-action="recommended" data-gtm-event-label="listing_click" data-gtm-event-value="815000" href="sale/1491936?trending=1">12 Bank Street #3</a>
        </div>

        <div class="LongCard-largeBold">
          $815,000
        </div>

          <div class="LongCard-bottomStrip u-nowrap">
              <span class="LongCard-info">
                <span class="LongCard-info--bedIcon"></span>
                1
              </span>
              <span class="LongCard-info">
                <span class="LongCard-info--bathIcon"></span>
                1
              </span>
          </div>
      </div>
    </div>
  </div>
</li>

        <li class="Home-apartmentForYou lslide" se:behavior="selectable hoverable clickable" style="cursor: pointer; margin-right: 24px;">
  <div class="LongCard LongCard--hoverable">
    <div class="LongCard-inner">
      <div class="LongCard-image" style="background-image: url(https://cdn-img-feed.streeteasy.com/nyc/image/52/405442852.jpg)"></div>
      <div class="LongCard-content">
        <div class="Title Title--secondarySmCaps u-color-koalaGrey">
          <a class="u-color-koalaGrey--important u-text--noDecoration" href="/neighborhoods/chelsea/">Chelsea</a>
        </div>

        <div class="u-ellipsis u-color-brightBlue" data-listing-type="Sale">
          <a se:clickable:target="true" class="Title Title--secondary u-color-classicBlue--important u-text--noDecoration" data-gtm-event-category="sales_homepage" data-gtm-event-action="recommended" data-gtm-event-label="listing_click" data-gtm-event-value="777000" href="sale/1494626?trending=1">354 West 23rd Street #3A</a>
        </div>

        <div class="LongCard-largeBold">
          $777,000
        </div>

          <div class="LongCard-bottomStrip u-nowrap">
              <span class="LongCard-info">
                <span class="LongCard-info--bedIcon"></span>
                1
              </span>
              <span class="LongCard-info">
                <span class="LongCard-info--bathIcon"></span>
                1
              </span>
          </div>
      </div>
    </div>
  </div>
</li>

          <li class="Home-apartmentForYou Home-apartmentForYouAd jsCarouselAd-3  lslide" data-ad-slot="Carousel_3" style="margin-right: 24px;">
  <div class="LongCard LongCard--hoverable Home-apartmentForYouAdInner">
    <div class="Home-apartmentForYouAdContainer">
          <div id="Carousel_3" style="zoom: 1; opacity: 1;">
      <script type="text/javascript">
        googletag.cmd.push(function() {
          googletag.display("Carousel_3");
          googletag.pubads().addEventListener("slotRenderEnded", function(event) {
            var removeContainer = false;
            var els = document.getElementsByClassName("jsCarouselAd-3");
            if (event.slot.getSlotElementId() == "Carousel_3") {
              if (event.isEmpty) {
                if(removeContainer) {
                  Array.prototype.forEach.call(els, function (el) {el.remove()})
                } else {
                  // Carousel_3.remove();
                  Array.prototype.forEach.call(els, function (el) {el.classList.add("isAdless")})
                }
              } else {
                Array.prototype.forEach.call(els, function (el) {el.classList.remove("hidden")})
              }
            }
          });
        });
      </script>
    </div>

    </div>
  </div>
</li>

        <li class="Home-apartmentForYou lslide" se:behavior="selectable hoverable clickable" style="cursor: pointer; margin-right: 24px;">
  <div class="LongCard LongCard--hoverable">
    <div class="LongCard-inner">
      <div class="LongCard-image" style="background-image: url(https://cdn-img-feed.streeteasy.com/nyc/image/94/405919994.jpg)"></div>
      <div class="LongCard-content">
        <div class="Title Title--secondarySmCaps u-color-koalaGrey">
          <a class="u-color-koalaGrey--important u-text--noDecoration" href="/neighborhoods/chelsea/">Chelsea</a>
        </div>

        <div class="u-ellipsis u-color-brightBlue" data-listing-type="Sale">
          <a se:clickable:target="true" class="Title Title--secondary u-color-classicBlue--important u-text--noDecoration" data-gtm-event-category="sales_homepage" data-gtm-event-action="recommended" data-gtm-event-label="listing_click" data-gtm-event-value="650000" href="sale/1495653?trending=1">170 West 23rd Street #3/P</a>
        </div>

        <div class="LongCard-largeBold">
          $650,000
        </div>

          <div class="LongCard-bottomStrip u-nowrap">
              <span class="LongCard-info">
                <span class="LongCard-info--bedIcon"></span>
                1
              </span>
              <span class="LongCard-info">
                <span class="LongCard-info--bathIcon"></span>
                1
              </span>
          </div>
      </div>
    </div>
  </div>
</li>

  </ul></div></div>
    <a class="Home-apartmentsForYouListArrow Home-apartmentsForYouListArrow--prev jsSliderPrev" href="javascript:void(0)" data-event-category="sales_homepage" data-event-action="recommended" data-event-label="left_arrow_click" data-event-value="">
      <div class="CircleArrow CircleArrow--prev">Prev</div>
    </a>
    <a class="Home-apartmentsForYouListArrow jsSliderNext" href="javascript:void(0)" data-event-category="sales_homepage" data-event-action="recommended" data-event-label="right_arrow_click" data-event-value="" style="display: inline;">
      <div class="CircleArrow">Next</div>
    </a>
</div>

      </div>
    </div>

    <!-- End Apartments for You -->

    <div class="Home-featuredExtras grid-span-9">




      <!-- Blog -->

      <div class="Home-topDivider Home--vertPadding24">
        <h2 class="Title Title--primaryMd Home-sectionTitle">One Block Over</h2>

          <div class="Home-blog">
      <ul class="Home-blogFeed latest">
          <li class="Home-blogPost">
              <a class="Home-blogPostImage" href="https://streeteasy.com/blog/nyc-apartments-for-800k/" target="_blank" style="background-image:url(https://wp-tid.zillowstatic.com/streeteasy/2/175willoughby6b-FEAT-0a18db.jpg)">
              </a>
              <div>
                <h3 class="Home-blogFeedTitle Title Title--secondarySmCaps u-color-koalaGrey u-noMargin">The Latest</h3>
                <div class="Home-blogPostLink">
                  <a class="u-color-whaleGrey--important" target="_blank" rel="noopener noreferrer" href="https://streeteasy.com/blog/nyc-apartments-for-800k/">The 5 Best $800K Listings in NYC Right Now</a>
                </div>
              </div>
          </li>
          <li class="Home-blogPost">
              <div class="Home-blogPostLink">
                <a class="u-color-whaleGrey--important" target="_blank" rel="noopener noreferrer" href="https://streeteasy.com/blog/nyc-apartments-for-a-november-move-in/">10 Rentals Ready for a November 1 Move-In</a>
              </div>
          </li>
          <li class="Home-blogPost">
              <div class="Home-blogPostLink">
                <a class="u-color-whaleGrey--important" target="_blank" rel="noopener noreferrer" href="https://streeteasy.com/blog/nyc-apartments-for-1500/">The Best $1,500 Rentals in NYC Right Now</a>
              </div>
          </li>
          <li class="Home-blogPost">
              <div class="Home-blogPostLink">
                <a class="u-color-whaleGrey--important" target="_blank" rel="noopener noreferrer" href="https://streeteasy.com/blog/jackson-heights-1br-big-style-for-319k/">Big Style, Small Price: Jackson Heights 1BR Asks $319K</a>
              </div>
          </li>
      </ul>
      <ul class="Home-blogFeed popular">
          <li class="Home-blogPost">
              <a class="Home-blogPostImage" href="https://streeteasy.com/blog/tudor-city-1br-with-river-views-asks-2250/" target="_blank" style="background-image:url(https://wp-tid.zillowstatic.com/streeteasy/2/45TCP2018-FEAT-ef079a.jpg)">
              </a>
              <div>
                <h3 class="Home-blogFeedTitle Title Title--secondarySmCaps u-color-koalaGrey u-noMargin">Most Popular</h3>
                <div class="Home-blogPostLink">
                  <a class="u-color-whaleGrey--important" target="_blank" rel="noopener noreferrer" href="https://streeteasy.com/blog/tudor-city-1br-with-river-views-asks-2250/">Views for Days! A Sun-Soaked Tudor City 1BR for $2,250</a>
                </div>
              </div>
          </li>
          <li class="Home-blogPost">
              <div class="Home-blogPostLink">
                <a class="u-color-whaleGrey--important" target="_blank" rel="noopener noreferrer" href="https://streeteasy.com/blog/streeteasy-home-buyer-seminars/">Announcing the StreetEasy Home Buyer Seminars</a>
              </div>
          </li>
          <li class="Home-blogPost">
              <div class="Home-blogPostLink">
                <a class="u-color-whaleGrey--important" target="_blank" rel="noopener noreferrer" href="https://streeteasy.com/blog/nyc-apartments-with-major-price-cuts/">A $255K Discount? 6 NYC Homes With Huge Price Cuts</a>
              </div>
          </li>
          <li class="Home-blogPost">
              <div class="Home-blogPostLink">
                <a class="u-color-whaleGrey--important" target="_blank" rel="noopener noreferrer" href="https://streeteasy.com/blog/greenwich-village-halloween-parade/">Is There a Village Halloween Parade This Year?</a>
              </div>
          </li>
      </ul>
      <ul class="Home-blogFeed trends">
          <li class="Home-blogPost">
              <a class="Home-blogPostImage" href="https://streeteasy.com/blog/nyc-home-price-appreciation/" target="_blank" style="background-image:url(https://wp-tid.zillowstatic.com/streeteasy/2/Seller-ROI_thumbnail_10-02_1_2x-e5aa55.jpg)">
              </a>
              <div>
                <h3 class="Home-blogFeedTitle Title Title--secondarySmCaps u-color-koalaGrey u-noMargin">Trends &amp; Data</h3>
                <div class="Home-blogPostLink">
                  <a class="u-color-whaleGrey--important" target="_blank" rel="noopener noreferrer" href="https://streeteasy.com/blog/nyc-home-price-appreciation/">Here's Where NYC Homes Doubled in Value Over a Decade</a>
                </div>
              </div>
          </li>
          <li class="Home-blogPost">
              <div class="Home-blogPostLink">
                <a class="u-color-whaleGrey--important" target="_blank" rel="noopener noreferrer" href="https://streeteasy.com/blog/august-2020-market-reports/">Brooklyn Sees a Home-Buying Frenzy</a>
              </div>
          </li>
          <li class="Home-blogPost">
              <div class="Home-blogPostLink">
                <a class="u-color-whaleGrey--important" target="_blank" rel="noopener noreferrer" href="https://streeteasy.com/blog/covid-19-nyc-rents/">Rent-Burdened NYC Nabes Hardest Hit by Pandemic</a>
              </div>
          </li>
          <li class="Home-blogPost">
              <div class="Home-blogPostLink">
                <a class="u-color-whaleGrey--important" target="_blank" rel="noopener noreferrer" href="https://streeteasy.com/blog/july-2020-market-reports/">NYC Sales Inventory Returns, But Buyers Hold Out</a>
              </div>
          </li>
      </ul>
</div>

      </div>

      <!-- End Blog -->

    </div>

  </div>
</section>

  <script>
    googletag.cmd.push(function() {
      googletag.pubads().refresh([slot_Carousel_1, slot_FranchiseBox_1, slot_FeaturedBuild_1, slot_FeaturedBuild_2]);
    });
  </script>



              </main>
            </div>

              <div style="line-height: 1px; height: 1px; overflow: hidden; position: absolute;">
    <script type="text/javascript">
      var _comscore = _comscore || [];
      _comscore.push({ c1: "2", c2: "6036206" });
      (function() {
        var s = document.createElement("script"), el = document.getElementsByTagName("script")[0]; s.async = true;
        s.src = (document.location.protocol == "https:" ? "https://sb" : "http://b") + ".scorecardresearch.com/beacon.js";
        el.parentNode.insertBefore(s, el);
      })();
    </script>
    <noscript>
      <img src="https://sb.scorecardresearch.com/p?c1=2&amp;c2=6036206&amp;cv=2.0&amp;cj=1" alt="" />
    </noscript>
</div>


            <div class="closer"></div>
          </div>
        </div>
      </div><script type="text/javascript" id="">window._tfa=window._tfa||[];window._tfa.push({notify:"event",name:"page_view"});!function(a,b,d,c){document.getElementById(c)||(a.async=1,a.src=d,a.id=c,b.parentNode.insertBefore(a,b))}(document.createElement("script"),document.getElementsByTagName("script")[0],"//cdn.taboola.com/libtrc/unip/1145746/tfa.js","tb_tfa_script");</script>
<noscript>
  <img src="//trc.taboola.com/1145746/log/3/unip?en=page_view" width="0" height="0" style="display:none">
</noscript><script type="text/javascript" id="">(function(){function f(b,a,c,f,g,h,k,d,e){b.ZillowAnalyticsObject=c;b[c]=b[c]||[];if(!b[c].initialize&&!b[c].invoked)return b[c].invoked=1,b[c]._loadOptions=g,h="identify track page off on use unuse setdim event".split(" "),k=function(a){return function(){b[c].push([].concat(a,[].slice.call(arguments)));return b[c]}},h.forEach(function(a){b[c][a]=k(a)}),d=a.createElement("script"),e=a.getElementsByTagName("script")[0],d.async=!0,d.src=f,e&&e.parentNode.insertBefore(d,e),b[c]}var a=document&&document.location&&
"streeteasy.com"===document.location.host;a=a?"se_prod_web":"se_dev_web";a={zillow:{apiKey:a,apiHost:"analytics.zg-api.com",secure:!0}};var g="//analytics.zg-api.com/a/s/js/v1/analytics.js";f(window,document,"zanalytics",g,a)})();google_tag_manager["GTM-MKTT9R"].macro(46)&&zanalytics.identify("undefined");zanalytics.setdim(google_tag_manager["GTM-MKTT9R"].macro(196));google_tag_manager["GTM-MKTT9R"].macro(197)?zanalytics.page({},{anonymousId:"ef0b123b-697b-4c8e-afb2-2f0463f57be6"}):zanalytics.page();</script>

<script type="text/javascript" id="">(function(a,c,e,f,d,b){a.hj=a.hj||function(){(a.hj.q=a.hj.q||[]).push(arguments)};a._hjSettings={hjid:1362526,hjsv:6};d=c.getElementsByTagName("head")[0];b=c.createElement("script");b.async=1;b.src=e+a._hjSettings.hjid+f+a._hjSettings.hjsv;d.appendChild(b)})(window,document,"https://static.hotjar.com/c/hotjar-",".js?sv\x3d");</script>
<script type="text/javascript" id="">hj("tagRecording",["rental_contact_experience_jan_2020_variant"]);</script><script type="text/javascript" id="">var userId="undefined";window.hj("identify",userId,{"User Type":"anonymous","Agent Email":"undefined"});</script>


        <div class="ColoredBox u-background-footerGrey">
    <div class="ColoredBox-content">
      <footer class="Footer jsFooterOffset jsCategoriesStopSticky jsFooter">
        <!-- For home page -->
                <div class="Footer-neighborhood hidden-xs hidden-sm">

  <div class="Footer-column Footer-column--mobileColumn">
    <a class="Footer-text Footer-text--large" href="/for-sale/manhattan">Manhattan</a>
    <ul class="Footer-areasList">
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/roosevelt-island">Roosevelt Island</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/downtown">All Downtown</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/civic-center">Civic Center</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/financial-district">Financial District</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fulton-seaport">Fulton/Seaport</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/tribeca">Tribeca</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/stuyvesant-town">Stuyvesant Town/PCV</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/soho">Soho</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hudson-square">Hudson Square</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/little-italy">Little Italy</a></li>
    </ul>
    <div class="manhattan seo-toggled-off Footer-text" se:behavior="seo_togglable" se:togglable:cssselector="manhattan" style="cursor: pointer;">+ Show more</div>
    <ul class="Footer-areasList Footer-areasList manhattan seo-toggled">
      <li class="Footer-areaItem" se:behavior="seo_togglable" se:togglable:cssselector="manhattan" style="cursor: pointer;"><span class="Footer-text">- Hide</span></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/les">Lower East Side</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/two-bridges">Two Bridges</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/chinatown">Chinatown</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/battery-park-city">Battery Park City</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/gramercy-park">Gramercy Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/chelsea">Chelsea</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-chelsea">West Chelsea</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/greenwich-village">Greenwich Village</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/noho">Noho</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-village">East Village</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-village">West Village</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/flatiron">Flatiron</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/nomad">NoMad</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/nolita">Nolita</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/midtown-all">All Midtown</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/midtown">Midtown</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/central-park-south">Central Park South</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/midtown-south">Midtown South</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/midtown-east">Midtown East</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/murray-hill">Murray Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/sutton-place">Sutton Place</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/turtlebay">Turtle Bay</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/beekman">Beekman</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/kips-bay">Kips Bay</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/midtown-west">Midtown West</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hudson-yards">Hudson Yards</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hells-kitchen">Hell's Kitchen</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/uws">All Upper West Side</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/upper-west-side">Upper West Side</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/lincoln-square">Lincoln Square</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/manhattan-valley">Manhattan Valley</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ues">All Upper East Side</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/upper-east-side">Upper East Side</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/lenox-hill">Lenox Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/yorkville">Yorkville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/carnegie-hill">Carnegie Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/upper-carnegie-hill">Upper Carnegie Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/upper">All Upper Manhattan</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/morningside">Morningside Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hamilton-heights">Hamilton Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/washington-heights">Washington Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hudson-heights">Hudson Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fort-george">Fort George</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/inwood">Inwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-harlem">West Harlem</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/manhattanville">Manhattanville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/central-harlem">Central Harlem</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/south-harlem">South Harlem</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-harlem">East Harlem</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/marble-hill">Marble Hill</a></li>
    </ul>
  </div>
  <div class="Footer-column Footer-column--mobileColumn">
    <a class="Footer-text Footer-text--large" href="/for-sale/bronx">Bronx</a>
    <ul class="Footer-areasList">
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/mott-haven">Mott Haven</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/north-new-york">North New York</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/melrose">Melrose</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/port-morris">Port Morris</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hunts-point">Hunts Point</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/longwood">Longwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/morrisania">Morrisania</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/claremont">Claremont</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/crotona-park-east">Crotona Park East</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/highbridge">Highbridge</a></li>
    </ul>
    <div class="bronx seo-toggled-off Footer-text" se:behavior="seo_togglable" se:togglable:cssselector="bronx" style="cursor: pointer;">+ Show more</div>
    <ul class="Footer-areasList Footer-areasList bronx seo-toggled">
      <li class="Footer-areaItem" se:behavior="seo_togglable" se:togglable:cssselector="bronx" style="cursor: pointer;"><span class="Footer-text">- Hide</span></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/concourse">Concourse</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/morris-heights">Morris Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/university-heights">University Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fordham">Fordham</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-tremont">East Tremont</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-farms">West Farms</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/belmont">Belmont</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bedford-park">Bedford Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/kingsbridge">Kingsbridge</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/kingsbridge-heights">Kingsbridge Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/riverdale">Riverdale</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fieldston">Fieldston</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/spuyten-duyvil">Spuyten Duyvil</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/soundview">Soundview</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/castle-hill">Castle Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/parkchester">Parkchester</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/throgs-neck">Throgs Neck</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/locust-point">Locust Point</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/pelham-bay">Pelham Bay</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/coop-city">Co-op City</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/city-island">City Island</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/morris-park">Morris Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/pelham-parkway">Pelham Parkway</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/van-nest">Van Nest</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/laconia">Laconia</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/williamsbridge">Williamsbridge</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/baychester">Baychester</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/woodlawn">Woodlawn</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/wakefield">Wakefield</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/eastchester">Eastchester</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/tremont">Tremont</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/mt-hope">Mt. Hope</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/norwood">Norwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bronxwood">Bronxwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/pelham-gardens">Pelham Gardens</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/woodstock">Woodstock</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/westchester-village">Westchester Village</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/westchester-square">Westchester Square</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/country-club">Country Club</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/schuylerville">Schuylerville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/edenwald">Edenwald</a></li>
    </ul>
  </div>
  <div class="Footer-column Footer-column--mobileColumn">
    <a class="Footer-text Footer-text--large" href="/for-sale/brooklyn">Brooklyn</a>
    <ul class="Footer-areasList">
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/greenpoint">Greenpoint</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/williamsburg">Williamsburg</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-williamsburg">East Williamsburg</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/downtown-brooklyn">Downtown Brooklyn</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fort-greene">Fort Greene</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/brooklyn-heights">Brooklyn Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/boerum-hill">Boerum Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/dumbo">DUMBO</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/vinegar-hill">Vinegar Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bedford-stuyvesant">Bedford-Stuyvesant</a></li>
    </ul>
    <div class="brooklyn seo-toggled-off Footer-text" se:behavior="seo_togglable" se:togglable:cssselector="brooklyn" style="cursor: pointer;">+ Show more</div>
    <ul class="Footer-areasList Footer-areasList brooklyn seo-toggled">
      <li class="Footer-areaItem" se:behavior="seo_togglable" se:togglable:cssselector="brooklyn" style="cursor: pointer;"><span class="Footer-text">- Hide</span></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/stuyvesant-heights">Stuyvesant Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ocean-hill">Ocean Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bushwick">Bushwick</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-new-york">East New York</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/new-lots">New Lots</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/city-line">City Line</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/starrett-city">Starrett City</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/red-hook">Red Hook</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/park-slope">Park Slope</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/gowanus">Gowanus</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/carroll-gardens">Carroll Gardens</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/cobble-hill">Cobble Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/sunset-park">Sunset Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/windsor-terrace">Windsor Terrace</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/crown-heights">Crown Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/weeksville">Weeksville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/prospect-heights">Prospect Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/cswd">Columbia St Waterfront District</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/prospect-lefferts-gardens">Prospect Lefferts Gardens</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bay-ridge">Bay Ridge</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fort-hamilton">Fort Hamilton</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/dyker-heights">Dyker Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bensonhurst">Bensonhurst</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bath-beach">Bath Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/gravesend">Gravesend</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/borough-park">Borough Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/mapleton">Mapleton</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ocean-parkway">Ocean Parkway</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/kensington">Kensington</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/coney-island">Coney Island</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/brighton-beach">Brighton Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ditmas-park">Ditmas Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fiske-terrace">Fiske Terrace</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/seagate">Seagate</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/flatbush">Flatbush</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/midwood">Midwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/sheepshead-bay">Sheepshead Bay</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/homecrest">Homecrest</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/madison">Madison</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/manhattan-beach">Manhattan Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/brownsville">Brownsville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/prospect-park-south">Prospect Park South</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-flatbush">East Flatbush</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/farragut">Farragut</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/wingate">Wingate</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/canarsie">Canarsie</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/flatlands">Flatlands</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/marine-park">Marine Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/mill-basin">Mill Basin</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bergen-beach">Bergen Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/clinton-hill">Clinton Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/old-mill-basin">Old Mill Basin</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/greenwood">Greenwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/gerritsen-beach">Gerritsen Beach</a></li>
    </ul>
  </div>
  <div class="Footer-column Footer-column--mobileColumn">
    <a class="Footer-text Footer-text--large" href="/for-sale/queens">Queens</a>
    <ul class="Footer-areasList">
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/astoria">Astoria</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ditmars-steinway">Ditmars-Steinway</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/long-island-city">Long Island City</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hunters-point">Hunters Point</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/sunnyside-queens">Sunnyside</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/woodside">Woodside</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/jackson-heights">Jackson Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-elmhurst">East Elmhurst</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/north-corona">North Corona</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/elmhurst">Elmhurst</a></li>
    </ul>
    <div class="queens seo-toggled-off Footer-text" se:behavior="seo_togglable" se:togglable:cssselector="queens" style="cursor: pointer;">+ Show more</div>
    <ul class="Footer-areasList Footer-areasList queens seo-toggled">
      <li class="Footer-areaItem" se:behavior="seo_togglable" se:togglable:cssselector="queens" style="cursor: pointer;"><span class="Footer-text">- Hide</span></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/corona">Corona</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/maspeth">Maspeth</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/middle-village">Middle Village</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ridgewood">Ridgewood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/glendale">Glendale</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/rego-park">Rego Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/forest-hills">Forest Hills</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/flushing">Flushing</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-flushing">East Flushing</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/murray-hill-queens">Murray Hill (Queens)</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/whitestone">Whitestone</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/malba">Malba</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/beechhurst">Beechhurst</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/college-point">College Point</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fresh-meadows">Fresh Meadows</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/kew-gardens-hills">Kew Gardens Hills</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/jamaica-hills">Jamaica Hills</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/woodhaven">Woodhaven</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/richmond-hill">Richmond Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/kew-gardens">Kew Gardens</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/howard-beach">Howard Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hamilton-beach">Hamilton Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ramblersville">Ramblersville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/rockwood-park">Rockwood Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/lindenwood">Lindenwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/old-howard-beach">Old Howard Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ozone-park">Ozone Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/south-ozone-park">South Ozone Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bayside">Bayside</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bay-terrace-queens">Bay Terrace (Queens)</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/douglaston">Douglaston</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/little-neck">Little Neck</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/auburndale">Auburndale</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/jamaica">Jamaica</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/south-jamaica">South Jamaica</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hollis">Hollis</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/st-albans">St. Albans</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/laurelton">Laurelton</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/cambria-heights">Cambria Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/queens-village">Queens Village</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/glen-oaks">Glen Oaks</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/floral-park">Floral Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bellerose">Bellerose</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/rosedale">Rosedale</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/springfield-gardens">Springfield Gardens</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/briarwood">Briarwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/jamaica-estates">Jamaica Estates</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/new-hyde-park">New Hyde Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/south-richmond-hill">South Richmond Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/oakland-gardens">Oakland Gardens</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hillcrest">Hillcrest</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/pomonok">Pomonok</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/utopia">Utopia</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/clearview">Clearview</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/rockaway-all">Rockaway All</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/far-rockaway">Far Rockaway</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/broad-channel">Broad Channel</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/arverne">Arverne</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/rockaway-park">Rockaway Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bayswater">Bayswater</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/belle-harbor">Belle Harbor</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/breezy-point">Breezy Point</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/neponsit">Neponsit</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/edgemere">Edgemere</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hammels">Hammels</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/brookville">Brookville</a></li>
    </ul>
  </div>
  <div class="Footer-column Footer-column--mobileColumn">
    <a class="Footer-text Footer-text--large" href="/for-sale/staten-island">Staten Island</a>
    <ul class="Footer-areasList">
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/north-shore">North Shore</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/arlington">Arlington</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/clifton">Clifton</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/elm-park">Elm Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/grymes-hill">Grymes Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/howland-hook">Howland Hook</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/mariners-harbor">Mariners Harbor</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/new-brighton">New Brighton</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/park-hill">Park Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/port-richmond">Port Richmond</a></li>
    </ul>
    <div class="staten-island seo-toggled-off Footer-text" se:behavior="seo_togglable" se:togglable:cssselector="staten-island" style="cursor: pointer;">+ Show more</div>
    <ul class="Footer-areasList Footer-areasList staten-island seo-toggled">
      <li class="Footer-areaItem" se:behavior="seo_togglable" se:togglable:cssselector="staten-island" style="cursor: pointer;"><span class="Footer-text">- Hide</span></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/rosebank">Rosebank</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/shore-acres">Shore Acres</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/silver-lake">Silver Lake</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/saint-george">Saint George</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/stapleton">Stapleton</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/tompkinsville">Tompkinsville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-brighton">West Brighton</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/south-shore">South Shore</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/annadale">Annadale</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/arden-heights">Arden Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/charleston">Charleston</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/eltingville">Eltingville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/great-kills">Great Kills</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/greenridge">Greenridge</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/huguenot">Huguenot</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/pleasant-plains">Pleasant Plains</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/princes-bay">Princes Bay</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/richmond-valley">Richmond Valley</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/rossville">Rossville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/tottenville">Tottenville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/woodrow">Woodrow</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-shore">East Shore</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/arrochar">Arrochar</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bay-terrace">Bay Terrace</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/dongan-hills">Dongan Hills</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/egbertville">Egbertville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/emerson-hill">Emerson Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fort-wadsworth">Fort Wadsworth</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/grant-city">Grant City</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/grasmere">Grasmere</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/lighthouse-hill">Lighthouse Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/midland-beach">Midland Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/new-dorp">New Dorp</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/oakwood">Oakwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ocean-breeze">Ocean Breeze</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/richmondtown">Richmondtown</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/south-beach">South Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/todt-hill">Todt Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/new-dorp-beach">New Dorp Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/oakwood-beach">Oakwood Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-shore">West Shore</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bloomfield">Bloomfield</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/chelsea-staten-island">Chelsea (Staten Island)</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/travis">Travis</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/mid-island">Mid-Island</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bulls-head">Bulls Head</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/castleton-corners">Castleton Corners</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/graniteville">Graniteville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/manor-heights">Manor Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/meiers-corners">Meiers Corners</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/new-springville">New Springville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/sunnyside-staten-island">Sunnyside (Staten Island)</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/westerleigh">Westerleigh</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/willowbrook">Willowbrook</a></li>
    </ul>
  </div>
  <div class="Footer-column Footer-column--mobileColumn">
    <a class="Footer-text Footer-text--large" href="/for-sale/new-jersey">New Jersey</a>
    <ul class="Footer-areasList">
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/cliffside-park">Cliffside Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/edgewater">Edgewater</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fort-lee">Fort Lee</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/jersey-city">Jersey City</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/historic-downtown">Historic Downtown</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/waterfront">Waterfront</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/paulus-hook">Paulus Hook</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/the-heights">The Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/journal-square">Journal Square</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-side-hudson-county">West Side</a></li>
    </ul>
    <div class="new-jersey seo-toggled-off Footer-text" se:behavior="seo_togglable" se:togglable:cssselector="new-jersey" style="cursor: pointer;">+ Show more</div>
    <ul class="Footer-areasList Footer-areasList new-jersey seo-toggled">
      <li class="Footer-areaItem" se:behavior="seo_togglable" se:togglable:cssselector="new-jersey" style="cursor: pointer;"><span class="Footer-text">- Hide</span></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/newport">Newport</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bergen-lafayette">Bergen/Lafayette</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bayonne">Bayonne</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hoboken">Hoboken</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-newark">East Newark</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/union-city">Union City</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/north-bergen">North Bergen</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/weehawken">Weehawken</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/guttenberg">Guttenberg</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/harrison">Harrison</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/kearny">Kearny</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/secaucus">Secaucus</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-new-york">West New York</a></li>
    </ul>
  </div>

</div>
<div class="Footer-expandableContent hidden-md">
  <div class="neighborhood seo-toggled-off Footer-text Footer-text--large Footer-text--bordered" se:behavior="seo_togglable" se:togglable:cssselector="neighborhood" style="cursor: pointer;">+ &nbsp;show nyc neighborhoods</div>
  <div class="neighborhood seo-toggled">
    <div class="Footer-neighborhood Footer-neighborhood--expandable">

  <div class="Footer-column Footer-column--mobileColumn">
    <a class="Footer-text Footer-text--large" href="/for-sale/manhattan">Manhattan</a>
    <ul class="Footer-areasList">
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/roosevelt-island">Roosevelt Island</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/downtown">All Downtown</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/civic-center">Civic Center</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/financial-district">Financial District</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fulton-seaport">Fulton/Seaport</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/tribeca">Tribeca</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/stuyvesant-town">Stuyvesant Town/PCV</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/soho">Soho</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hudson-square">Hudson Square</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/little-italy">Little Italy</a></li>
    </ul>
    <div class="manhattan seo-toggled-off Footer-text" se:behavior="seo_togglable" se:togglable:cssselector="manhattan" style="cursor: pointer;">+ Show more</div>
    <ul class="Footer-areasList Footer-areasList manhattan seo-toggled">
      <li class="Footer-areaItem" se:behavior="seo_togglable" se:togglable:cssselector="manhattan" style="cursor: pointer;"><span class="Footer-text">- Hide</span></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/les">Lower East Side</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/two-bridges">Two Bridges</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/chinatown">Chinatown</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/battery-park-city">Battery Park City</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/gramercy-park">Gramercy Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/chelsea">Chelsea</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-chelsea">West Chelsea</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/greenwich-village">Greenwich Village</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/noho">Noho</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-village">East Village</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-village">West Village</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/flatiron">Flatiron</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/nomad">NoMad</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/nolita">Nolita</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/midtown-all">All Midtown</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/midtown">Midtown</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/central-park-south">Central Park South</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/midtown-south">Midtown South</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/midtown-east">Midtown East</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/murray-hill">Murray Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/sutton-place">Sutton Place</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/turtlebay">Turtle Bay</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/beekman">Beekman</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/kips-bay">Kips Bay</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/midtown-west">Midtown West</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hudson-yards">Hudson Yards</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hells-kitchen">Hell's Kitchen</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/uws">All Upper West Side</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/upper-west-side">Upper West Side</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/lincoln-square">Lincoln Square</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/manhattan-valley">Manhattan Valley</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ues">All Upper East Side</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/upper-east-side">Upper East Side</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/lenox-hill">Lenox Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/yorkville">Yorkville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/carnegie-hill">Carnegie Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/upper-carnegie-hill">Upper Carnegie Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/upper">All Upper Manhattan</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/morningside">Morningside Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hamilton-heights">Hamilton Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/washington-heights">Washington Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hudson-heights">Hudson Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fort-george">Fort George</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/inwood">Inwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-harlem">West Harlem</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/manhattanville">Manhattanville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/central-harlem">Central Harlem</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/south-harlem">South Harlem</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-harlem">East Harlem</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/marble-hill">Marble Hill</a></li>
    </ul>
  </div>
  <div class="Footer-column Footer-column--mobileColumn">
    <a class="Footer-text Footer-text--large" href="/for-sale/bronx">Bronx</a>
    <ul class="Footer-areasList">
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/mott-haven">Mott Haven</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/north-new-york">North New York</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/melrose">Melrose</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/port-morris">Port Morris</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hunts-point">Hunts Point</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/longwood">Longwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/morrisania">Morrisania</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/claremont">Claremont</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/crotona-park-east">Crotona Park East</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/highbridge">Highbridge</a></li>
    </ul>
    <div class="bronx seo-toggled-off Footer-text" se:behavior="seo_togglable" se:togglable:cssselector="bronx" style="cursor: pointer;">+ Show more</div>
    <ul class="Footer-areasList Footer-areasList bronx seo-toggled">
      <li class="Footer-areaItem" se:behavior="seo_togglable" se:togglable:cssselector="bronx" style="cursor: pointer;"><span class="Footer-text">- Hide</span></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/concourse">Concourse</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/morris-heights">Morris Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/university-heights">University Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fordham">Fordham</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-tremont">East Tremont</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-farms">West Farms</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/belmont">Belmont</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bedford-park">Bedford Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/kingsbridge">Kingsbridge</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/kingsbridge-heights">Kingsbridge Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/riverdale">Riverdale</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fieldston">Fieldston</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/spuyten-duyvil">Spuyten Duyvil</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/soundview">Soundview</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/castle-hill">Castle Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/parkchester">Parkchester</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/throgs-neck">Throgs Neck</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/locust-point">Locust Point</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/pelham-bay">Pelham Bay</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/coop-city">Co-op City</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/city-island">City Island</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/morris-park">Morris Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/pelham-parkway">Pelham Parkway</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/van-nest">Van Nest</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/laconia">Laconia</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/williamsbridge">Williamsbridge</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/baychester">Baychester</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/woodlawn">Woodlawn</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/wakefield">Wakefield</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/eastchester">Eastchester</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/tremont">Tremont</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/mt-hope">Mt. Hope</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/norwood">Norwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bronxwood">Bronxwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/pelham-gardens">Pelham Gardens</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/woodstock">Woodstock</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/westchester-village">Westchester Village</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/westchester-square">Westchester Square</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/country-club">Country Club</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/schuylerville">Schuylerville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/edenwald">Edenwald</a></li>
    </ul>
  </div>
  <div class="Footer-column Footer-column--mobileColumn">
    <a class="Footer-text Footer-text--large" href="/for-sale/brooklyn">Brooklyn</a>
    <ul class="Footer-areasList">
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/greenpoint">Greenpoint</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/williamsburg">Williamsburg</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-williamsburg">East Williamsburg</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/downtown-brooklyn">Downtown Brooklyn</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fort-greene">Fort Greene</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/brooklyn-heights">Brooklyn Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/boerum-hill">Boerum Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/dumbo">DUMBO</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/vinegar-hill">Vinegar Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bedford-stuyvesant">Bedford-Stuyvesant</a></li>
    </ul>
    <div class="brooklyn seo-toggled-off Footer-text" se:behavior="seo_togglable" se:togglable:cssselector="brooklyn" style="cursor: pointer;">+ Show more</div>
    <ul class="Footer-areasList Footer-areasList brooklyn seo-toggled">
      <li class="Footer-areaItem" se:behavior="seo_togglable" se:togglable:cssselector="brooklyn" style="cursor: pointer;"><span class="Footer-text">- Hide</span></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/stuyvesant-heights">Stuyvesant Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ocean-hill">Ocean Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bushwick">Bushwick</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-new-york">East New York</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/new-lots">New Lots</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/city-line">City Line</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/starrett-city">Starrett City</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/red-hook">Red Hook</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/park-slope">Park Slope</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/gowanus">Gowanus</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/carroll-gardens">Carroll Gardens</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/cobble-hill">Cobble Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/sunset-park">Sunset Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/windsor-terrace">Windsor Terrace</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/crown-heights">Crown Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/weeksville">Weeksville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/prospect-heights">Prospect Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/cswd">Columbia St Waterfront District</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/prospect-lefferts-gardens">Prospect Lefferts Gardens</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bay-ridge">Bay Ridge</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fort-hamilton">Fort Hamilton</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/dyker-heights">Dyker Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bensonhurst">Bensonhurst</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bath-beach">Bath Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/gravesend">Gravesend</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/borough-park">Borough Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/mapleton">Mapleton</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ocean-parkway">Ocean Parkway</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/kensington">Kensington</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/coney-island">Coney Island</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/brighton-beach">Brighton Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ditmas-park">Ditmas Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fiske-terrace">Fiske Terrace</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/seagate">Seagate</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/flatbush">Flatbush</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/midwood">Midwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/sheepshead-bay">Sheepshead Bay</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/homecrest">Homecrest</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/madison">Madison</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/manhattan-beach">Manhattan Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/brownsville">Brownsville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/prospect-park-south">Prospect Park South</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-flatbush">East Flatbush</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/farragut">Farragut</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/wingate">Wingate</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/canarsie">Canarsie</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/flatlands">Flatlands</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/marine-park">Marine Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/mill-basin">Mill Basin</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bergen-beach">Bergen Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/clinton-hill">Clinton Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/old-mill-basin">Old Mill Basin</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/greenwood">Greenwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/gerritsen-beach">Gerritsen Beach</a></li>
    </ul>
  </div>
  <div class="Footer-column Footer-column--mobileColumn">
    <a class="Footer-text Footer-text--large" href="/for-sale/queens">Queens</a>
    <ul class="Footer-areasList">
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/astoria">Astoria</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ditmars-steinway">Ditmars-Steinway</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/long-island-city">Long Island City</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hunters-point">Hunters Point</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/sunnyside-queens">Sunnyside</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/woodside">Woodside</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/jackson-heights">Jackson Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-elmhurst">East Elmhurst</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/north-corona">North Corona</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/elmhurst">Elmhurst</a></li>
    </ul>
    <div class="queens seo-toggled-off Footer-text" se:behavior="seo_togglable" se:togglable:cssselector="queens" style="cursor: pointer;">+ Show more</div>
    <ul class="Footer-areasList Footer-areasList queens seo-toggled">
      <li class="Footer-areaItem" se:behavior="seo_togglable" se:togglable:cssselector="queens" style="cursor: pointer;"><span class="Footer-text">- Hide</span></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/corona">Corona</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/maspeth">Maspeth</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/middle-village">Middle Village</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ridgewood">Ridgewood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/glendale">Glendale</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/rego-park">Rego Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/forest-hills">Forest Hills</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/flushing">Flushing</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-flushing">East Flushing</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/murray-hill-queens">Murray Hill (Queens)</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/whitestone">Whitestone</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/malba">Malba</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/beechhurst">Beechhurst</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/college-point">College Point</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fresh-meadows">Fresh Meadows</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/kew-gardens-hills">Kew Gardens Hills</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/jamaica-hills">Jamaica Hills</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/woodhaven">Woodhaven</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/richmond-hill">Richmond Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/kew-gardens">Kew Gardens</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/howard-beach">Howard Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hamilton-beach">Hamilton Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ramblersville">Ramblersville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/rockwood-park">Rockwood Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/lindenwood">Lindenwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/old-howard-beach">Old Howard Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ozone-park">Ozone Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/south-ozone-park">South Ozone Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bayside">Bayside</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bay-terrace-queens">Bay Terrace (Queens)</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/douglaston">Douglaston</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/little-neck">Little Neck</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/auburndale">Auburndale</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/jamaica">Jamaica</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/south-jamaica">South Jamaica</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hollis">Hollis</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/st-albans">St. Albans</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/laurelton">Laurelton</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/cambria-heights">Cambria Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/queens-village">Queens Village</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/glen-oaks">Glen Oaks</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/floral-park">Floral Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bellerose">Bellerose</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/rosedale">Rosedale</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/springfield-gardens">Springfield Gardens</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/briarwood">Briarwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/jamaica-estates">Jamaica Estates</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/new-hyde-park">New Hyde Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/south-richmond-hill">South Richmond Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/oakland-gardens">Oakland Gardens</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hillcrest">Hillcrest</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/pomonok">Pomonok</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/utopia">Utopia</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/clearview">Clearview</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/rockaway-all">Rockaway All</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/far-rockaway">Far Rockaway</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/broad-channel">Broad Channel</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/arverne">Arverne</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/rockaway-park">Rockaway Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bayswater">Bayswater</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/belle-harbor">Belle Harbor</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/breezy-point">Breezy Point</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/neponsit">Neponsit</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/edgemere">Edgemere</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hammels">Hammels</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/brookville">Brookville</a></li>
    </ul>
  </div>
  <div class="Footer-column Footer-column--mobileColumn">
    <a class="Footer-text Footer-text--large" href="/for-sale/staten-island">Staten Island</a>
    <ul class="Footer-areasList">
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/north-shore">North Shore</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/arlington">Arlington</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/clifton">Clifton</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/elm-park">Elm Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/grymes-hill">Grymes Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/howland-hook">Howland Hook</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/mariners-harbor">Mariners Harbor</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/new-brighton">New Brighton</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/park-hill">Park Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/port-richmond">Port Richmond</a></li>
    </ul>
    <div class="staten-island seo-toggled-off Footer-text" se:behavior="seo_togglable" se:togglable:cssselector="staten-island" style="cursor: pointer;">+ Show more</div>
    <ul class="Footer-areasList Footer-areasList staten-island seo-toggled">
      <li class="Footer-areaItem" se:behavior="seo_togglable" se:togglable:cssselector="staten-island" style="cursor: pointer;"><span class="Footer-text">- Hide</span></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/rosebank">Rosebank</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/shore-acres">Shore Acres</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/silver-lake">Silver Lake</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/saint-george">Saint George</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/stapleton">Stapleton</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/tompkinsville">Tompkinsville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-brighton">West Brighton</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/south-shore">South Shore</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/annadale">Annadale</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/arden-heights">Arden Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/charleston">Charleston</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/eltingville">Eltingville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/great-kills">Great Kills</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/greenridge">Greenridge</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/huguenot">Huguenot</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/pleasant-plains">Pleasant Plains</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/princes-bay">Princes Bay</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/richmond-valley">Richmond Valley</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/rossville">Rossville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/tottenville">Tottenville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/woodrow">Woodrow</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-shore">East Shore</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/arrochar">Arrochar</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bay-terrace">Bay Terrace</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/dongan-hills">Dongan Hills</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/egbertville">Egbertville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/emerson-hill">Emerson Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fort-wadsworth">Fort Wadsworth</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/grant-city">Grant City</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/grasmere">Grasmere</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/lighthouse-hill">Lighthouse Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/midland-beach">Midland Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/new-dorp">New Dorp</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/oakwood">Oakwood</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/ocean-breeze">Ocean Breeze</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/richmondtown">Richmondtown</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/south-beach">South Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/todt-hill">Todt Hill</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/new-dorp-beach">New Dorp Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/oakwood-beach">Oakwood Beach</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-shore">West Shore</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bloomfield">Bloomfield</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/chelsea-staten-island">Chelsea (Staten Island)</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/travis">Travis</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/mid-island">Mid-Island</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bulls-head">Bulls Head</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/castleton-corners">Castleton Corners</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/graniteville">Graniteville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/manor-heights">Manor Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/meiers-corners">Meiers Corners</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/new-springville">New Springville</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/sunnyside-staten-island">Sunnyside (Staten Island)</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/westerleigh">Westerleigh</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/willowbrook">Willowbrook</a></li>
    </ul>
  </div>
  <div class="Footer-column Footer-column--mobileColumn">
    <a class="Footer-text Footer-text--large" href="/for-sale/new-jersey">New Jersey</a>
    <ul class="Footer-areasList">
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/cliffside-park">Cliffside Park</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/edgewater">Edgewater</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/fort-lee">Fort Lee</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/jersey-city">Jersey City</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/historic-downtown">Historic Downtown</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/waterfront">Waterfront</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/paulus-hook">Paulus Hook</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/the-heights">The Heights</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/journal-square">Journal Square</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-side-hudson-county">West Side</a></li>
    </ul>
    <div class="new-jersey seo-toggled-off Footer-text" se:behavior="seo_togglable" se:togglable:cssselector="new-jersey" style="cursor: pointer;">+ Show more</div>
    <ul class="Footer-areasList Footer-areasList new-jersey seo-toggled">
      <li class="Footer-areaItem" se:behavior="seo_togglable" se:togglable:cssselector="new-jersey" style="cursor: pointer;"><span class="Footer-text">- Hide</span></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/newport">Newport</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bergen-lafayette">Bergen/Lafayette</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/bayonne">Bayonne</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/hoboken">Hoboken</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/east-newark">East Newark</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/union-city">Union City</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/north-bergen">North Bergen</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/weehawken">Weehawken</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/guttenberg">Guttenberg</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/harrison">Harrison</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/kearny">Kearny</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/secaucus">Secaucus</a></li>
        <li class="Footer-areaItem"><a class="Footer-text" href="/for-sale/west-new-york">West New York</a></li>
    </ul>
  </div>

    </div>
  </div>
</div>
<div>

    <div class="Footer-column Footer-column--navigation u-height--auto">
  <ul class="Footer-navigation">
    <li class="Footer-navigationItem">
      <a class="Footer-text Footer-text--large" href="/blog/">Blog</a>
    </li>
    <li class="Footer-navigationItem">
      <a class="Footer-text Footer-text--large" href="/jobs">We're hiring!</a>
    </li>
  </ul>
  <ul class="Footer-navigation">
    <li class="Footer-navigationItem hidden-xs hidden-sm">
      <a class="Footer-text Footer-text--large" href="https://streeteasy.com/nyc/submit_your_listings?lct=footer&amp;prd=submit_your_listing">Submit your listings</a>
    </li>
    <li class="Footer-navigationItem">
      <a class="Footer-text Footer-text--large" href="https://streeteasy.com/agent-resources/advertise/">Work With Us</a>
    </li>
    <li class="Footer-navigationItem">
      <a class="Footer-text Footer-text--large" href="/nycrentalnetwork">NYC Rental Network</a>
    </li>
    <li class="Footer-navigationItem hidden-xs hidden-sm">
      <a target="_blank" class="Footer-text Footer-text--large" rel="noopener noreferrer" href="http://press.streeteasy.com">Press</a>
    </li>
  </ul>
  <ul class="Footer-navigation">
    <li><a class="Footer-text Footer-text--large" href="/browse/">Browse all homes</a></li>
  </ul>
  <ul class="Footer-navigation">
    <li class="Footer-navigationItem hidden-md"><a class="Footer-text" href="sales/all">View All Sales</a></li>
      <li class="Footer-navigationItem">
        <a target="_blank" class="Footer-text" rel="noopener noreferrer" href="https://support.streeteasy.com/">Help</a>
      </li>
    <li class="Footer-navigationItem">
      <a class="Footer-text" href="//www.zillow.com/corp/Terms.htm">Terms of Use &amp; Privacy Policy</a>
    </li>
    <li class="Footer-navigationItem hidden-xs hidden-sm">
      <a class="Footer-text" href="//www.zillow.com/corp/Privacy.htm#behavioralAdvertising">Ad Choice</a>
    </li>
  </ul>
  <ul>
    <li class="Footer-navigationItem hidden-xs hidden-sm">
      <a href="https://outeast.com/" class="Footer-text">The Hamptons Site</a>
    </li>
  </ul>
</div>

            <div>
              <a id="app_store_link" class="Footer-applicationLink Footer-applicationLink--apple" href="https://app.adjust.com/twslzb">App Store</a>
              <a id="android_link" class="Footer-applicationLink Footer-applicationLink--android" href="https://app.adjust.com/p2p50p">Play Market</a>
            </div>

</div>


          <div class="Footer-separator"></div>
          <div class="Footer-socialIcons">
            <a class="Footer-linkIcon" href="https://twitter.com/streeteasy">
              <img srcset="//cdn-assets-s3.streeteasy.com/assets/icons/twitter@2x-64ae8e9960dee01a541a3ff0e6bb8c9f5d43d71818e23b452100117296ddaa6d.png 2x" alt="Streeteasy twitter" class="Footer-icon" src="//cdn-assets-s3.streeteasy.com/assets/icons/twitter-57501be2209fad15d6359c723a78ef948e08c84cf47452cab799071d362e664c.png">
</a>            <a class="Footer-linkIcon" href="https://www.facebook.com/streeteasy/">
              <img srcset="//cdn-assets-s3.streeteasy.com/assets/icons/facebook@2x-c064e086f194db695b1effb1470bbf436c4a7694773041ce482e112b02f53652.png 2x" alt="Streeteasy facebook" class="Footer-icon" src="//cdn-assets-s3.streeteasy.com/assets/icons/facebook-beecef4f47f406f7d11894d526897a02f3d46f798e7981c3feb4eaf4d5c07d59.png">
</a>            <a class="Footer-linkIcon" href="https://www.instagram.com/streeteasy/">
              <img srcset="//cdn-assets-s3.streeteasy.com/assets/icons/instagram@2x-cd1101d6c8d8a3998260937391c392ba0f2e283d66a5f0ad9f4eb9470bd0f47d.png 2x" alt="Streeteasy instagram" class="Footer-icon Footer-icon--withoutMargin" src="//cdn-assets-s3.streeteasy.com/assets/icons/instagram-3441573dd0ddbbe8af00ab6ef4d499cd7faf5f1969d99eca9f039d735edf4059.png">
</a>          </div>
          <div class="u-width--full u-text--alignCenter">
            <div class="Footer-text Footer-text--brokerage">StreetEasy is a brand and registered trademark of Zillow,
              Inc. Zillow, Inc. has a real estate
              brokerage license in multiple states. A list of these real estate licenses can be found
              <a class="" target="_blank" rel="noopener noreferrer" href="https://www.zillow.com/info/real-estate-licenses/">here</a>.
            </div>
          </div>
          <!-- End for home page -->

        <div class="Footer-zgBrands">
          <a class="Footer-text Footer-text--large Footer-text--zgBrand" href="https://www.zillow.com/">Zillow</a>
          <span class="Footer-dot Footer-dot--zgBrands hidden-xs hidden-sm">·</span>
          <a class="Footer-text Footer-text--large Footer-text--zgBrand" href="https://www.trulia.com/">Trulia</a>
          <span class="Footer-dot Footer-dot--zgBrands hidden-xs hidden-sm">·</span>
          <a class="Footer-text Footer-text--large Footer-text--zgBrand" href="https://hotpads.com/">Hotpads</a>
          <span class="Footer-dot Footer-dot--zgBrands hidden-xs hidden-sm">·</span>
          <a class="Footer-text Footer-text--large Footer-text--zgBrand" href="https://outeast.com">Out East</a>
        </div>

        <div class="Footer-text hidden-md">
          Zillow Inc. Sites © 2006-2020 Zillow
        </div>

        <div class="Footer-copyright hidden-xs hidden-sm Footer-copyright--zgBrands">

            <span class="Footer-text">
  Zillow Inc. Sites © 2006-2020 Zillow
  <span class="Footer-dot">·</span>
  <span class="only-print"><b>https://streeteasy.com/</b></span>
  <a rel="nofollow" class="Footer-text" href="http://nytm.org/made">Made In NYC</a>
  <span class="Footer-dot">·</span>
  Powered by Bikes, Coffee and Doughnuts.
</span>

        </div>
        <div class="u-width--full">
          <img alt="Footer Image" class="Footer-image" src="//cdn-assets-s3.streeteasy.com/assets/svg/footer-f3b296bd4be445e92b2d0fd4b1d3c1050d30933b14e76d7b2fcf8215bb01ba1a.svg">
        </div>
      </footer>
    </div>
  </div>






      <script src="//cdn-assets-s3.streeteasy.com/assets/home-5dc3a72a30561650ad7f96b55ca4c33fc08b1102079f9b74a0b8095b0ac807af.js"></script>
<script src="//cdn-assets-s3.streeteasy.com/assets/desktop-2d5b611857b30834cd18127c259f74ebc5295dad50dc809fec3608e494248dca.js"></script>
            <script>
        (function (root) {
          root.SEDeviceType = 'desktop';
        }(window));
      </script>

      <script src="//cdn-assets-s3.streeteasy.com/assets/pages/home/search_price-c5d377953240d0e9fc300d18c45ac625200a82a65d778233445e8577ad715c65.js"></script>
  <script src="//cdn-assets-s3.streeteasy.com/assets/pages/home/search_beds-44530735b932988810a880f9264094684f30f952e8c8a41bf78485290901b915.js"></script>
<script src="//cdn-assets-s3.streeteasy.com/assets/scripts/dynamic/virtual_view_tooltip-ac0ade3c6c349beeebcb7ae4aada9c2e663a1d05e16b82d9f341b4e360f53955.js"></script><script src="//cdn-assets-s3.streeteasy.com/assets/scripts/dynamic/square_footage_field-9d832802a9e972e38251adc990239cbd3f9396ea87132b4a243c34d2550785e4.js"></script>    <script src="//cdn-assets-s3.streeteasy.com/assets/pages/home/search_area_dropdown-ec8d47679cd99b8da52f3be04c01941d54d7770c81f7d832ac9cf4eb11369cdf.js"></script>

  <script src="//cdn-assets-s3.streeteasy.com/assets/pages/home/index_home-74b9e57e26e01146421c1c902db62c46e09eb26a82d50f645d3dc532806dd550.js"></script>

        <script src="//cdn-assets-s3.streeteasy.com/assets/pages/home/search_beds-44530735b932988810a880f9264094684f30f952e8c8a41bf78485290901b915.js"></script>


    <script type="text/javascript">
  window.addEventListener('load', function() {
    document.cookie = "google_one_tap=0;path=/;expires='N/A'"
  });
</script>

    <div id="authentication" data-site-key="6LcsCN8UAAAAABcTaJDzilIOyzXuLAtKafjcE051"><div class="styled__AuthModalWrap-sc-16frzwi-4 jJheEv"></div></div>

    <script src="//cdn-assets-s3.streeteasy.com/assets/build/js/runtime-67d244317a0c2ec45347.js"></script>
<script src="//cdn-assets-s3.streeteasy.com/assets/build/js/framework-d82e2e668001e0756b2f.chunk.js"></script>
<script src="//cdn-assets-s3.streeteasy.com/assets/build/js/commons-f87ebe7449cd9a0c7c80.chunk.js"></script>
<script src="//cdn-assets-s3.streeteasy.com/assets/build/js/authentication-c5f99e377dcee285111e.chunk.js"></script>
<script src="//cdn-assets-s3.streeteasy.com/assets/build/js/styles-a6fda2e3c2c3b07af86f.chunk.js"></script>
<script src="//cdn-assets-s3.streeteasy.com/assets/build/js/map-d9629e6702eb5ae65ac3.chunk.js"></script>
  <script type="text/javascript" id="d__inj" class="d__inj_delayed" src="/dstlstrt.js" defer=""></script><style type="text/css">#d__fFH{position:absolute;top:-5000px;left:-5000px}#d__fF{font-family:serif;font-size:200px;visibility:hidden}#ubbfccwz{display:none!important}</style>
  <!-- nyc main 749192685df73253a5292501505395b4c00299dc app-6788f69f8c-tzzfb -->

<div style="display: none; visibility: hidden;">

<script type="text/javascript">var _kiq=_kiq||[];(function(){setTimeout(function(){var a=document,b=a.getElementsByTagName("script")[0];a=a.createElement("script");a.type="text/javascript";a.async=!0;a.src="//s3.amazonaws.com/ki.js/51812/cvV.js";b.parentNode.insertBefore(a,b)},1)})();</script>

<script type="text/javascript" charset="utf-8">_kiq.push(["identify","undefined"]);</script>

<script type="text/javascript" charset="utf-8">_kiq.push(["set",{user_type:"anonymous",listing_type:"undefined",building_id:"undefined","3d_tour":"undefined"}]);</script>

<script type="text/javascript">+function(a){a&&_kiq.push(["eventHandler","show",function(){a.ajax({url:"/_q"})}])}(window.jQuery);</script></div><iframe name="_hjRemoteVarsFrame" title="_hjRemoteVarsFrame" id="_hjRemoteVarsFrame" src="https://vars.hotjar.com/box-469cf41adb11dc78be68c1ae7f9457a4.html" style="display: none !important; width: 1px !important; height: 1px !important; opacity: 0 !important; pointer-events: none !important;"></iframe><div id="credential_picker_container" style="position: fixed; z-index: 99999; height: 205px;"><iframe src="https://accounts.google.com/gsi/iframe/select?client_id=147313643782-6g6eiu6pva3rofhad6e7csk4r701hbpf.apps.googleusercontent.com&amp;ux_mode=popup&amp;ui_mode=card&amp;as=mECAowrBgisPmuAYTgr4Ug&amp;channel_id=fc7bbc3909d5810f04b21b81c151f848f99c108c57323f19667a3374579d0167&amp;origin=https%3A%2F%2Fstreeteasy.com" style="height: 205px; width: 391px; overflow: hidden;"></iframe></div><div id="d__fFH" style="position: absolute !important; top: -5000px !important; left: -5000px !important;"><object id="d_dlg" classid="clsid:3050f819-98b5-11cf-bb82-00aa00bdce0b" width="0px" height="0px"></object><span id="d__fF" style="font-family: Courier, serif !important; font-size: 72px !important; visibility: hidden;">The quick brown fox jumps over the lazy dog.</span></div></body>'''

body = {"textBlob": text, "htmlBlob": html, "url": "kgjasdkfjgidsabfkjgsadikf"}

resp = requests.post(api, json=body)

print(resp.content.decode())
