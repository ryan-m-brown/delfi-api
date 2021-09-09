import uuid
from random import randint

site = {
    "name": f"site name {uuid.uuid4()}",
    "shipping_address": {
        "street_address": f"{randint(0, 100)} My Street",
        "city": "my city",
        "state": "CA",
        "zip": randint(10000, 99999)
    },
    "instruments": {
        "freezers": [
            {
                "name": "freezer name",
                "containers": [
                    {
                        "barcode": f"{uuid.uuid4()}",
                        "description": "Some desc"
                    }
                ]
            }
        ],
        "computers": [
            {
                "name": "computer name",
                "mac_address": "computer mac"
            }
        ]
    }

}
