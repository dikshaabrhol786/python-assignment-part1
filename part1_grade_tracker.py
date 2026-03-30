# python assignment part 1


raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for s in raw_students:
    # strip() removes extra spaces from both sides, title() makes it like "Ayesha Sharma"
    name = s["name"].strip().title()

    # roll was stored as string "101", converting to actual number 101
    roll = int(s["roll"])

    # marks were all in one string like "88, 72, 95"
    # so i split by ", " to get each mark separately, then convert to int
    marks = []
    for m in s["marks_str"].split(", "):
        marks.append(int(m))

    cleaned_students.append({"name": name, "roll": roll, "marks": marks})

    # checking if name is valid - every word should have only letters
    # if any word has a number or symbol, valid becomes False
    valid = True
    for word in name.split():
        if not word.isalpha():
            valid = False

    if valid:
        print(name, "- valid name")
    else:
        print(name, "- invalid name")

    print("================================")
    print("Student :", name)
    print("Roll No :", roll)
    print("Marks   :", marks)
    print("================================")
    print()

# task asked to print roll 103 name in upper and lower case
for s in cleaned_students:
    if s["roll"] == 103:
        print(s["name"].upper())
        print(s["name"].lower())
        print()


# task 2

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

# going through each subject one by one and deciding grade based on marks range
for i in range(len(subjects)):
    m = marks[i]
    if m >= 90:
        grade = "A+"
    elif m >= 80:
        grade = "A"
    elif m >= 70:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "F"
    print(subjects[i], ":", marks[i], "[" + grade + "]")

# adding all marks one by one to get total
total = 0
for m in marks:
    total = total + m

avg = round(total / len(marks), 2)

# starting with first subject as highest and lowest, then comparing rest
highest = marks[0]
highest_sub = subjects[0]
lowest = marks[0]
lowest_sub = subjects[0]

for i in range(len(marks)):
    if marks[i] > highest:
        highest = marks[i]
        highest_sub = subjects[i]
    if marks[i] < lowest:
        lowest = marks[i]
        lowest_sub = subjects[i]

print("Total :", total)
print("Average :", avg)
print("Highest :", highest_sub, highest)
print("Lowest :", lowest_sub, lowest)
print()

new_marks = []
added = 0

# this loop keeps asking for subjects until user types "done"
# try/except is used so program doesn't crash if user types letters instead of numbers
while True:
    sub = input("enter subject name (done to stop): ")
    if sub.lower() == "done":
        break
    val = input("enter marks (0-100): ")
    try:
        val = float(val)
        if 0 <= val <= 100:
            new_marks.append(val)
            added += 1
        else:
            # valid number but out of range
            print("marks should be 0 to 100")
    except:
        # user typed something that is not a number
        print("please enter a valid number")

# combining original marks with newly added ones to recalculate average
all_marks = marks + new_marks
new_total = 0
for m in all_marks:
    new_total = new_total + m
new_avg = round(new_total / len(all_marks), 2)

print("subjects added:", added)
print("new average:", new_avg)
print()


# task 3

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("Name               | Average | Status")
print("-" * 40)

passed = 0
failed = 0
all_avgs = []
topper_name = ""
topper_avg = 0  # will update this whenever someone has higher avg

for i in range(len(class_data)):
    name = class_data[i][0]
    m_list = class_data[i][1]

    # manually adding all marks to find total, then dividing for average
    total = 0
    for m in m_list:
        total = total + m
    avg = round(total / len(m_list), 2)

    # if average is 60 or more, student passes
    if avg >= 60:
        status = "Pass"
        passed = passed + 1
    else:
        status = "Fail"
        failed = failed + 1

    all_avgs.append(avg)

    # checking if this student has higher avg than previous topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    print(name.ljust(18), "|", str(avg).center(7), "|", status)

# calculating average of all students averages
class_total = 0
for a in all_avgs:
    class_total = class_total + a
class_avg = round(class_total / len(all_avgs), 2)

print()
print("passed:", passed)
print("failed:", failed)
print("topper:", topper_name, topper_avg)
print("class average:", class_avg)
print()


# task 4

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# first removing spaces from both ends before doing anything else
clean_essay = essay.strip()
print(clean_essay)
print()

# title() capitalises first letter of every word
print(clean_essay.title())
print()

# splitting essay into words and checking each word for "python"
count = 0
words = clean_essay.split()
for w in words:
    if w.lower() == "python":
        count = count + 1
print("python appears", count, "times")
print()

# replace() finds every "python" and swaps it with "Python 🐍"
print(clean_essay.replace("python", "Python 🐍"))
print()

# splitting on ". " gives us each sentence as a separate item in a list
sentences = clean_essay.split(". ")
print(sentences)
print()

# printing each sentence with a number, adding "." at end if missing
for i in range(len(sentences)):
    s = sentences[i]
    if not s.endswith("."):
        s = s + "."
    print(str(i + 1) + ".", s)