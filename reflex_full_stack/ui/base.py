import reflex as rx

from .nav import navbar


def base(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.container(navbar(), child, rx.color_mode.button(position="bottom-right"))
