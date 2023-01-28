This program defines a function typing_test() that takes no arguments. 
It uses the random.choice() function to randomly select a sentence from a list of sample sentences. 
The function then uses the input() function to prompt the user to type the sentence as fast as they can. 
The function then calculates the time taken by subtracting the start time from the end time and uses this 
value to calculate the typing speed in words per minute (WPM) by dividing the number of words in the sentence by the time taken in minutes.
Then it calculates the accuracy by comparing the sentence and user input letter by letter, 
and count the number of errors. Finally, it returns the typing speed and accuracy.
You can improve this further by adding more sentences, giving the user multiple chances to type the sentence and taking the average of the WPM and accuracy, 
and also you can add a feature that stops the typing test if they make more than 2 or 3 mistakes.
