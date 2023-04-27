# ML-Practical-Exam
Emotion Detection from Text using ML models - To design and develop a Binary Classification model for Sentimental Analysis based on User-Input answers to three questions and to provide generalised video suggestions based on the mood of the user.

The preprocessing steps followed on this dataset are : 
1. Lower Casing : Each text is converted to lowercase.
2. Replacing URLS : Links starting with ‘www’ or ‘http’ are replaced with ‘URL’.
3. Replacing Emojis : The emojis mentioned in the tweets are replaced with a meaning which describes it with the help of predefined dictionary containing emojis along with their meanings.
4. Replacing Usernames : Replace @usernames with the word ‘USER’.
5. Removing Non Alphabets : Replacing characters except digits and alphabets with space.
6. Removing Consecutive Letters : 3 or more consecutive letters are replaced by 2 letters.
7. Removing Short Words : Words with length less than 2 are removed.
8. Removing Stopwords : Stopwords are the words which do not much add meaning to the sentence.
9. Lemmatizing : Lemmatization is the process of converting a word to its base form.

Different types of model for our sentiment analysis problem:
Logistic Regression (LR)
Support Vector Classification (SVC)
Naive Bayesian
Decision Tree
Random Forest






