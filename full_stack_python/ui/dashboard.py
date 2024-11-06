import reflex as rx

from .sidebar import sidebar

def base_dashboard_page(child:rx.Component, *args, **kwargs) -> rx.Component:

    if not isinstance(child,rx.Component):
        child = rx.heading("This is not a valid child element")

    return rx.fragment( # does nt unlike container 
        rx.hstack(
            sidebar(), # To show the sidebar in here in case it is True,
            rx.box(
                child,
                rx.logo(),
                padding="1em",
                text_alling = "center",
                width= "100%",
                id="my-content-area-el",
            ),
            

        ),
        #rx.color_mode.button(position="bottom-left",id="my-light-color-btn"),
        # id="my-base-container"
    )

    