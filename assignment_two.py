# -*- coding: utf-8 -*-
"""
Created on a cloudy day
@Student Name: Milan Labus
@Student id: R00221283
@Cohort: SD3 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter
df = pd.read_csv("movie_metadata.csv", encoding = "ISO-8859-1")
 
def Task1():
    
    #First cleaning the Data by adding the mean to empty cells of imdbscore
   df['imdb_score']= df['imdb_score'].apply(pd.to_numeric, errors='coerce')
   imdbmean = df['imdb_score'].mean()
   df['imdb_score'] = df['imdb_score'].fillna(imdbmean)

   #Creating the subgroups using the criteria
   subgroup1 = df.loc[ df['director_name']==df['actor_1_name']]
   sub1mean = subgroup1['imdb_score'].mean()
  
   subgroup2 = df.loc[ df['director_name']==df['actor_2_name']]
   sub2mean = subgroup2['imdb_score'].mean()

   subgroup3 = df.loc[ df['director_name']==df['actor_3_name']]
   sub3mean = subgroup3['imdb_score'].mean()
  
   subgroup4 = df.loc[  ( df['director_name']!=df['actor_1_name'] )
                & (df['director_name']!=df['actor_2_name']) 
                & (df['director_name']!=df['actor_3_name']) ]
   sub4mean = subgroup4['imdb_score'].mean()
   
   x = np.array(["direct+act1", "direct+act2", "direct+act3", "only director"])
   y = np.array([sub1mean,sub2mean,sub3mean,sub4mean])
   plt.ylim(5,7)
   plt.bar(x,y)
   plt.title("Director Role mean")
   plt.xlabel("Director Role")
   plt.ylabel("Mean imdb score") 
   plt.show()
   
   #I use the df.loc function with appropriate criteria to find the subgroups
   #Then i store the means of the subgroups into variable and plot then to a bar
   #I also change the y axis to be in the ranges 5-7 to better represent the data
   #we see that the higher on the actor tier the director was
   #the better the score the movie got
   #and for movies where the director didnt act got an imbd score
   #in the middle of the other three
    

Task1()
  

def Task2():
    
    
    #excluding empty cells from the analysis
   df.dropna(subset=['Type'], inplace=True)


    #filtering the Type Columnß
   blacknwhite =  ((df['Type']!= "Color") & (df['Type'].str.contains('Black', na=False))) 
   color = df['Type'] == "Color"

   y = np.array([ len(df[blacknwhite]),len(df[color])  ])
   mylabels = ["Black and White", "Color"]
   plt.pie(y, labels = mylabels)
   plt.title("Movie Types")
   plt.show() 
   #adding to blacknwhite only the cells in the type column that contain the 
   #word black in it because after analysing the data all of the variations contain
   #Some form of this word in it and as an added filter i added that it does not
   #contain the word color in it
   #I then also extract all the coor types and store their lenghts in a np array
   #and put it in y and write my label in my labels and plot it to a pie chart
   #Which best visually show the proportion of color not non color movies
   #and we see that the majority are color movies
   
    
Task2()


def Task3():

     
     print(df['genres'])
     
     df['genres'] = df['genres'].str.split('|')
     new_df = df.explode('genres')

     genreCounts = new_df['genres'].value_counts()
     #print(bestGenres.head(5))
     topFive = genreCounts.head(5)  #new series called topFive
    
     plt.title("Top 5 Genres")
     ax =  topFive.plot.bar()
     ax.set_xlabel("Genres")
     ax.set_ylabel("Frequency")
     plt.show()
     
     #First I split the genres column to remove all of the pip
     #Then I used the explode function to turn every genre column into a row
     #Then i store the value_counts into genreCount and the head(5) into topFive
     #Then i plot it to a bar because it visually is the best representation of this data
     #and we see Drama is the most common genre
     
    
Task3()


def Task4():
    #a:
    #excluding empty cells from the analysis
     df.dropna(subset=['duration'], inplace=True)
     #excluding all non numerical values
     df['duration']= df['duration'].apply(pd.to_numeric, errors='coerce')
     
     #b:
     plt.boxplot(df['duration'])
     plt.ylabel("duration(mins)")
     plt.title("Duration boxplot")
     plt.show()
     
     #c
     #getting the firt and third quartile
     q1=df['duration'].quantile(0.25)  

     q3=df['duration'].quantile(0.75) 


    #sorting the durations lowerst to highest and resetting the indexes
     df['duration'] = df['duration'].sort_values(ascending=True).reset_index(drop=True)
     #putting upper,lower and middle parts into segments using the quartiles
     seg1 = df.loc[df['duration'] <= q1]
     seg2 = df.loc[(df['duration'] >= q1)
                   & (df['duration'] <= q3) ]
     seg3 = df.loc[df['duration'] >= q3]
     
     #plotting all of the segments in different colors for illustration
     plt.plot(seg1['duration'], "b")
     plt.plot(seg2['duration'],"g")
     plt.plot(seg3['duration'], "r")
     #labelling x and y 
     plt.ylabel("duration(min)")
     plt.xlabel("count")
     plt.title("Durations")
     #we can see that the majority of movies are between 100 and 200 minutes long
    

    
Task4()

def Task5():

    #data cleaning: excluding empty cell
    df.dropna(subset=['budget'], inplace=True)
    C = df['budget'].median()

    #Filtering into but by greater and less than C
    Sub1 = df.loc[df['budget'] < C]
    Sub2 = df.loc[df['budget'] > C]
    #making A and B equal to the median of the subs
    A = Sub1['budget'].median()
    B = Sub2['budget'].median()

    #fitlering between A and B
    filt = df.loc[ (df['budget'] > A)  
                      & (df['budget'] > B)  ]
    #defining targetSet
    targetSet = filt['budget']   

    #function to format the x axis millions
    def millionsformat(x, pos):
        return '%1.0fM' % (x*1e-6)

    formatter = FuncFormatter(millionsformat)


    #plotting targetSet to a histogram with ranges 40-200 million
    ax = targetSet.plot(kind='hist',range=[40000000, 200000000]) #40 and 200 mil
    ax.set_xlabel("Budget Millions")
    ax.set_ylabel("Frequency")
    ax.xaxis.set_major_formatter(formatter) 


    #we see from the histogram that movie budgets are
    #most commonly between 40 and  80 million
   

Task5()


     
    
    
    
    
    
    
    
    
     
    
    
  
