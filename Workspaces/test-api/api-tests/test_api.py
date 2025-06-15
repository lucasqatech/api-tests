import requests

def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    print(f"ID: {data['id']}")
    print(f"Title: {data['title']}")
    print("Teste passou!")

if __name__ == "__main__":
    test_get_post()
