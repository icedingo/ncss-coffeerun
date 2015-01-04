
from application import app, db
from application.models import *

db.drop_all()
db.init_app(app)
db.create_all()

sopen = Status("Open")
sorder = Status("Ordering")
spickup = Status("Pickup")
sclosed = Status("Closed")

inituser = User("Maddy")
inituser.email = "maddy.reid.21@gmail.com"
inituser.tutor = True

db.session.add(sopen)
db.session.add(sorder)
db.session.add(spickup)
db.session.add(sclosed)
db.session.add(inituser)
db.session.commit()
