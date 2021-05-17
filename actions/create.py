import requests
from st2common.runners.base_action import Action


__all__ = ["Create"]


class Create(Action):
    def __init__(self, config) -> None:
        super(Create, self).__init__(config)
        self.url = self.config.get("base_url")

    def run(self, title, content):
        headers = {'Content-type': 'application/json',
                   'Accept': 'application/json'}
        note = a = requests.post(self.url,
                                 json={"title": title, "content": content}, headers=headers)
        return note
