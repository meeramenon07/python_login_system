print("MY LOGIN SYSTEM")
username = input("Username > ")
password = input("Password > ")
if username == "meera" and password == "meera":
  print("A warm welcome to you, Meera! You are our regular loyal customer, so, a very important notification for you. \n A Mother's Day Gift Voucher has been emailed to you with lovely treats.\n Have a very good day!")
elif username == "murali" and password == "bull":
  print("Hey there Murali! It's been a very long time since you logged in to this system.\n We hope, you are doing fine!")
elif username == "john" and password == "netie":
  print("Hey there John, I think, you have forgotten your login as you are here after a long time! \n How about either trying to remember the password again or if you have forgotten your current login password, why don't you create a very strong password and ensure that you write it down somewhere for you to retrieve it when you are log in! ")
else:
  print("Hey Imposter! Looks like you are not an eligible user and trying to break in to our system. \n Let us warn you that we have strong security system in place and you will not get away with stealing other users' passwords and stuff!!")
