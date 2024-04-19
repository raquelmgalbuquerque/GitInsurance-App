import json
import sys

# Simplified database
filename = "policies.json"

# Read and update JSON file by adding new policy
with open(filename) as f:
  policies = json.load(f)

# Function to add a new policy given the user inputs
def add_policy():
  print("Add policy")
  client_name = input("Client name? ")
  insurance_type = input("Insurance type (auto/house)?").lower()

  # Update JSON file by adding new policy
  with open(filename, 'w') as f:
    new_policy = {"policyId": len(policies), "clientName": client_name, "insuranceType": insurance_type, "clientHasClaims": False, "claims":[]}
    policies.append(new_policy)
    json.dump(policies, f)

# Function to remove a policy given and ID provided by the user
def remove_policy():
  print("Remove policy")
  policy_id = int(input("Policy ID? "))

  for p in policies:
    if p["policyId"] == policy_id:
      policies.remove(p)
      break
  
  # Update JSON file by removing policy
  with open(filename, 'w') as f:
    json.dump(policies, f)

# Function to list policies stored in the JSON file
def list_policies():
  print("List policies")
  print(json.dumps(policies, indent=2))

# Function the provide an improved user experience
def options():
  print("------------------------------")
  print("   Welcome to PyInsurance!")
  print("   What do you want to do?")
  print("------------------------------")
  print("-> Add policy (a)?")
  print("-> Remove policy (r)?")
  print("-> List policies (l)?")
  print("-> Quit (q)?\n")

  answer = input("Answer: ").lower()

  if answer == "a":
    add_policy()
  elif answer == "r":
    remove_policy()
  elif answer == "l":
    list_policies()
  elif answer == "q":
    sys.exit("See you next time!")
  else:
    print("Invalid answer. Please try again.")

# Lets run this!
options()

# Uncomment for testing purposes
# add_policy()
# remove_policy()
# list_policies()
