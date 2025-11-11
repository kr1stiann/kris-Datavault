from app.models import db, Item

def seed_data():
    """Populate the database with some example items if empty."""
    if Item.query.count() > 0:
        print("Database already seeded — skipping.")
        return

    print("Seeding database with initial data...")

    items = [
        Item(title="Server Backup", description="Nightly backup job", price=49.99),
        Item(title="Data Sync", description="Cloud replication service", price=29.99),
        Item(title="Monitoring", description="24/7 uptime monitoring", price=19.99),
    ]

    db.session.add_all(items)
    db.session.commit()

    print("Database seeded successfully.")
