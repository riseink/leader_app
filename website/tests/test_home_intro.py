from django.test import TestCase
from unittest.mock import patch
from website.models import HomePage, HomeIntroVideos

from django.db.models.query import QuerySet



class TestHomeIntro(TestCase):

	@classmethod
	def setUpTestData(cls):
		HomePage.objects.create(title="Home Page", path='/home', depth=1, pk=1)
		HomeIntroVideos.objects.create(id=1, page_id=1)
		HomeIntroVideos.objects.create(id=2, page_id=1)

	"""
		Simple test example
	"""
	def test_home_page_title(self):
		page = HomePage.objects.get(path='/home')
		self.assertEqual(page.title, "Home Page")


	"""
		Home page should return one intro video
	"""
	def test_get_first_intro_video(self):
		page = HomePage.objects.get(path='/home')
		video = page.get_first_intro_video()
		self.assertIsInstance(video, HomeIntroVideos)