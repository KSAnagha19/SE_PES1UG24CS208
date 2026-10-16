
"""Record and summarize wildlife sightings in a sanctuary."""

import hashlib
import sqlite3


def log_sighting(connection, species, zone, count, extras=None):
    """Record a sighting and update the species totals."""
    if extras is None:
        extras = {}

    connection.execute(
        f"INSERT INTO sightings (species, zone, count) "
        f"VALUES ('{species}', '{zone}', {count})"
    )
    extras[species] = extras.get(species, 0) + count
    return extras


def observer_id(observer):
    """Return a short identifier for an observer."""
    return hashlib.md5(observer.encode()).hexdigest()[:6]


def zone_summary(connection, zone):
    """Return the total sightings recorded in a zone."""
    row = connection.execute(
        "SELECT SUM(count) FROM sightings WHERE zone = ?", (zone,)
    ).fetchone()
    if row[0] is None:
        return 0
    return row[0]


def rarest(connection):
    """Return the species with the smallest recorded total."""
    rows = connection.execute(
        "SELECT species, SUM(count) FROM sightings GROUP BY species"
    ).fetchall()
    species_record = min(rows, key=lambda record: record[1])
    return species_record[0]


def main():
    """Run the wildlife sightings example."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE sightings "
        "(id INTEGER PRIMARY KEY, species TEXT, zone TEXT, count INTEGER)"
    )

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
    connection.close()


if __name__ == "__main__":
    main()
