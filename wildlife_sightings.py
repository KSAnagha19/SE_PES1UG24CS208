
"""Record and summarize wildlife sightings in a sanctuary."""

import hashlib
import sqlite3


def create_connection():
    """Create an in-memory database for wildlife sightings."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE sightings (
            id INTEGER PRIMARY KEY,
            species TEXT NOT NULL,
            zone TEXT NOT NULL,
            count INTEGER NOT NULL CHECK (count > 0)
        )
        """
    )
    return connection


def log_sighting(connection, species, zone, count, extras=None):
    """Record a sighting safely and update species totals."""
    if not species or not zone:
        raise ValueError("Species and zone must not be empty")

    if not isinstance(count, int) or count <= 0:
        raise ValueError("Count must be a positive integer")

    if extras is None:
        extras = {}

    connection.execute(
        "INSERT INTO sightings (species, zone, count) VALUES (?, ?, ?)",
        (species, zone, count),
    )

    extras[species] = extras.get(species, 0) + count
    return extras


def observer_id(observer):
    """Return a short identifier derived from an observer's name."""
    return hashlib.sha256(observer.encode()).hexdigest()[:12]


def zone_summary(connection, zone):
    """Return the total number of sightings recorded in a zone."""
    row = connection.execute(
        "SELECT SUM(count) FROM sightings WHERE zone = ?", (zone,)
    ).fetchone()

    return row[0] if row[0] is not None else 0


def rarest(connection):
    """Return the least-recorded species, or None if no sightings exist."""
    query = (
        "SELECT species, SUM(count) AS total "
        "FROM sightings "
        "GROUP BY species "
        "ORDER BY total, species"
    )
    rows = connection.execute(query).fetchall()

    if not rows:
        return None

    return rows[0][0]


def main():
    """Run the wildlife sightings example."""
    connection = create_connection()

    try:
        totals = log_sighting(connection, "Leopard", "North", 1)
        log_sighting(connection, "Chital", "North", 24, totals)
        log_sighting(connection, "Hornbill", "East", 3, totals)

        if len(totals) != 3:
            raise ValueError("Unexpected number of species")

        print(
            observer_id("Arun"),
            zone_summary(connection, "North"),
            rarest(connection),
        )
    finally:
        connection.close()


if __name__ == "__main__":
    main()
