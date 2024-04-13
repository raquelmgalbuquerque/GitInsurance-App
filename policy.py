import json
import sys

# Simplified database
filename = "policies.json"

# Read and update JSON file by adding new policy
with open(filename) as f:
  policies = json.load(f)

def add_policy():
  print("Add policy")
  client_name = input("Client name? ")
  insurance_type = input("Insurance type (auto/house)?").lower()

  # Update JSON file by adding new policy
  with open(filename, 'w') as f:
    new_policy = {"policyId": len(policies), "clientName": client_name, "insuranceType": insurance_type}
    policies.append(new_policy)
    json.dump(policies, f)

add_policy()