def serializer_module(model):
    return {
        "name": model.name,
        "pg_description": model.pg_description,
        "quantity": model.quantity,
        "price": model.price
    }


def serializer_teacher(model):
    return {
        "surname": model.surname,
        "name": model.name,
        "education": model.education,
        "teaching_exp": model.teaching_exp,
        "vocal_exp": model.vocal_exp,
        "description": model.description
    }
