from typing import Callable

from fexample.location.data_model import Location


LocationProxy = Callable[[str], Location]


def current_location(car_id: str) -> Location: ...

