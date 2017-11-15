class Input:
    def __init__(self, occupantNumber, isWeekends, month, timeResolution):
        self.occupantNumber = occupantNumber;
        self.isWeekends = isWeekends;
        self.month = month;
        self.timeResolution = timeResolution;

    def __str__(self):
        return "Input: [occupantNumber] = %s, [isWeekend] = %s, [month] = %s, [timeResolution] = %s" %(self.occupantNumber,self.isWeekends,self.month,self.timeResolution)