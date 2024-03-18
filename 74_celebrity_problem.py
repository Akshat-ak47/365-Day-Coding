'''
Celebrity Problem

There are ( N+1 ) people in a party, they might or might not know each others names. 

There is one celebrity in the group (total N + 1 people), celebrity does not know any of N peoples by name and all N people know celebrity by name.

You are given the list of people’s names (N + 1),

You can ask only one question from the people.

	Do you know this name?
How many maximum number of questions you need to ask to know the celebrity name?
'''

'''
Answer - N

When you ask a person whether they know someone, you can eliminate at most one person as the celebrity. This means with each question, the number of potential celebrities decreases by one.
Since there are N + 1 people and one celebrity, you need to ask N questions to eliminate all other people except the celebrity.
Therefore, the maximum number of questions needed to identify the celebrity is N.
'''