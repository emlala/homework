# Raw text data processing task for the course Introduction to Data Science

This assignment looks into Amazon reviews, and the steps needed to transform a raw dataset into one more suitable for prediction tasks.
Download the automotive 5-core json format dataset. 

The reviewText field contains the unstructured review text written by the user. 
When applying statistical methods on this data, it is useful to ensure that words with the same meaning are represented by the same string.
To do this, we usually normalize the data, by for example removing punctuation and capitalization differences. A related issue is that, for example, while again the words "swims" and "swim" are distinct string, they both refer to swimming. Stemming refers to the process of mapping words in inflected form to their base form: swims -> swim, etc.

Finally, another popular approach is to remove so called stop-words, words that are very common and have little to do with the actual content matter. There's plenty of openly available lists of stop-words for almost any (natural) language.

Do the following:

a) Open the json file in python
b) Access the reviewText field, and downcase the contents
c) Remove all punctuation, as well as the stop-words. You can find a stop-word lists for English online
d) Apply a stemmer on the paragraphs, so that inflected forms are mapped to the base form. 
e) Filter the data by selecting reviews where the field overall is 4 or 5, and store the review texts in file pos.txt. Similarly, select reviews with rating 1 or 2 and store the reviews in file neg.txt. (Ignore the reviews with overall rating 3.) Each line in the two files should contain exactly one preprocessed review text without the rating.
