# much. Challenge - EVSE/Charging Challenge

Do as much as you can, it’s not necessary to solve all challenges. A well-documented, well-committed solution for some of
the challenge is better than an unreadable solution for all.
All tasks build up on each other. Commit as often and add as much documentation as you think is reasonable. Organize your
repository and your branches as you think the tasks demands.
Contact us in challenge@muchconsulting.de if you have any questions, or something seems wrong. Being able to communicate
questions and do requirements engineering is an important skill.
The structure (folders and files) of the solution is up to you, use the patterns and distribute the files in the way you think it makes
to most sense for the problem.
Try to do the challenge in no more than 4 hours.

# EVSE/Charging

In this project, you’re building a solution for a huge company that manages electric charging stations charges. Your module, that
later will be integrated to the ERP system of the company, is responsible for calculating the final price for the customer of their
charging sessions.
First, you’ll have to connect to an external server to download a JSON file containing the data for charges and supplier prices.

# 1. Get JSON with Data
In this task, you’ll connect to the server and get the base JSON file with all information. In the root structure of the JSON you will
have the Supplier Prices and the Charges .

# 2. Parse Data
In this task, you already have the data for the system, but the JSON that the company sent to you is messed up and you’ll have to
parse the data in a format that’s more readable for the ERP system. Your task is to clean the data, use meaningful names for the
variables, convert values to the correct types (native Python types), create objects (if needed) and any other clean/conversion that
is suitable for the data.

# 3. Calculate Prices
In this task, you already have all data parsed and converted, now you should calculate the price for the charges. Remeber that
calculating the price is the most important task of the system.

# 4. Export the Data
Now that you got everything good to go, add functions which combine all steps: Import, clean up the data, calculate prices and
finally export the models either to CSV or JSON file. There should be a separate file for every model.