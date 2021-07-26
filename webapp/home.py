import justpy as jp
from webapp import layout, page


class Home(page.Page):
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is about the home page!",
               classes="text-4xl m-2")
        jp.Div(a=div, text="""
               Nothing particular about this""")
        return wp
