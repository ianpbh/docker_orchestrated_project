from app.celery_app import celery
from app.repositories.session import finish_session
        
@celery.task
def finish_session_task(topic_id: int):
    print(f"Finishing session with ID: {topic_id}")
    try:
        finish_session(topic_id)
    except Exception as e:
        print(f"Error finishing session {topic_id}: {e}")