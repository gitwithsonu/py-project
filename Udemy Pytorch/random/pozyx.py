from requests import post, get
from hashlib import sha256
import json


def get_tags(email, password, tenant_name):
    response = post('https://uauth.cloud.pozyxlabs.com/', json={
        "email": email,
        "password": sha256(password.encode("utf-8")).hexdigest(),
        "remember": True,
    })
    if response.status_code == 200:
        body = response.json()
        token = body["accessToken"]
        tenants = body["tenants"]
        # tenant_names = [tenant["name"] for tenant in tenants]

        tags_request = get('https://capi.cloud.pozyxlabs.com/tags', headers={
            "authorization": f"JWT {token}",
            "x-tenant-id": "61577cbcb94bf591377a3c80",
        })
        tags = tags_request.json()

        json_object = json.dumps(tags, indent=4)
        with open("dummy2.json", "w") as outfile:
            outfile.write(json_object)

        # print("Found tenants", tenant_names)
        # if tenant_name not in tenant_names:
        #     print(f"Tenant {tenant_name} not in tenants, try again")

    # for tenant in tenants:
    #     if tenant["name"] == tenant_name:
    #         tags_request = get('https://capi.cloud.pozyxlabs.com/tags', headers={
    #             "authorization": f"JWT {token}",
    #             "x-tenant-id": tenant["id"],
    #         })
    #         tags = tags_request.json()
    #         for tag in tags:
    #             if tag.get("labels"):
    #                 print(f"Tag {tag['id']} with labels:", tag["labels"])
    #         print("complete -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    #         print(" ")
    #         print(" ")


if __name__ == '__main__':
    email = 'ankit@gemba.systems'
    password = 'ankit@123'
    name = 'AFL Accessories'
    # while True:
    #     get_tags(email, password, name)
    get_tags(email, password, name)
