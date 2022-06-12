# Practical examination

Solve the provided problem, using object oriented programming, C++ and Qt.

The application must use layered architecture in order for functionalities to be graded.

Do not forget to add the required tests and specifications.

Using existing code is forbidden, you must start your application from scratch.

For function documentation you may use:
- http://doc.qt.io/qt-6/
- https://en.cppreference.com/w/
- https://www.cplusplus.com/


---

# Quiz

Write an application which simulates a quiz, as follows:
1. The information about the questions is in a text file. Each **Question** has **an id**(int), **a text**(string), the **corect answer**(string) and **a score**(int). There are read when the application starts and are also stored in the file by the program.
2. Another file contains information aboout the participants. Each **Participant** has **a name**(string) and **a score**(int). This file is manually created and it is read when the application starts. The initial score is 0 for each participant.
3. When the application is launched, a new window is created for the presenter (with the title "Presenter") and also one for each participant, having as title the participant's name. **(0.5p)**
4. TThe window of the presenter will show all the questions, with their id, text, correct abswer and assoctiated score, sorted by id.**(0.75p)**
5. The windows of the participants will show all the questions, with their id, text and associated score, sorted descending by score.**(0.75p)**
6. Only the presenter can add questions, by inputting the question's id, text, correct answer and associated score by pressing a button "Add" **(1p)**. This operation fails if the text is empty or if there is another question with the same id. The user will be informed if the operation fails.**(0.5p)**
7. The participants can answer questions, by selecting the question, inputting the answer in a text edit and pressing a button "Answer":
    a. A participant cannot answer the same questions twice. When a question is answered, it will have a green background in the participant's list **(0.75p)** and when clicking it , the "Answer" button will be disabled **(0.75p)**.
    b. The score of each participant is shown in his/her window. When a question was answered correctly, the score of the participant increases by the score of the question that was answered. **(1p)**
8. When a modification is made by the presenter, all the participants will automatically see the modified list of questions. Use the Observer dessign pattern. **(2p)**
9. When the application is finished, the questions and participants files will be updated. **(1p)**

**Observations**
1. **1p - of**
2. The application must use layered architecture in order for functionalities to be graded.
3. If you do not read the data from file, you will receive 50% of functionalities 4, 5, 6 and 7.

You are allowed to use Qt Designer.