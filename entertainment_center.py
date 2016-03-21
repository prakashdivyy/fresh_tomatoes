import media
import fresh_tomatoes

# Movie declaration
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

deadpool = media.Movie("Deadpool",
                       "Bad superhero",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=9vN6DHB6bJc")

batman_vs_superman = media.Movie("Batman v Superman: Dawn of Justice",
                                 "Batman vs Superman",
                                 "https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg",
                                 "https://www.youtube.com/watch?v=Cle_rKBpZ28")

kung_fu_panda_3 = media.Movie("Kung Fu Panda 3",
                              "Po meets his dad",
                              "https://upload.wikimedia.org/wikipedia/en/e/e6/Kung_Fu_Panda_3_poster.jpg",
                              "https://www.youtube.com/watch?v=10r9ozshGVE")

zootopia = media.Movie("Zootopia",
                       "A rabbit wants to be a police",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=bY73vFGhSVk")

# Array of Movie
movies = [toy_story, avatar, deadpool,
          batman_vs_superman, kung_fu_panda_3, zootopia]

# Display Movie in HTML page
fresh_tomatoes.open_movies_page(movies)
