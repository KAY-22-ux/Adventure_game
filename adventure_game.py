#This is a text-based adventure game with three levels of choices, using nested if-else statements. 
# The player make choices that lead to different scenarios, and the game includes an additional creative feature.


def run_game ():
    player_name = input("Enter player name: ")
    print(f"Welcome to the Adventure game ,{player_name.upper()} Let's begin")
    points = 0
    # Level 1: Starting scenario
    print("You are walking through a dark forest and find three items: a MATCH, a FLASHLIGHT, and a SWORD. Which one do you want to pick up?\n")
    choice1 = input("Type MATCH, FLASHLIGHT, or SWORD: ").lower()  # Convert input to lowercase to handle case insensitivity
    if choice1 == "match":
        points += 10
        # Level 2: Scenario after picking the match
        print("You pick up the match and strike it, and for an instant, the forest around you is illuminated.")
        print("You see a large grizzly bear, and then the match burns out.\n")
        choice2 = input("Do you want to RUN, HIDE behind a tree, or THROW the match at the bear? \n").lower() 

        if choice2 == "run":
            points += 5
            # Level 3: Scenario after choosing to run
            print("You start running as fast as you can, but the bear is faster. It catches up to you.")
            print("You have three options: FIGHT the bear, PLAY DEAD, or CLIMB a tree.\n")
            choice3 = input("Type FIGHT, PLAY DEAD, or CLIMB: ").lower()

            if choice3 == "fight":
                points += 5
                # Level 4: Scenario after choosing to fight
                print("You try to fight the bear, but it's too strong. The bear overpowers you.")
                print("Game over! The bear got you.\n")

            elif choice3 == "play dead":
                points += 20
                # Level 4: Scenario after choosing to play dead
                print("You play dead, and the bear loses interest in you. It walks away.")
                print("You survived! You win the game.\n")

            elif choice3 == "climb":
                points += 10
                # Level 4: Scenario after choosing to climb a tree
                print("You climb a tree, but the bear starts shaking it. You fall and get injured.")
                print("Game over! The bear got you.")
                

            else:
            # Handle invalid input for Level 3
                print("Invalid choice. You hesitated too long, and the bear got you. Game over!\n")
                
        elif choice2 == "hide":
            points += 10
            # Level 3: Scenario after choosing to hide
            print("You hide behind a tree and stay very quiet. The bear walks past you without noticing.")
            print("You see a path leading out of the forest. Do you want to FOLLOW the path, STAY hidden, or EXPLORE deeper into the forest?\n")       
            choice3 = input("Type FOLLOW, STAY, or EXPLORE: ").lower()
            if choice3 == "follow":
                points += 20
            # Level 4: Scenario after choosing to follow the path
                print("You follow the path and eventually find your way out of the forest.")
                print("Congratulations! You escaped the forest and won the game.\n")
                

            elif choice3 == "stay":
                points += 5
            # Level 4: Scenario after choosing to stay hidden
                print("You stay hidden, but the bear comes back and finds you.")
                print("Game over! The bear got you.\n")
                
            elif choice3 == "explore":
                    points += 50
                    # Level 4: Scenario after choosing to explore deeper
                    print("You explore deeper into the forest and find a hidden treasure!")
                    print("Congratulations! You found treasure and won the game.\n")
                    
            else:
                # Handle invalid input for Level 3
                print("Invalid choice. You hesitated too long, and the bear found you. Game over!\n")
                
                
        elif choice2 == "throw":
            points += 10
            # Level 3: Scenario after choosing to throw the match
            print("You throw the match at the bear, but it does nothing. The bear charges at you.")
            print("You have three options: FIGHT the bear, PLAY DEAD, or RUN away.\n")
            choice3 = input("Type FIGHT, PLAY DEAD, or RUN: ").lower()
            if choice3 == "fight":
                points += 5
                # Level 4: Scenario after choosing to fight
                print("You try to fight the bear, but it's too strong. The bear overpowers you.")
                print("Game over! The bear got you.\n")
                
            elif choice3 == "play dead":
                points += 30
                # Level 4: Scenario after choosing to play dead
                print("You play dead, and the bear loses interest in you. It walks away.")
                print("You survived! You win the game.\n")
                
            elif choice3 == "run":
                points += 5
                # Level 4: Scenario after choosing to run
                print("You run away, but the bear catches up to you.")
                print("Game over! The bear got you.\n")
                
            else:
                # Handle invalid input for Level 3
                print("Invalid choice. You hesitated too long, and the bear got you. Game over!\n")
                

        else:
            # Handle invalid input for Level 2
                print("Invalid choice. You hesitated too long, and the bear got you. Game over!\n")
                

                
    elif choice1 == "flashlight":
        points += 10
        #Level 2: Scenario after picking the flashlight
        print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you.")
        print("You thought you also heard something off to the side.\n")
        choice2 = input("Do you want to FOLLOW the path, LOOK in the trees, or SHOUT for help? ").lower()
        if choice2 == "follow":
            points += 15
            # Level 3: Scenario after choosing to follow the path
            print("You follow the path and see a river ahead. Do you want to SWIM across, LOOK for a bridge, or TURN back?\n")
            choice3 = input("Type SWIM, LOOK, or TURN: ").lower()
            if choice3 == "swim":
                points += 5
                # Level 4: Scenario after choosing to swim
                print("You try to swim across the river, but the current is too strong. You get swept away.")
                print("Game over! You drowned in the river.\n")
                 
            elif choice3 == "look":
                points += 25
                # Level 4: Scenario after choosing to look for a bridge
                print("You look around and find a sturdy bridge. You cross the river safely.")
                print("Congratulations! You escaped the forest and won the game.\n")
                
            elif choice3 == "turn":
                points += 5
                # Level 4: Scenario after choosing to turn back
                print("You turn back, but you get lost in the forest.")
                print("Game over! You never found your way out.\n")
                 
            else:
                # Handle invalid input for Level 3
                print("Invalid choice. You hesitated too long, and something in the darkness got you. Game over!\n")
                 
        
        elif choice2 == "look":
            points += 15
            # Level 3: Scenario after choosing to look in the trees
            print("You look in the trees and see a pair of glowing eyes staring back at you.")
            print("You have three options: THROW a rock at the eyes, SHINE your flashlight at them, or RUN away.")
            choice3 = input("Type THROW, SHINE, or RUN: ").lower()
            if choice3 == "throw":
                points += 6
                # Level 4: Scenario after choosing to throw a rock
                print("You throw a rock at the eyes, and a wolf jumps out and attacks you.")
                print("Game over! The wolf got you.\n")
                 
            elif choice3 == "shine":
                points += 30
                # Level 4: Scenario after choosing to shine the flashlight
                print("You shine your flashlight at the eyes, and the wolf runs away.")
                print("You survived! You win the game.\n")
            elif choice3 == "run":
                points += 5
                 # Level 4: Scenario after choosing to run
                print("You run away, but the wolf chases you and catches up.")
                print("Game over! The wolf got you.\n")
                
            else:
                # Handle invalid input for Level 3
                print("Invalid choice. You hesitated too long, and the wolf attacked you. Game over!\n")
                

        elif choice2 == "shout":
            points += 5
            # Level 3: Scenario after choosing to shout for help
            print("You shout for help, but no one answers. You hear rustling in the bushes.")
            print("You have three options: INVESTIGATE the noise, RUN away, or HIDE.\n")
            choice3 = input("Type INVESTIGATE, RUN, or HIDE: ").lower()
            if choice3 == "investigate":
                points += 20
                # Level 4: Scenario after choosing to investigate
                print("You investigate the noise and find a friendly traveler who helps you escape.")
                print("Congratulations! You escaped the forest and won the game.")
                
            elif choice3 == "run":
                points += 5
                # Level 4: Scenario after choosing to run.
                print("You run away, but you trip and fall. The wolf catches up to you.")
                print("Game over! The wolf got you.")
                
            elif choice3 == "hide":
                points += 5
                # Level 4: Scenario after choosing to hide
                print("You hide, but the wolf finds you.")
                print("Game over! The wolf got you.")
                
            else:
                # Handle invalid input for Level 3
                print("Invalid choice. You hesitated too long, and the wolf attacked you. Game over!")
                

        else:
            # Handle invalid input for Level 2
            print("Invalid choice. You hesitated too long, and something in the darkness got you. Game over!")

    elif choice1 == "sword":
        points += 15
        # Level 2: Scenario after picking the sword
        print("You pick up the sword and feel a surge of confidence.")
        print("You hear growling nearby. Do you want to SEARCH for the source, DEFEND yourself, or IGNORE it and keep walking?")
        choice2 = input("Type SEARCH, DEFEND, or IGNORE: ").lower()
        if choice2 == "search":
            points += 10
            # Level 3: Scenario after choosing to search
            print("You search for the source of the growling and find a wounded wolf.")
            print("You have three options: HELP the wolf, KILL it, or LEAVE it alone.")
            choice3 = input("Type HELP, KILL, or LEAVE: ").lower()
            if choice3 == "help":
                points += 30
                # Level 4: Scenario after choosing to help the wolf
                print("You help the wolf, and it becomes your loyal companion.")
                print("Congratulations! You escaped the forest with a new friend and won the game.")
                
            elif choice3 == "kill":
                points += 3
                # Level 4: Scenario after choosing to kill the wolf
                print("You kill the wolf, but its pack attacks you in revenge.")
                print("Game over! The wolf pack got you.")
                
            elif choice3 == "leave":
                points += 15
                # Level 4: Scenario after choosing to leave the wolf
                print("You leave the wolf alone and continue walking. You find your way out of the forest.")
                print("Congratulations! You escaped the forest and won the game.")
                
            else:
                # Handle invalid input for Level 3
                print("Invalid choice. You hesitated too long, and the wolf attacked you. Game over!")
                
        elif choice2 == "defend":
            points += 15
            # Level 3: Scenario after choosing to defend
            print("You prepare to defend yourself, but the wolf doesn't attack.")
            print("You have three options: ATTACK the wolf, SCARE it away, or WAIT.")
            choice3 = input("Type ATTACK, SCARE, or WAIT: ").lower()
            if choice3 == "attack":
                points += 5
                # Level 4: Scenario after choosing to attack
                print("You attack the wolf, but it fights back. You are injured.")
                print("Game over! The wolf got you.")
                
            elif choice3 == "scare":
                points += 20
                # Level 4: Scenario after choosing to scare the wolf
                print("You scare the wolf away, and it runs off into the forest.")
                print("Congratulations! You survived and won the game.")
                
            elif choice3 == "wait":
                points += 20
                # Level 4: Scenario after choosing to wait
                print("You wait, and the wolf eventually leaves you alone.")
                print("Congratulations! You survived and won the game.")
                
            else:
                # Handle invalid input for Level 3
                print("Invalid choice. You hesitated too long, and the wolf attacked you. Game over!")
                       
        elif choice2 == "ignore":
            points += 15
            # Level 3: Scenario after choosing to ignore
            print("You ignore the growling and keep walking. You find a hidden path.")
            print("You have three options: FOLLOW the path, TURN back, or REST for a while.")
            choice3 = input("Type FOLLOW, TURN, or REST: ").lower()
            
            if choice3 == "follow":
                points += 50
                # Level 4: Scenario after choosing to follow the path
                print("You follow the path and find a hidden treasure!")
                print("Congratulations! You found treasure and won the game.")
                
            elif choice3 == "turn":
                points += 6
                # Level 4: Scenario after choosing to turn back
                print("You turn back, but you get lost in the forest.")
                print("Game over! You never found your way out.")
                
            elif choice3 == "rest":
                points += 3
                # Level 4: Scenario after choosing to rest
                print("You rest, but the wolf finds you and attacks.")
                print("Game over! The wolf got you.")
                
            else:
                # Handle invalid input for Level 3
                print("Invalid choice. You hesitated too long, and the wolf attacked you. Game over!")

        else:
            # Handle invalid input for Level 2
            print("Invalid choice. You hesitated too long, and the wolf attacked you. Game over!")
    else:
    # Handle invalid input for Level 1
        print("Invalid choice. You didn't pick up anything, and now you're lost in the dark forest. Game over!")

    def determine_medal(points):
        if points > 65:
            return 'Gold 🥇'
        elif points < 50:
            return 'Bronze 🥉'
        else:
            return 'Silver 🥈'

    def player_stats():
        print("==============================")
        print("PLAYER REPORT")
        print("==============================")
        print(f"PLAYER NAME: {player_name}")
        print(f"POINTS EARNED(XP): {points}")
        print(f"MEDAL : {determine_medal(points)}")
        print("==============================\n")

    player_stats()
    replay = input("would you like to REPLAY or EXIT? : ")
    if replay.lower() == "replay":
        run_game()
    else:
        print("You have exited the game successfully.")


run_game()
    






