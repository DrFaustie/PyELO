import math

# Function to calculate the Probability
def Probability(rating1, rating2):

    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))

# Function to calculate Elo rating
# K is a constant.
# d determines winner
def EloRating(Ra, Rb, K, d):


    # To calculate the Winning
    # Probability of Player A
    Pa = Probability(Rb, Ra)

    # To calculate the Winning
    # Probability of Player B
    Pb = Probability(Ra, Rb)

    Pa = round(Pa, 2)
    Pb = round(Pb, 2)

    # Case -1 When Player A wins
    if (d == 0):
        Ra = Ra + K * (1 - Pa)
        Rb = Rb + K * (0 - Pb)


    # Case -2 When Player B wins
    if (d == 1):
        Ra = Ra + K * (0 - Pa)
        Rb = Rb + K * (1 - Pb)

    # Case -3 when Player A and Player B draw
    if (d == 2):
        Rb = Rb + K * (Pa - Pb)
        Ra = Ra + K * (Pb - Pa)


    # Ratings for player1 and player2
    r1 = round(Ra, 6)
    r1 = int(r1)
    r2 = round(Rb, 6)
    r2 = int(r2)

    return (r1, r2)

# Driver code

# Ra and Rb are current ELO ratings
Ra = 1200
Rb = 1000
K = 32
d = 1
EloRating(Ra, Rb, K, d)