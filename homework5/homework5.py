# File: homework5.py

# --- 3 Homework 1+2 Review ---

# --- 3.1 Vocabulary Review

# 1. GitHub is an online cloud of repositories where you can store your local repositories and borrow others' code. Git allows you to manage code between your repositories.
# 2. The command line tells the terminal what to do. The terminal communicates to the computer to execute the command. 
# 3. A local repository is a repository on your computer. A remote repository is stored on a cloud like GitHub.
# 4. Version control is how you track changes to folders and files and collaborate on repositories. Git and Github are the primary method for version control.
# 5. Staging area is where changes to folders and files are set before they are committed.
# 6. git add adds files and folders to the staging area.
# 7. git commit commits the changes to the local repository.
# 8. git push pushes the changes to the remote repository.
# 9. git status returns the status of your remote repository relative to the local repository.
# 10. git pull brings changes to a remote repository to the local repository.
# 11. pwd prints the current directory.
# 12. ls lists the directories and files in the current directory.
# 13. cd changes the directory you're in.
# 14. nano edits a txt or py file from the terminal.
# 15. touch creates a new file.
# 16. mv moves a file or directory to a new location.
# 17. rm removes a file or directory.
# 18. cat prints out the contents of a file.

# ---3.2 A Directory Tree ---
# 
# 1. pwd
# 2. ls -a
# 3. cd, git pull
# 4. mv -r homework.py ~/python_decal/judy_decal/homework/
# 5. cd .. then cd judy_decal then cd homework
# 6. cat homework.py
# 7. git add, git commit, git push
# 8. Judy tried to push changes but her local repository wasn't up to date with the remote repository before she did so. She needs to pull the changes from the remote repository before committing her local changes.
# 9. (cd) ~/Recents

# --- 4 Homework 3 Review ---

#  --- 4.1 Data Types ---

def checkDataType(entry):
    print(type(entry))

# checkDataType(3.14)
# checkDataType(True)

def even0r0dd(numero):
    if numero%2 == 0:
        return "Even"
    else:
        return "Odd"

# print(even0r0dd(7))
# print(even0r0dd(10))

# --- 5 Loops ---

def sumWithLoop(list):
    total = 0
    for i in list:
        total += i
    return total

# numbers = [1,2,3,4,5]
# print(sumWithLoop(numbers))

# --- 6 Homework 4 ---

# --- 6.1 Lists ---

def duplicateList(lst):
    n = len(lst)
    counter = 0
    while counter < n:
        lst.append(lst[counter])
        counter += 1
    return lst

# print(duplicateList(['a','b','c']))

def square(num): # added the colon
    return num*num

# print(square(4))

print(f"The number 5 is {even0r0dd(5)}")