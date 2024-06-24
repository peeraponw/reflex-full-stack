"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    header = "Hello, Reflex!xxx"
    
    def handle_change_header(self, val):
        self.header = val + " erwerw"
    
    
    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading(State.header, size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            # rx.button(State.btn, on_click=State.change_btn),
            rx.input(on_change=State.handle_change_header),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
