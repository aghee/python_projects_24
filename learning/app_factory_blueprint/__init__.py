from flask import Flask

from .app_factory_blueprint  import pages

def create():
  app=Flask(__name__)

  app.register_blueprint(pages.bp)
  return app