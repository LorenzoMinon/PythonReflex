import reflex as rx
import asyncio


from datetime import datetime, timezone

from ..ui.base import base_page

from . import form, state

from ..models import ContactEntryModel

def contact_entry_list_item(contact: ContactEntryModel):
    return rx.box(
        rx.heading(contact.first_name),
        rx.text("Message:", contact.message),
        rx.cond(contact.user_id, 
                rx.text("User Id:", f"{contact.user_id}",), 
                rx.fragment("")),
        padding='1em'
    )

# def foreach_callback(text):
#     return rx.box(rx.text(text))

def contact_entries_list_page() ->rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Contact entries", size="9"),
            rx.foreach(state.ContactState.entries,
            contact_entry_list_item),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child",
        )
    )



def contact_page() -> rx.Component:
    my_child=rx.vstack(
            rx.heading("Contact", size="9"),
            rx.cond(state.ContactState.did_submit, state.ContactState.thank_you,
            ""),
            rx.desktop_only(
                rx.box(
                    form.contact_form(),
                    id="my-form-box",
                    width="25vw",
                )
            ),
            rx.mobile_and_tablet(
                rx.box(
                    form.contact_form(),
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