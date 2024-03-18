'''
Medicine Chest on a Boat

Alice and Bob are on separate islands. Bob is sick, and Alice has the medicine. Eve has a boat and a chest that can be locked. She is willing to transport objects between Alice and Bob, but only in the chest, and if the chest is unlocked, she will steal whatever is inside.

If both Alice and Bob have a padlock and a key such that their own key only opens their own lock.  Is it possible for Alice to send the medicine to Bob? If so, how many minimum trips are required? Note that Bob and Alice cannot travel in the boat. The boat going from Alice to Bob or Bob to Alice counts as 1 trip.

Case 1 : Answer is a integer. Just put the number without any decimal places if its an integer. If its not possible for Alice to send the medicine to Bob, output Infinity.
Case 2 : Floating point number. Round it off to 2 decimal places and output it as I.xx where I is the integer part of the answer, and xx are 2 decimal digits after rounding off.
'''


'''
1. Alice puts the medicine in the chest, locks it with her padlock, and sends it to Bob.

2. Bob receives the chest, adds his padlock on it without opening Alice's lock, and sends it back to Alice.

3. Alice receives the chest with both her and Bob's padlocks on it. She removes her padlock, leaving only Bob's padlock on the chest, and sends it back to Bob.

Bob receives the chest with only his padlock on it and can now unlock it to access the medicine.
'''