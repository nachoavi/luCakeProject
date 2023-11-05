def get_username(request):
    username = request.session.get('username', None)

    return {
        "username": username
    }

def get_role(request):
    role = request.session.get("role")

    return {
        "role": role
    }
