import reflex as rx
import asyncio
from sqlmodel import Field

from datetime import datetime, timezone


from ..import navigation
from ..import contact
from ..ui.base import base_page


@rx.page(
    route = navigation.routes.CONTACT_US_PATH
    )

def contact_page() -> rx.Component:
    my_child=rx.vstack(
            rx.heading("Contact", size="9"),
            rx.cond(contact.ContactState.did_submit, contact.ContactState.thank_you,
            ""),
            rx.desktop_only(
                rx.box(
                    contact.contact_form(),
                    id="my-form-box",
                    width="25vw",
                )
            ),
            rx.mobile_and_tablet(
                rx.box(
                    contact.contact_form(),
                    id="my-form-box",
                    width="55vw",
                )
            ),
            rx.text(
                "Sth cool about us contact! ",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child",

            
        )
    return base_page(my_child)