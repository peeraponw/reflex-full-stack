import reflex as rx
from ..ui.base import base
from ..navigation import routes 

@rx.page(route=routes.PRICING_PATH)
def pricing_page() -> rx.Component:
    child = rx.container(
                rx.vstack(
                    rx.heading("Pricing", size="9"),
                    rx.text("This is the pricing page!"),
                    spacing="5",
                    justify="center",
                    align="center",
                    min_height="85vh",
                    
                ),
                id="pricing-container"
            )   
    return base(
        child    
    )