from datetime import datetime, timezone
from hashlib import md5
from typing import Optional
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import sqlalchemy as sa
from sqlalchemy import String, Integer, Boolean, DateTime
import sqlalchemy.orm as so
from app import db
from app import login


class Truck(db.Model):
    id: so.Mapped[int] = so.mapped_column(Integer, primary_key=True)
    
    driver_name: so.Mapped[str] = so.mapped_column(String(64), index=True)
    
    license_plate: so.Mapped[str] = so.mapped_column(String(20), default="DL ABC 1234")

    phone: so.Mapped[str] = so.mapped_column(String(15))
    
    email: so.Mapped[str] = so.mapped_column(String(120), index=True, unique=True)
    
    schedule: so.Mapped[str] = so.mapped_column(String(20))
    
    current_location: so.Mapped[str] = so.mapped_column(String(100))
    
    status: so.Mapped[str] = so.mapped_column(String(20))
    
    last_pickup_time: so.Mapped[DateTime] = so.mapped_column(DateTime, default=datetime.utcnow)
    
    next_pickup_date: so.Mapped[DateTime] = so.mapped_column(DateTime, default=datetime.utcnow)
        
    district: so.Mapped[str] = so.mapped_column(String(100))
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f"https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Truck {self.license_plate}>'


class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(Integer, primary_key=True)
    
    username: so.Mapped[str] = so.mapped_column(String(64), index=True, unique=True)
    
    email: so.Mapped[str] = so.mapped_column(String(120), index=True, unique=True)
    
    password_hash: so.Mapped[str] = so.mapped_column(String(256))
    
    location: so.Mapped[str] = so.mapped_column(String(100))
        
    scheduled_pickup_alerts: so.Mapped[Boolean] = so.mapped_column(Boolean, default=True)
    
    proximity_alerts: so.Mapped[Boolean] = so.mapped_column(Boolean, default=True)
    
    phone: so.Mapped[str] = so.mapped_column(String(15))
    
    registration_date: so.Mapped[DateTime] = so.mapped_column(DateTime, default=datetime.utcnow)
    
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f"https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


# Test User Class
    
# class User(UserMixin, db.Model):
#     id: so.Mapped[int] = so.mapped_column(
#         primary_key=True
#     )

#     username: so.Mapped[str] = so.mapped_column(
#         sa.String(64),
#         index=True,
#         unique=True
#     )

#     email: so.Mapped[str] = so.mapped_column(
#         sa.String(120),
#         index=True,
#         unique=True
#     )

#     password_hash: so.Mapped[Optional[str]] = so.mapped_column(
#         sa.String(256)
#     )

#     about_me: so.Mapped[Optional[str]] = so.mapped_column(
#         sa.String(140)
#     )

#     last_seen: so.Mapped[Optional[datetime]] = so.mapped_column(
#         default=lambda: datetime.now(timezone.utc)
#     )
    
#     def avatar(self, size):
#         digest = md5(self.email.lower().encode('utf-8')).hexdigest()
#         return f"https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}"

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password) # type: ignore

#     def __repr__(self):
#         return f'<User {self.username}>'

@login.user_loader
def load_user(id):
    user = db.session.get(User, int(id))
    return user