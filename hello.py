from datetime import datetime
print("Hello, world! It's ", (str(datetime.now().time()).split(".")[0]), " this ", datetime.now().date())
