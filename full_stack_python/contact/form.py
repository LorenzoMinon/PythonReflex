import reflex as rx
import asyncio
from sqlmodel import Field

from datetime import datetime, timezone

from ..auth.state import SessionState

from .state import ContactState


def contact_form() -> rx.Component:
    user_id = SessionState.my_user_id
    return rx.form(
            # rx.cond(
            #     SessionState.my_user_id,
            #     rx.box( 
            #         rx.input(
            #         type='hidden',
            #         name='user_id',
            #         value=SessionState.my_user_id
            #         ),
            #         display='none'
            #     ),
            #     rx.fragment(''), 
            # ),
            rx.vstack(
                rx.hstack(
                    rx.input(
                        placeholder="First Name",
                        name="first_name",
                        required=True,
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Last Name",
                        name="last_name",
                        required=True,
                        width="100%",
                    ),
                    width='100%'
                ),
                rx.input(
                    placeholder="Your email",
                    name="email",
                    required=False,
                    width="100%",
                ),
                rx.text_area(
                    name="message",
                    placeholder="your msg",
                    required=False,
                    width="100%",
                ),
                rx.button("Submit", type="submit"),
                width="100%",
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
    )