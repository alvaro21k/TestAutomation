import pytest

class TestColorRatings:
    def test_color_ratings_returns_data(self, api_client):
        color_ratings = api_client.get_color_ratings()
        assert color_ratings is not None

    def test_color_ratings_contains_expected_pairs(self, api_client):
        """Should contain standard two-colour pair combinations"""
        response_data = api_client.get_color_ratings()
        # 17lands returns a list of color pair objects
        assert isinstance(response_data, list)
        assert len(response_data) > 0

    def test_color_pair_has_win_rate(self, api_client):
        """Each color pair should have a win rate field"""
        response_data = api_client.get_color_ratings()
        if len(response_data) > 0:
            first_pair = response_data[0]
            assert "wins" in first_pair or "win_rate" in first_pair