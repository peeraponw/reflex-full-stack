"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .ui.base import base

from . import navigation, pages


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
    child = rx.container(
                rx.vstack(
                    rx.heading(State.header, size="9"),
                    
                    rx.text("This is my new app!"),
                    rx.link(
                        rx.button("Go to About"),
                        href=navigation.routes.ABOUT_PATH,
                        ),
                    spacing="5",
                    justify="center",
                    align="center",
                    min_height="85vh",
                ),
                id = "child-base",
            )
    return base(
        child
    )


app = rx.App()
app.add_page(index)
