        
# n=5
# coins = [1,1,1,0,1]
# Sample Output:
# 2
# Explanation:
# If player 1 plays 0 segments, their score would be 0, and Player 2's score would be 4-1=3
# If player 1 plays 1 segments, their score would be 1, and Player 2's score would be 3-1=2
# If player 1 plays 2 segments, their score would be 2, and Player 2's score would be 2-1=1

# Only in this last case, by playing 2 segments, would Player 1's score be greater than Player 2's.Therefore, return the answer 2

coins = [1, 1, 0, 1]
for i in range(len(coins)):
    if coins[i]==0:
        coins[i]=-1
print(coins)        
n= len(coins)
player_a = 0
player_b = sum(coins)
if(player_a>player_b):
    print(player_a)
else:
    for i in range(n):
        player_a += coins[i]
        player_b =0
        sublist = coins[i+1:n]
        player_b = sum(sublist)
    
        if(player_a > player_b):
            print(i+1)
            break   
    
# def playSegments(coins):
#     n= len(coins)
#     player1_score = 0
#     player2_score = sum(coins)

#     for i in range(n):
#         if coins[i] == 1:
#             player1_score += 1
#         else:
#             player1_score -= 1

#         if player1_score > player2_score:
#             return i + 1

#     return 0   

# print(playSegments(coins))