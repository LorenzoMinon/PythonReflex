import reflex as rx
import asyncio
from typing import List
from sqlmodel import Field, select

from datetime import datetime, timezone

from .model import ContactEntryModel

from .. import navigation
from ..auth.state import SessionState

class ContactState(SessionState):
    form_data: dict = {}
    entries:  List['ContactEntryModel'] = []
    did_submit: bool = False


    @rx.var
    def thank_you(self):
        first_name = self.form_data.get("first_name") or ""
        return f"Thank you {first_name}"

    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data
        data = {}
        for k,v in form_data.items():
            if v == "" or v is None:
                continue
            data[k] = v
        if self.my_user_id is not None:
            data['user_id'] = self.my_user_id
        with rx.session() as session:
            db_entry = ContactEntryModel(
                **data
            )
            session.add(db_entry)
            session.commit()
            self.did_submit = False
            yield

        self.did_submit = True
        yield 
        # sleep !! con un timeout
        await asyncio.sleep(4)
        self.did_submit = False
        yield

    def list_entries(self):
        with rx.session() as session: 
            entries = session.exec(
                select(ContactEntryModel)
            ).all()
            print(entries)
            self.entries = entries

