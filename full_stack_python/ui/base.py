import reflex as rx

from .nav import navbar

def base_page(child:rx.Component,hide_navbar=False, *args, **kwargs) -> rx.Component:

    if not isinstance(child,rx.Component):
        child = rx.heading("This is not a valid child element")
    if hide_navbar:
        return rx.container(
        child,
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
    )
    return rx.fragment( # does nt unlike container 
        navbar(), # To show the navbar in here in case it is True,
        rx.box(
            child,
            padding="1em",
            text_alling = "center",
            width= "100%",
            id="my-content-area-el",
        ),
        rx.color_mode.button(position="bottom-left",id="my-light-color-btn"),
        id="my-base-container"
    )

    