import reflex as rx

from . import routes

class NavState(rx.State):
    def to_home(self):
        return rx.redirect(routes.HOME_PATH)
    def to_about(self):
        return rx.redirect(routes.ABOUT_PATH)
    def to_pricing(self):
        return rx.redirect(routes.PRICING_PATH)
    def to_contact(self):
        return rx.redirect(routes.CONTACT_PATH)