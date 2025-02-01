from django.test import TestCase
from .models import FAQ

class FAQTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(question="How does this feature work?", answer="It enables translation and caching.")
    
    def test_faq_creation(self):
        self.assertEqual(self.faq.question, "How does this feature work?")
        self.assertEqual(self.faq.answer, "It enables translation and caching.")
    
    def test_faq_translation(self):
        self.assertTrue(self.faq.question_hi)
        self.assertTrue(self.faq.question_bn)
    
    def test_get_translated_question(self):
        self.assertEqual(self.faq.get_translated_question('hi'), self.faq.question_hi)
        self.assertEqual(self.faq.get_translated_question('bn'), self.faq.question_bn)
        self.assertEqual(self.faq.get_translated_question('fr'), self.faq.question)