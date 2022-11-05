#-----------------------------------#
# Taken from lecture 2 slides 10-12 #
#-----------------------------------#


def greedy_activity_selection(activities):
    """
:   find list of activities that its lenght is maximum
:   that can be. for full explanetion look at slide 12.
:   param activities: list of sorted activities ordered by 'finish-time'
:   type activities: list of sorted activities ordered by 'finish-time'.
:                    every activity looks like: (index, (start-time, finish-time))
:                    when index is integer, start-time is integer between 0 to 99,
:                    and finish-time is integer which sustains: start-time < finish-time <= 99. 
    """
    n = len(activities)
    
    # insert the index (ordered by user input before) of
    # the first activities after sorting 'by-finish'    
    A = [activities[0][0]]
    
    # hold the current place of the last act that was taken.
    j = 0
    
    for i in range(1, n):
        _, (_, fj) = activities[j]
        index, (si, _) = activities[i]
        
        if fj <= si:
            # append the real index (as explain abouve) to A
            A.append(index)
            
            # update the current place of last act was taken.
            j = i

    return A


def sortActivities(activities):
    """
:   sort list of activities.
:   param activities: list of sorted activities ordered by 'finish-time'
:   type activities: list of sorted activities ordered by 'finish-time'.
:                    every activity looks like: (index, (start-time, finish-time))
:                    when index is integer, start-time is integer between 0 to 99,
:                    and finish-time is integer which sustains: start-time < finish-time <= 99. 
    """
    activities.sort(key = lambda act: act[1][1])
    

def getActivities():
    """
:   ask user for list of activities.
:   for each activity user input 'start-time'
:   and 'finish-time', as integer between 0-99,
:   when 0 <= start-time < finish-time <=99.
:   in addition, every activity gets index number,
:   so every activity looks like: (index, (start-time, finish-time)).
:   return: list of activities.
:   rtype: list of activities as explain abouve.
    """
    activities = []
    num_of_activities = int(input("Enter number of activities: "))
    
    for i in range(num_of_activities):
        s = int(input(f"{i+1}. Enter value for start (0-99): "))
        f = int(input(f"{i+1}. Enter value for finish ({s+1}-99): "))
        activities.append((i+1,(s, f)))
    
    return activities


def printActivities(activities):
    """
:   prints activities.
:   param activities: list of sorted activities ordered by 'finish-time'
:   type activities: list of sorted activities ordered by 'finish-time'.
:                    every activity looks like: (index, (start-time, finish-time))
:                    when index is integer, start-time is integer between 0 to 99,
:                    and finish-time is integer which sustains: start-time < finish-time <= 99. 
    """
    for i,(s, f) in activities:
        print(f"{i}. " + ("-" * s) + ("#" * (f - s)) + ("-" * (100 - f)))
        
        
def main():
    # This list is example for list of activities according to slide 13 (here, every value mult by 4)
    #[(4,16),(12,20),(0,24), (20, 28), (12,32), (20, 36), (24, 40), (32, 44), (32, 48), (44, 52)]
    
    # get activities from user
    activities = getActivities()
    print()
    
    # print the activities before sort
    print("Before sort:")
    printActivities(activities)
    print()
    
    # sort the activities by 'finish-time'
    sortActivities(activities)
    
    # print the activities after sort.
    print("After sort:")
    printActivities(activities)
    print()
    
    # finds list of activities (list with max length that can be) by the algorithm
    selected_activities_indexes = greedy_activity_selection(activities)
    print("list of activities nmubers was taken by the algorithm: " + str(selected_activities_indexes))
    
    
if __name__ == "__main__":
    main()

