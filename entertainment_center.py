# -*- coding: utf-8 -*-

import media
import fresh_tomatoes

spirited_away = media.Movie("Spirited Away", "Anime fantasy film about a girl who travels into the spirit world", "https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG", "https://www.youtube.com/watch?v=ByXuk9QqQkk")

million_dollar_baby = media.Movie("Million Dollar Baby", "An aging boxing trainer takes on an underdog female boxer", "https://upload.wikimedia.org/wikipedia/en/d/d3/Million_Dollar_Baby_poster.jpg", "https://www.youtube.com/watch?v=IH7gQqpw7ok")

mulholland_drive = media.Movie("Mulholland Drive", "A neo-noir mystery film", "https://upload.wikimedia.org/wikipedia/en/0/0f/Mulholland.png", "https://www.youtube.com/watch?v=96R9MG0DxLc")

inside_out = media.Movie("Inside Out", "Animated film set in the mind of an adolescent girl", "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg", "https://www.youtube.com/watch?v=yRUAzGQ3nSY")

mad_max_fury_road = media.Movie("Mad Max: Fury Road", "The fourth Mad Max film", "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg", "https://www.youtube.com/watch?v=hEJnMQG9ev8")

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind", "Romantic science fiction comedy-drama", "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg", "https://www.youtube.com/watch?v=yE-f1alkq9I")

movies = [spirited_away, million_dollar_baby, mulholland_drive, inside_out, mad_max_fury_road, eternal_sunshine]
fresh_tomatoes.open_movies_page(movies)

#avatar.show_trailer()
#mulholland_drive.show_trailer
