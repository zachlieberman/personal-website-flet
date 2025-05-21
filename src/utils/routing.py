# Routing logic for the Flet app


def get_routes():
    return {
        "/home": 0,
        "/about": 1,
        "/projects": 2,
        "/resume": 3,
        "/contact": 4,
    }


def update_route(e, page, routes):
    # Get the selected tab index
    index = e.control.selected_index
    # Convert index to route
    route_keys = list(routes.keys())
    if index < len(route_keys):
        new_route = route_keys[index]
        # Only update if route is different to avoid loops
        if page.route != new_route:
            page.route = new_route
            page.update()


def route_change(e, page, tabs, routes):
    if page.route in routes:
        # Only update if the tab index is different to avoid loops
        if tabs.selected_index != routes[page.route]:
            tabs.selected_index = routes[page.route]
            page.update()
    else:
        # Default to home if unknown route
        page.route = "/home"
        tabs.selected_index = 0
        page.update()
