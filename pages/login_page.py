from utils.config_reader import load_config


class LoginPage:

    def __init__(self, page):

        self.page = page

        self.config = load_config()


    def open(self):

        self.page.goto(
            self.config["base_url"] + "/login"
        )


    def login(
        self,
        username=None,
        password=None
    ):

        username = username or self.config["username"]

        password = password or self.config["password"]


        self.page.fill(
            "#username",
            username
        )


        self.page.fill(
            "#password",
            password
        )


        self.page.click(
            "button[type='submit']"
        )


    def get_message(self):

        return self.page.locator(
            "#flash"
        ).inner_text()