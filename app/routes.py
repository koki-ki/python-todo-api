from flask import Blueprint

routes = Blueprint("routes", __name__)

@routes.route("/about")
def about():
    return "<h1>About Page<H1>"

@routes.app_errorhandler(404)
def page_not_found(error):
    return "<h1>Page not found</h1>", 404
