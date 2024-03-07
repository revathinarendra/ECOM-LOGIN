from decouple import config

# Attempt to fetch a test variable
test_var = config("TEST_VAR", default="NOT FOUND")
print(f"TEST_VAR: {test_var}")
