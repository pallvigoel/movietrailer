# importing module in which website renders the list of movies
import fresh_tomatoes
import movie  # importing module in which Movie class is defined

kuchkuchhotahai = movie.Movie(
    "kuchkuchhotahai",
    "a story of sharukhkhan and kajal",
    "download.jpg",
    "https://www.youtube.com/watch?v=05i3eIuJLaU")
# instantiating instance variables
krrish = movie.Movie(
    "krrish", "a story of alien", "k.jpg",
    "https://www.youtube.com/watch?v=MCCVVgtI5xU")
dhoom = movie.Movie(
    "dhoom", "a story of thief", "dhoom.jpg",
    "https://www.youtube.com/watch?v=sWE458JxSZA")
dabang = movie.Movie(
    "dabang", "a story of cop", "d.jpg",
    "https://www.youtube.com/watch?v=7nPN1M9zVcI")
bahubali = movie.Movie(
    "bahubali", "a story of bahubali", "b.jpg",
    "https://www.youtube.com/watch?v=qD-6d8Wo3do")
junglebook = movie.Movie(
    "junglebook", "a story of jungle animals", "j.jpg",
    "https://www.youtube.com/watch?v=C4qgAaxB_pc")
movies = [kuchkuchhotahai, krrish, dhoom, dabang, bahubali, junglebook]
fresh_tomatoes.open_movies_page(
    movies
    )  # passing argument of movie list
