def letters(a):
  print(a + " has " + str(len(a)) + " characters.")
  for i in range(len(a)):
    print("a["+str(i)+"] is "+ a[i])
    #print(chr(a[i]))
letters("this is a test with more words")
