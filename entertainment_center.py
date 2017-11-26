import fresh_tomatoes
import media

guardians = media.Movie("Guardians of the Galaxy",
                        "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.",
                        "http://t1.gstatic.com/images?q=tbn:ANd9GcRBeWiUyul0Y9qPP6FKnAMLgbDnVDWK9GSaWD29ozMz9s8Y_WuE",
                        "https://www.youtube.com/watch?v=of1OhDiwVD0&index=1&list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7jzFy-")
 
 
movies = [guardians]
fresh_tomatoes.open_movies_page(movies)
