import json
from typing import List
from uuid import UUID


class Address:

    def __init__(self, street_address: str, city: str, state: str, zip_code: int):
        assert len(state) == 2, "US State abbreviation expected"
        assert len(str(zip_code)) == 5, "5 digit zip expected"

        self._street_address = street_address
        self._city = city
        self._state = state
        self._zip = zip_code

    @property
    def street_address(self) -> str:
        return self._street_address

    @street_address.setter
    def street_address(self, street_address: str):
        self._street_address = street_address

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, city: str):
        self._city = city

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, state: str):
        self._state = state

    @property
    def zip(self) -> int:
        return self._zip

    @zip.setter
    def zip(self, zip_code: int):
        self._zip = zip_code

    def __str__(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Container:

    def __init__(self, barcode: UUID, description: str):
        self._barcode = barcode
        self._description = description

    @property
    def barcode(self) -> UUID:
        return self._barcode

    @barcode.setter
    def barcode(self, barcode: UUID):
        self._barcode = barcode

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    def __str__(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Instrument:

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name


class Computer(Instrument):

    def __init__(self, name: str, mac_address: str):
        super().__init__(name)
        self._mac_address = mac_address

    @property
    def mac_address(self) -> str:
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address: str):
        self._mac_address = mac_address

    def __str__(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Freezer(Instrument):

    def __init__(self, name: str, containers: List[Container]):
        super().__init__(name)
        self._containers = containers

    @property
    def containers(self) -> List[Container]:
        return self._containers

    @containers.setter
    def containers(self, containers: List[Container]):
        self._containers = containers

    def __str__(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Site:

    def __init__(self, name: str, address: Address, instruments: List[Instrument]):
        self._name = name
        self._address = address
        self._instruments = instruments

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def address(self) -> Address:
        return self._address

    @address.setter
    def address(self, address: Address):
        self._address = address

    @property
    def instruments(self) -> List[Instrument]:
        return self._instruments

    @instruments.setter
    def instruments(self, instruments: List[Instrument]):
        self._instruments = instruments

    def __str__(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
