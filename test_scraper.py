from unittest import TestCase
from unittest.mock import MagicMock


class TestScraper(TestCase):
    def setUp(self):
        from scraper import Scraper
        self.mock = MagicMock()
        self.mock.read.return_value = r'<div class="thread"><h3>Conversation with Bob Ross</h3>Participants: Bob ' \
                                      r'Ross<div class="message"><div class="message_header"><span class="user">Zack ' \
                                      r'Xiang</span><span class="meta">Wednesday, 12 November 2014 at 10:06 ' \
                                      r'UTC</span></div></div><p></p><div class="message"><div ' \
                                      r'class="message_header"><span class="user">Bob Ross</span><span ' \
                                      r'class="meta">Wednesday, 12 November 2014 at 09:06 ' \
                                      r'UTC</span></div></div><p>Thanks you\'re the best ❤️< /p></div> '
        self.scraper = Scraper(self.mock)

    def test_soup(self):
        user_span = self.scraper.soup.find_all("span", class_="user")
        self.assertEqual(user_span[0].text, "Zack Xiang")

    def test_get_all_messages(self):
        messages = self.scraper._get_all_messages()
        self.assertEqual(len(messages), 2)

    def test_match_datetime(self):
        self.assertIsNotNone(self.scraper.datetime_pattern_matcher.match("Wednesday, 12 November 2014 at 10:06"))

    def test_get_correct_datetime_components(self):
        pass

    def test_reformat_datetime(self):
        pass