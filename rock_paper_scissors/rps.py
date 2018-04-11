print("...rock...")
print("...paper...")
print("...scissors...")
p1 = input("(enter Player 1's choice): ")
print("*** NO PEEKING ***\n"*30)
p2 = input("(enter Player 2's choice): ")
print("SHOOT!")

if p1 == p2:
    print("Draw")
elif p1 == "rock" and p2 == "scissors":
    print("p1 wins")
elif p1 == "paper" and p2 == "rock":
    print("p1 wins")
elif p1 == "scissors" and p2 == "paper":
    print("p1 wins")
else:
    print("p2 wins")
