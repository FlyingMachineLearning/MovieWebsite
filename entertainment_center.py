# -*- coding: utf-8 -*-
"""
These are the released Marvel movies.
fresh_tomatoes does all of the leg work of formatting into a website.
"""

import fresh_tomatoes
import media

iron_man = media.Movie("Iron Man",
"A boy and his suit",
"https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Ironmanposter.JPG/\
220px-Ironmanposter.JPG",
"https://www.youtube.com/watch?v=8hYlB38asDY",
"May 2, 2008",
"Jon Favreau",
"Phase One")

hulk = media.Movie("The Incredible Hulk",
"A boy and his rage",
"https://upload.wikimedia.org/wikipedia/en/thumb/8/88/\
The_Incredible_Hulk_poster.jpg/220px-The_Incredible_Hulk_poster.jpg",
"https://www.youtube.com/watch?v=xbqNb2PFKKA",
"June 13, 2008",
"Louis Leterrier",
"Phase One")

iron_man_2 = media.Movie("Iron Man 2",
"Now my friend has a suit",
"https://upload.wikimedia.org/wikipedia/en/thumb/e/ed/Iron_Man_2_poster.jpg/\
220px-Iron_Man_2_poster.jpg",
"https://www.youtube.com/watch?v=BoohRoVA9WQ",
"May 7, 2010",
"Jon Favreau",
"Phase One")

thor = media.Movie("Thor",
"A boy and his hammer",
"https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Thor_poster.jpg/\
220px-Thor_poster.jpg",
"https://www.youtube.com/watch?v=JOddp-nlNvQ",
"May 6, 2011",
"Kenneth Branagh",
"Phase One")

captain = media.Movie("Captain America: The First Avenger",
"A boy and his shield",
"https://upload.wikimedia.org/wikipedia/en/thumb/3/37/Captain_America_The\
_First_Avenger_poster.jpg/220px-Captain_America_The_First_Avenger_poster.jpg",
"https://www.youtube.com/watch?v=JerVrbLldXw",
"July 22, 2011",
"Joe Johnston",
"Phase One")

avengers = media.Movie("Marvel's The Avengers",
"We only have two hours to become friends",
"https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/\
TheAvengers2012Poster.jpg/220px-TheAvengers2012Poster.jpg",
"https://www.youtube.com/watch?v=eOrNdBpGMv8",
"May 4, 2012",
"Joss Whedon",
"Phase One")

iron_man_3 = media.Movie("Iron Man 3",
"Now my girlfriend has a suit",
"https://upload.wikimedia.org/wikipedia/en/thumb/d/d5/\
Iron_Man_3_theatrical_poster.jpg/220px-Iron_Man_3_theatrical_poster.jpg",
"https://www.youtube.com/watch?v=Ke1Y3P9D0Bc",
"May 3, 2013",
"Shane Black",
"Phase Two")

thor_2 = media.Movie("Thor: The Dark World",
"Dad, I brought a girl home",
"https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/\
Thor_-_The_Dark_World_poster.jpg/220px-Thor_-_The_Dark_World_poster.jpg",
"https://www.youtube.com/watch?v=npvJ9FTgZbM",
"November 8, 2013",
"Alan Taylor",
"Phase Two")

captain_2 = media.Movie("Captain America: The Winter Soldier",
"Now my friend has my shield",
"https://upload.wikimedia.org/wikipedia/en/thumb/e/e8/Captain_America\
_The_Winter_Soldier.jpg/220px-Captain_America_The_Winter_Soldier.jpg",
"https://www.youtube.com/watch?v=7SlILk2WMTI",
"April 4, 2014",
"Anthony and Joe Russo",
"Phase Two")

guardians = media.Movie("Guardians of the Galaxy",
"We only have two hours to do origins and become friends",
"https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/GOTG-poster.jpg/\
220px-GOTG-poster.jpg",
"https://www.youtube.com/watch?v=d96cjJhvlMA",
"August 1, 2014",
"James Gunn",
"Phase Two")

avengers_2 = media.Movie("Avengers: Age of Ultron",
"Friendship means never having to say you're sorry for \
creating a supervillain",
"https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/\
Avengers_Age_of_Ultron.jpg/220px-Avengers_Age_of_Ultron.jpg",
"https://www.youtube.com/watch?v=JAUoeqvedMo",
"May 1, 2015",
"Joss Whedon",
"Phase Two")

ant = media.Movie("Ant-Man",
"Paul Rudd and a suit",
"https://upload.wikimedia.org/wikipedia/en/thumb/7/75/\
Ant-Man_poster.jpg/220px-Ant-Man_poster.jpg",
"https://www.youtube.com/watch?v=pWdKf3MneyI",
"July 17, 2015",
"Peyton Reed",
"Phase Two")

captain_3 = media.Movie("Captain America: Civil War",
"Now the government has my shield",
"https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Captain_America\
_Civil_War_poster.jpg/220px-Captain_America_Civil_War_poster.jpg",
"https://www.youtube.com/watch?v=dKrVegVI0Us",
"May 6, 2016",
"Anthony and Joe Russo",
"Phase Three")

doctor_strange = media.Movie("Doctor Strange",
"A boy and yoga",
"https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/\
Doctor_Strange_poster.jpg/220px-Doctor_Strange_poster.jpg",
"https://www.youtube.com/watch?v=HSzx-zryEgM",
"November 4, 2016",
"Scott Derrickson",
"Phase Three")

guardians_2 = media.Movie("Guardians of the Galaxy Vol. 2",
"Friendship means never having to say you're sorry that \
your family will probably try to destroy everyone",
"https://upload.wikimedia.org/wikipedia/en/thumb/9/95/\
GotG_Vol2_poster.jpg/220px-GotG_Vol2_poster.jpg",
"https://www.youtube.com/watch?v=2cv2ueYnKjg",
"May 5, 2017",
"James Gunn",
"Phase Three")

spider_man = media.Movie("Spider-Man: Homecoming",
"I'm not even supposed to be here, but can I also be friends?",
"https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Spider-Man\
_Homecoming_poster.jpg/220px-Spider-Man_Homecoming_poster.jpg",
"https://www.youtube.com/watch?v=U0D3AOldjMU",
"July 7, 2017",
"Jon Watts",
"Phase Three")


movies = [iron_man, hulk, iron_man_2, thor, captain, avengers, iron_man_3, \
          thor_2, captain_2, guardians, avengers_2, ant, captain_3, \
          doctor_strange, guardians_2, spider_man]

fresh_tomatoes.open_movies_page(movies)