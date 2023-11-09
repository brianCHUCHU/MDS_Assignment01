import matplotlib.pyplot as plt
class WorkStation:
    def __init__(self, StationNo, T_0):
        self.StationNo = StationNo
        self.T_0 = T_0
        self.WorkingHr = []
        self.isWorking = []
        for i in range(StationNo):
            self.isWorking.append(False)
            self.WorkingHr.append(0)
        self.standby = 0
    
    def add(self, input_num):
        self.standby += input_num
    
    def update(self):
        finished_num = 0
        for i in range(len(self.WorkingHr)):
            if(self.standby > 0 and (not self.isWorking[i])):
                self.isWorking[i] = True
                self.standby -= 1
            if(self.isWorking[i]):
                self.WorkingHr[i] += 1
            if(self.WorkingHr[i] == self.T_0):
                self.WorkingHr[i] = 0
                finished_num += 1
                self.isWorking[i] = False
        return finished_num
    
    def getStandby(self):
        return self.standby

Wip = []
Ct = []
Th = []
cycle = 1000
for w in range(1, 50):
    wip = []
    wipnum = 0
    CTtotal = 0
    tempAdd = 0
    for i in range(w):
        wip.append(0)

    hr = 0
    final = 0

    Station = [WorkStation(5, 7), WorkStation(2, 3), WorkStation(6, 15), WorkStation(3, 5)]
    Station_standby = [0, 0, 0]
    Station[0].add(w)
    while True:
        for i in range(len(Station)):
            if(i != 3):
                Station_standby[i] = Station[i].update()
            else:
                temp = Station[i].update()
                for i in range(temp):
                    CTtotal += hr + 1 - wip[wipnum]
                    wip[wipnum] = hr + 1 - wip[wipnum]
                    wipnum += 1
                    # if (hr+1) % 5 == 0 or Station[1].getStandby() == 0: temptemp = hr + 1
                    # else: temptemp = int((hr + 1) / 5)*5 + 5
                    wip.append(hr + 1)
                    Station[0].add(1)
                final += temp

        for i in range(len(Station_standby)):
            Station[i + 1].add(Station_standby[i])
        hr += 1
        # print(final, w)
        if(final >= cycle * w): 
            for i in range(len(wip) - cycle * w):
                wip.pop()
            break
    if(w <= 12):print(wip)
    Wip.append(w)
    CT = CTtotal / (cycle * w)
    Ct.append(CT)
    Th.append(w / (CT))
    print('WIP = ', w, 'CT = ', round(CT, 2), 'TH = ', w / (CT))

plt.plot(Wip, Th)
plt.xlabel('Wip')
plt.ylabel('TH(/hr)')
plt.show()

plt.plot(Wip, Ct)
plt.xlabel('WIP')
plt.ylabel('CT (hr)')
plt.show()