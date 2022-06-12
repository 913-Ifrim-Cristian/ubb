# Lab Test 3

Solve the provided problem, using object oriented programming, C++ and Qt (for the GUI). No score is awarded for a console-based user interface.

The application must use layered architecture in order for functionalities to be graded.

In case reading from a file is required: if the data are not read from the file, 0.5 points are subtracted from the indicated score for each functionality.

Using existing code is forbidden, you must start your application from scratch.

You may use Qt Designer, as well as the following sites for documentation:
- http://doc.qt.io/qt-6/ 
- http://en.cppreference.com/w/ 
- http://www.cplusplus.com/ 

Time: 60 minutes.

---

# Weather

Write an application allowing you to see the weather for the current day. Each Time Interval is represented by *its hours (start and end), temperature, precipitation probability and a short description*(e.g. "sunny", "rainy", "cloudy"). Create a file that contains at leat 5 time intervals. The application will read data from the file. See below a few examples.

6;9;10;13;foggy

9;12;13;7;cloudy

12;14;18;23;sunny

14;18;20;52;sunny

18;21;20;68;rainy

Write a weather application using C++ with a **graphical user interface(use the Qt framework)* which allows to:
1. Visualize all time intervals in a list (QListWidget or QListView). The list will display the time interval, the temperature, the precipitation probability and the description. When the application starts, the list is populated automatically **(2.5p)** and the time intervals are sorted in ascending order **(1p)**.
2. Filter the list according to precipitation probability. The list will present the time intervals where the precipitation probability is less than a given value. Input the value in a QLineEdit. **(2p)**
3. Compute the total number of hours, for a given description and start time(e.g. "sunny" - how many hours of sunny weather will there be today after 14 o'clock?). Input the description and start time in QLineEdits and when the button "Compute total" is clicked, show the total number of hours for that description after the given start time (in a QLineEdit, a QLabel or in a new widget)**(2.5p)**. Show an error message if there are no such intervals **(1p)**.

- **If the data are not read from the file, 0.5 points are substracted from the indicated score for each functionality.**
- **The application must use layered architecture in order for functionalities to be graded.**
- **No score is awarded for a console-based interface.**

**1p - of**
