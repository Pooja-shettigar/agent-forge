from database.db_manager import (
    save_startup,
    get_all_startups
)


def test_startup_save():

    save_startup(
        "Test Startup",
        "Test Report"
    )

    startups = get_all_startups()

    assert len(startups) > 0