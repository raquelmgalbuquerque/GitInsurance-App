import json

# Simplified database
filename = "policies.json"

# Read JSON file
with open(filename) as f:
  policies = json.load(f)

# Function to list policies with claims stored in the JSON file
def list_claims():

  for p in policies:
    if not p["clientHasClaims"]:
      policies.remove(p)

  print("List policies with claims")
  print(json.dumps(policies, indent=2))

list_claims()