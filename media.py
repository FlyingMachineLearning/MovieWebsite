# -*- coding: utf-8 -*-

import webbrowser

class Movie():
	"""
	Create an Movie object complete with title, storyline, 
	poster, trailer, release date, and Marvel phase
	Method displays trailer
	"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, date, director, phase):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.date = date
		self.director = director
		self.phase = phase

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)