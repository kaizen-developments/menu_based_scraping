#Create a program, that runs a crawler that can be navigated by user input.
#The crawler must be able to find links from a given page pointing to other pages. Bonus: Find links until depth 5 with respect to document distance, determined by the number 
#of links required to reach 1 document from another!
#Be able to write down strategies during running to match data on sites, and be able to store these strategies, aswell as the data that was matched by them!
#Be able to visualize the current website's parse tree, aswell as the current parse tree assuming, that there is a pattern that specifies the parse tree!
#Be able to define types during runtime, and have a way to determine how to gather a given type of data during runtime!

import requests
from bs4 import BeautifulSoup

from liveScrapingClasses import *
from liveScrapingTyping import *
from liveScrapingStrategies import *
from liveScrapingPatterns import *

from functools import partial

#Define how to obtain the components of a class with a default value!
def componentsOf(dataModel : type): #TODO: Test whether base class has default value or not
    # if not issubclass(dataModel, TypeWithADefaultValue):
    #     raise TypeError("The dataModel does not have a default value.")
    return list(dataModel().__dict__.keys())


def scrapeDomainForComponentsOfDataModel(url : Url, patterns : Patterns, strategyForComponentsforAWebsite : Strategies, dataModel : type):
    dataModelComponents = list()
    components = componentsOf(dataModel)
    for component in components:
        dataModelComponents += [strategyForComponentsforAWebsite[component](url, patterns[component])]
    return dataModel(*dataModelComponents)

scrapeWebsiteForTitleAndBody = partial(scrapeDomainForComponentsOfDataModel, dataModel = Content)

domains = ["brookings.edu", "nytimes.com"]


scrapers = {
    "brookings.edu" : partial(scrapeDomainForComponentsOfDataModel, patterns = BrookingsPatterns,  strategyForComponentsforAWebsite = BrookingsStrategy, dataModel = Content),
    "nytimes.com"   : partial(scrapeDomainForComponentsOfDataModel, patterns = NYTimesPatterns,    strategyForComponentsforAWebsite = NYTimesStrategy, dataModel = Content)
}

content = scrapers["brookings.edu"](url = "https://www.brookings.edu/articles/bill-baers-testimony-before-the-u-s-senate-committee-on-the-judiciary-subcommittee-on-competition-policy-antitrust-and-consumer-rights/")
print(content)

state = ("url", "pattern", "dataModel", "strategies", "patterns", "functionalities", "websites that can be reached", "new strategy", "new pattern", "navigation")
"extract current pattern", "keep pattern while going to next site"
""