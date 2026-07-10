from src.workers.tasks import run_simulation_cycle


def test_run_simulation_cycle():
    """Test that the run_simulation_cycle celery task executes correctly with placeholders."""
    simulation_id = "sim_9999"
    result = run_simulation_cycle(simulation_id)

    assert result["simulation_id"] == simulation_id
    assert result["status"] == "completed"
    assert "result" in result
