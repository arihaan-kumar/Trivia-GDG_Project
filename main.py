import mysql.connector

#connecting the python file with the sql database

connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="trivia"
)

cursor = connect.cursor()

def new_player():
    p_name = input("Enter your name: ")

    cursor.execute("select username from users")
    data = cursor.fetchall()

#checking if the name exists in the database
    
    name_list = []
    for i in data:

        name_list.append(i[0])


    if p_name in name_list:
        print("Welcome back!")
        cursor.execute("select user_id from users where username = %s", (p_name,))
        result = cursor.fetchone()
        return result[0]
    else:
        cursor.execute("insert into users (username) values (%s)", (p_name,))
        connect.commit()
        print("User added successfully.")
        return cursor.lastrowid

def question(level_num):

#extracting the questions from the sql database
    
    table = "level" + str(level_num)
    cursor.execute("SELECT * FROM " + table + " ORDER BY RAND() LIMIT 1")
    question = cursor.fetchone()

#displaying the questions along with the options

    print(question[1])
    print("a.", question[2])
    print("b.", question[3])
    print("c.", question[4])
    print("d.", question[5])

    choice = input("Enter your answer (a/b/c/d): ").strip().lower()
    return choice == question[6].lower()

def play_game(user_id):

    prize = [1000, 5000, 10000, 50000, 100000, 500000, 2000000, 10000000]
    amount_won = 0
    questions_correct = 0

#the main part of the game, calling the question function and mainting the records of the user

    for level in range(1, 9):

        print("Level", level,": ₹",prize[level-1])
    
        
        answer = question(level)

        if answer == True:
            amount_won = prize[level-1]
            questions_correct += 1
            print("Correct Answer !", "Your prize is ₹", amount_won)
            

        else:
            print("Incorrect Answer, Game Over! You leave with ₹", amount_won)
            break

    cursor.execute("UPDATE users SET total_games_played = total_games_played + 1, total_questions_correct = total_questions_correct + %s, best_score = GREATEST(best_score, %s) WHERE user_id = %s", (questions_correct, amount_won, user_id))
    connect.commit()
    
    return amount_won

def show_leaderboard():
    cursor.execute("SELECT username, best_score FROM users ORDER BY best_score DESC LIMIT 5")
    top_players = cursor.fetchall()

    print("\n=== TOP 5 PLAYERS ===")
    for i, row in enumerate(top_players, 1):
        print(i, ".", row[0], "- ₹", row[1])

def main():

#menu driven function with choices to select
    
    while True:
        print("\n=== TRIVIA GAME ===")
        print("1. Play")
        print("2. View Leaderboard")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            user_id = new_player()
            winnings = play_game(user_id)
            print("Game finished. You won: ₹", winnings)
        elif choice == "2":
            show_leaderboard()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, try again.")

    connect.close()

main()
