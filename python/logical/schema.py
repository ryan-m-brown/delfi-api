schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "shipping_address": {
            "type": "object",
            "properties": {
                "street_address": {
                    "type": "string"
                },
                "city": {
                    "type": "string"
                },
                "state": {
                    "type": "string"
                },
                "zip": {
                    "type": "integer"
                }
            },
            "required": [
                "street_address",
                "city",
                "state",
                "zip"
            ]
        },
        "instruments": {
            "type": "object",
            "properties": {
                "freezers": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "string"
                                },
                                "containers": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "object",
                                            "properties": {
                                                "barcode": {
                                                    "type": "string"
                                                },
                                                "description": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "barcode",
                                                "description"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "required": [
                                "name",
                                "containers"
                            ]
                        }
                    ]
                },
                "computers": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "string"
                                },
                                "mac_address": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "name",
                                "mac_address"
                            ]
                        }
                    ]
                }
            },
            "required": [
                "freezers",
                "computers"
            ]
        }
    },
    "required": [
        "name",
        "shipping_address",
        "instruments"
    ]
}
