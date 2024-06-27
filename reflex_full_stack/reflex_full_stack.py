"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .ui.base import base


class State(rx.State):
    header = "Hello, Reflex!"
    clicked = "No"

    def handle_change_header(self, val):
        self.header = val

    def handle_did_click(self):
        if self.clicked == "No":
            self.clicked = "Yes"
        elif self.clicked == "Yes":
            self.clicked = "No"

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return base(
        rx.container(
            rx.vstack(
                rx.heading(State.header, size="9"),
                rx.text(
                    "Get started by editing ",
                    rx.code(f"{config.app_name}/{config.app_name}.py"),
                    size="5",
                ),
                rx.button(State.clicked, on_click=State.handle_did_click, id="button"),
                rx.input(
                    default_value="Hello",
                    on_change=State.handle_change_header,
                ),
                rx.link(
                    rx.button("Check out our docs!"),
                    href="https://reflex.dev/docs/getting-started/introduction/",
                    is_external=True,
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
            )
        )
    )


app = rx.App()
app.add_page(index)
