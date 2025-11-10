from app.models import db, Item

def seed_data():
    if Item.query.count() == 0:
        demo_items = [
            Item(name="Server Backup", description="Nightly job", price=49.99),
            Item(name="Data Analysis", description="Monthly insights", price=149.00),
        ]
        db.session.add_all(demo_items)
        db.session.commit()
        print("Database seeded with demo items.")
    else:
        print("Database already seeded.")
