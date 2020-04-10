import os
def alloc(age, Concession_Authority):
    B1Lower = []
    f = open(os.getcwd() + "\seatbooking\seating\B1Lower.txt", "r")
    for x in f:
        B1Lower.append(int(x))
    f.close()

    B1Others = []
    f = open(os.getcwd() + "\seatbooking\seating\B1Others.txt", "r")
    for x in f:
        B1Others.append(int(x))
    f.close()

    if(int(age)>=60 or Concession_Authority!='No'):
        if(len(B1Lower)!=0):
            seat = B1Lower[0]
            coach = 'B1'
            B1Lower = B1Lower[1:]
            f = open(os.getcwd() + "\seatbooking\seating\B1Lower.txt", "w")
            for i in range (len(B1Lower)):
                temp = str(B1Lower[i])+"\n"
                f.write(temp) 
            f.close()  
            return seat,coach
        else:
            B2Lower = []
            f = open(os.getcwd() + "\seatbooking\seating\B2Lower.txt", "r")
            for x in f:
                B2Lower.append(int(x))
            f.close()   
            if(len(B2Lower)!=0):
                seat = B2Lower[0]
                coach = 'B2'
                B2Lower = B2Lower[1:]
                f = open(os.getcwd() + "\seatbooking\seating\B2Lower.txt", "w")
                for i in range (len(B2Lower)):
                    temp = str(B2Lower[i])+"\n"
                    f.write(temp) 
                f.close() 
                return seat,coach
            else:
                B3Lower = []
                f = open(os.getcwd() + "\seatbooking\seating\B3Lower.txt", "r")
                for x in f:
                    B3Lower.append(int(x))
                f.close()
                if(len(B3Lower)!=0):
                    seat = B3Lower[0]
                    coach = 'B3'
                    B3Lower = B3Lower[1:]
                    f = open(os.getcwd() + "\seatbooking\seating\B3Lower.txt", "w")
                    for i in range (len(B3Lower)):
                        temp = str(B3Lower[i])+"\n"
                        f.write(temp) 
                    f.close()   
                    return seat,coach
                else:
                    seat = 'Not Available'
                    coach = 'Not Available'
                    return seat,coach

    else:
        if(len(B1Others)!=0):
            seat = B1Others[0]
            coach = 'B1'
            B1Others = B1Others[1:]
            f = open(os.getcwd() + "\seatbooking\seating\B1Others.txt", "w")
            for i in range (len(B1Others)):
                temp = str(B1Others[i])+"\n"
                f.write(temp) 
            f.close()
            return seat,coach
        else:
            B2Others = []
            f = open(os.getcwd() + "\seatbooking\seating\B2Others.txt", "r")
            for x in f:
                B2Others.append(int(x))
            f.close()
            if(len(B2Others)!=0):
                seat = B2Others[0]
                coach = 'B2'
                B2Others = B2Others[1:]
                f = open(os.getcwd() + "\seatbooking\seating\B2Others.txt", "w")
                for i in range (len(B2Others)):
                    temp = str(B2Others[i])+"\n"
                    f.write(temp) 
                f.close()
                return seat,coach
            else:
                B3Others = []
                f = open(os.getcwd() + "\seatbooking\seating\B3Others.txt", "r")
                for x in f:
                    B3Others.append(int(x))
                f.close()
                if(len(B3Others)!=0):
                    seat = B3Others[0]
                    coach = 'B3'
                    B3Others = B3Others[1:]
                    f = open(os.getcwd() + "\seatbooking\seating\B3Others.txt", "w")
                    for i in range (len(B3Others)):
                        temp = str(B3Others[i])+"\n"
                        f.write(temp) 
                    f.close()
                    return seat,coach
                else:
                    seat = 'Not Available'
                    coach = 'Not Available'
                    return seat,coach

