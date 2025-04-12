from app import create_app , db
from app.extensions import db
from app.models.user import User
from app.models.bus import Bus
from app.models.route import Route
from app.models.schedule import Schedule
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta

# Create app instance
app = create_app()

# Push app context
with app.app_context():
    # Drop and recreate tables
    db.drop_all()
    db.create_all()

    # Users
    admin = User(name="Admin User", email="admin@example.com", password=generate_password_hash("admin123"), role="admin")
    user1 = User(name="Alice", email="alice@example.com", password=generate_password_hash("alice123"), role="user")
    user2 = User(name="Bob", email="bob@example.com", password=generate_password_hash("bob123"), role="user")

    # Buses
    bus1 = Bus(number_plate="KAB123X", capacity=45, operator="Greenline")
    bus2 = Bus(number_plate="KBC456Y", capacity=30, operator="CityBus")

    # Routes
    route1 = Route(source="Nairobi", destination="Mombasa", distance=480)
    route2 = Route(source="Nakuru", destination="Kisumu", distance=180)

    # Schedules
    schedule1 = Schedule(
        route=route1,
        bus=bus1,
        departure_time=datetime.now() + timedelta(days=1),
        arrival_time=datetime.now() + timedelta(days=1, hours=8)
    )
    schedule2 = Schedule(
        route=route2,
        bus=bus2,
        departure_time=datetime.now() + timedelta(days=2),
        arrival_time=datetime.now() + timedelta(days=2, hours=4)
    )

    db.session.add_all([admin, user1, user2, bus1, bus2, route1, route2, schedule1, schedule2])
    db.session.commit()

    print("✅ Dummy data seeded successfully!")
