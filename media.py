# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 16:57:05 2017

@author: miste
"""

import webbrowser

class Movie():
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