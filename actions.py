import requests
from functools import wraps
from CTkMessagebox import CTkMessagebox

headers = {
    "X-USER-TOKEN": ""
}

def require_internet(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not check_connection():
            CTkMessagebox(title="No internet connection", message="Please make sure you have an internet connection.", icon="warning", font=("arial", 17))
            return "no internet connection"
        return func(*args, **kwargs)
    return wrapper


def load_graphs(user):
    result = requests.get(f"https://pixe.la/v1/users/{user}/graphs", headers=headers)
    while result.status_code != 200:
        result = requests.get(f"https://pixe.la/v1/users/{user}/graphs", headers=headers)

    graphs = result.json()
    values = []
    for graph in graphs["graphs"]:
        values.append(graph["id"])
    return values


def check_connection():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except requests.exceptions.RequestException:
        return False

def headers_value(token):
    headers["X-USER-TOKEN"] = token


@require_internet
def check_user(user):
    user_endpoint = f"https://pixe.la/@{user}"
    user_response = requests.get(url=user_endpoint)
    user_exist = True if user_response.status_code < 400 else False
    token_endpoint = f"https://pixe.la/v1/users/{user}"
    token_config = {
        "newToken": headers["X-USER-TOKEN"]
    }
    token_response = requests.put(url=token_endpoint, json=token_config, headers=headers)
    token_exist = True if token_response.status_code < 400 else False
    print("user: ", user_response.status_code)
    print("token: ", token_response.status_code)
    return True if user_exist and token_exist else False

@require_internet
def create_user(user, token):
    pixela_endpoint = "https://pixe.la/v1/users"
    pixela_parameters = {
        "token": token,
        "username": user,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(url=pixela_endpoint, json=pixela_parameters)
    print("new user: ", response.status_code)
    return response.json()["isSuccess"]


@require_internet
def create_graph(graph_id, name, unit, g_type, color, timezone, user):
    new_graph_endpoint = f"https://pixe.la/v1/users/{user}/graphs"
    new_graph_config = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": g_type,
        "color": color,
        "timezone": timezone,
        "startOnMonday": True
    }
    print(new_graph_config)
    response = requests.post(url=new_graph_endpoint, json=new_graph_config, headers=headers)
    print("new_graph: ", response.status_code)
    return True if response.status_code < 400 else False


@require_internet
def delete_graph(user, graph_id):
    graph_endpoint = f"https://pixe.la/v1/users/{user}/graphs/{graph_id}"
    response = requests.delete(graph_endpoint, headers=headers)
    print("delete graph: ", response.status_code)
    if response.status_code == 503:
        return delete_graph(user, graph_id)
    elif response.status_code < 400:
        return True
    return False


@require_internet
def add_pixel(date, quantity, user, graph_id):
    graph_endpoint = f"https://pixe.la/v1/users/{user}/graphs/{graph_id}"
    graph_config = {
        "date": date,
        "quantity": quantity
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print("add pixel: ", response.status_code)
    if response.status_code == 503:
        return add_pixel(date, quantity, user, graph_id)
    elif response.status_code < 400:
        return True
    return False

@require_internet
def delete_pixel(user, graph_id, date):
    graph_endpoint = f"https://pixe.la/v1/users/{user}/graphs/{graph_id}/{date}"
    response = requests.delete(graph_endpoint, headers=headers)
    print("delete pixel: ", response.status_code)
    if response.status_code == 503:
        return delete_pixel(user, graph_id, date)
    elif response.status_code < 400:
        return True
    return False
