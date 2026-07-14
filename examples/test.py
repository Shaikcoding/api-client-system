from apiclient import APIClient, ClientConfig

config = ClientConfig(
    base_url="https://jsonplaceholder.typicode.com"
)

client = APIClient(config)
print("Testing API...")

try:
    users = client.get("/users")
    print(f"✅ Found {len(users)} users!")
    print(f"First user: {users[0]['name']}")
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    client.close()