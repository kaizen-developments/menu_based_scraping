BrookingsPatterns = {
    "url"   : {},
    "title" : {'name' : 'title'},
    "body"  : {'name' : 'div', 'attrs' : {'class' : "byo-block -narrow wysiwyg-block wysiwyg"}}
}

NYTimesPatterns = {
    "url"   : {},
    "title" : {'name' : 'title'},
    "body"  : {'selector' : ('div.StoryBodyCompanionColumn div p')}
}
domainPatterns = {
    "brookings.edu" : BrookingsPatterns,
    "nytimes.com"   : NYTimesPatterns
}