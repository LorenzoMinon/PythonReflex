import reflex as rx


from ..import navigation
from ..ui.base import base_page


class ContactState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data



@rx.page(route = navigation.routes.CONTACT_US_PATH)
def contact_page() -> rx.Component:
    my_form = rx.form(
            rx.vstack(
                rx.input(
                    placeholder="First Name",
                    name="first_name",
                ),
                rx.input(
                    placeholder="Last Name",
                    name="last_name",
                ),
                rx.text_area(
                    name="message",
                    placeholder="your msg"
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
    )

    my_child=rx.vstack(
            rx.heading("Contact", size="9"),
            my_form,
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