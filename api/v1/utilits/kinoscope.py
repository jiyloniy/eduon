import requests

KINESCOPE_API_KEY = "76204bfd-7974-4b2b-bd12-3246885035ad"
KINESCOPE_API_URL = "https://uploader.kinescope.io/video"
DELETE_API_URL = "https://api.kinescope.io/v1/"


def upload_video_to_kinescope(file_path, title, description, filename):
    headers = {
        "X-Video-Title": title,
        "X-Video-Description": description,
        "X-File-Name": filename,
        "Authorization": f"Bearer {KINESCOPE_API_KEY}",
    }
    try:
        with open(file_path, "rb") as stream:
            response = requests.post(
                KINESCOPE_API_URL, headers=headers, data=stream, timeout=None
            )

        response.raise_for_status()  # Raise an exception for non-200 status codes

        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 413:
            raise ValueError(
                "Video file size exceeds the maximum allowed by Kinescope API"
            )
        else:
            raise ValueError(f"HTTP error occurred: {e}")
    except Exception as e:
        raise ValueError(f"Error uploading video to Kinescope: {str(e)}")


def delete_video(video_id):
    headers = {
        "Authorization": f"Bearer {KINESCOPE_API_KEY}",
    }
    try:
        response = requests.delete(
            f"{DELETE_API_URL}videos/{video_id}", headers=headers
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            raise ValueError(f"Video with ID {video_id} not found")
        else:
            raise ValueError(f"HTTP error occurred while deleting video: {e}")
    except Exception as e:
        raise ValueError(f"Error deleting video from Kinescope: {str(e)}")


# Ishlatish namunasi
try:
    video_id = "un13h892trNqtFjRZEzFSm"
    result = delete_video(video_id)
    print(result)
except ValueError as e:
    print(f"Error: {e}")
