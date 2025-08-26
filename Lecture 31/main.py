from pymongo import MongoClient

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

# print(client.list_database_names())

db = client['PP-28']

students = db['students']

# print(students.count_documents({}))
# print(students.count_documents({"first_name": "murman"}))

# for student in students.find():
#     print(student)

# print(students.find_one())

# for student in students.find({"first_name": "murman"}):
#     print(student)

# student = {
#     'name' : 'vaniko',
#     'age' : 26
# }
#
# students.insert_one(student)

# students_list = [
#     {'name': 'fridon', 'age': 28},
#     {'name': 'luka', 'age': 22},
#     {'name': 'nikoloz', 'age': 21}
# ]
#
# students.insert_many(students_list)


# for student in students.find({"age": 22}):
#     print(student)

# for student in students.find({"age": { "$gte": 22 }}):
#     print(student)

# for student in students.find({"age": { "$lte": 22 }}):
#     print(student)

# for student in students.find({"age": { "$gte": 22, "$lte": 26 }}):
#     print(student)

# for student in students.find({"$or": [{"name": "luka"}, {"first_name": "murman"}]}):
#     print(student)

# for student in students.find({"$and": [{"name": "luka"}, {"age": 22}]}):
#     print(student)

# students.update_one({"name": "vaniko"}, {"$set": {"age": 27}})

# students.update_one({"name": "luka"}, {"$set": {"age": 27}})

# students.update_many({"name": "luka"}, {"$set": {"age": 24}})

# students.update_many({"name": "nikoloz"}, {"$set": {"email": "test@yahoo.com"}})

# students.delete_one({"name": "luka"})

# students.delete_many({"first_name": "murman"})

# students.update_many({}, {"$set": {'status': 'active'}})

students.delete_many({})