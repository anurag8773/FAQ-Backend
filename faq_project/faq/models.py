import asyncio
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField(verbose_name=_('Question'))
    answer = RichTextField(verbose_name=_('Answer'))
    question_hi = models.TextField(blank=True, null=True, verbose_name=_('Question (Hindi)'))
    question_bn = models.TextField(blank=True, null=True, verbose_name=_('Question (Bengali)'))

    def get_translated_question(self, lang):
        """Returns the translated question based on the requested language."""
        return getattr(self, f'question_{lang}', self.question)  # Fallback to default if translation is missing

    def translate_text(self, text, dest_lang):
        """Helper function to handle async translation synchronously."""
        try:
            translator = Translator()
            return asyncio.run(translator.translate(text, dest=dest_lang)).text
        except Exception as e:
            print(f"Translation error for {dest_lang}: {e}")
            return None

    def save(self, *args, **kwargs):
        if not self.pk:  # Only translate when a new FAQ is created
            if not self.question_hi:
                self.question_hi = self.translate_text(self.question, 'hi')
            if not self.question_bn:
                self.question_bn = self.translate_text(self.question, 'bn')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
