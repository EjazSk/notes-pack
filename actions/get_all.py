import requests
from st2common.runners.base_action import Action


__all__ = ["GetAll"]


class GetAll(Action):

    def __init__(self, config) -> None:
        super(GetAll, self).__init__(config)
        self.url = self.config.get('base_url')

    def run(self):
        notes = requests.get(self.url).json()
        return notes
