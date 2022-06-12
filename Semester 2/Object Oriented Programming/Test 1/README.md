# Lab Test 1

Solve the provided problem, using object oriented programming and C++.

Input at least 5 entities in your repository.

The application must use layered architecture in order for functionalities to be graded.

Do not forget to add the required tests and specifications.

Using existing code is forbidden, you must start your application from scratch. The only exception is the source code for the dynamic vector, in case you decide to use your vector and not the one from STL.

For function documentation you may use:
- https://en.cppreference.com/w/
- https://www.cplusplus.com/

Time: 60 minutes.

---

# Bills, bills, bills

Emily needs to manage her list of ever-growing bills. Each **Bill** has a serial number, a company, a due date, a sum and an isPaid fild that illustrates wheter the bill was paid. See below a few examples:

0A33455X; Digi Sport; 15.04.2016; 75.00; false
EED36677; E-On; 16.03.2016; 122.00; true
X990TTRR; Orange; 18.04.2016; 46.00; false
1234RR55; Vodafone; 20.04.2016; 23.00; false
TRE3EERR; Tcomm; 21.04.2016; 10.00; true

Write a bill manager application with a console based user interface which allows to:
1. Remove a bill. A message wil be shown if the bill was succesffully removed (**1.5p**). If there are no bills with the given serial number, show an adequate message (**1.5p**).
2. Show all the bills, with all their information (**1p**).
3. Sort all unpaid bills by their dute date (**2p**).
4. Calculate the total of unpaid bills(**1p**).

*Hint: functions std::string::find and std::string::substr*

Input at least 5 bills to your initial list of bills(from the source code).

Write specifications and white-box tests for the following functions:
- Functions to remove a bill(the repository/service function). (**0.5** - specification, **0.5** - test)
- Function which calculates the total of unpaid bills. (**0.5** - specification, **0.5** - test)

**The application must use layered architecture in order for functionalities to be graded.**

**1p - of.**

**Time: 60 minutes**