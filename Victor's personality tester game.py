print("\nWELCOME TO PERSONALITY TESTER GAME\n")
print("Note - CHOOSE THE MATCHING ANSWER AND WRITE THE NUMBER")
print("\nQ.You enjoy social event with lots of people?")
print("""1.Not at all
2.Sometimes
3.Yes most of the time
4.Hell yeah always""")
ans1 = int(input("->"))

print("\nQ.You don't spent time exploring intriguing ideas.")
print("""1.Not at all
2.Sometimes
3.Yes most of the time
4.Hell yeah always""")
ans2 = int(input("->"))


print("\nQ.You start the conversation.")
print("""1.Not at all
2.Sometimes
3.Yes most of the time
4.Hell yeah always""")
ans3 = int(input("->"))



print("\nQ.You like outings with friends.")
print("""1.Not at all
2.Sometimes
3.Yes most of the time
4.Hell yeah always""")
ans4 = int(input("->"))

print("\nQ.You are imprecise.") 
print("""1.Not at all
2.Sometimes
3.Yes most of the time
4.Hell yeah always""")
ans5 = int(input("->"))


print("\nQ.You feel bored when alone.")
print("""1.Not at all
2.Sometimes
3.Yes most of the time
4.Hell yeah always""")
ans6 = int(input("->"))


print("\nQ.You have a careful and methodical approach to life.")
print("""1.Not at all
2.Sometimes
3.Yes most of the time
4.Hell yeah always""")
ans7 = int(input("->"))

if 1<(ans1 + ans2 + ans3 + ans4 + ans5 + ans6 + ans7)<14:
    print("\nYou are an introvert")

elif 13<(ans1 + ans2 + ans3 + ans4 + ans5 + ans6 + ans7)<20:
    print("\nYou are an Ambivert")

else:
    print("\nYou are an Extrovert")