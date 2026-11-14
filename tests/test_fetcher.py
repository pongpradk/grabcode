from unittest.mock import patch, Mock
import pytest
import requests

from grabcode.fetcher import get_media


@patch("grabcode.fetcher.requests.get")
def test_get_media_success(mock_get):
    # Arrange
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
                                        "business_discovery": {
                                            "media": {
                                                "data": [
                                                    {
                                                        "caption": "Code 'FOODIE'",
                                                        "id": "18130983143489491",
                                                        "permalink": "https://www.instagram.com/p/DfmRR5KEmAP/",
                                                        "timestamp": "2026-11-11T10:30:03+0000"
                                                    },
                                                    {
                                                        "caption": "Code 'GUBONUS'",
                                                        "id": "28130983143489491",
                                                        "permalink": "https://www.instagram.com/p/AfmRR5KEmAP/",
                                                        "timestamp": "2026-11-11T03:02:54+0000"
                                                    }
                                                ]
                                            }   
                                        }
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    # Act
    result = get_media()

    # Assert
    assert result == {
                        "business_discovery": {
                            "media": {
                                "data": [
                                    {
                                        "caption": "Code 'FOODIE'",
                                        "id": "18130983143489491",
                                        "permalink": "https://www.instagram.com/p/DfmRR5KEmAP/",
                                        "timestamp": "2026-11-11T10:30:03+0000"
                                    },
                                    {
                                        "caption": "Code 'GUBONUS'",
                                        "id": "28130983143489491",
                                        "permalink": "https://www.instagram.com/p/AfmRR5KEmAP/",
                                        "timestamp": "2026-11-11T03:02:54+0000"
                                    }
                                ]
                            }   
                        }
    }
    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/users/1", timeout=5
    )
