from app import app, db
from models import Message
from datetime import datetime, timedelta

with app.app_context():
    # Clear existing messages
    Message.query.delete()
    db.session.commit()
    
    # Create sample messages
    messages = [
        Message(
            body="Hello everyone! Welcome to Chatterbox!",
            username="Alice",
            created_at=datetime.utcnow() - timedelta(minutes=10),
            updated_at=datetime.utcnow() - timedelta(minutes=10)
        ),
        Message(
            body="This is a great chat application!",
            username="Bob",
            created_at=datetime.utcnow() - timedelta(minutes=8),
            updated_at=datetime.utcnow() - timedelta(minutes=8)
        ),
        Message(
            body="I agree! Really enjoying this so far.",
            username="Charlie",
            created_at=datetime.utcnow() - timedelta(minutes=5),
            updated_at=datetime.utcnow() - timedelta(minutes=5)
        ),
        Message(
            body="Can't wait to see what's next!",
            username="Diana",
            created_at=datetime.utcnow() - timedelta(minutes=2),
            updated_at=datetime.utcnow() - timedelta(minutes=2)
        ),
        Message(
            body="Thanks for building this with us!",
            username="Eve",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        ),
    ]
    
    db.session.add_all(messages)
    db.session.commit()
    
    print("Seed data created successfully!")