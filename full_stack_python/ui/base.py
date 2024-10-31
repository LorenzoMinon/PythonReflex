import reflex as rx

from .nav import navbar
from .dashboard import base_dashboard_page

def base_layout_component(child,*args,**kwargs) -> rx.Component:
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

def base_page(child:rx.Component, *args, **kwargs) -> rx.Component:
    is_logged_in = True
    if not isinstance(child,rx.Component):
        child = rx.heading("This is not a valid child element")
    return rx.cond(
        is_logged_in,
        base_dashboard_page(child,*args,**kwargs),
        base_layout_component(child,*args,**kwargs),
    )
    