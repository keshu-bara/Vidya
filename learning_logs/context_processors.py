# Create a new file in your learning_logs app: context_processors.py

def sidebar_data(request):
    """Context processor that adds topic data to all templates."""
    from .models import Topic
    
    # Only get topics if user is authenticated
    if request.user.is_authenticated:
        topics = Topic.objects.filter(owner=request.user).order_by('date_added')
        return {'topics': topics}
    return {'topics': []}