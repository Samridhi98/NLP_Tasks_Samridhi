# Task - 5 (Samridhi Murarka 17BCE2038)
(December 20, 2019)

## 5.1 Webtext Corpus
NLTK's small collection of web text includes content from a Firefox discussion forum, conversations etc
   
   1. Viewing files in the corpus like firefox.txt, pirates.txt
   2. Extracting and displaying words from by specifying *fileids*
   3. Upto 10 words from each file in webtext corpus

## 5.2 Analysis of tweets in form of text
   1. Tweets are stored in a text file 'tweets.txt' 
   2. Splitting
   3. Concordance using token 'good'

## 5.3 Extracting data from URL / Web Links
   1. https://www.gutenberg.org/files/2554/2554-0.txt is the link used for extracting text
   2. Displaying features of the text
   
## 5.4 Tokenizing Data
   1. Used word_tokenize from NLTK library
   2. Joined the tokens using join and nltk.Text
   
## Issues Faced
   nltk.Text returns a 'Sentence' type data which is stored in angular brackets.
   To get a normal sentence manual joining was thus used 
