import reflex as rx

def blog_post_not_found() -> rx.Component:
    return rx.hstack(
        rx.heading("BLOG POST NOT FOUND"),
        spacing="5",
        align="center",
        min_height="85vh"
    )