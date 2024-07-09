import request

for i in range(1,5000):
    url = f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id=1"
    r = request.get(url=URL)
    if r.status_code == 200:
        print(url)