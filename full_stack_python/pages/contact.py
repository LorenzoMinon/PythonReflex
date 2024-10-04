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
                rx.hstack(
                    rx.input(
                        placeholder="First Name",
                        name="first_name",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Last Name",
                        name="last_name",
                        width="100%",
                    ),
                    width='100%'
                ),
                rx.input(
                    placeholder="Your email",
                    name="last_name",
                    width="100%",
                ),
                rx.text_area(
                    name="message",
                    placeholder="your msg",
                    width="100%",
                ),
                rx.button("Submit", type="submit"),
                width="100%",
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
    )

    my_child=rx.vstack(
            rx.heading("Contact", size="9"),
            rx.desktop_only(
                rx.box(
                    my_form,
                    id="my-form-box",
                    width="25vw",
                )
            ),
            rx.mobile_and_tablet(
                rx.box(
                    my_form,
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