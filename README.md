# GitInsurance-App

Git and GitHub Workshop - Assignment 1

Exercise to practice basic git commands from [Roberto's repo](https://github.com/RoberVega/lp-git-basics/tree/main/assignments/assignment_1).

By running the Python script with the command

```
$ python policy.py
```

the user will be asked if he/she wants to add, remove or list policies. The first two options imply changes in the JSON file provided in this repository. Below you find a brief description of each function available inside `policy.py`:

- add_policy(): asks the user for the name of the client and type of insurance (auto/house). Based on those inputs, a new dictionary is created and added to the database (policies.json).
- remove_policy(): asks the user for the policy ID and removes the corresponding dictionary from the database.
- list_policies(): prints in the terminal all the policies available in the database.
