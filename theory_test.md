# CFG Foundation Assessment 2 
## Section 1: Theory Questions [31 marks] 
**1.1 What does SDLC stand for?**  
Software Development Life Cycle


**1.2 What exception is thrown when you divide a number by 0?**
In python, the program will throw a ZeroDivisionError. In JavaScript, Returns Infinity, does not actually throw an exception.

**1.3 What is the git command that moves code from the local repository to the remote repository?** 
git push 

**1.4 What does NULL represent in a database?** 
In a database, NULL represents the absence of a value or the fact that a value is unknown. It's not equivalent to zero or an empty string.


**1.5 Name 2 responsibilities of the Scrum Master**
1. Facilitating Scrum ceremonies: The Scrum Master is responsible for orchestrating Scrum meetings, ensuring they are productive and efficient. 
2. Removing obstacles: The Scrum Master finds and removes impediments that are blocking the team's progress to help the team work smoothly and stay focused on their tasks.

**1.6 Name 2 debugging methods, and when you would use them.** 
1. Breakpoint Debugging: To set stops in your code to inspect it while running. Use when you know where the issue might be.
2. Log Debugging: To add print statements to track values and flow. Use for overall behaviour or in complex systems where stops aren't practical.

**1.7 Looking at the following code, describe a case where this function would throw an error when called. Describe this case and talk about what exception handling you’ll need.** 
```python
def can_pay(price, cash_given):
    if cash_given >= price:
        return True
   else:
 return False
```

The function **can_pay(price, cash_given)** expects two arguments that are numeric. It will throw a TypeError if any non-numeric argument is passed. 
For example, calling **can_pay('a hundred', 50)** would throw a TypeError as **'a hundred '** is a string.

To handle this, we could implement exception handling with a try-except block to catch TypeErrors. The code would be:
```python
def can_pay(price, cash_given): 
    try: 
        if cash_given >= price: 
            return True 
        else: 
            return False 
    except TypeError: 
        return "Both price and cash_given need to be numbers."
```


**1.8 What is git branching? Explain how it is used in Git.**
Git branching is a feature that allows developers to create independent lines of development within a single project. It's used to isolate work in progress from the stable codebase. Developers create branches to add new features, fix bugs, or experiment, without affecting the main branch.
To use it, you can create a new branch using the git branch command followed by the name of the new branch. For example, git branch developer.
After the changes on a new branch have been tested and are ready to be integrated, they are usually merged back into the main branch through a process called a pull request or directly using the git merge command.

**1.9 Design a restaurant ordering system.** 
**You do not need to write code, but describe a high-level approach:** 
**1.	Draw a list of key requirements**
**2.	What are your main considerations and problems?**
**3.	What components or tools would you potentially use?**

1. The list of key requirements
- User Account: Customers can create accounts, to save their preferences, and to view their order history.
- Ordering: Customers can view the menu, select items, and place orders.
- Menu Management: Managers can add, update, or remove items from the menu.
- Order Tracking: Both restaurant staff and customers can track order status. For example, pending, preparing or ready.
- Food Allergy: Ability for customers to add special requests or customize their order, such as adding allergy or preparation instructions.
- Notifications: The system should be able to push notifications to give real-time updates for customers regarding their order status.

2. Main Considerations and Problems:
- The number of potential users: The system should be able to handle a growing number of orders and users.
- Feature design: The interface should be user-friendly for both customers and staff.
- Data security: Users data and payment information need to be protected. 
- Ease of maintenance: The system should be simple to update and debug.

3. Components and Tools
- Frontend development: A web-based user interface for customers to place orders, and a separate interface for staff. These could be built using JavaScript, HTML and CSS.
- Backend development: A server-side application to process orders, handle payments, and manage users and menu items. This could be built with Python, and a framework like Flask.
- Database: A database to store order information, user profiles, and menu items. SQL databases like MySQL could be used.
- Payment API: An API with a service like PayPal for payment processing.
- Server: The application needs to be hosted on a cloud platform like Google Cloud to ensure scalability and reliability.
- Version Control: Create a git repository to manage codebase and collaboration among the development team.

