import reflex as rx

from reflex_local_auth.pages.login import LoginState, login_form, PADDING_TOP
from reflex_local_auth.pages.registration import RegistrationState, register_form

from ..ui.base import base_page
from .forms import my_register_form


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
