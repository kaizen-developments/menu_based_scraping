import requests
from bs4 import BeautifulSoup

import abc
import inspect
from typing import Type
import re


#Abstract classes
#Class for testing whether subclass has default value or not
class TypeWithADefaultValue(abc.ABC):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._check_init_defaults()

    @classmethod
    def _check_init_defaults(cls):
        init_signature = inspect.signature(cls.__init__)
        for name, param in init_signature.parameters.items():
            if name == 'self':
                continue
            if param.default is inspect.Parameter.empty:
                raise TypeError(f"Parameter '{name}' in {cls.__name__}.__init__ must have a default value")

class Content:
    def __init__(self, url = "s", title = "s", body = "s"):
        self.url = url
        self.title = title
        self.body = body
    def __str__(self):
        return 'Title: {}'.format(self.title) + "\n" + ('URL: {}\n'.format(self.url)) + "\n" + (self.body)
    
# class Crawler:
#     def __init__(self, site):
#         self.site = site
#         self.visited = []

#     def getPage(self, url):
#         try:
#             req = requests.get(url)
#         except requests.exceptions.RequestException:
#             return None
#         return BeautifulSoup(req.text, 'html.parser')

#     def safeGet(self, pageObj, selector):
#         selectedElems = pageObj.select(selector)
#         if selectedElems is not None and len(selectedElems) > 0:
#             return '\n'.join([elem.get_text() for elem in selectedElems])
#         return ''

#     def parse(self, url):
#         bs = self.getPage(url)
#         if bs is not None:
#             title = self.safeGet(bs, self.site.titleTag)
#             body = self.safeGet(bs, self.site.bodyTag)
#             if title != '' and body != '':
#                 content = Content(url, title, body)
#                 content.print()

#     def crawl(self):
#         """
#         Get pages from website home page
#         """
#         bs = self.getPage(self.site.url)
#         targetPages = bs.findAll('a', href=re.compile(self.site.targetPattern))
#         for targetPage in targetPages:
#             targetPage = targetPage.attrs['href']
#             if targetPage not in self.visited:
#                 self.visited.append(targetPage)
#                 if not self.site.absoluteUrl:
#                     targetPage = '{}{}'.format(self.site.url, targetPage)
#                 self.parse(targetPage)