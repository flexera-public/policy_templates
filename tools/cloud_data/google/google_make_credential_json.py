import os
import json

# File names for reading/writing
output_filename = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
os.makedirs(os.path.dirname(output_filename), exist_ok=True)

# Store JSON from environment variable in local file
with open(output_filename, "w") as type_file:
    type_file.write(os.getenv("GOOGLE_AUTH_JSON"))
