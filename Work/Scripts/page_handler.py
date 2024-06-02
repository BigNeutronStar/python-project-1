from math import pi
import flet as ft
from flet_route import Routing, path
import os
from multiprocessing import Process, Queue

from Library.pages import Home
from Library.pages import Graphics
from Library.pages import Reports
from Library.pages import Info
from Library.pages import Loading
from Library.pages import ViewData
from Library.pages import setup_table_views
import time
from Library import data

from Scripts import data_collector

def setup_page(page: ft.Page):
    theme = ft.Theme()
    theme.page_transitions.windows = ft.PageTransitionTheme.NONE
    theme.page_transitions.macos = ft.PageTransitionTheme.NONE
    theme.page_transitions.linux = ft.PageTransitionTheme.NONE
    page.theme = theme
    page.theme_mode = 'dark'

    if os.name == 'nt':
        page.window_title_bar_hidden = True
        page.window_title_bar_buttons_hidden = True

    page.window_min_height = 800
    page.window_min_width = 700
    page.spacing = 0
    page.padding = 0

    app_routes = [
        path(url = "/", clear = True, view=Loading),
        path(url = "/home", clear = True, view=Home),
        path(url = "/graphics", clear=True, view=Graphics),
        path(url = "/info", clear=True, view=Info),
        path(url = "/view_data", clear=True, view=ViewData),
        path(url = "/reports", clear=True, view=Reports),
    ]

    Routing(page=page,
            app_routes=app_routes)

    page.update()

    page.window_maximized = True
    page.update()

def run_app(page: ft.Page):
    page.go(page.route)
    data_collector.read_data()
    page.go('/home')
    data_collector.generate_main()


    
     
    