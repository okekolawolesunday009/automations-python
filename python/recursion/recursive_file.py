# Corrected code
def count_users(group):
  count = 0
  for member in get_members(group):
    if is_group(member):
      count += count_users(member) # Recursively count users in the sub-group
    else:
      count += 1 # Only count if it's a user, not a group
  return count

# Assuming get_members(group) and is_group(member) functions exist
# print(count_users("sales")) # Expected: 3
# print(count_users("engineering")) # Expected: 8
# print(count_users("everyone")) # Expected: 18
