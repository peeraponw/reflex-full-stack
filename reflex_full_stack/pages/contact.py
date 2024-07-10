import reflex as rx
from ..ui.base import base


def contact_page() -> rx.Component:
    child = rx.container(
                rx.vstack(
                    rx.heading("Contact", size="9"),
                    rx.text("This is the contact page!"),
                    spacing="5",
                    justify="center",
                    align="center",
                    min_height="85vh",
                    
                ),
                id="contact-container"
            )   
    return base(
        child    
    )