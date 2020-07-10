class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        #historyToUndo and historyToRedo keep tracks of all the actions
        self.historyToUndo = []
        self.historyToRedo = []

    def add(self, num: int):
        #Becuase we have done something, we keep track of the action to historyToUndo
        self.historyToUndo.append(num)
        self.value = self.value + num

    #subtracting is equivalent to adding negative
    def subtract(self, num: int):
        num = -num
        self.add(num)
    

    def undo(self):
        try:
            #we negate the most recent action (by subtracting it [since we added]) in historyToUndo
            self.value = self.value - self.historyToUndo[-1]
            #We keep track of the undo in historyToRedo
            self.historyToRedo.append(self.historyToUndo[-1])
            #We no longer need to keep track of that action in historyToUndo
            self.historyToUndo.pop()
        #If we can't undo, we do nothing
        except:
            pass


    def redo(self):
        try:
            #We negate the most recent redo (by adding it [since we subtracted]) in historyToRedo
            self.value = self.value + self.historyToRedo[-1]
            #We keep track of the redo in historyToUndo
            self.historyToUndo.append(self.historyToRedo[-1])
            #We no longer need to keep track of that action in historyToRedo
            self.historyToRedo.pop()
        #If we can't redo, we do nothing
        except:
            pass


    def bulk_undo(self, steps: int):
        index = steps
        #We undo until we can't do it anymore
        while (index > 0 and len(self.historyToUndo) > 0):
            self.undo()
            print(self.value)
            index -= 1


    def bulk_redo(self, steps: int):
        index = steps
        #We redo until we can't do it anymore
        while (index > 0 and len(self.historyToRedo) > 0):
            self.redo()
            index -=1


