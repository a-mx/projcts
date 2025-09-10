tasks = []
while True:
    choice=int(input('------------------\n1: Show your tasks\n2: Add a new task\n3: Remove a task\n4: Mark as DONE\n0: Exit\n------------------\n>>>: '))
    if choice==1:
        if not tasks:
            print('No tasks yet.')
        else:
            for i in range(len(tasks)):
                print(f'{i+1}: {tasks[i]}')
    elif choice==2:
        new_task=input('Insert a task you want to add: ')
        tasks.append(new_task)
        print(f'New task added: {new_task}')
    elif choice==3:
        if not tasks:
            print('No tasks to remove.')
        else:
            for i in range(len(tasks)):
                print(f'{i+1}: {tasks[i]}')
            remove=int(input('Which task do you want to remove? '))
            if 1 <= remove <= len(tasks):
                if 1 <= remove <= len(tasks):
                    tasks.pop(remove-1)
                    print(f'Task removed')
                else:
                    print('Invalid number.')
            else:
             print('Please enter a valid number.')
    elif choice==4:
        if not tasks:
            print('No tasks yet.')
        else:
            for i in range(len(tasks)):
                print(f'{i+1}: {tasks[i]}')
            try:
                done=int(input('Which task do you want to mark as done?\n>>>: '))
                if 1 <= done <= len(tasks):
                    tasks[done-1]=f"[{tasks[done-1]}] DONE"
                    print(f'Task done')
                else:
                    print('Invalid number.')
            except:
                print('Please enter a valid number.')
    elif choice==0:
        print('Goodbye!')
        break
    else:
        print('Invalid choice.')