#converting json to dict and dict to json
import json

student = {
    "name": "Your Name",
    "skills": ["Python", "Git", "Docker"]
}
stu_json=json.dumps(student)
print(stu_json)
print(type(stu_json))

stu_obj=json.loads(stu_json)
print(stu_obj)
print(type(stu_obj))
print(stu_obj.keys())
print(stu_obj.values())