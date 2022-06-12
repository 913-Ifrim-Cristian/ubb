# Lab Test 2

Solve the provided problem, using object oriented programming and C++.

Input at least 3 entities in your initial list (from the source code).

In order for functionalities to be graded the application must use layered architecture, as shown in the given UML diagram (a UI layer will also be necessary).

Using existing code is forbidden, you must start your application from scratch.

For function documentation you may use:
- https://en.cppreference.com/w/
- https://www.cplusplus.com/

Time: 70 minutes.

---

# Real Estate Agency

A real estate agency needs an application to deal with its clients and with the dwellings it manages. Each dwelling is characterized by a *price* and whether it *is profitable* or not.

Each client of the agency is characterized by *a name* and *an income*. The agency keeps track of two types of clients: persons and companies. Besides the two characteristics of ac client, a company also has *money* from *investments*. The total income for each type of client is computed in the following way:
- Person: the total income is the income
- Company: the total income is the income, to which the money from investments is added.

The agency needs to know which clients are interested in which dwellings:
- A person is interested in a dwelliSng if the price of the dwelling / 1000 <= the client's total income.
- A company is interested in a dwelling if the price of the dwelling / 10 is <= to the client's total income and if the dwelling is profitable.

The application should allow the foloowing functionalities:
1. Update a client's income. The name of the client and the new income are given. **(2p)**
2. Show all clients, with all their information **(1p)** and all dwellings **(0.5p)**.
3. Add a dwelling. Input the price and if it is profitable or not. **(1p)** Immediately after the dwelling is added, the aplication should display all clients that are interested in the added dwelling. **(2p)** *The score for this functionality is given only if you use inheritance and polymorphism, as show in the UML diagram below*.
4. Save all clients to a file. For each client, write the correct data to the file: name, income, money from investments(in the case of companies) and total income. **(2.5p)** *The score for this functionality is given only if you use inheritance and polymorphism, as shown in the UML diagram below.*

From the source code, add in your application at least: 2 persons, 2 companies and 1 dwelling.

In order for functionalities to be graded the application must use layered architecture, as shown in the diagram(a UI layer will also be necessary).

**1p - of**


![UML Diagram](https://i.postimg.cc/G3xymXSc/Real-Estate-Agency.png)


**Obs. You can add new attributes or operations besides the ones on the diagram, if needed. Allotted time: 70 minutes.**
