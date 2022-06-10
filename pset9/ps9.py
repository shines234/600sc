# 6.00 Problem Set 9
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

SUBJECT_FILENAME = "subjects.txt"
SHORT_SUBJECT_FILENAME = "shortened_subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    subjects = {}
    inputFile = open(filename)
    for line in inputFile:
        line = line.strip().split(',')
        subjects[line[0]] = (int(line[1]),int(line[2]))
    return subjects

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).


def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print( res)

#
# Problem 2: Subject Selection By Greedy Optimization
#

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    # TODO...
    return subInfo1[0] > subInfo2[0]

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    # TODO...
    return subInfo1[1] < subInfo2[1]

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    # TODO...
    return (subInfo1[0]/subInfo1[1]) < (subInfo2[0]/subInfo2[1])

def merge(left, right, comparator):
    """Assumes left and right are sorted lists.
     lt defines an ordering on the elements of the lists.
     Returns a new sorted(by lt) list containing the same elements
     as (left + right) would contain."""
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if comparator(left[i][1], right[j][1]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result
            
def sort(subjects, comparator):
    """Returns a new sorted list containing the same elements as L"""
    if len(subjects) < 2:
        return subjects[:]
    else:
        middle = int(len(subjects)/2)
        left = sort(subjects[:middle], comparator)
        right = sort(subjects[middle:], comparator)
        return merge(left, right, comparator)

def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    total_work = 0
    item = 0
    best_schedule = {}
    subjects_list = list(subjects.items())
    sorted_list = sort(subjects_list, comparator)
    total_value = 0
    while item <= (len(sorted_list) - 1):
        if total_work + sorted_list[item][1][1] > maxWork:
            item += 1 
            continue
        else:     
            total_work += sorted_list[item][1][1]
            best_schedule[sorted_list[item][0]] = sorted_list[item][1]
            total_value += sorted_list[item][1][0]
            item += 1
    print("Best total value of my courses is: ", total_value)
    return best_schedule
    

#
# Problem 3: Subject Selection By Brute Force
#

def getBiOptions(length):
    if length == 0:
        return [[binary] for binary in [0,1]]
    else:
        result_strings = []
        for item in [0,1]:
            for remainder in getBiOptions((length - 1)):
                result_strings.append([item] + remainder)
        return result_strings

indexCombs = getBiOptions(2)
print(indexCombs)

def getIndexCombi(binaryOptions, subjects_list):
    del binaryOptions[0]
    options = []
    for bi_option in binaryOptions:
        option = []
        for index, value in enumerate(bi_option):
            if value == 1:
                option.append(subjects_list[index])
            else:
                continue
        options.append(option)
    return options

subjects = loadSubjects(SHORT_SUBJECT_FILENAME)
subjects_list = list(subjects.items())
getIndexCombi(getBiOptions(3), subjects_list[0:4])


def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    subjects_list = list(subjects.items())
    solutions = []
    best_value = 0
    for schedule in getIndexCombi(getBiOptions(len(subjects_list) - 1), subjects_list):
#         print(schedule)
        total_work = 0
        total_value = 0
        solution = []
        for course in schedule:
            total_work += course[1][1]
            total_value += course[1][0]
        if total_work <= maxWork:
            if total_value > best_value:
                best_value = total_value
                best_courses = schedule
    best_timetable = {}
    for course in best_courses:
        best_timetable[course[0]] = course[1]
    print("Best total value of my courses:", best_value)
    return best_timetable


if __name__ == '__main__':
    loadSubjects('shortened_subjects.txt')