"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


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
def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("About", "/#"),
                    navbar_link("Pricing", "/#"),
                    navbar_link("Contact", "/#"),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                    ),
                    rx.button("Log In", size="3"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )

def base(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.container(
        navbar(),
        child,
        rx.color_mode.button(position="bottom-right")
    )

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
            rx.button(State.clicked, on_click=State.handle_did_click),
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
    # return rx.container(
    #     rx.color_mode.button(position="top-right"),
    #     rx.vstack(
    #         rx.heading(State.header, size="9"),
    #         rx.text(
    #             "Get started by editing ",
    #             rx.code(f"{config.app_name}/{config.app_name}.py"),
    #             size="5",
    #         ),
    #         rx.button(State.clicked, on_click=State.handle_did_click),
    #         rx.input(
    #             default_value="Hello",
    #             on_change=State.handle_change_header,
    #             ),
    #         rx.link(
    #             rx.button("Check out our docs!"),
    #             href="https://reflex.dev/docs/getting-started/introduction/",
    #             is_external=True,
    #         ),
    #         spacing="5",
    #         justify="center",
    #         min_height="85vh",
    #     ),
    #     rx.logo(),
    # )


app = rx.App()
app.add_page(index)
