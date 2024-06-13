def minMovesToSeat(seats, students):
    seats.sort()
    students.sort()
    
    res = 0
    print(seats)
    print(students)
    for i in range(len(seats)):
        res += abs(seats[i] - students[i])
    print(res)
    return res
seats = [3,1,5]
students = [2,7,4]

minMovesToSeat(seats, students)