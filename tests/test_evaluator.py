def test_score_alignment():
    from src.analysis import score_alignment
    assert score_alignment("this is helpful advice") == 1
    assert score_alignment("this is unsafe content") == 0
    assert score_alignment("neutral output") == 0.5
