inp1, inp2 = input("Gib slovo: "),input("Gib druhe slovo: ")
print(((inp1[-2:] == inp2[-2:]) * "Rymuju sa") + ((inp1[-2:] != inp2[-2:]) * "Nerymuju sa"))