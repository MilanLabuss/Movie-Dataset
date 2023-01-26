# Movie-Dataset

The objective of this project is to provide an insight into the underlying pattern of the dataset such
as statistical details of different features and etc. Please perform the following tasks:

1. Each movie has a feature that shows the imdb score of the movie. For this task you are
required to find the average of imdb score for the following sub-groups:
•A group of movies where the director of the movie is also the first actor of the movie.
•A group of movies where the director of the movie is also the second actor of the movie.
•A group of movies where the director of the movie is also the third actor of the movie.
•A group of movies where the director of the movie is not acting as the first, second or
third actor.
Use an appropriate visualization technique and visually compare the average of imdb score of
the above groups. Interpret your findings.

2. Each movie is either color or black and white. Use appropriate visualization technique and
display the number of color movies and the number of black and white movies. Perform
appropriate data cleaning before visualization so at the end you will have only two unique
values in the dataset. If a movie type is Unknown, they need to be excluded from this analysis.
Explain your decisions for data cleaning and finally interpret the results.

3. Each movie may contain one or more than one genre(s). If a movie has more than one genre,
the genres are separated by pipe symbol (i.e., |). You are required to first extract all the
unique genres and then find the top 5 popular genres within the dataset. And finally apply
an appropriate visualization to visually depict the population of each genre.

4. Each movie has a length (duration). For this task, you are required to analyse this feature of
the movies and visually depict the collection of movies’ duration as follows:
(a) Remove all cells that are either empty of have non numerical values.
(b) Apply boxplot and visually depict the distribution of the movies’ duration, e.g., what is
the minimum, maximum, median, first quartile and third quartile.
(c) Apply another visualization (simple diagram) to display all the movies’ duration in a
sorted ordering. The low-outliers and high-outliers should be visualized with different
colors. Blue indicates the low-outliers (duration that are smaller than the minimum) and
red indicates high-outliers (duration that are larger than the maximum) See Figure 1 as
a reference for this task.

5. Each movie has a budget in the input file. In this task, you are required to extract a subset
of all movies (targetSet) where their budget falls in the range of Aand B. Aand Bare
identified as follows:
(a) The median of the entire collection of movie budgets is identified and named C.
(b) Two sub-collections are created: Sub1: movies with budget less than Cand Sub2:
movies with budget greater than C.
(c) The median of Sub1 is called Aand the median of Sub2 is called B.
Use an appropriate visualization technique and visually depict the common movie-budgets in
targetSet. Explain your finding.
Note that all visualization plots need to have proper labels and annotations if needed. Lack of
visualization features attracts penalty. 
