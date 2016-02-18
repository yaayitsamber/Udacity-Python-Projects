import fresh_tomatoes
import movies


fast_1 = movies.Movie("The Fast & The Furious","A story of family, fuel and fast cars","http://thesource.com/wp-content/uploads/2015/04/The-fast.jpg","http://www.dailymotion.com/video/x2cnroj_the-fast-and-the-furious-2001_shortfilms")
fast_2 = movies.Movie("2Fast 2Furious","A man on the run, is given a chance for redemption ","http://www.theworkprint.com/wp-content/uploads/2015/03/2-Fast-2-Furious-2003-poster.jpg","https://www.youtube.com/watch?v=ZZGkV_xWGw4")
fast_4 = movies.Movie("Fast and Furious", "Old friendships die hard, the family is reunited to avenge a heinous murder of one of their own","http://www.filmofilia.com/wp-content/uploads/2009/02/fastandthefurious4_poster.jpg","https://www.youtube.com/watch?v=bcY7HkvF1aw")
fast_5 = movies.Movie("Fast Five", "On the run from the law, but their reputaion proceeds them. The team assembles for one last job","http://www.uphe.com/sites/default/files/2015/04/Fast-Five-Gallery-23.jpg","https://www.youtube.com/watch?v=bf4oDjHUmkY")
fast_6 = movies.Movie("Furious 6", "The team must take down a terrorist with ties to a ally once presumed dead.","https://i.ytimg.com/vi/zmow0O2rsLE/maxresdefault.jpg","https://www.youtube.com/watch?v=dKi5XoeTN0k")
fast_7 = movies.Movie("Furious 7", "Remember that terrorist guy, well he has an older brother...","http://blogs-images.forbes.com/markhughes/files/2015/04/Furious-7.jpg","https://www.youtube.com/watch?v=Skpu5HaVkOc")

#print(hateful.storyline)
#hateful.show_trailer()
films = [fast_1, fast_2, fast_4, fast_5, fast_6, fast_7]
fresh_tomatoes.open_movies_page(films)
