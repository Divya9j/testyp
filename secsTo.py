inp = int(input("Please enter Number of seconds: "))
days=0
hours=0
minutes=0
seconds=0
if inp < 0 :
    print("INVALID")
else :
    days = inp // (60 * 60 * 24);
    inp -= days * (60 * 60 * 24);
    if inp > 0 :
        hours = inp // (60 * 60);
        inp -= hours * (60 * 60);
    if inp > 0 :
        minutes = inp // 60;
        inp -= minutes * (60);
    seconds = inp
    print(days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")