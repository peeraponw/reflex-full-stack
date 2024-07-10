import reflex as rx
from ..ui.base import base
from ..navigation import routes 

@rx.page(route=routes.ABOUT_PATH)
def about_page() -> rx.Component:
    child = rx.container(
                rx.vstack(
                    rx.heading("About", size="9"),
                    rx.text("This is the about page!"),
                    spacing="5",
                    justify="center",
                    align="center",
                    min_height="85vh",
                    
                ),
                id="about-container"
            )   
    return base(
        child    
    )