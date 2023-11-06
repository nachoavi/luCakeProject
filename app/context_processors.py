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

def get_low_stock(request):
    low_stock = request.session.get("low_stock")

    return {
        "low_stock": low_stock
    }


