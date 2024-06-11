def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
arr = [5,2,1,3,9,0,4,5,6]

def selectionSort(arr):
    for i in range(len(arr)):
        kmin = i
        for j in range(i, len(arr)):
            if arr[j] < arr[kmin]:
                kmin = j
        
        if kmin != i:
            arr[kmin], arr[i] = arr[i], arr[kmin]
            
    print(arr)

def insertSort(arr):
    for i in range(len(arr)):
        k = i
        while k > 0 and arr[k-1] > arr[k]:
            arr[k-1], arr[k] = arr[k], arr[k-1]
            k -= 1
            
    print(arr)
class Employee:
        
    def __init__(self, employee_id):
        self.employee_id = employee_id

    def __repr__(self):
        return "Employee('{0}', )".format(self.employee_id)
    
    
    def __str__(self) -> str:
        return 'string form'
employeeObj1 = Employee("100001")
result = repr(employeeObj1)
print(result)
print(employeeObj1)

try:
    mark = int('x')
except ValueError as e:
    raise ValueError("{0} mark is invalid".format())

outputFormat = '{0:<10}{1:10}{2:10}'
with open('./studentList.csv') as studentList:
    # for line in studentList:
    #     print(line.rstrip())
    print(outputFormat.format('Student Number', 'First Name', 'Last Name'))
    while True:
        studentNumber = studentList.readline().strip()
        if not studentNumber:
            break
        print(studentNumber)
        name = studentList.readline().strip()
        last = studentList.readline().strip()
        
        print(outputFormat.format(studentNumber, name, last))