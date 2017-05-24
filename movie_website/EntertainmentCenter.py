import moviewebsite
import fresh_tomatoes

shawshank = moviewebsite.Movie('Shawshank Redemption',
                               'Story of a prison escape',
                               'https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg',
                               'https://www.youtube.com/watch?v=6hB3S9bIaco')

aliens = moviewebsite.Movie('Aliens',
                            'Story about aliens invading a human space ship',
                            'https://upload.wikimedia.org/wikipedia/en/f/fb/Aliens_poster.jpg',
                            'https://www.youtube.com/watch?v=XKSQmYUaIyE')

fracture = moviewebsite.Movie('Fracture',
                              'A movie about a murder trial',
                              'https://www.youtube.com/watch?v=iewD4nuXlF4',
                              'https://upload.wikimedia.org/wikipedia/en/thumb/0/01/Fracture2007Poster.jpg/220px-Fracture2007Poster.jpg')

hot_tub_time_machine = moviewebsite.Movie('Hot tub time Machine',
                                          'A movie about a group of middle age men that find out there hot tub is actualy a time machine',
                                          'https://www.youtube.com/watch?v=Bbkr8_-Hehk',
                                          'https://upload.wikimedia.org/wikipedia/en/thumb/6/64/Hot_tub_time_machine_poster.jpg/220px-Hot_tub_time_machine_poster.jpg')

avengers = moviewebsite.Movie('Avengers age of ultron',
                              'A marvel comic based movie about the group of super heroes known as the avengers',
                              'https://www.youtube.com/watch?v=tmeOjFno6Do',
                              'https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/Avengers_Age_of_Ultron.jpg/220px-Avengers_Age_of_Ultron.jpg')

ghostbusters = moviewebsite.Movie('GhostBusters',
                                  'Bustin makes me feel good!',
                                  'https://www.youtube.com/watch?v=vntAEVjPBzQ',
                        r'https://upload.wikimedia.org/wikipedia/en/thumb/2/2f/Ghostbusters_%281984%29_theatrical_poster.png/220px-Ghostbusters_%281984%29_theatrical_poster.png')

movies = [shawshank, aliens, fracture, hot_tub_time_machine, avengers, ghostbusters]
fresh_tomatoes.open_movies_page(movies)