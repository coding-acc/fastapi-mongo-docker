def serializer(todo)->dict:
    return{
        "id":str(todo["_id"]),
        "name":todo["name"],
        "field1":todo["field1"],
        "completed":todo["completed"]
    }

def serializers(todos)->list:
    return [serializer(todo) for todo in todos]