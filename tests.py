from unittest import TestCase
from xml.etree import ElementTree

import xmltodict

from markdown import Markdown

from mdx_staticfiles import (
    DjangoStaticAssetsProcessor, StaticfilesExtension, makeExtension)


class XmlTestCaseMixin(object):
    """ Helper class for asserting that XML documents describe the same XML
        structures.
    """

    def mk_doc(self, s):
        return ElementTree.fromstring(
            "<div>" + s.strip() + "</div>")

    def assert_xml_equal(self, a, b):
        self.assertEqual(
            xmltodict.parse(ElementTree.tostring(a)),
            xmltodict.parse(ElementTree.tostring(b)))

    def assert_xmltext_equal(self, a, b):
        self.assert_xml_equal(self.mk_doc(a), self.mk_doc(b))


class TestSubstitution(XmlTestCaseMixin, TestCase):
    """ Test our substitions of django static paths """

    def setUp(self):
        self.md = Markdown()
        ext = StaticfilesExtension()
        ext.extendMarkdown(self.md)

    def test_link(self):
        xml = self.md.convert('[a]({% static "a.html" %})')
        self.assert_xmltext_equal(xml, '<p><a href="/st/a.html">a</a></p>')

    def test_image(self):
        xml = self.md.convert('![a]({% static "a.jpg" %})')
        self.assert_xmltext_equal(xml, '<p><img alt="a" src="/st/a.jpg"/></p>')

    def test_inline_html(self):
        xml = self.md.convert('<img src="{% static "a.jpg" %}"/>')
        self.assert_xmltext_equal(xml, '<p><img src="/st/a.jpg"/></p>')


class TestStaticfilesExtension(TestCase):
    """ Test StaticfilesExtension class. """

    def mk_markdown(self):
        md = Markdown()
        return md

    def assert_registered(self, md):
        postprocessor = md.postprocessors['staticfiles']
        self.assertTrue(isinstance(postprocessor, DjangoStaticAssetsProcessor))

    def assert_not_registered(self, md):
        self.assertFalse('staticfiles' in md.postprocessors)

    def test_extend_markdown(self):
        md = self.mk_markdown()
        ext = StaticfilesExtension()
        self.assert_not_registered(md)
        ext.extendMarkdown(md)
        self.assert_registered(md)


class TestExtensionRegistration(TestCase):
    """ Test registration of staticfiles extension. """

    def test_make_extension(self):
        ext = makeExtension()
        self.assertTrue(isinstance(ext, StaticfilesExtension))
