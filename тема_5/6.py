lessons_dict = {}
with open("my_file6.txt", encoding="utf-8") as file:
    for line in file:
        print(line)
        lesson_type, *lessons = line.split()
        lesson_count = [int(lesson.rstrip("(л)(пр)(лаб)")) for lesson in lessons if lesson != "—"]
        lessons_dict.update({lesson_type.rstrip(":"): sum(lesson_count)})
print(lessons_dict)
