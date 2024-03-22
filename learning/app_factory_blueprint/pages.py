from flask import BluePrint

bp=BluePrint('pages',__name__)

@bp.route('/')
def home():
  return 'GOOD DAY'

@bp.route('/about')
def about():
  return 'ABOUT TODAY'