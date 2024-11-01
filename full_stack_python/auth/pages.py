import reflex as rx

from reflex_local_auth.pages.login import LoginState, login_form, PADDING_TOP
from reflex_local_auth.pages.registration import RegistrationState, register_form
from .. import navigation
from ..ui.base import base_page
from .forms import my_register_form
from .state import SessionState


def my_login_page()->rx.Component:

    return base_page(
        rx.center(
            rx.cond(
                LoginState.is_hydrated,
                rx.card(login_form()),
            ),
            min_height ="85vh",
            padding_top = PADDING_TOP,
        ),
    )

def my_logout_page() -> rx.Component:
    # Welcome Page (Index)
    my_child=rx.vstack(
            rx.heading("Sure you want to logout?", size="7"),
            rx.link(
                rx.button("No", color_scheme="gray"),
                href=navigation.routes.HOME_PATH
            ),
            rx.button("Yes, logout", on_click=SessionState.perform_logout),
            spacing="5",
            justify="center",
            text_align="center",
            align="center",
            min_height="85vh",
            id="my-child",

            
        )
    return base_page(my_child)


def my_register_page()->rx.Component:

    return base_page(
        rx.center(
            rx.cond(
                RegistrationState.is_hydrated,
                rx.card(my_register_form()),
            ),
            min_height ="85vh",
            padding_top = PADDING_TOP,
        ),
    )
