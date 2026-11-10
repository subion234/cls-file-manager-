def add_task(data):
  print('to stop adding task pls type done')
  while True:
    t = input('pls add task you want to do: ')
    try:      
      if not t.strip():
        raise ValueError()
      if t.lower() == 'done':
         break
      data.append(t)
    except:
      print('A task can not be empty')
  return data

def view_task(data):
  if len(data) != 0:
    print('These are the tasks you added:')
    for index, tasks in enumerate(data, start=1):
      print(index, tasks)
  else:
    print('You didn\'t added any task')

def edit_task(data):
  if len(data) != 0:
    indlis = [ind for ind, item in enumerate(data)]
    datalis = [item for ind, item in enumerate(data)]
    view_task(data)
    while True:
       choice = input('Pls enter the task you want to edit and done to stop edditing: ')
       if choice == 'done':
         break
       try:
         n = int(choice) -1
         if not choice.strip() or n not in indlis:
           raise ValueError()
         data[n] = input('pls eddit your task: ')  
         if not data[n].strip():
           print(f'You didn\'t eddited your task\n the task will remain same {data[n]}')
           data[n] = datalis[n]
         print(f'Your eddited task is {data[n]}')
       except:
          print('You didn\'t enter any task no. to be edited')
  else:
     print('There is no tasks to eddit')

def  remove_task(data):
  if len(data) != 0:
    indlis = [ind for ind, item in enumerate(data)]
    datalis = [item for ind, item in enumerate(data)]
    view_task(data)
    while True:
       choice = input('Pls enter the task you want to remove, clear to erase every task and done to stop removing: ')
       if choice == 'done':
         break
       if choice == 'clear':
         data.clear()
         break
         print('Your evert tasks are cleared')
       try:
         n = int(choice) -1
         if not choice.strip() or n not in indlis:
           raise ValueError()
         del data[n]
         print('your intended task is deleted')
       except:
          print('You didn\'t enter any task no. to be removed')
  else:
     print('There is no tasks to remove')
    
def main():
  print('Welcome to task manager\n')
  print('starting your personalised manager\nYour manager is ready to start working.')
  print('Pls enter correct choices to aviod errors\n')
  print('1. for Adding task.\n2. for Viewing task.\n3. for Edditing the tasks.\n4. for removing tasks.\n5. for stopping.')
  task = []
  while True:
   choice = input('Choose an option: ')
   match choice:
     case '1':
       task = add_task(task)
     case '2':
       view_task(task)
     case '3':
       edit_task(task)
     case '4':
       remove_task(task)
     case '5':
       print('Exiting from task manager.\nThank you for working with us.')
       break
     case _:
       print('pls choose appropiate choice')
  
if __name__ == '__main__':
  main()