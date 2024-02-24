from tap import Tap


class Args(Tap):
    username: str

    def configure(self):
        self.add_argument("username", help="The GitHub username to get data for.")

    def process_args(self):
        if len(self.username) == 0:
            raise ValueError("Username cannot be empty.")
