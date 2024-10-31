import reflex as rx

import reflex_local_auth
from ..ui.base import base_page

# @rx.page(route='about')
@reflex_local_auth.require_login
def protected_page() -> rx.Component:
    my_child=rx.vstack(
            rx.heading("Protected Page", size="9"),
            rx.text(
                "Sth cool about us ",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child",

            
        )
    return base_page(my_child)