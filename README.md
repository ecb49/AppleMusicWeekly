This project was created from my curiousity to see how my music listening habits change from week to week.

To get the data, I downloaded my Apple Music library as an xml file which contains useful information from every track included in my library.
For this project, I am interested in keeping track of how many times I play a given track in a week from my library. For the purposes of this project, only tracks that are in my library are analyzed. 

From 7 unique pieces of data from each track. They are:
- Track ID
- Track Name
- Artist
- Album
- Total Time (milliseconds)
- Date Added to Library
- Play Count

Next a Dataframe is created with the columns being the fields listed above, and the rows being individual tracks.

To analyze my listening habits for the week I pass in two Dataframes, one that contains data from 1 week ago, and the other containing data from the current date. To see the songs I have been listening to in that week I simply subtract the play count values for each song in the two Dataframes, and output a third Dataframe contaning only songs that have a play count > 0 after the subtraction operation.

This is a fun way for me to keep track of what music I have been listening to, and let's me get a sneak peak into my music analytics before the Apple Music Replay comes out at the end of the year!

Happy listening.