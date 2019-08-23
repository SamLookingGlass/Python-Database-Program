# Importing time library to use timestamp feature
import time
# Importing pickle to read and write dictionary into .txt files
import pickle

# Timestamp function
def timestamp():
  now = int(round(time.time()*1000))
  time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now/1000))
  return time_now

"""
Sample Structure of Dictionary (Database) Used

history_txt = {
  "test":{
    "number_of_sentence" : 3,
    "number_of_revisions" : 2,
    "last_revised_on" : 'None',
    "word" : "test",
    "sentence" : [
      "This is a test.", 
      "This is a test2.", 
      "This is a test3."
     ] 
    },
  "happy":{
   "number_of_sentence" : 2,
    "number_of_revisions" : 0,
    "last_revised_on" : 'None',
    "word" : "happy",
    "sentence" : [
      "This is a test.", 
      "This is a test2."
     ] 
    },    
  }
"""

# Read data from file
with open('history.txt','rb+') as handle:
  history_txt = pickle.loads(handle.read())
  handle.close()

# Function to add new words/sentence(s) (Completed)
def add_function():
  while True:
    # Prompts user to input word they wish to add.
    word_input = (input("What word do you wish to add: ")).lower()
    # Check if user input is alphanumeric.
    if not word_input.isalpha():
      print("Invalid input entered. No special characters and numbers allowed.")
    else:
      while True:
        # If word exists, existing sentences are displayed.
        if word_input in history_txt.keys():
          word_selected = history_txt[word_input]
          print(f"Entry for word - '{word_input}' exists. \nHere is your existing entry:")    
          index = 0
          print('-------------------------------------------------------\n','{:<15}  {:<35}'.format('Index', 'Sentence(s)'),'\n-------------------------------------------------------')
          for  i in range(len(word_selected["sentence"])):
            index += 1
            line = '{} {:<15}  {:<35}'.format('',index, word_selected["sentence"][i])
            print(line)
            i += 1         
          print('-------------------------------------------------------')  
          while True:
              # Prompts user if they would like to add another sentence.   
              user_decision = (input("Do you want to add another sentence (y/n)? ")).lower()
              if user_decision == "y":
                word_selected['number_of_sentence'] += 1
                word_selected['number_of_revisions'] += 1
                word_selected['last_revised_on'] = timestamp()
                while True:
                  sentence_input = input("Please enter your sentence: ")
                  if sentence_input.isnumeric() or sentence_input.isspace():
                    print("Invalid input entered. No spaces or numeric values allowed.")
                  else:
                    word_selected["sentence"].append(sentence_input)
                    index = 0
                    print('Sentence has been added successfully:\n','-------------------------------------------------------\n','{:<15}  {:<35}'.format('Index', 'Sentence(s)'),'\n-------------------------------------------------------')
                    for  i in range(len(word_selected["sentence"])):
                      index += 1
                      line = '{} {:<15}  {:<35}'.format('',index, word_selected["sentence"][i])
                      print(line)
                      i += 1         
                    print("-------------------------------------------------------\nReturning to Menu.")
                    return
              elif user_decision == "n":
                print("No new sentence was added.")
                print("-------------------------------------------------------\nReturning to Menu.")
                return
              else:
                print("Please choose a valid option.")
        #  If word does not exist, prompts user if they want to add new word. Then prompts user for an example sentence to be given.
        else:  
          print(f"Entry for word - '{word_input}' does not exists.")
          while True:
            user_decision = (input(f"Would you like to add '{word_input}' (y/n)? ")).lower()
            if user_decision == "y":
              while True:
                sentence_input = (input(f"Please enter a sentence that uses '{word_input}': ")).lower()
                if sentence_input.isnumeric() or sentence_input.isspace():
                  print("Invalid input entered. No blanks or numeric values allowed.")
                else:
                  entry = {
                    "number_of_sentence" : 1,
                    "number_of_revisions" : 0,
                    "last_revised_on" : timestamp(),
                    "word" : f"{word_input}",
                    "sentence" : [sentence_input],
                  }
                  history_txt[word_input] = entry
                  print('Entry has been added successfully:\n','-------------------------------------------------------\n','{:<15}  {:<15}  {:<15}'.format('Entry', 'No. of Revisions', 'Last Revised On'),'\n-------------------------------------------------------')
                  for i in history_txt.keys():
                    a = history_txt[i]['number_of_revisions']
                    b = history_txt[i]['last_revised_on'] 
                    line = '{} {:<15}  {:<16}  {:<20}'.format('',i, a, b)
                    print(line)
                  print("-------------------------------------------------------\nReturning to Menu.")
                  return
            elif user_decision == "n":
              print("No new entry was added.")
              print("-------------------------------------------------------\nReturning to Menu.")
              return
            else:
              print("Please choose a valid option.")

# Function to edit existing words (Completed)
def edit_function():
  while True:
    print("Here are your entries:")
    print('-------------------------------------------------------\n','{:<15}  {:<15}  {:<15}'.format('Entry', 'No. of Revisions', 'Last Revised On'),'\n-------------------------------------------------------')
    for i in history_txt.keys():
      a = history_txt[i]['number_of_revisions']
      b = history_txt[i]['last_revised_on'] 
      line = '{} {:<15}  {:<16}  {:<20}'.format('',i, a, b)
      print(line)
    print('-------------------------------------------------------')  
    # Prompts user to input word they would like to edit.
    word_input = input("Enter the word you would like to edit: ")
    # If word exists, prompts user whether they want to edit the sentence.
    if word_input in history_txt.keys():
      no_of_sentence = history_txt[f"{word_input}"]["number_of_sentence"]
      word_selected = history_txt[f"{word_input}"]
      choice = (input(f"There are {no_of_sentence} of sentence(s) for '{word_input}'. \nDo you want to edit your sentence(s) (y/n)? ")).lower()
      while True:
        # If user choose yes, prompts user to select sentence to edit.
        if choice == "y":
          index = 0
          print('-------------------------------------------------------\n','{:<15}  {:<35}'.format('Index', 'Sentence(s)'),'\n-------------------------------------------------------')
          for  i in range(len(word_selected["sentence"])):
            index += 1
            line = '{} {:<15}  {:<35}'.format('',index, word_selected["sentence"][i])
            print(line)
            i += 1         
          print('-------------------------------------------------------')  
          while True:
            choice = int(input("Enter the index you would like to edit? "))
            if not 0 < choice < (len(word_selected["sentence"]) + 1):
              print("The index does not exist. Please enter a valid number.")
            else:
                sentence_input = input("Enter your sentence: ")
                if sentence_input.isnumeric() or sentence_input.isspace():
                  print("Invalid input entered. No spaces or numeric values allowed.")
                else:
                  word_selected["sentence"][choice - 1] = sentence_input
                  word_selected['number_of_revisions'] += 1
                  word_selected['last_revised_on'] = timestamp()
                  print("Sentence successfully edited:\n",'-------------------------------------------------------\n','{:<15}  {:<35}'.format('Index', 'Sentence(s)'),'\n-------------------------------------------------------')
                  index = 0
                  for  i in range(len(word_selected["sentence"])):
                    index += 1
                    line = '{} {:<15}  {:<35}'.format('',index, word_selected["sentence"][i])
                    print(line)
                    i += 1         
                  print("-------------------------------------------------------\nReturning to Menu.") 
                  return 
        # If user choose no, no sentence is edited. 
        elif choice == "n":
          print("No entries were edited.")
          print("-------------------------------------------------------\nReturning to Menu.") 
          return
        # If user gives random input, program prompts for y or n. 
        else:
          choice = (input("invalid option. Please enter 'y' or 'n': ")).lower()   
    else:  
      print(f"The entry for '{word_input}' does not exists. Please enter an existing entry.")

# Function to delete word or sentence. (Completed)
def delete_function():
  while True:
      print("Here are your entries:")
      print('-------------------------------------------------------\n','{:<15}  {:<15}  {:<15}'.format('Entry', 'No. of Revisions', 'Last Revised On'),'\n-------------------------------------------------------')
      for i in history_txt.keys():
        a = history_txt[i]['number_of_revisions']
        b = history_txt[i]['last_revised_on'] 
        line = '{} {:<15}  {:<16}  {:<20}'.format('',i, a, b)
        print(line)
      print('-------------------------------------------------------')  
      # Prompts user to input word they would like to delete a word entry.
      choice = (input("Do you want to delete a word entry (y/n)? ")).lower()
      while True:
        if choice == "y":
          while True:
            try:
              word_input = (input("Enter word you would like to delete: ")).lower()
              word_selected = history_txt[word_input]
              history_txt.pop(word_input)
              print('Entry deleted successfully. Here is your updated notebook\n','-------------------------------------------------------\n','{:<15}  {:<15}  {:<15}'.format('Entry', 'No. of Revisions', 'Last Revised On'),'\n-------------------------------------------------------')
              for i in history_txt.keys():
                a = history_txt[i]['number_of_revisions']
                b = history_txt[i]['last_revised_on'] 
                line = '{} {:<15}  {:<16}  {:<20}'.format('',i, a, b)
                print(line)
              print('-------------------------------------------------------\n','Returning to Menu.')
              return  
            except KeyError:
              print("Entry does not exist. Enter another word.") 
        elif choice == "n":
          choice_2 = (input("Do you want to delete a sentence in the entry (y/n)? ")).lower()
          while True:
            if choice_2 == "y":
              word_input = (input("Enter the entry name: ")).lower()
              try:
                word_selected = history_txt[word_input]
                while True:
                  if word_input in history_txt.keys():
                    print('-------------------------------------------------------\n','{:<15}  {:<35}'.format('Index', 'Sentence(s)'),'\n-------------------------------------------------------')
                    index = 0
                    for  i in range(len(word_selected["sentence"])):
                      index += 1
                      line = '{} {:<15}  {:<35}'.format('',index, word_selected["sentence"][i])
                      print(line)
                      i += 1
                    print('-------------------------------------------------------')  
                    choice_3 = int(input("Enter index of sentence you would like to delete: "))
                    while True:
                      if not 0 < choice_3 < (len(word_selected["sentence"]) + 1):
                        print("The index does not exist. Please enter a valid number.")
                      else:
                        (word_selected["sentence"]).remove(word_selected["sentence"][choice_3 - 1])
                        word_selected['number_of_revisions'] += 1
                        word_selected['number_of_sentence'] -= 1
                        word_selected['last_revised_on'] = timestamp()
                        print('Sentence successfully deleted:\n','-------------------------------------------------------\n','{:<15}  {:<35}'.format('Index', 'Sentence(s)'),'\n-------------------------------------------------------')
                        index = 0
                        for  i in range(len(word_selected["sentence"])):
                          index += 1
                          line = '{} {:<15}  {:<35}'.format('',index, word_selected["sentence"][i])
                          print(line)
                          i += 1
                        print('-------------------------------------------------------\n','Returning to Menu.')  
                        return         
              except KeyError:
                print(f"Entry '{word_input}' was not found. Enter a valid entry name.")
            elif choice_2 == "n":
              print('No deletions made.\n','-------------------------------------------------------\n','Returning to Menu.')
              return
            else:
              choice_2 = (input("invalid option. Please enter 'y' or 'n': ")).lower()   
        else:
          choice = (input("invalid option. Please enter 'y' or 'n': ")).lower()
          
# Function to display all word entries. (Complete)
def browse_function():  
  # Shows all the entries in the journal
  print('-------------------------------------------------------\n','{:<15}  {:<15}  {:<15}'.format('Entry', 'No. of Revisions', 'Last Revised On'),'\n-------------------------------------------------------')
  for i in history_txt.keys():
    a = history_txt[i]['number_of_revisions']
    b = history_txt[i]['last_revised_on'] 
    line = '{} {:<15}  {:<16}  {:<20}'.format('',i, a, b)
    print(line)
  print('-------------------------------------------------------')
  while True:
    word_input = (input("Enter entry you wish to browse: ")).lower()
    if word_input in history_txt.keys():
      word_selected = history_txt[word_input]
      print('Here is your entry:\n','-------------------------------------------------------\n','{:<15}  {:<35}'.format('Index', 'Sentence(s)'),'\n-------------------------------------------------------')
      index = 0
      for  i in range(len(word_selected["sentence"])):
        index += 1
        line = '{} {:<15}  {:<35}'.format('',index, word_selected["sentence"][i])          
        print(line)
        i += 1  
      print('-------------------------------------------------------\n','Returning to Menu.')  
      return
    else:    
      print(f"Entry for word - '{word_input}' does not exists. Enter a valid word.")

# Function to save data to history.txt file
def save():
  with open('history.txt','wb+') as handle:
    pickle.dump(history_txt,handle)
    handle.close() 
  return

while True:
  # Option Menu
  print("------------------------------------------------------- \n<Welcome to Revision Notebook>\n-------------------------------------------------------  \nOptions Menu:\n1. Add new word entry OR sentence(s) to existing entry\n2. Edit sentence(s) in existing entry\n3. Delete word entry OR sentence(s) in existing entry\n4. Browse notebook\n5. Save and Exit Notebook\n------------------------------------------------------- ")
  # User Choice for programme to execute certain tasks
  try:
    user_choice = int(input("What do you want to do? (Key in 1, 2, 3, 4 or 5): "))
    if not 0 < user_choice  < 6:
      print("That was not valid. Please enter a valid option.")
    else:
      print(f"You have selected option {user_choice}.")
      if user_choice == 1:
        add_function()
      if user_choice == 2:
        edit_function()
      if user_choice == 3:
        delete_function()  
      if user_choice == 4:
        browse_function()
      # Saves user's changes to history.txt and exits program. 
      if user_choice == 5:          
        print("Notebook saved to history.txt. \nProgram shutting down.")
        save()
        break 
  except ValueError:
    print("That was not valid. Please enter a valid option or restart program.")
  # except:
  #   print("Unexpected error. Please restart program.")
