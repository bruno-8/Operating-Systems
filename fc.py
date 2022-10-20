#FCFS
def completiontime(processes,n,bt):
    ct = []
    ct.append(bt[0])
    for i in range(1,n):
       temp  = ct[i-1] + bt[i]
       ct.append(temp)
    return ct

def turnarounttime(processes,n,ct,at):
    tat = []
    for i in range(n):
        temp1 = ct[i] - at[i]
        tat.append(temp1)
    return tat

def waitingtime(processes,n,tat,bt):
    wt = []
    for i in range(n):
        temp2 = tat[i] - bt[i]
        wt.append(temp2)
    return wt

def avgwt(processes,n,wt):
    avgwt = 0
    twt = 0
    for i in range(n):
        twt = twt + wt[i]
    avgwt = twt/(n)
    return avgwt

def display(processses,n,at,bt):
    ct = completiontime(processes,n,bt)
    tat = turnarounttime(processes,n,ct,at)
    wt = waitingtime(processes,n,tat,bt)
    avgwt1 = avgwt(processes,n,wt)
    print("PROCESS | AT | BT | CT | TAT | WT")
    for i in range(n):
        print(" " + str(i) + " " + str(at[i]) + " " + str(bt[i]) + " " + str(ct[i]) + " " + str(tat[i]) + " " + str(wt[i]))
    print("Average waiting time:" + str(avgwt1))

if __name__ =="__main__":
    processes = [0,1,2,3,4]
    n = len(processes)
    at = [0,1,2,3,6]
    bt = [2,6,4,9,12]
    display(processes,n,at,bt)