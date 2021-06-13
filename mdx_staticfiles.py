import re

from django.templatetags.static import static

from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor

assetRE = re.compile(r'{% static (\'|"|&quot;)(.*?)(\1) %}')


class DjangoStaticAssetsProcessor(Postprocessor):
    def replacement(self, match):
        path = match.group(2)
        url = static(path)
        return url

    def run(self, text):
        return assetRE.sub(self.replacement, text)


class StaticfilesExtension(Extension):
    def extendMarkdown(self, md, md_globals=None):
        md.postprocessors.register(
            DjangoStaticAssetsProcessor(md), 'staticfiles', 20)


def makeExtension(**kwargs):
    return StaticfilesExtension(**kwargs)
