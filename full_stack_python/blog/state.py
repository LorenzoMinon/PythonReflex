from typing import Optional, List
import reflex as rx

from sqlmodel import select

from .model import BlogPostModel

class BlogPostState(rx.State):
    posts: List['BlogPostModel'] = []
    post: Optional['BlogPostModel'] = None

    @rx.var
    def blog_post_id(self):
        print(self.router.page.params)
        return self.router.page.params.get("blog_id") or None
    
    def load_posts(self):
        with rx.session() as session:
            result = session.exec(
                select(BlogPostModel)
            ).all()
            self.posts = result
        # return
        



    def get_post_detail(self):
        with rx.session() as session:
            if self.blog_post_id == "":
                self.post=None
                return
            result = session.exec(
                select(BlogPostModel).where(
                    BlogPostModel.id == self.blog_post_id
                )
            ).one_or_none()
            self.posts = result

    def add_post(self, form_data:dict):
        with rx.session() as session:
            post = BlogPostModel(**form_data)
            # print("adding", post)
            session.add(post)
            session.commit()
            session.refresh(post) # post.id
            # print("added", post)
            self.post = post


class BlogAddPostFormState(BlogPostState):
    form_data: dict = {}
    def handle_submit(self, form_data):
        self.form_data = form_data
        self.add_post(form_data)
        # redirect