class Actor:
    
    def __init__(self, actor_id, name, gender):
        
        self.__actor_id = actor_id
        self.__name = name
        self.__gender = gender
        self.__movielist = []
        
    def a_movie(self, movie):
        
        self.__movielist.append(movie)
    
    @property
    def actor_id(self):
        return self.__actor_id

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender  
    
    @property
    def movielist(self):
        return self.__movielist

        
    def __str__(self):
        return 'actor id:' + str(self.__actor_id) + ', name:' + self.__name + ', gender:' + self.__gender + ','
    
    
class Genre:

    def __init__(self, genre_id, genre_title):
                
        self.__genre_id = genre_id
        self.__genre_title = genre_title
        self.__movielist = []

    @property
    def genre_id(self):
        return self.__genre_id

    @property
    def genre_title(self):
        return self.__genre_title
    
    @property
    def movielist(self):
        return self.__movielist
    
    
    def g_movie(self, movie):
        self.__movielist.append(movie)    
            
        
    def __str__(self):
        return 'genre_id: ' + str(self.__genre_id) + ', title: ' + self.__genre_title + ', '
    
        
class Movie:
    
    def __init__(self, movie_id, movie_title, release_date):
        
        self.__movie_id = movie_id
        self.__movie_title = movie_title
        self.__release_date = release_date
        self.__rating = None
        self.__actors = []
        self.__genres = []
        
    @property
    def movie_id(self):
        return self.__movie_id

    @property
    def movie_title(self):
        return self.__movie_title

    @property
    def release_date(self):
        return self.__release_date

    @property
    def rating(self):
        return self.__rating

    @property
    def actors(self):
        return self.__actors

    @property
    def genres(self):
        return self.__genres
    
    
    def addActor(self, actor):
        self.actors.append(actor)
        
        
    def addGenres(self, genre):
        self.genres.append(genre)
        

    def __str__(self):
        return 'movie_id: ' + str(self.__movie_id) + ', title: ' + self.__movie_title + ', release date: ' + self.__release_date
    

class Rating:
    def __init__(self, rating_id, category):
        
        self.__rating_id = rating_id
        self.__category = category

    @property
    def rating_id(self):
        return self.__rating_id
    
    @property
    def category(self):
        return self.__category
    
    def __str__(self):
        return 'rating_id: ' + str(self.__rating_id) + ', category: ' + self.__category
    

def main():
    
    movie_list = [Movie(1, '아이 캔 스피크', '20170921'), Movie(2, '킹스맨', '20170927'),  Movie(3, '남한산성', '20171003')]
    actor_list = [Actor(1, '나문희', '여'), Actor(2, '콜린 퍼스', '남'), Actor(3, '이병헌', '남')]
    genre_list = [Genre(1, '드라마'), Genre(2, '액션'), Genre(3, '드라마')]
    rating_list = [Rating(1, '12세 이상 관람가'), Rating(2, '19세 이상 관람가'), Rating(3, '15세 이상 관람가')]
    
    
    for num in range(0,3):
        actor_list[num].a_movie(movie_list[num])
        genre_list[num].g_movie(movie_list[num])
        movie_list[num].addActor(actor_list[num])
        movie_list[num].addGenres(genre_list[num])
        
        print(actor_list[num].movielist[0], movie_list[num].actors[0], movie_list[num].genres[0], rating_list[num])
    
    
main()

    