import json
import ast

#Creating the Json file
jsonfile = open('questions.json', 'w')
json.dump(questions_db,jsonfile)
jsonfile.close()

#Reading the Json file to check if the questions are properly loaded
questions_json = open('questions.json', 'r')
new_db = json.load(questions_json)
questions_json.close()

for keys in new_db:
  print(keys)
  
#Selecting a question to delete or edit function
def select_question(questions_db):
  select_ans = input(f'Select a question?Y/N \n').upper()
  while select_ans == 'Y':
    i = 0
    for i in range(len(questions_db)):
      num = i + 1
      questions_list = questions_db[i]['Question']
      print(f'{num}: {questions_list}')
      i = i + 1
      try:
        j = int(input(f'Choose the question\'s number that you want: \n '))
        k = j - 1
        if k > -1:
          return (k)
        else:
          print(f'No Question in that number.')
      except:
        print(f'Sorry, no question in that number')
    select_ans = input(f'Select a question?Y/N \n').upper()
  game_on(questions_db)

#Delete a Question Function
def delete_questions(questions_db):
  delete_ans = input(f'Delete a question?Y/N \n').upper()
  while delete_ans == 'Y':
    id_num = select_question(question_db)
    del (questions_db[id_num])
    print(f'Question has been deleted')
  game_on(questions_db)

#Edit Function
def edit_questions(questions_db):
  edit_ans = input(f'Edit a question?Y/N \n').upper()
  while edit_ans == 'Y':
    id_num = select_question(questions_db)
    edit_choices = int(input(f'Choose number to edit \n\t1.Question \n\t2.Choice A \n\t3.Choice B \n\t4.Choice C \n\t5.Answer\n'))
    if edit_choices == 1:
      new_question = input(f'Enter new question here: \n')
      print(new_question)
      questions_db[id_num]['Questions'] = new_question
      edit_ans = input(f'Edit a question?Y/N \n').upper()
    elif edit_choices == 2:
      new_A = input(f'Enter new choice A here: \n')
      print(new_A)
      questions_db[id_num]['A'] = new_A
      edit_ans = input(f'Edit a question?Y/N \n').upper()
    elif edit_choices == 3:
      new_B = input(f'Enter new choice A here: \n')
      print(new_B)
      questions_db[id_num]['B'] = new_B
      edit_ans = input(f'Edit a question?Y/N \n').upper()
    elif edit_choices == 4:
      new_C = input(f'Enter new choice C here: \n')
      print(new_C)
      questions_db[id_num]['C'] = new_C
      edit_ans = input(f'Edit a question?Y/N \n').upper()
    elif edit_choices == 5:
      new_ans = input(f'Enter new Answer here: \n').upper()
      print(new_ans)
      questions_db[id_num]['Answer'] = new_ans
      edit_ans = input(f'Edit a question?Y/N \n').upper()
    else:
      edit_ans = input(f'Edit a question?Y/N \n').upper()
  game_on(questions_db)

#Adding a new question function
def add_questions(questions_db):
  add_question = input(f'Add another question?Y/N\n').upper()
  while add_question == 'Y':
    question_sample = input(f'Enter Question:')
    choice_a = input(f'Enter A:')
    choice_b = input(f'Enter B:')
    choice_c = input(f'Enter C:')
    answer = input(f'Answer: \n').upper()
    questions_list = f'{{\'Question\': \'{question_sample}\',\'A\': \'{choice_a}\',\'B\': \'{choice_b}\',\'C\': \'{choice_c}\',\'Answer\': \'{answer}\'}}'
    question_dict = eval(questions_list)
    questions_db.append(question_dict)
    add_question = input(f'Add another question?Y/N \n').upper()
  game_on(questions_db)

#Function to list all the questions from the Json file
def list_questions(questions):
  user_answers = []
  i = 0
  for i in range(len(questions)):
    num = i + 1
    question_list = questions[i]['Question']
    print(f'{num}: {question_list}')
    A = questions[i]['A']
    B = questions[i]['B']
    C = questions[i]['C']
    print(f'\tA.{A} \n\tB.{B} \n\tC.{C}')
    answer = (input("Enter answer: ")).upper()
    print(f'Your answer is: {answer} \n')
    user_answers.append(answer)
    i = i + 1
  return (user_answers)

#Function the determines if the user passed or fail the game
def pass_fail(score):
  if score >= 70:
    print(f'Your score is {int(score)}% .You Passed! \n')
  else:
    print(f'Your score is {int(score)}% . We will be deducting 10 points from your house. \n')

#Function that computes the scores of the user from the quiz
def compute_score(user_answers, answers):
  correct = 0
  wrong = 0
  i = 0
  for i in range(len(user_answers)):
    if user_answers[i] == answers[i]["Answer"].upper():
      correct = correct + 1
    else:
      wrong = wrong + 1

  score = ((correct)/(correct + wrong )) * 100
  return (score)

#Function that starts the entire 
def start_question(quiz_data):
  user_answer = list_questions(quiz_data)
  score = compute_score(user_answer, quiz_data)
  pass_fail(score)
  return (score)

#Function that gets the player name
def get_playerName():
  player_name = input(f'Enter your name:' ).upper()
  print(f'Hi {player_name}! \n')
  return (player_name)

#Function that prints the player scores after the having several retaking of the quiz.
#The score resets when the game is ended.
def list_playerScore(player,scores):
  num = len(player)
  i = num - 5
  for i in range(num):
    player_name = player[i]
    player_score = int(scores[i])
    print(f'{player_name} score: {player_score}%')
  print('\n')

#Function that starts the quiz.
def start_quiz(quiz_data):
  list_player = []
  list_score = []
  start_answer = input(f'\nDo you wanna play?Y/N: \n').upper()
  while start_answer == 'Y':
    name = get_playerName()
    list_player.append(name)
    score = start_question(quiz_data)
    list_score.append(score)
    print('*'*40)
    start_answer = input(f'Do you wanna play a new Game?Y/N: \n').upper()
  print(f'\nThank you for playing')
  list_playerScore(list_player, list_score)
  print('*'*40)
  game_on(quiz_data)
  
  #Function that starts the entire game. You can play quiz or edit/add questions to the quiz.
def game_on(quiz_data):
  player_answer = input(f'Choose what you want to do: \n\t1:Play Game \n\t2.Add Questions \n\t3.Edit a Question \n\t4.Delete Questions \n\t5.Exit \n')
  if player_answer == '1':
    start_quiz(quiz_data)
  elif player_answer == '2':
    add_questions(quiz_data)
  elif player_answer == '3':
    edit_questions(quiz_data)
  elif player_answer == '4':
    delete_questions(quiz_data)
  else:
    print('Thank you for stopping by')
    
    
game_on(new_db)
